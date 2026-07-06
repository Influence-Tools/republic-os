#!/usr/bin/env python3
"""Extract the authority axis: U.S. Code section -> executive office/department.

Named-reference extraction (v1): matches the canonical office and department
names in data/executive_offices.jsonl against each section's operative text
(the '## Text' body, excluding historical Notes), and emits one edge per
(section, target) into data/section_authority_edges.jsonl.

Deterministic and mechanical — no NLP, no network. This is a committed input,
generated like county_district_edges.jsonl; scripts/build.py renders it into
reciprocal links on the executive office nodes (the section files are never
touched). Relative references ("the Secretary") are out of scope for v1.

Usage:  python3 scripts/extract_authority.py
"""

import json
import re
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OFFICES = REPO / "data" / "executive_offices.jsonl"
CODE = REPO / "legal" / "us" / "code"
OUT = REPO / "data" / "section_authority_edges.jsonl"

# An alias immediately preceded by one of these is a *different*, lower office
# (a Deputy/Assistant/Under Secretary, a Solicitor/Inspector General, etc.) —
# not the cabinet-rank principal, so it must not match.
SUBORDINATE_PREFIX = re.compile(
    r"(?:Deputy|Assistant|Associate|Under|Acting|Solicitor|Inspector|Principal|"
    r"Special|Vice|Former|Additional)\s*$")


def load_targets():
    """Return alias-matchers sorted longest-first: (regex, target_id, name, kind, rel)."""
    targets = []
    for line in OFFICES.open():
        r = json.loads(line)
        dept_id = f"us/executive/{r['slug']}"
        office_id = f"{dept_id}/{r['head']['slug']}"
        rel_kind = "references"          # a department/agency mention
        for alias in r["aliases"]:
            targets.append((alias, dept_id, r["name"], r["kind"], rel_kind))
        for alias in r["head"]["aliases"]:      # the officer the law empowers
            targets.append((alias, office_id, r["head"]["name"], "office", "empowers"))
    # longest alias first so "Secretary of the Treasury" wins over any substring
    targets.sort(key=lambda t: -len(t[0]))
    return [(re.compile(r"\b" + re.escape(a) + r"\b"), tid, name, kind, rel)
            for a, tid, name, kind, rel in targets]


def operative_text(md):
    """The section's live text only — frontmatter and historical Notes dropped."""
    parts = md.split("---", 2)
    body = parts[2] if len(parts) >= 3 else md
    return re.split(r"\n##\s+Notes", body, maxsplit=1)[0]


def frontmatter_field(md, key):
    m = re.search(rf"(?m)^{key}:\s*(.+)$", md.split("---", 2)[1] if "---" in md else md)
    if not m:
        return None
    v = m.group(1).strip()
    return v[1:-1] if len(v) >= 2 and v[0] == v[-1] == '"' else v


def main():
    targets = load_targets()
    edges = []
    for path in sorted(CODE.rglob("section-*.md")):
        md = path.read_text(encoding="utf-8")
        text = operative_text(md)
        section = frontmatter_field(md, "source_identifier")
        citation = frontmatter_field(md, "citation")
        title_num = frontmatter_field(md, "title_number")
        if not section:
            continue
        rel_path = str(path.relative_to(REPO))
        # (target_id) -> [name, kind, rel, mentions]; keep the most-specific hit
        hits = {}
        for rx, tid, name, kind, rel in targets:
            occ = 0
            for m in rx.finditer(text):
                pre = text[max(0, m.start() - 24):m.start()]
                if SUBORDINATE_PREFIX.search(pre):
                    continue
                occ += 1
            if occ:
                cur = hits.get(tid)
                if cur is None:
                    hits[tid] = [name, kind, rel, occ]
                else:
                    cur[3] += occ
        for tid, (name, kind, rel, mentions) in hits.items():
            edges.append({
                "section": section,
                "citation": citation,
                "path": rel_path,
                "title": int(title_num) if title_num and title_num.isdigit() else None,
                "target": tid,
                "target_name": name,
                "target_kind": kind,
                "relationship": rel,
                "mentions": mentions,
            })

    edges.sort(key=lambda e: (e["section"], e["target"]))
    with OUT.open("w", encoding="utf-8") as f:
        for e in edges:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")

    sections = len({e["section"] for e in edges})
    offices = len({e["target"] for e in edges if e["target_kind"] == "office"})
    print(f"authority edges: {len(edges)}  "
          f"(sections with authority: {sections}; distinct targets hit: {len({e['target'] for e in edges})}; "
          f"office targets: {offices})")
    print(f"wrote {OUT.relative_to(REPO)}")


if __name__ == "__main__":
    main()
