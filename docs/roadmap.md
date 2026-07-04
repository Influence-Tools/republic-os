# Roadmap

An honest account of what exists, what's next, and what's further out. This repository will always be evolving; there is no "finished."

## Done

- **The substrate** — repo-canonical, OKF markdown + YAML frontmatter, JSON-Schema validated, deterministic build (byte-identical on rerun).
- **Four entity types, 17,506 files** — Person (11,285), Body (233), Candidate (2,494), Jurisdiction (3,494).
- **The federal government, structurally** — every member of Congress, the chambers, 49 committees and 181 subcommittees with their leadership, and every member's committee seats.
- **The nationwide county skeleton** — all 3,131 U.S. counties as demographic nodes, plus 363 congressional districts, from Census ACS.
- **The 2026 federal candidate field** — every FEC filing as a Candidate.
- **Florida to the ground** — officeholders down to the municipal level across all 67 counties.
- **The pipeline** — `make build` / `validate` / `changelog` / `check`, standard-library only.
- **The changelog engine** — git diffs rendered as a plain-language civic changelog.
- **The Board** — a self-contained coverage map ([`viz/board.html`](../viz/board.html)).

## Next

- **Self-updating mirror** — a GitHub Action running `make check` on every push, then a scheduled job that pulls a fresh Atlas export, rebuilds, and commits the changelog automatically. This is the point where the mirror maintains itself and the daily civic changelog becomes real (the first *re-sync* diff, where only genuine government changes surface).
- **The demographic choropleth** — the Board already has ACS data for every county; shade the map by population, income, and poverty, turning it from a coverage indicator into an instrument.
- **State and local bodies** — Bodies currently exist only at the federal level. Mint them for state legislatures and, following the Florida depth, county commissions and city councils.
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
