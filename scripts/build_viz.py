#!/usr/bin/env python3
"""Rebuild the Board's viz data from the officeholders export + ACS counties.

The Board (viz/board.html) is a rebuilt *view* of the canonical tree, never a
source. This regenerates its two companions deterministically:

  viz/county_data.json    {fips: {name, state, pop, income, poverty, home,
                           unemp, oh}}  — nationwide choropleth + officeholder
                           count per county.
  viz/county_detail.json  {fips: {slug, county:[{n,r}], munis:[{m, p:[{n,r}]}]}}
                           — per-county drill-down roster.

County/municipal officials are mapped to a county the same way build.py places
them in the tree (shared county_slug + place_resolver), so the viz and the tree
agree by construction. Officials whose county still can't be resolved to an ACS
FIPS (ambiguous names, county-level rows mislabeled municipal, CT planning
regions, label-less rows) are counted in the tree but do not appear in the
county-keyed viz — an honest gap, not a silent drop; the tally is printed.

Deterministic: sorted iteration, fixed key order. Two runs are byte-identical.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402  — reuse the exact tree-placement helpers

DATA = build.DATA
VIZ = build.REPO / "viz"


def city_name(rec):
    """Human city label for a municipal rec (matches the tree's municipality)."""
    m = re.match(r"(.+?),\s*[A-Z]{2}$", rec.get("jurisdiction_label") or "")
    if m:
        return m.group(1).strip()
    m = re.match(r"Mayor of (.+)$", rec.get("title") or "")
    if m:
        return m.group(1).strip()
    return build.city_slug(rec).replace("-", " ").title()


def main():
    officeholders = build.load("officeholders-v3.jsonl")
    acs_county = build.load("acs_county.jsonl")
    candidates = build.load("fec_candidates.jsonl")
    acs_cd = build.load("acs_cd.jsonl")
    place_to_cslug = build.place_resolver(acs_county, build.load("place_county_crosswalk.jsonl"))

    # slug -> fips, and fips -> (name, state, demographics), deduped by fips
    slug_to_fips = {}
    county_meta = {}
    for row in sorted(acs_county, key=lambda r: build.canonical_fips(r["county_fips"])):
        cf = build.canonical_fips(row["county_fips"])
        if cf in county_meta:
            continue
        st = row.get("state_abbr")
        if not st:
            continue
        base = re.sub(r",\s*[A-Z]{2}$", "", row.get("county_name") or "")
        cslug = build.slugify(build.norm_county(re.sub(r"\s+County$", "", base)))
        demog = build.normalize_demog(row)
        county_meta[cf] = {"name": base, "state": st, "slug": cslug, "demog": demog}
        slug_to_fips[(st.lower(), cslug)] = cf

    # officials grouped by resolved county key (state, slug)
    oh_count = defaultdict(int)
    county_roster = defaultdict(list)          # key -> [(name, role)]
    muni_roster = defaultdict(lambda: defaultdict(list))  # key -> city -> [(name, role)]
    unresolved = 0
    for rec in officeholders:
        if rec["level"] not in ("county", "municipal"):
            continue
        key = ((rec.get("state_abbr") or "").lower(), build.county_slug(rec, place_to_cslug))
        oh_count[key] += 1
        name = rec.get("full_name") or rec.get("title") or "Unknown"
        role = rec.get("title") or ""
        if rec["level"] == "county":
            county_roster[key].append((name, role))
        else:
            muni_roster[key][city_name(rec)].append((name, role))
        if key not in slug_to_fips:
            unresolved += 1

    # ---- county_data.json (nationwide) ----
    county_data = {}
    for cf, meta in sorted(county_meta.items()):
        d = meta["demog"]
        key = (meta["state"].lower(), meta["slug"])
        county_data[cf] = {
            "name": meta["name"],
            "state": meta["state"],
            "pop": d.get("population"),
            "income": d.get("median_household_income"),
            "poverty": d.get("poverty_rate"),
            "home": d.get("homeownership_rate"),
            "unemp": d.get("unemployment_rate"),
            "oh": oh_count.get(key, 0),
        }

    # ---- county_detail.json (only counties with resolved officials) ----
    county_detail = {}
    keys_with_people = set(county_roster) | set(muni_roster)
    for key in keys_with_people:
        cf = slug_to_fips.get(key)
        if cf is None:
            continue
        county = [{"n": n, "r": r} for n, r in sorted(county_roster.get(key, []))]
        munis = []
        for city in sorted(muni_roster.get(key, {})):
            people = [{"n": n, "r": r} for n, r in sorted(muni_roster[key][city])]
            munis.append({"m": city, "p": people})
        county_detail[cf] = {"slug": key[1], "county": county, "munis": munis}
    county_detail = {k: county_detail[k] for k in sorted(county_detail)}

    totals = {
        "people": len(officeholders),
        "candidates": len(candidates),
        "counties": len(county_data),
        "districts": len(acs_cd),
    }

    VIZ.mkdir(exist_ok=True)
    # Human-readable / diffable companions (not read by the Board itself).
    (VIZ / "county_data.json").write_text(
        json.dumps(county_data, ensure_ascii=False, sort_keys=True) + "\n")
    (VIZ / "county_detail.json").write_text(
        json.dumps(county_detail, ensure_ascii=False, sort_keys=True) + "\n")

    # The Board is a self-contained Artifact (CSP blocks fetch), so its data is
    # inlined. Inject the fresh dicts + totals into the three marked const lines.
    inject_board(county_data, county_detail, totals)

    total_oh = sum(oh_count.values())
    print(f"county_data.json:   {len(county_data)} counties, "
          f"{sum(1 for v in county_data.values() if v['oh'])} with officeholders")
    print(f"county_detail.json: {len(county_detail)} counties with rosters")
    print(f"officials mapped: {total_oh - unresolved}/{total_oh}  "
          f"(county-unresolvable, tree-only: {unresolved})")
    print(f"board.html injected: totals={totals}")


def inject_board(county_data, county_detail, totals):
    """Rewrite board.html's three injected const lines in place. The data must
    be inlined (self-contained Artifact), so build the Board here rather than
    letting it fetch the JSON companions."""
    board = VIZ / "board.html"
    text = board.read_text()
    payload = {"D": county_data, "CDETAIL": county_detail, "TOTALS": totals}
    for name, obj in payload.items():
        literal = "const %s = %s;" % (
            name, json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")))
        pat = re.compile(r"^const %s = .*;$" % name, re.M)
        if not pat.search(text):
            raise SystemExit(f"board.html: injection marker 'const {name} = …;' not found")
        text = pat.sub(lambda _m, s=literal: s, text, count=1)
    board.write_text(text)


if __name__ == "__main__":
    main()
