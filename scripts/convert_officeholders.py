#!/usr/bin/env python3
"""Convert the raw Atlas officeholders JSONL into the OKF entity tree.

Reads  data/officeholders-v2.jsonl  (canonical raw export, committed as-is)
Writes data/jurisdictions/**        (one Person file per officeholder record)

Deterministic by construction: records are processed in sorted order, keys
are emitted in a fixed order, and rerunning on the same input produces a
byte-identical tree (the determinism discipline — see the technical brief).
"""

import json
import re
import shutil
import sys
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RAW = REPO / "data" / "officeholders-v2.jsonl"
OUT = REPO / "data" / "jurisdictions"
DATASET_DATE = "2026-06-20"  # officeholders v2 build date (see raw export)


def slugify(text):
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", text) or "unnamed"


def yval(v):
    """Serialize a scalar for YAML. JSON string quoting is valid YAML."""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    return json.dumps(v, ensure_ascii=False)


def norm_county(name):
    """Unify spelling variants so one county gets one directory."""
    return re.sub(r"\bSaint\b", "St", name)


def county_slug(rec):
    """Derive the county directory slug for county/municipal records."""
    label = norm_county(rec.get("jurisdiction_label") or "")
    m = re.match(r"(.+?) County, FL$", label)
    if m:
        return slugify(m.group(1))
    if rec["level"] == "municipal":
        d = rec.get("description") or ""
        m = re.search(r"County:\s*([^;]+)", d)
        if m:
            return slugify(norm_county(m.group(1).strip()))
    # fall back to the office title, e.g. "Sheriff of Pasco County"
    title = rec.get("title") or ""
    m = re.search(r"\bof\s+(.+?)\s+County\b", title) or \
        re.match(r"(.+?)\s+County\b", title)
    if m:
        return slugify(norm_county(m.group(1)))
    return "_unresolved"


def city_slug(rec):
    label = rec.get("jurisdiction_label") or ""
    m = re.match(r"(.+?), FL$", label)
    if m:
        return slugify(m.group(1))
    m = re.match(r"Mayor of (.+)$", rec.get("title") or "")
    if m:
        return slugify(m.group(1))
    return "_unresolved"


def person_dir(rec):
    lvl = rec["level"]
    st = (rec.get("state_abbr") or "").lower()
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


def build_frontmatter(rec):
    """Fixed key order; nulls omitted. Returns list of YAML lines."""
    lines = ["type: Person"]
    lines.append(f"title: {yval(display_name(rec))}")
    desc = rec.get("title") or ""
    jl = rec.get("jurisdiction_label")
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
    contact = [(k, rec.get(k)) for k in ("email", "phone", "website") if rec.get(k)]
    if contact:
        lines.append("contact:")
        for k, v in contact:
            lines.append(f"  {k}: {yval(v)}")
    if rec.get("image_url"):
        lines.append(f"image: {yval(rec['image_url'])}")
    tenure = [(k2, rec.get(k1)) for k1, k2 in
              (("start_date", "start"), ("end_date", "end"), ("is_current", "current"),
               ("tenure_notes", "notes")) if rec.get(k1) is not None]
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
    srcs = []
    for field, key in (("office", "office_source"), ("tenure", "tenure_source"),
                       ("jurisdiction", "jurisdiction_source")):
        if rec.get(key):
            srcs.append((field, rec[key]))
    if srcs:
        lines.append("sources:")
        for field, s in srcs:
            lines.append(f"  - field: {field}")
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


def build_body(rec):
    name = display_name(rec)
    role = rec.get("title") or "officeholder"
    jl = rec.get("jurisdiction_label")
    where = f" ({jl})" if jl and jl not in role else ""
    cur = "Current" if rec.get("is_current") else "Former"
    out = [f"# {name}", "", f"{cur} {role}{where}.", ""]
    out.append("## Sources")
    out.append("")
    any_src = False
    for field, key in (("office", "office_source"), ("tenure", "tenure_source"),
                       ("jurisdiction", "jurisdiction_source")):
        if rec.get(key):
            out.append(f"- {field}: {rec[key]}")
            any_src = True
    if not any_src:
        out.append("- (no field-level source recorded in the raw export)")
    out.append("")
    out.append(f"Generated from the Atlas officeholders v2 export ({DATASET_DATE}).")
    return out


def main():
    recs = [json.loads(l) for l in RAW.open()]
    recs.sort(key=lambda r: r["person_id"])

    # Assign paths; disambiguate slug collisions deterministically with the
    # first 8 chars of person_id (applied to *all* members of a collision set).
    planned = {}
    for rec in recs:
        d = person_dir(rec)
        base = slugify(display_name(rec))
        planned.setdefault((d, base), []).append(rec)

    files = {}
    for (d, base), group in planned.items():
        # First pass: person_id disambiguates different people sharing a name.
        # Second pass: office_id disambiguates one person holding two offices.
        by_person = {}
        for rec in group:
            slug = base if len(group) == 1 else f"{base}-{rec['person_id'][:8]}"
            by_person.setdefault(slug, []).append(rec)
        for slug, subgroup in by_person.items():
            for rec in subgroup:
                final = slug if len(subgroup) == 1 else f"{slug}-{rec['office_id'][:8]}"
                path = d / f"{final}.md"
                assert path not in files, f"path collision: {path}"
                files[path] = rec

    if OUT.exists():
        shutil.rmtree(OUT)
    for path, rec in sorted(files.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        content = "---\n" + "\n".join(build_frontmatter(rec)) + "\n---\n\n" \
                  + "\n".join(build_body(rec)) + "\n"
        path.write_text(content, encoding="utf-8")

    print(f"records: {len(recs)}  files written: {len(files)}")
    by_level = {}
    for rec in files.values():
        by_level[rec["level"]] = by_level.get(rec["level"], 0) + 1
    for lvl in sorted(by_level):
        print(f"  {lvl}: {by_level[lvl]}")


if __name__ == "__main__":
    sys.exit(main())
