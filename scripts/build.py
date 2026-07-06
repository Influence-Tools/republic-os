#!/usr/bin/env python3
"""Build the OKF entity tree from the raw source exports in data/.

Inputs (committed raw, one JSON object per line):
  officeholders-v3.jsonl        Atlas — person->seat records          (13,329)
  bodies.jsonl                  congress-legislators — institutions      (233)
  leadership.jsonl              current federal leadership roles          (28)
  committee_memberships.jsonl   person->committee edges                (3,879)
  place_county_crosswalk.jsonl  Census place -> county (PostGIS join)  (32,041)
  county_district_edges.jsonl   county -> district area-overlap edges  (16,328)

Outputs (fully regenerated each run):
  data/jurisdictions/**         Person files (federal ones enriched with
                                bioguide, leadership, committee seats)
  data/jurisdictions/us/bodies/**   Body files (chambers, committees,
                                    subcommittees) with their leadership

Deterministic by construction: sorted iteration, fixed key order, one full
rebuild per run. Two consecutive runs produce a byte-identical tree.
"""

import json
import re
import shutil
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA = REPO / "data"
OUT = DATA / "jurisdictions"
BODIES_OUT = OUT / "us" / "bodies"
DATASET_DATE = "2026-07-04"          # officeholders v3 export date
CONGRESS_DATE = "2026-07-03"         # congress-legislators ingest date


# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #

def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", text) or "unnamed"


def yval(v):
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return json.dumps(v, ensure_ascii=False)


def norm_name(n):
    """Normalize a person name for cross-source reconciliation."""
    n = re.sub(r'["\'][^"\']*["\']', "", n)                 # quoted nickname
    n = re.sub(r",?\s+(Jr|Sr|II|III|IV)\.?(?=\s|$)", "", n)  # suffix (any pos)
    return re.sub(r"\s+", " ", n).strip().lower()


def norm_county(name):
    return re.sub(r"\bSaint\b", "St", name)


def norm_place(s):
    """Normalize a Census place name for crosswalk lookup (bare, ascii, alnum)."""
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def acs_cslug(row):
    """County directory slug derived from an ACS county row (the authority for
    county node names — municipals must nest under the same slug)."""
    base = re.sub(r",\s*[A-Z]{2}$", "", row.get("county_name") or "")
    return slugify(norm_county(re.sub(r"\s+County$", "", base)))


def place_resolver(acs_county, crosswalk):
    """(normalized place name, state) -> county dir slug, from the crosswalk.

    county_geoid is the stable key; the slug is taken from the ACS county node
    (the same source that names county dirs) so municipals nest correctly. Only
    unique name matches whose county has an ACS node are included — ambiguous
    names, label-less rows, and counties with no ACS node fall through.
    Shared by build.py and build_viz.py so the tree and the Board agree.
    """
    fips_to_cslug = {canonical_fips(r["county_fips"]): acs_cslug(r) for r in acs_county}
    geoids = {}
    for x in crosswalk:
        geoids.setdefault(
            (norm_place(x["place_name"]), x["state_code"]), set()).add(x["county_geoid"])
    out = {}
    for key, geos in geoids.items():
        if len(geos) == 1:
            cf = canonical_fips(next(iter(geos)))
            if cf in fips_to_cslug:
                out[key] = fips_to_cslug[cf]
    return out


# committee_title (source) -> normalized role on the committee
ROLE_MAP = {
    "member": "member", "Chair": "chair", "Chairman": "chair",
    "Chairwoman": "chair", "Cochairman": "co-chair", "Vice Chair": "vice-chair",
    "Vice Chairman": "vice-chair", "Vice Chairwoman": "vice-chair",
    "Ranking Member": "ranking-member", "Ex Officio": "ex-officio",
}
LEADER_ROLES = {"chair", "co-chair", "vice-chair", "ranking-member"}


# --------------------------------------------------------------------------- #
# body paths / ids
# --------------------------------------------------------------------------- #

INSTITUTIONS = {"house", "senate", "executive"}


def committee_codes(bodies):
    return sorted((b["code"] for b in bodies if b["type"] == "committee"),
                  key=len, reverse=True)


def parent_code(sub_code, comm_codes):
    for c in comm_codes:
        if sub_code.startswith(c) and sub_code != c:
            return c
    return None


def body_id(code, bodies_by_code, comm_codes):
    """Stable path-based id (relative to data/jurisdictions) for a body."""
    b = bodies_by_code[code]
    if b["type"] in INSTITUTIONS:
        return f"us/bodies/{slugify(b['name'])}"
    if b["type"] == "committee":
        return f"us/bodies/{b['chamber']}/committees/{slugify(short_name(b))}"
    parent = parent_code(code, comm_codes)
    pb = bodies_by_code[parent]
    return (f"us/bodies/{pb['chamber']}/committees/{slugify(short_name(pb))}"
            f"/subcommittees/{slugify(short_name(b))}")


def short_name(b):
    """Committee/subcommittee name minus redundant chamber/parent prefix."""
    name = b["name"]
    name = re.sub(r"^(House|Senate|Joint)\s+(Committee|Subcommittee)\s+on\s+",
                  "", name)
    if " - " in name:                       # subcommittee: keep the tail
        name = name.split(" - ", 1)[1]
    return name


# --------------------------------------------------------------------------- #
# federal enrichment index (name -> bioguide, leadership, committee seats)
# --------------------------------------------------------------------------- #

def build_enrichment(leadership, memberships, bodies_by_code, comm_codes):
    idx = {}

    def slot(name):
        return idx.setdefault(norm_name(name),
                              {"bioguide": None, "leadership": [], "committees": []})

    for l in leadership:
        s = slot(l["person_name"])
        s["bioguide"] = l["bioguide"]
        s["leadership"].append({
            "role": l["role_title"], "body": l["body_code"],
            "since": l.get("start_date"),
        })
    for m in memberships:
        s = slot(m["person_name"])
        s["bioguide"] = m["bioguide"]
        s["committees"].append({
            "code": m["body_code"], "name": m["committee_name"],
            "role": ROLE_MAP.get(m["committee_title"], "member"),
            "rank": m.get("rank"),
            "id": body_id(m["body_code"], bodies_by_code, comm_codes),
        })
    for s in idx.values():
        s["leadership"].sort(key=lambda r: (r["role"], r["body"]))
        s["committees"].sort(key=lambda c: (c["id"]))
    return idx


# --------------------------------------------------------------------------- #
# Person files
# --------------------------------------------------------------------------- #

def county_slug(rec, place_to_cslug=None):
    label = norm_county(rec.get("jurisdiction_label") or "")
    m = re.match(r"(.+?) County, FL$", label)
    if m:
        return slugify(m.group(1))
    if rec["level"] == "municipal":
        m = re.search(r"County:\s*([^;]+)", rec.get("description") or "")
        if m:
            return slugify(norm_county(m.group(1).strip()))
    title = rec.get("title") or ""
    m = re.search(r"\bof\s+(.+?)\s+County\b", title) or re.match(r"(.+?)\s+County\b", title)
    if m:
        return slugify(norm_county(m.group(1)))
    # Census place -> county via the committed crosswalk (place_county_crosswalk).
    # Only unique name matches whose county has an ACS node are resolved here;
    # ambiguous names, label-less rows, and CT planning regions fall through.
    if place_to_cslug and rec["level"] == "municipal":
        jl = rec.get("jurisdiction_label") or ""
        pm = re.match(r"(.+?),\s*[A-Z]{2}$", jl)          # "Tampa, FL" -> "Tampa"
        placename = pm.group(1) if pm else jl             # "Elgin" -> "Elgin"
        cslug = place_to_cslug.get((norm_place(placename), rec.get("state_abbr")))
        if cslug:
            return cslug
    return "_unresolved"


def city_slug(rec):
    jl = rec.get("jurisdiction_label") or ""
    m = re.match(r"(.+?),\s*[A-Z]{2}$", jl)          # "Elgin, TX" / "Naples, FL"
    if m:
        return slugify(m.group(1))
    if jl:                                           # bare "Elgin"
        return slugify(jl)
    m = re.match(r"Mayor of (.+)$", rec.get("title") or "")
    if m:
        return slugify(m.group(1))
    return "_unresolved"


def person_dir(rec, place_to_cslug=None):
    lvl, st = rec["level"], (rec.get("state_abbr") or "").lower()
    if lvl == "federal":
        return OUT / "us" / "people"
    if lvl == "state":
        return OUT / "us" / "states" / st / "people"
    if lvl == "county":
        return OUT / "us" / "states" / st / "counties" / county_slug(rec, place_to_cslug) / "people"
    if lvl == "municipal":
        return (OUT / "us" / "states" / st / "counties" / county_slug(rec, place_to_cslug)
                / "municipalities" / city_slug(rec) / "people")
    return OUT / "_unresolved" / "people"


def display_name(rec):
    return rec.get("full_name") or rec.get("title") or "Unknown"


def person_frontmatter(rec, enr):
    lines = ["type: Person", f"title: {yval(display_name(rec))}"]
    jl = rec.get("jurisdiction_label")
    desc = rec.get("title") or ""
    if jl and jl not in desc:
        desc = f"{desc} — {jl}" if desc else jl
    if desc:
        lines.append(f"description: {yval(desc)}")
    if rec.get("title"):
        lines.append(f"role: {yval(rec['title'])}")
    if rec.get("party"):
        lines.append(f"party: {yval(rec['party'])}")
    lines.append(f"level: {yval(rec['level'])}")
    if rec.get("branch"):
        lines.append(f"branch: {yval(rec['branch'])}")
    if rec.get("state_abbr"):
        lines.append(f"state: {yval(rec['state_abbr'])}")
    if rec.get("jurisdiction_type") == "district" and jl:
        lines.append(f"district: {yval(jl)}")
    dnode = person_district_node(rec)
    if dnode:
        lines.append(f"represents: {yval(dnode)}")
    if enr and enr["leadership"]:
        lines.append("leadership:")
        for r in enr["leadership"]:
            lines.append(f"  - role: {yval(r['role'])}")
            lines.append(f"    body: {yval(r['body'])}")
            if r.get("since"):
                lines.append(f"    since: {yval(r['since'])}")
    if enr and enr["committees"]:
        lines.append("committees:")
        for c in enr["committees"]:
            lines.append(f"  - name: {yval(c['name'])}")
            lines.append(f"    role: {yval(c['role'])}")
            lines.append(f"    body: {yval(c['id'])}")
    contact = [(k, rec.get(k)) for k in ("email", "phone", "website") if rec.get(k)]
    if contact:
        lines.append("contact:")
        for k, v in contact:
            lines.append(f"  {k}: {yval(v)}")
    tenure = [(k2, rec.get(k1)) for k1, k2 in
              (("start_date", "start"), ("end_date", "end"),
               ("is_current", "current"), ("tenure_notes", "notes"))
              if rec.get(k1) is not None]
    if tenure:
        lines.append("tenure:")
        for k, v in tenure:
            lines.append(f"  {k}: {yval(v)}")
    election = [(k2, rec.get(k1)) for k1, k2 in
                (("next_election_year", "next"), ("term_length", "term_length"),
                 ("term_limit", "term_limit")) if rec.get(k1) is not None]
    if election:
        lines.append("election:")
        for k, v in election:
            lines.append(f"  {k}: {yval(v)}")
    lines.append("ids:")
    for k1, k2 in (("person_id", "person"), ("office_id", "office"),
                   ("tenure_id", "tenure"), ("jurisdiction_id", "jurisdiction")):
        if rec.get(k1):
            lines.append(f"  {k2}: {yval(rec[k1])}")
    if enr and enr["bioguide"]:
        lines.append(f"  bioguide: {yval(enr['bioguide'])}")
    srcs = [(f, rec[k]) for f, k in (("office", "office_source"),
            ("tenure", "tenure_source"), ("jurisdiction", "jurisdiction_source"))
            if rec.get(k)]
    if enr and (enr["leadership"] or enr["committees"]):
        srcs.append(("roles", "congress-legislators (unitedstates project)"))
    if srcs:
        lines.append("sources:")
        for f, s in srcs:
            lines.append(f"  - field: {f}")
            lines.append(f"    source: {yval(s)}")
    lines.append("confidence: official")
    tags = ["officeholder", rec["level"]]
    if rec.get("branch"):
        tags.append(rec["branch"])
    if rec.get("state_abbr"):
        tags.append(rec["state_abbr"].lower())
    lines.append("tags: [" + ", ".join(tags) + "]")
    lines.append(f"timestamp: {yval(DATASET_DATE)}")
    return lines


def person_body(rec, enr):
    name = display_name(rec)
    role = rec.get("title") or "officeholder"
    jl = rec.get("jurisdiction_label")
    where = f" ({jl})" if jl and jl not in role else ""
    cur = "Current" if rec.get("is_current") else "Former"
    out = [f"# {name}", "", f"{cur} {role}{where}.", ""]
    dnode = person_district_node(rec)
    if dnode:
        out += [f"Represents [{rec.get('jurisdiction_label')}](/{dnode}.md).", ""]
    if enr and enr["leadership"]:
        out += ["## Leadership", ""]
        for r in enr["leadership"]:
            since = f" (since {r['since']})" if r.get("since") else ""
            out.append(f"- {r['role']}{since}")
        out.append("")
    if enr and enr["committees"]:
        out += ["## Committees", ""]
        for c in enr["committees"]:
            tag = "" if c["role"] == "member" else f" — **{c['role']}**"
            out.append(f"- [{c['name']}](/{c['id']}.md){tag}")
        out.append("")
    out += ["## Sources", ""]
    any_src = False
    for f, k in (("office", "office_source"), ("tenure", "tenure_source"),
                 ("jurisdiction", "jurisdiction_source")):
        if rec.get(k):
            out.append(f"- {f}: {rec[k]}")
            any_src = True
    if enr and (enr["leadership"] or enr["committees"]):
        out.append("- roles: congress-legislators (unitedstates project)")
        any_src = True
    if not any_src:
        out.append("- (no field-level source recorded)")
    out += ["", f"Generated from the Atlas officeholders v3 export ({DATASET_DATE})."]
    return out


# --------------------------------------------------------------------------- #
# Body files
# --------------------------------------------------------------------------- #

TYPE_LABEL = {"house": "Chamber", "senate": "Chamber", "executive": "Executive Office",
              "committee": "Committee", "subcommittee": "Subcommittee"}


def body_file(b, bid, bodies_by_code, comm_codes, leaders_of, members_count):
    lines = ["type: Body", f"title: {yval(b['name'])}",
             f"classification: {yval(b['type'])}",
             f"chamber: {yval(b['chamber'])}", f"code: {yval(b['code'])}"]
    if b["type"] == "subcommittee":
        pc = parent_code(b["code"], comm_codes)
        lines.append(f"parent: {yval(body_id(pc, bodies_by_code, comm_codes))}")
    lead = leaders_of.get(b["code"], [])
    if lead:
        lines.append("leadership:")
        for person_name, role, pid in lead:
            lines.append(f"  - person: {yval(person_name)}")
            lines.append(f"    role: {yval(role)}")
    lines.append("sources:")
    lines.append("  - field: definition")
    lines.append("    source: congress-legislators (unitedstates project)")
    lines.append("confidence: official")
    tags = ["body", b["type"], b["chamber"]]
    lines.append("tags: [" + ", ".join(dict.fromkeys(tags)) + "]")
    lines.append(f"timestamp: {yval(CONGRESS_DATE)}")

    body = [f"# {b['name']}", "",
            f"{TYPE_LABEL.get(b['type'], 'Body')} ({b['chamber']}).", ""]
    if lead:
        body += ["## Leadership", ""]
        for person_name, role, pid in lead:
            body.append(f"- {role}: {person_name}")
        body.append("")
    if members_count:
        body += [f"{members_count} members "
                 "(see each member's file for their seat on this body).", ""]
    body += ["## Source", "",
             "- definition: congress-legislators (unitedstates project)"]
    return "---\n" + "\n".join(lines) + "\n---\n\n" + "\n".join(body) + "\n"


# --------------------------------------------------------------------------- #
# Candidate files (FEC)
# --------------------------------------------------------------------------- #

STANCE = {"I": "incumbent", "C": "challenger", "O": "open-seat"}
CAND_STATUS = {"C": "statutory candidate", "N": "not yet a candidate",
               "P": "prior candidate", "F": "future candidate"}
PARTY_FULL = {"REP": "Republican", "DEM": "Democratic", "IND": "Independent",
              "LIB": "Libertarian", "GRE": "Green",
              "DFL": "Democratic-Farmer-Labor"}


def candidate_name(raw):
    """'CARL, JERRY LEE, JR' -> 'Jerry Lee Carl Jr'."""
    parts = [p.strip() for p in raw.split(",")]
    last = parts[0] if parts else raw
    first = parts[1] if len(parts) > 1 else ""
    suffix = parts[2] if len(parts) > 2 else ""
    return " ".join(x for x in (first, last, suffix) if x).title()


def candidate_office(rec):
    return "U.S. Senate" if rec.get("office") == "S" else "U.S. House"


def candidate_seat(rec):
    st = rec.get("state") or ""
    if rec.get("office") == "H" and rec.get("district"):
        return f"{st}-{rec['district']}"
    return st


def candidate_frontmatter(rec, disp):
    office, seat, yr = candidate_office(rec), candidate_seat(rec), rec.get("election_year")
    lines = ["type: Candidate", f"title: {yval(disp)}",
             f"description: {yval(f'{office} candidate, {seat} ({yr})')}",
             f"office: {yval(office)}"]
    if rec.get("state"):
        lines.append(f"state: {yval(rec['state'])}")
    if rec.get("office") == "H" and rec.get("district"):
        lines.append(f"district: {yval(seat)}")
    if rec.get("party"):
        lines.append(f"party: {yval(rec['party'])}")
    if rec.get("incumbent_challenge") in STANCE:
        lines.append(f"stance: {yval(STANCE[rec['incumbent_challenge']])}")
    if yr:
        lines.append(f"election_year: {yr}")
    if rec.get("candidate_status") in CAND_STATUS:
        lines.append(f"status: {yval(CAND_STATUS[rec['candidate_status']])}")
    if rec.get("committee_name"):
        lines.append("committee:")
        lines.append(f"  name: {yval(rec['committee_name'])}")
        if rec.get("committee_id"):
            lines.append(f"  id: {yval(rec['committee_id'])}")
    lines.append("ids:")
    lines.append(f"  fec: {yval(rec['fec_id'])}")
    lines.append("sources:")
    lines.append("  - field: filing")
    lines.append("    source: FEC (Federal Election Commission)")
    lines.append("confidence: official")
    tags = ["candidate", "federal",
            "senate" if rec.get("office") == "S" else "house"]
    if rec.get("state"):
        tags.append(rec["state"].lower())
    lines.append("tags: [" + ", ".join(tags) + "]")
    lines.append(f"timestamp: {yval(CONGRESS_DATE)}")
    return lines


def candidate_body(rec, disp):
    office, seat = candidate_office(rec), candidate_seat(rec)
    stance = STANCE.get(rec.get("incumbent_challenge"), "candidate")
    party = PARTY_FULL.get(rec.get("party"), rec.get("party") or "")
    out = [f"# {disp}", "",
           f"{party} {stance} for {office} ({seat}), {rec.get('election_year')}.", ""]
    if rec.get("committee_name"):
        cid = f" ({rec['committee_id']})" if rec.get("committee_id") else ""
        out += ["## Campaign Committee", "", f"- {rec['committee_name']}{cid}", ""]
    out += ["## Source", "", "- filing: FEC (Federal Election Commission)", "",
            "Federal candidate filing; not yet linked to an officeholder record."]
    return out


# --------------------------------------------------------------------------- #
# Jurisdiction demographic nodes (ACS)
# --------------------------------------------------------------------------- #

def numify(v):
    if v is None or v == "":
        return None
    if isinstance(v, (int, float)):
        return v
    try:
        f = float(v)
        return int(f) if "." not in str(v) and f == int(f) else round(f, 4)
    except (ValueError, TypeError):
        return v


def canonical_fips(fips):
    return re.sub(r"\D", "", str(fips))[-5:]


DEMOG_LABELS = {
    "population": "Population", "population_under_18": "Under 18",
    "population_18_64": "18–64", "population_65_plus": "65+",
    "median_household_income": "Median household income",
    "poverty_rate": "Poverty rate", "homeownership_rate": "Homeownership rate",
    "unemployment_rate": "Unemployment rate", "median_home_value": "Median home value",
    "gini_index": "Gini index", "vacancy_rate": "Vacancy rate",
    "race_white": "White", "race_black": "Black", "race_asian": "Asian",
    "race_native": "Native", "hispanic": "Hispanic/Latino",
    "bachelors_plus": "Bachelor's or higher",
}


def normalize_demog(row):
    def pick(*cols):
        for c in cols:
            if row.get(c) not in (None, ""):
                return numify(row.get(c))
        return None
    d = {
        "population": pick("total_population"),
        "population_under_18": pick("population_under_18"),
        "population_18_64": pick("population_18_64"),
        "population_65_plus": pick("population_65_plus"),
        "median_household_income": pick("median_household_income"),
        "poverty_rate": pick("poverty_rate"),
        "homeownership_rate": pick("homeownership_rate"),
        "unemployment_rate": pick("unemployment_rate"),
        "median_home_value": pick("median_home_value"),
        "gini_index": pick("gini_index"),
        "vacancy_rate": pick("vacancy_rate"),
        "race_white": pick("race_white"), "race_black": pick("race_black"),
        "race_asian": pick("race_asian"), "race_native": pick("race_native"),
        "hispanic": pick("hispanic_latino", "hispanic"),
    }
    bp = pick("edu_bachelors_plus")
    if bp is None:
        bp = (pick("edu_bachelors") or 0) + (pick("edu_graduate") or 0) or None
    d["bachelors_plus"] = bp
    return {k: v for k, v in d.items() if v is not None}


def demog_yaml(demog):
    lines = ["demographics:"]
    for k, v in demog.items():
        lines.append(f"  {k}: {yval(v) if isinstance(v, str) else v}")
    return lines


def demog_table(demog):
    out = ["## Demographics (ACS 2023)", "", "| Measure | Value |", "| --- | --- |"]
    for k, v in demog.items():
        out.append(f"| {DEMOG_LABELS.get(k, k)} | {v} |")
    return out + [""]


# --------------------------------------------------------------------------- #
# District nodes + county->district edges (the geographic authority layer)
# --------------------------------------------------------------------------- #

DTYPE_CLASS = {"CD": "congressional-district",
               "SS": "state-senate-district", "SH": "state-house-district"}
DTYPE_RANK = {"CD": 0, "SS": 1, "SH": 2}
DTYPE_WORD = {"CD": "congressional", "SS": "state senate", "SH": "state house"}
DISTRICT_SOURCE = "PostGIS area-intersection over Census TIGER 2024 boundaries"


def cd_ident(label):
    """'Congressional District 5' -> '05'; at-large -> '00'."""
    if re.search(r"at.?large", label, re.I):
        return "00"
    m = re.search(r"(\d+)", label)
    return f"{int(m.group(1)):02d}" if m else "00"


def leg_ident(label):
    """State-leg identifier: text after 'District '. 'GA State Senate District 10A' -> '10A'."""
    m = re.search(r"\bDistrict\s+(.+)$", label.strip())
    return (m.group(1).strip() if m else label.strip())


def district_node_id(dtype, state, ident):
    """Concept id (path under data/jurisdictions) for a district node."""
    st = (state or "").lower()
    if dtype == "CD":
        return f"us/states/{st}/districts/{ident}"
    sub = "senate" if dtype == "SS" else "house"
    return f"us/states/{st}/districts/{sub}/{slugify(ident)}"


def edge_node_id(e):
    """District node id for a county_district_edges row."""
    dt = e["type"]
    ident = cd_ident(e["district_label"]) if dt == "CD" else leg_ident(e["district_label"])
    return district_node_id(dt, e["district_state"], ident)


def district_title(dtype, state, ident):
    if dtype == "CD":
        return f"{state}-{ident}"
    return f"{state} {'Senate' if dtype == 'SS' else 'House'} District {ident}"


def person_district_parts(rec):
    """(dtype, state, ident) of the district a legislator / US House member holds, else None."""
    jl = rec.get("jurisdiction_label") or ""
    if rec["level"] == "federal" and re.search(r"congressional district", jl, re.I):
        return ("CD", rec.get("state_abbr"), cd_ident(jl))
    if rec["level"] == "state" and rec.get("branch") == "legislative":
        m = re.match(r"^([A-Z]{2})\s", jl)
        st = m.group(1) if m else rec.get("state_abbr")
        dt = ("SS" if re.search(r"state senate", jl, re.I)
              else "SH" if re.search(r"state house|house of rep", jl, re.I) else None)
        if dt and st:
            return (dt, st, leg_ident(jl))
    return None


def person_district_node(rec):
    """District node id a legislator / US House member represents, else None."""
    p = person_district_parts(rec)
    return district_node_id(*p) if p else None


def jurisdiction_file(title, classification, extra_fm, demog, st, body_intro,
                      district_edges=None, sources=None):
    """district_edges: sorted list of (node_id, dtype, title, area_weight).
    sources: explicit [(field, source)] list; when None it is derived from
    whatever data the node carries (demographics / edges / bare boundary)."""
    lines = ["type: Jurisdiction", f"title: {yval(title)}",
             f"classification: {classification}"]
    lines += extra_fm
    if demog:
        lines += demog_yaml(demog)
    if district_edges:
        lines.append("districts:")
        for nid, dt, dtitle, w in district_edges:
            lines += [f"  - to: {yval(nid)}", "    rel: in-district",
                      f"    area_weight: {w}"]
    if sources is not None:
        src = sources
    else:
        src = []
        if demog:
            src.append(("demographics", "Census ACS 2023"))
        if district_edges:
            src.append(("districts", DISTRICT_SOURCE))
        if not src:                                   # sparse district node
            src.append(("boundary", "Census TIGER 2024"))
    lines.append("sources:")
    for f, s in src:
        lines += [f"  - field: {f}", f"    source: {yval(s)}"]
    lines += ["confidence: official",
              f"tags: [jurisdiction, {classification}, {st}]",
              f"timestamp: {yval(CONGRESS_DATE)}"]
    body = [f"# {title}", "", body_intro, ""]
    if demog:
        body += demog_table(demog)
    if district_edges:
        body += ["## Districts", ""]
        for nid, dt, dtitle, w in district_edges:
            body.append(f"- [{dtitle}](/{nid}.md) — {round(w * 100)}% ({DTYPE_WORD[dt]})")
        body.append("")
    body += ["## Source", ""] + [f"- {f}: {s}" for f, s in src]
    return "---\n" + "\n".join(lines) + "\n---\n\n" + "\n".join(body) + "\n"


# --------------------------------------------------------------------------- #
# City nodes — incorporated Census places (the municipal jurisdiction layer)
#
# A city is modelled exactly like a county: a Jurisdiction node that fuses the
# place and its government, with officeholders nested beneath it — not a
# separate Body. Identity is the Census place GEOID; officeholders are joined
# to it by name+state (county-hint disambiguated) off the same jurisdiction_label
# that city_slug uses for placement, so node and people co-locate by construction.
# --------------------------------------------------------------------------- #

# Census LSAD descriptor -> node classification. CDPs (statistical, ungoverned)
# are dropped entirely — only incorporated places become nodes of influence.
PLACE_CLASS = {"city": "city", "town": "town", "village": "village",
               "borough": "borough", "municipality": "city",
               "township": "town", "corporation": "city",
               "government": "city", "plantation": "town"}


def place_classification(namelsad):
    return PLACE_CLASS.get(namelsad.split()[-1].lower(), "city") if namelsad else "city"


def officeholder_place_name(rec):
    """The place a municipal officeholder serves, taken from jurisdiction_label
    (the same field city_slug places them under), falling back to the title."""
    jl = rec.get("jurisdiction_label") or ""
    m = re.match(r"(.+?),\s*[A-Z]{2}$", jl)                    # "Bronson, FL" -> "Bronson"
    if m:
        return m.group(1)
    if jl:                                                     # bare "Elgin" / "Town of Pecos"
        return re.sub(r"^(?:town|city|village|borough)\s+of\s+", "", jl, flags=re.I)
    m = re.match(r"Mayor of (.+)$", rec.get("title") or "")
    return m.group(1) if m else ""


def city_index(crosswalk):
    """Incorporated Census places only (CDPs dropped). Returns:
       by_name:    (state, norm_place) -> [ {geoid, county_norm} ]   for resolution
       geoid_meta: geoid -> {name, state, classification, counties:set}
    """
    by_name, geoid_meta = {}, {}
    for r in crosswalk:
        namelsad = r["place_namelsad"]
        if namelsad.split()[-1].lower() == "cdp":
            continue
        g = r["place_geoid"]
        meta = geoid_meta.get(g)
        if meta is None:
            meta = geoid_meta[g] = {"name": r["place_name"], "state": r["state_code"],
                                    "classification": place_classification(namelsad),
                                    "counties": set()}
        meta["counties"].add(r["county_name"])
        by_name.setdefault((r["state_code"], norm_place(r["place_name"])), []).append(
            {"geoid": g, "county": norm_place(re.sub(r"\s+County$", "", r["county_name"]))})
    return by_name, geoid_meta


def resolve_place_geoid(rec, by_name):
    """Officeholder -> Census place GEOID (or None). Unique name-in-state match;
    ambiguous names are disambiguated by the County: hint in the description."""
    cand = by_name.get((rec.get("state_abbr"), norm_place(officeholder_place_name(rec))), [])
    if len(cand) == 1:
        return cand[0]["geoid"]
    if len(cand) > 1:
        m = re.search(r"County:\s*([^;]+)", rec.get("description") or "")
        if m:
            ch = norm_place(re.sub(r"\s+County$", "", m.group(1).strip()))
            nar = [c for c in cand if c["county"] == ch]
            if len(nar) == 1:
                return nar[0]["geoid"]
    return None


def city_arrays(counties):
    return "[" + ", ".join(yval(c) for c in counties) + "]"


# --------------------------------------------------------------------------- #
# Executive branch nodes + the authority axis (§ -> office)
#
# The Code empowers the executive branch, but the mirror only had legislative
# Bodies. These nodes are minted from the Code's own enumerations — 5 U.S.C.
# §101 (the departments) and §5312 (Executive Schedule Level I, the cabinet-rank
# officers) — and the section_authority_edges (a committed input from
# scripts/extract_authority.py) render as reciprocal "empowered by" links here.
# The 59,740 section files are never touched; the edge lives on the office node.
# --------------------------------------------------------------------------- #

def exec_body_file(title, classification, code, extra_fm, sources, intro,
                   auth_header, auth_verb, edges, cap=25):
    lines = ["type: Body", f"title: {yval(title)}",
             f"classification: {yval(classification)}",
             'chamber: "executive"', f"code: {yval(code)}"]
    lines += extra_fm
    lines.append("sources:")
    for field, src in sources:
        lines += [f"  - field: {field}", f"    source: {yval(src)}"]
    lines += ["confidence: official",
              f"tags: [body, executive, {classification}]",
              f"timestamp: {yval(CONGRESS_DATE)}"]
    body = [f"# {title}", "", intro, ""]
    if edges:
        sample = " A sample:" if len(edges) > cap else ""
        body += [f"## {auth_header}", "",
                 f"{len(edges):,} sections of the U.S. Code {auth_verb}.{sample}", ""]
        for e in edges[:cap]:
            body.append(f"- [{e['citation']}](/{e['path']})")
        if len(edges) > cap:
            body.append(f"- …and {len(edges) - cap:,} more (full set in "
                        "data/section_authority_edges.jsonl)")
        body.append("")
    return "---\n" + "\n".join(lines) + "\n---\n\n" + "\n".join(body).rstrip() + "\n"


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def load(name):
    return [json.loads(l) for l in (DATA / name).open()]


def main():
    officeholders = load("officeholders-v3.jsonl")
    bodies = load("bodies.jsonl")
    leadership = load("leadership.jsonl")
    memberships = load("committee_memberships.jsonl")
    candidates = load("fec_candidates.jsonl")
    acs_county = load("acs_county.jsonl")
    acs_cd = load("acs_cd.jsonl")
    crosswalk = load("place_county_crosswalk.jsonl")
    place_to_cslug = place_resolver(acs_county, crosswalk)
    county_district_edges = load("county_district_edges.jsonl")

    # --- geographic edge layer: county fips -> district edges, and the full
    #     district node set (edge targets + districts legislators represent) ---
    district_nodes = {}                 # node_id -> (dtype, state, ident)

    def reg_district(dt, state, ident):
        district_nodes.setdefault(district_node_id(dt, state, ident), (dt, state, ident))

    edges_by_county = {}
    for e in county_district_edges:
        dt = e["type"]
        ident = cd_ident(e["district_label"]) if dt == "CD" else leg_ident(e["district_label"])
        reg_district(dt, e["district_state"], ident)
        edges_by_county.setdefault(canonical_fips(e["county_geoid"]), []).append(
            (edge_node_id(e), dt, district_title(dt, e["district_state"], ident),
             e["area_weight"]))
    for lst in edges_by_county.values():
        lst.sort(key=lambda x: (DTYPE_RANK[x[1]], -x[3], x[0]))
    for row in acs_cd:                              # keep every existing ACS CD node
        reg_district("CD", row["state_abbr"], row["district"])
    for rec in officeholders:                       # ensure represents targets exist
        p = person_district_parts(rec)
        if p:
            reg_district(*p)

    bodies_by_code = {b["code"]: b for b in bodies}
    comm_codes = committee_codes(bodies)
    enrichment = build_enrichment(leadership, memberships, bodies_by_code, comm_codes)

    # reverse index: body code -> its leaders, and -> member count
    leaders_of, members_count = {}, {}
    name_to_pid = {norm_name(r.get("full_name") or ""): r.get("person_id")
                   for r in officeholders if r.get("full_name")}
    for m in memberships:
        members_count[m["body_code"]] = members_count.get(m["body_code"], 0) + 1
        role = ROLE_MAP.get(m["committee_title"], "member")
        if role in LEADER_ROLES:
            pid = name_to_pid.get(norm_name(m["person_name"]))
            leaders_of.setdefault(m["body_code"], []).append(
                (m["person_name"], role, pid))
    for v in leaders_of.values():
        v.sort(key=lambda t: (t[1], t[0]))

    matched = sum(1 for r in officeholders if r["level"] == "federal"
                  and norm_name(r.get("full_name") or "") in enrichment)

    # ---- plan person paths (disambiguate deterministically) ----
    planned = {}
    for rec in sorted(officeholders, key=lambda r: r["person_id"]):
        planned.setdefault((person_dir(rec, place_to_cslug), slugify(display_name(rec))), []).append(rec)
    person_files = {}
    for (d, base), group in planned.items():
        by_person = {}
        for rec in group:
            slug = base if len(group) == 1 else f"{base}-{rec['person_id'][:8]}"
            by_person.setdefault(slug, []).append(rec)
        for slug, sub in by_person.items():
            for rec in sub:
                final = slug if len(sub) == 1 else f"{slug}-{rec['office_id'][:8]}"
                p = d / f"{final}.md"
                assert p not in person_files, f"collision {p}"
                person_files[p] = rec

    # ---- write ----
    if OUT.exists():
        shutil.rmtree(OUT)

    for path, rec in sorted(person_files.items()):
        enr = enrichment.get(norm_name(rec.get("full_name") or "")) \
            if rec["level"] == "federal" else None
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("---\n" + "\n".join(person_frontmatter(rec, enr))
                        + "\n---\n\n" + "\n".join(person_body(rec, enr)) + "\n",
                        encoding="utf-8")

    for b in sorted(bodies, key=lambda x: x["code"]):
        bid = body_id(b["code"], bodies_by_code, comm_codes)
        path = OUT / (bid + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(body_file(b, bid, bodies_by_code, comm_codes,
                                  leaders_of, members_count.get(b["code"], 0)),
                        encoding="utf-8")

    # ---- candidates (FEC) ----
    cand_plan = {}
    for rec in sorted(candidates, key=lambda r: r["fec_id"]):
        d = OUT / "us" / "states" / (rec.get("state") or "xx").lower() / "candidates"
        cand_plan.setdefault((d, slugify(candidate_name(rec["candidate_name"]))), []).append(rec)
    n_cand = 0
    for (d, base), group in sorted(cand_plan.items(), key=lambda kv: str(kv[0][0]) + kv[0][1]):
        for rec in group:
            slug = base if len(group) == 1 else f"{base}-{rec['fec_id'][-4:].lower()}"
            disp = candidate_name(rec["candidate_name"])
            path = d / f"{slug}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("---\n" + "\n".join(candidate_frontmatter(rec, disp))
                            + "\n---\n\n" + "\n".join(candidate_body(rec, disp)) + "\n",
                            encoding="utf-8")
            n_cand += 1

    # ---- county jurisdictions (ACS, deduped by canonical fips) ----
    oh_count = {}
    for rec in officeholders:
        if rec["level"] in ("county", "municipal"):
            key = ((rec.get("state_abbr") or "").lower(), county_slug(rec, place_to_cslug))
            oh_count[key] = oh_count.get(key, 0) + 1
    seen_fips, n_county = set(), 0
    for row in sorted(acs_county, key=lambda r: canonical_fips(r["county_fips"])):
        cf = canonical_fips(row["county_fips"])
        if cf in seen_fips:
            continue
        seen_fips.add(cf)
        st = row.get("state_abbr")
        if not st:
            continue
        base = re.sub(r",\s*[A-Z]{2}$", "", row.get("county_name") or "")
        cslug = acs_cslug(row)
        title = f"{base}, {st}"
        demog = normalize_demog(row)
        ohc = oh_count.get((st.lower(), cslug), 0)
        intro = (f"County jurisdiction — {ohc} officeholders mapped."
                 if ohc else "County jurisdiction.")
        extra = [f"fips: {yval(cf)}", f"state: {yval(st)}"]
        path = OUT / "us" / "states" / st.lower() / "counties" / cslug / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(jurisdiction_file(title, "county", extra, demog, st.lower(),
                                          intro, district_edges=edges_by_county.get(cf)),
                        encoding="utf-8")
        n_county += 1

    # ---- district jurisdictions (CD demographics from ACS; state-leg + gap CDs sparse) ----
    acs_cd_by_key = {(r["state_abbr"], r["district"]): r for r in acs_cd}
    n_cd = n_sld = 0
    for nid in sorted(district_nodes):
        dt, st, ident = district_nodes[nid]
        title = district_title(dt, st, ident)
        cls = DTYPE_CLASS[dt]
        if dt == "CD":
            row = acs_cd_by_key.get((st, ident))
            demog = normalize_demog(row) if row else None
            extra = [f"state: {yval(st)}", f"district: {yval(title)}"]
            intro = f"Congressional district {title}."
            n_cd += 1
        else:
            demog = None
            extra = [f"state: {yval(st)}",
                     f"chamber: {yval('senate' if dt == 'SS' else 'house')}",
                     f"district: {yval(ident)}"]
            intro = f"{DTYPE_WORD[dt].title()} district {ident} ({st})."
            n_sld += 1
        path = OUT / (nid + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(jurisdiction_file(title, cls, extra, demog, st.lower(), intro),
                        encoding="utf-8")

    # ---- city jurisdictions (incorporated Census places) ----
    by_name, geoid_meta = city_index(crosswalk)

    # (a) filled cities — one node per municipal-officeholder folder, written
    #     into the folder its people already occupy (co-located by construction).
    folders = {}   # (st, cslug, cityslug) -> {n, geoids:{geoid:votes}, label, st_abbr}
    for rec in officeholders:
        if rec["level"] != "municipal":
            continue
        st = (rec.get("state_abbr") or "").lower()
        key = (st, county_slug(rec, place_to_cslug), city_slug(rec))
        f = folders.get(key)
        if f is None:
            f = folders[key] = {"n": 0, "geoids": {},
                                "label": officeholder_place_name(rec),
                                "st_abbr": rec.get("state_abbr")}
        f["n"] += 1
        g = resolve_place_geoid(rec, by_name)
        if g:
            f["geoids"][g] = f["geoids"].get(g, 0) + 1

    written, filled_geoids = set(), set()
    n_city = n_filled = n_resolved = n_skel = n_skipped = 0
    for (st, cslug, cityslug), f in sorted(folders.items()):
        if cslug == "_unresolved" or cityslug == "_unresolved":
            n_skipped += 1                       # county/place couldn't be placed — honest gap
            continue
        g = (sorted(f["geoids"].items(), key=lambda kv: (-kv[1], kv[0]))[0][0]
             if f["geoids"] else None)
        meta = geoid_meta.get(g)
        if meta:
            filled_geoids.add(g)
            n_resolved += 1
            title, cls, counties = f"{meta['name']}, {meta['state']}", meta["classification"], sorted(meta["counties"])
        else:
            lbl = f["label"] or cityslug.replace("-", " ").title()
            title = f"{lbl}, {f['st_abbr']}" if f["st_abbr"] else lbl
            cls, counties = "city", []
        extra = ([f"geoid: {yval(g)}"] if g else []) + [f"state: {yval(st.upper())}"]
        if counties:
            extra.append(f"counties: {city_arrays(counties)}")
        srcs = [("government", f"Atlas officeholders v3 ({DATASET_DATE})")]
        if g:
            srcs.append(("identity", "Census place GEOID (place_county_crosswalk)"))
        intro = f"{cls.title()} government — {f['n']} officeholder{'' if f['n'] == 1 else 's'} mapped."
        path = OUT / "us" / "states" / st / "counties" / cslug / "municipalities" / cityslug / "index.md"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(jurisdiction_file(title, cls, extra, None, st, intro, sources=srcs),
                        encoding="utf-8")
        written.add(path)
        n_city += 1
        n_filled += 1

    # (b) skeleton — every incorporated place with no officeholder node yet:
    #     a truthful stub (exists, governed, unmirrored) keyed by GEOID, nested
    #     under its primary county. Same discipline as the county skeleton.
    for g in sorted(geoid_meta):
        if g in filled_geoids:
            continue
        meta = geoid_meta[g]
        st = meta["state"].lower()
        counties = sorted(meta["counties"])
        cslug = slugify(norm_county(re.sub(r"\s+County$", "", counties[0])))
        cityslug = slugify(meta["name"])
        path = OUT / "us" / "states" / st / "counties" / cslug / "municipalities" / cityslug / "index.md"
        if path in written:                      # slug collision — filled node or prior stub wins
            n_skipped += 1
            continue
        extra = [f"geoid: {yval(g)}", f"state: {yval(meta['state'])}",
                 f"counties: {city_arrays(counties)}"]
        intro = f"{meta['classification'].title()} — no officeholders mirrored yet."
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(jurisdiction_file(
            title=f"{meta['name']}, {meta['state']}", classification=meta["classification"],
            extra_fm=extra, demog=None, st=st, body_intro=intro,
            sources=[("identity", "Census place GEOID (place_county_crosswalk)")]),
            encoding="utf-8")
        written.add(path)
        n_city += 1
        n_skel += 1

    # ---- executive branch nodes + authority axis (§ -> office) ----
    exec_offices = load("executive_offices.jsonl")
    authority = load("section_authority_edges.jsonl")
    edges_by_target = {}
    for e in authority:
        edges_by_target.setdefault(e["target"], []).append(e)
    for lst in edges_by_target.values():
        lst.sort(key=lambda e: (e["title"] or 0, e["section"]))

    EXEC = OUT / "us" / "executive"
    n_exec = 0
    for r in sorted(exec_offices, key=lambda x: x["slug"]):
        dept_id = f"us/executive/{r['slug']}"
        head = r["head"]
        office_id = f"{dept_id}/{head['slug']}"
        is_dept = r["kind"] == "department"
        estab = ("5 U.S.C. § 101 (Executive departments)" if is_dept
                 else "5 U.S.C. § 5312 (Executive Schedule, Level I)")

        # department / agency node
        dept_extra = [f"head: {yval(office_id)}"]
        if r.get("parent"):
            dept_extra.append(f"parent: {yval(r['parent'])}")
        if is_dept:
            intro = (f"Executive department, established by 5 U.S.C. § 101. "
                     f"Headed by the [{head['name']}](/{office_id}.md).")
        else:
            par = (f" It sits within the [Executive Office of the President]"
                   f"(/{r['parent']}.md)." if r.get("parent") else "")
            intro = (f"Executive agency. Its head, the [{head['name']}](/{office_id}.md), "
                     f"is a Level I position in the Executive Schedule (5 U.S.C. § 5312).{par}")
        (EXEC / r["slug"]).mkdir(parents=True, exist_ok=True)
        (EXEC / r["slug"] / "index.md").write_text(exec_body_file(
            title=r["name"], classification="executive-department" if is_dept else "executive-agency",
            code=f"EXEC-{r['slug'].upper()}", extra_fm=dept_extra,
            sources=[("definition", estab)], intro=intro,
            auth_header="Referenced by the U.S. Code",
            auth_verb=f"reference this {'department' if is_dept else 'agency'}",
            edges=edges_by_target.get(dept_id, [])), encoding="utf-8")

        # head office node (the position the law empowers)
        seat = "department" if is_dept else "agency"
        office_intro = (f"Cabinet-rank office (Executive Schedule Level I, 5 U.S.C. § 5312), "
                        f"head of the [{r['name']}](/{dept_id}/index.md).")
        (EXEC / r["slug"] / f"{head['slug']}.md").write_text(exec_body_file(
            title=head["name"], classification="executive-office",
            code=f"EXEC-{r['slug'].upper()}-{head['slug'].upper()}",
            extra_fm=[f"parent: {yval(dept_id)}", 'schedule_level: "I"'],
            sources=[("definition", "5 U.S.C. § 5312 (Executive Schedule, Level I)")],
            intro=office_intro,
            auth_header="Empowered by the U.S. Code",
            auth_verb="vest authority in this office",
            edges=edges_by_target.get(office_id, [])), encoding="utf-8")
        n_exec += 2

    print(f"candidate files: {n_cand}   county jurisdictions: {n_county}   "
          f"CD nodes: {n_cd}   state-leg district nodes: {n_sld}   "
          f"county->district edges: {len(county_district_edges)}")
    print(f"city jurisdictions: {n_city}  (filled {n_filled}: {n_resolved} GEOID-resolved; "
          f"skeleton {n_skel}; skipped {n_skipped})")
    print(f"executive nodes: {n_exec}  (departments/agencies + offices)   "
          f"authority edges: {len(authority)} across "
          f"{len({e['section'] for e in authority})} sections")
    print(f"person files: {len(person_files)}  "
          f"(federal enriched: {matched}/{sum(1 for r in officeholders if r['level']=='federal')})")
    print(f"body files: {len(bodies)}  "
          f"(chambers/exec {sum(1 for b in bodies if b['type'] in INSTITUTIONS)}, "
          f"committees {sum(1 for b in bodies if b['type']=='committee')}, "
          f"subcommittees {sum(1 for b in bodies if b['type']=='subcommittee')})")


if __name__ == "__main__":
    main()
