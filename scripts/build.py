#!/usr/bin/env python3
"""Build the OKF entity tree from the raw source exports in data/.

Inputs (committed raw, one JSON object per line):
  officeholders-v2.jsonl        Atlas — person->seat records          (11,285)
  bodies.jsonl                  congress-legislators — institutions      (233)
  leadership.jsonl              current federal leadership roles          (28)
  committee_memberships.jsonl   person->committee edges                (3,879)

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
DATASET_DATE = "2026-06-20"          # officeholders v2 build date
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

def county_slug(rec):
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
    return "_unresolved"


def city_slug(rec):
    m = re.match(r"(.+?), FL$", rec.get("jurisdiction_label") or "")
    if m:
        return slugify(m.group(1))
    m = re.match(r"Mayor of (.+)$", rec.get("title") or "")
    if m:
        return slugify(m.group(1))
    return "_unresolved"


def person_dir(rec):
    lvl, st = rec["level"], (rec.get("state_abbr") or "").lower()
    if lvl == "federal":
        return OUT / "us" / "people"
    if lvl == "state":
        return OUT / "us" / "states" / st / "people"
    if lvl == "county":
        return OUT / "us" / "states" / st / "counties" / county_slug(rec) / "people"
    if lvl == "municipal":
        return (OUT / "us" / "states" / st / "counties" / county_slug(rec)
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
    out += ["", f"Generated from the Atlas officeholders v2 export ({DATASET_DATE})."]
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
# main
# --------------------------------------------------------------------------- #

def load(name):
    return [json.loads(l) for l in (DATA / name).open()]


def main():
    officeholders = load("officeholders-v2.jsonl")
    bodies = load("bodies.jsonl")
    leadership = load("leadership.jsonl")
    memberships = load("committee_memberships.jsonl")

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
        planned.setdefault((person_dir(rec), slugify(display_name(rec))), []).append(rec)
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

    print(f"person files: {len(person_files)}  "
          f"(federal enriched: {matched}/{sum(1 for r in officeholders if r['level']=='federal')})")
    print(f"body files: {len(bodies)}  "
          f"(chambers/exec {sum(1 for b in bodies if b['type'] in INSTITUTIONS)}, "
          f"committees {sum(1 for b in bodies if b['type']=='committee')}, "
          f"subcommittees {sum(1 for b in bodies if b['type']=='subcommittee')})")


if __name__ == "__main__":
    main()
