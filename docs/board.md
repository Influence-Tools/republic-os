# The Board

`viz/board.html` is the Board — a rebuilt *view* of the canonical tree, never a
source. It is a nationwide county choropleth with four lenses — **income,
population, poverty, and partisan lean** (the head-count D/R balance of each
county's covering state + federal representatives) — that is **zoomable and
pannable** (scroll to zoom 1×–16× toward the cursor, drag to pan, double-click to
reset). Any county opens a drill-down of its officeholders, its demographics, and
the **districts + representatives** that cover it (congressional, state senate,
and state house, each with the share of the county it covers).

## Pipeline

```text
data/officeholders-v3.jsonl ─┐
data/acs_county.jsonl        ├─ scripts/build_viz.py ─> viz/board.html (inlined)
data/place_county_crosswalk  ┤                        └> viz/county_*.json (companions)
data/fec_candidates, acs_cd ─┘
```

`build_viz.py` resolves each official to a county with the **same**
`build.place_resolver` + `county_slug` the tree uses, so the Board and the tree
agree by construction. It then does two things:

1. Writes `viz/county_data.json` and `viz/county_detail.json` — human-readable,
   diffable companions.
2. **Injects** the fresh data straight into `board.html`, rewriting three marked
   lines: `const D` (per-county summary), `const CDETAIL` (per-county rosters),
   and `const TOTALS` (the header counts).

## Why the data is inlined

The Board is deployed as a **self-contained Artifact**, and the Artifact CSP
blocks every external request — no `fetch`, no external scripts, styles, or
fonts. So the county data cannot be loaded at runtime; it must live inside
`board.html`. That is why `build_viz.py` writes into the file rather than letting
the page read the JSON companions (nothing reads them — they exist for diffs).

The header totals (officeholders, candidates, counties, districts) read from the
injected `const TOTALS` object — never hardcoded — so they cannot drift out of
sync on the next rebuild.

## Rebuild

```bash
make board       # regenerate board.html + the JSON companions from the tree
```

`board.html` is deterministic: two runs are byte-identical.

## Redeploy the Artifact

Editing `board.html` in the repo does **not** update a live Artifact — the
deployed copy is a snapshot. After `make board`, the Board must be **republished**
to its existing Artifact URL for the change to appear on claude.ai.

Republishing to the *same* URL requires passing that URL back to the publish step
(`Artifact url=<existing-url>`); publishing without it mints a new URL. Keep the
current Board Artifact URL in the team's deployment record so redeploys stay in
place instead of scattering new links.
