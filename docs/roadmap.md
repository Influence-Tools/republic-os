# Roadmap

An honest account of what exists, what's next, and what's further out. This repository will always be evolving; there is no "finished."

## Done

- **The substrate** — repo-canonical, OKF markdown + YAML frontmatter, JSON-Schema validated, deterministic build (byte-identical on rerun).
- **Five entity types, 37,667 files** — Person (13,329), Body (233), Candidate (2,494), Jurisdiction (10,390), LegalText (11,221).
- **The federal government, structurally** — every member of Congress, the chambers, 49 committees and 181 subcommittees with their leadership, and every member's committee seats.
- **The nationwide county skeleton** — all 3,131 U.S. counties as demographic nodes, plus all 435 congressional districts (Census ACS demographics on 363).
- **The authority layer** — every state legislative district (4,927 house, 1,897 senate) linked county↔district↔legislator, nationwide.
- **The legal corpus, seeded wide** — U.S. Code Titles 1–11 and 52 as 11,221 per-section records, mirrored from pinned OLRC XML (release 119-100) with manifests and checksums. Titles 12–54 pending an OLRC XML retry (the GovInfo HTML fallback is not source-quality).
- **The 2026 federal candidate field** — every FEC filing as a Candidate.
- **Florida to the ground** — officeholders down to the municipal level across all 67 counties.
- **The pipeline** — `make build` / `validate` / `changelog` / `check`, standard-library only.
- **The changelog engine** — git diffs rendered as a plain-language civic changelog.
- **The Board** — a self-contained coverage map ([`viz/board.html`](../viz/board.html)).

## Next

- **Self-updating mirror** — the `make check` GitHub Action now guards every push; next is the scheduled job that pulls a fresh Atlas export, rebuilds, and commits the changelog automatically. That is the point where the mirror maintains itself and the daily civic changelog becomes real (the first *re-sync* diff, where only genuine government changes surface).
- **The full U.S. Code** — titles 12–54 as OLRC USLM XML at the same release point (retry in progress on Atlas; the WAF-blocked titles currently exist only as GovInfo HTML, which stays a secondary snapshot).
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
