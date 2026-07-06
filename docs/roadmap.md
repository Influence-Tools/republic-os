# Roadmap

An honest account of what exists, what's next, and what's further out. This repository will always be evolving; there is no "finished."

## Done

- **The substrate** — repo-canonical, OKF markdown + YAML frontmatter, JSON-Schema validated, deterministic build (byte-identical on rerun).
- **Five entity types, 105,743 files** — Person (13,329), Body (275), Candidate (2,494), Jurisdiction (29,905), LegalText (59,740).
- **The federal government, structurally** — every member of Congress, the chambers, 49 committees and 181 subcommittees with their leadership, and every member's committee seats.
- **The nationwide county skeleton** — all 3,131 U.S. counties as demographic nodes, plus all 435 congressional districts (Census ACS demographics on 363).
- **The authority layer** — every state legislative district (4,927 house, 1,897 senate) linked county↔district↔legislator, nationwide.
- **The municipal layer** — every incorporated place in the country (19,513 cities, towns, villages, boroughs) as a first-class Jurisdiction node keyed by Census place GEOID, modelled like a county (place + government fused). 2,229 are filled with their officeholders today (2,217 GEOID-resolved off a 98.8% name→GEOID join); the rest are truthful skeleton stubs — "governed, not yet mirrored" — waiting for depth, the same discipline as the county skeleton.
- **The complete U.S. Code** — every section of all 53 populated titles (Title 53 is reserved), 59,740 per-section records, mirrored from the official OLRC USLM XML at release point 119-100, uniform edition end to end, with manifests and checksums.
- **The authority axis (v1)** — the executive branch minted as nodes from the Code's own enumerations (15 Cabinet departments from 5 U.S.C. § 101, 21 Level I offices from § 5312), and **27,804 edges** linking 17,031 sections to the offices they empower. `scripts/extract_authority.py` → `data/section_authority_edges.jsonl` (a committed input, like the district edges); reciprocal "empowered by" links render on each office node. Named references only for now (cabinet-level); relative refs ("the Secretary") and the agency long tail are next.
- **The 2026 federal candidate field** — every FEC filing as a Candidate.
- **Florida to the ground** — officeholders down to the municipal level across all 67 counties.
- **The pipeline** — `make build` / `validate` / `changelog` / `check`, standard-library only.
- **The changelog engine** — git diffs rendered as a plain-language civic changelog.
- **The Board** — a self-contained coverage map ([`viz/board.html`](../viz/board.html)).

## Next

- **Self-updating mirror** — the `make check` GitHub Action now guards every push; next is the scheduled job that pulls a fresh Atlas export, rebuilds, and commits the changelog automatically. That is the point where the mirror maintains itself and the daily civic changelog becomes real (the first *re-sync* diff, where only genuine government changes surface).
- **Deepen the authority axis** — v1 links cabinet-level *named* references. Next: resolve relative references ("the Secretary", "the Commission") via each title's definitions section; mint the agency long tail (~600 more offices the Code names — EPA, OPM, FCC, GAO…); attach current occupants (a Person for the sitting Secretary, from Atlas); and render the reverse edge on the section files themselves.
- **The Code as a living diff** — re-sync the Code at each new OLRC release point so amendments surface as diffs: a new public law becomes a visible change to the affected sections.
- **The demographic choropleth** — the Board already has ACS data for every county; shade the map by population, income, and poverty, turning it from a coverage indicator into an instrument.
- **Fill the municipal skeleton** — the 19,513 city nodes exist; 2,229 carry officeholders. The work now is depth: pull municipal officeholders for the next states (Texas, California, Ohio all have a spine already), each a diff against a node that's waiting. Municipal ACS demographics would enrich every city node the way ACS already enriches counties.
- **State and local bodies** — Bodies (as distinct institution files) currently exist only at the federal level. Mint them for state legislatures and, following the municipal layer, county commissions where they warrant a Body of their own.
- **Graph export** — a loader that walks the tree and builds the relationship graph (Memgraph) as a materialized view, so the repo can rehydrate the graph rather than the reverse.

## Later

- **The issues axis** — cross-cutting `Issue` entities that link people, bodies, and places across the jurisdiction tree, so the mirror answers "who, nationwide, is touching this issue?" and not only "who governs here?"
- **The money layer** — donations, contracts, and grants as sourced event files; the flows that make influence legible (the Sankey / "circuit-breaker" views from the brief).
- **Meetings and agendas** — the highest-value local data, and the hardest: scraped from Legistar / Granicus / CivicPlus portals and, where towns publish nothing in text, from meeting video. A new agenda item is a diff with a deadline — a mission.
- **Contribution as correction** — let people propose fixes to the mirror (a wrong phone number, a missed meeting) as pull requests, making the public literal contributors to their own civic record.

## Non-goals

Deliberately out of scope, to keep the mirror honest and buildable:

- Becoming an authority. This is a mirror; official sources remain the source of truth.
- A heavy web application, database dependency, or graph-database setup in the core repository. The substrate stays flat files.
- Ingesting all of government at once. Depth follows attention, county by county.
