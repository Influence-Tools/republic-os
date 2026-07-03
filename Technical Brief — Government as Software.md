# Government as Software
## A Technical Brief on Mirroring Power with Git, and Making Influence Visible

**Project:** influence.tools / Republic OS
**Date:** July 3, 2026
**Status:** Exploratory — a thinking document, not a spec

---

## 1. The Premise: Government Is Already Software

Government is an operating system that has been running for 250 years without version control.

The analogy is not decorative — it maps almost mechanically:

| Software | Government |
|---|---|
| Source code | Statutes, ordinances, charters, budgets |
| Running processes | Agencies, departments, courts |
| Maintainers with commit rights | Elected officials, appointed boards |
| A pull request | A bill, a rezoning petition, a budget amendment |
| Code review | Committee hearings, public comment periods |
| The merge vote | The floor vote, the commission vote |
| A release | An adopted budget, an enacted law |
| Changing the maintainers | An election |
| The changelog | **Does not exist. This is the product.** |

Everything on the right side is public. Almost none of it is *legible*. The state of government is scattered across PDFs, agenda portals, campaign finance filings, property rolls, and meeting videos — published, technically, but not readable, not diffable, and above all not *watchable*. A change to your city's zoning code and a change to a codebase are the same category of event; only one of them triggers a notification.

The core move of this project: **we cannot read government's source directly, but we can mirror its observable state into files — and version the mirror.** Git then gives us, for free, the tooling that software has had for decades:

- `git log` — the timeline of any official, body, or rule
- `git diff` — what changed, exactly, since yesterday
- `git blame` — the provenance of any single fact, line by line
- `git show` — one change, in full, on the permanent record
- branches — possible futures (a pending bill is a branch of the law)
- tags — eras (election night, a new congress, an adopted budget)

The honest caveat: the mirror's history starts the day we start watching. Git's value here is entirely forward-looking — from first commit on, *nothing changes unnoticed*. Nobody can quietly pull an item off an agenda; that removal is itself a diff, timestamped, permanent.

**The diff is the product.** Everything else in this brief is a rendering of diffs or a precondition for them.

---

## 2. The Mirror: How the Repo Works

### 2.1 Two axes: geography is a tree, issues are a graph

Every government entity lives in exactly one place in a jurisdiction hierarchy. Issues do not — "short-term rentals" is simultaneously live in 400 counties and three state legislatures. So the repo has two axes:

```
/data
  /jurisdictions              ← the tree (containment)
    /us                          federal spine — thin
      /states/fl
        /counties/st-lucie       seed counties — deep
          people/  bodies/  organizations/  meetings/  elections/  money/
          /municipalities/port-st-lucie/   ← same shape, all the way down
  /issues                     ← the overlay (cross-cutting edges)
    short-term-rentals.md        links to jurisdictions, people, meetings,
    school-curriculum.md         bills, money — anywhere in the tree
  /sources                    ← registry of where every fact comes from
```

The tree can be **complete on day one**: the Census of Governments enumerates every unit in the country (~90,000: 3,144 counties, ~19,500 municipalities, ~12,500 school districts, plus townships and special districts). The map is total; the territory fills in unevenly — and an empty directory is not a failure state, it is a mission ("your city hasn't been mapped").

### 2.2 The fractal schema

A county commissioner and a US senator are the same `Person` schema. A school board and a congressional committee are the same `Body`. A commission meeting and a floor session are the same `Meeting`. One set of schemas, valid at every level — this is what makes "populate down to municipal" a data problem rather than a design problem.

Core entity types: `Jurisdiction`, `Person`, `Body`, `Organization`, `Meeting`, `Election`, `Issue`, `Source` — plus typed **edges carried in frontmatter**: `funds`, `employs`, `owns`, `contracts-with`, `appoints`, `covers`, `sits-on`, `sponsors`.

Every file is Markdown with YAML frontmatter (human-readable, Obsidian-native, agent-parseable), validated against JSON Schema, carrying path-based stable IDs:

```
us/fl/st-lucie/person/jane-doe
us/fl/st-lucie/port-st-lucie/body/city-council
issue/short-term-rentals
```

The repo *is* a graph, serialized as files. Memgraph is a materialized index rebuilt from it — never written to directly. The repo is canonical; the graph is a view. This is what makes every node in the app auditable: click anything → a sourced, timestamped, diffable file.

### 2.3 The determinism discipline

Diffs are only as good as the files are boring. The sync must be deterministic: same entity always at the same path, keys always in the same order, identical formatting every run. Volatile bookkeeping ("checked, nothing changed") lives in a side log — entity files change **only when the government changes**. This single discipline is 80% of the engineering; violate it and the product drowns in noise.

### 2.4 Data flow

```
official sources ──► scrapers ──► repo (canonical) ──► graph (Memgraph index)
 (APIs, agendas,     (Botasaurus,      │
  ACFRs, filings,     Whisper STT       └──► renderings:
  property rolls)     on meeting             changelogs · missions ·
                      video)                 dossiers · videos · feeds
```

Existing infrastructure slots in without invention: Botasaurus scrapes the agenda portals (Legistar, Granicus, CivicPlus cover most municipalities; Legistar has an API), Whisper-on-video extracts what small towns never publish in text, PostGIS resolves ZIP → county → district, Mapbox MCP handles the spatial reasoning, Hermes runs the crons.

---

## 3. Influence as a Tool

"Influence" is usually vibes. To build a tool out of it, it needs an operational definition:

> **Influence is the capacity to change an outcome at a decision point.**

That definition decomposes into three concrete, data-backed questions:

1. **What decisions are pending?** → the diff feed. Agenda items added, bills moving, contracts up for award. In git terms: *what is about to merge*.
2. **Who decides?** → the maintainers. The 5 commissioners, the 7 board members. Small numbers at local level — a city council decision swings on 3 people.
3. **Who reaches the deciders?** → the edges. Who funds them, employs their voters, owns the land in question, covers them in the press, appointed them, sits with them on other boards.

Question 3 is the one nobody has assembled, and the remarkable fact is that the raw material is *already published in standardized public documents*:

| Influence edge | Public source |
|---|---|
| Top 10 employers & taxpayers | The county's own annual financial report (ACFR) — every county and city publishes one; those two tables are a standardized influence roster |
| Who funds local campaigns | FEC (federal), state division of elections, county supervisor of elections |
| Who receives government money | Procurement/vendor records, USAspending |
| Who owns the land | County property appraiser rolls |
| Who shapes narrative | Local outlets, radio, hyperlocal blogs |
| Who lobbies | State/county lobbyist registrations |
| Organized civil society | IRS 990s — churches, foundations, chambers, unions, HOAs |

Assembled per county, this is the **power dossier**: the noun to the diff's verb. The dossier is useful at first commit ("who is in my sphere?"); the diff engine makes it more useful every day after ("what did they just do?"). Together they answer the founding question — *who or what is influencing you* — with receipts.

**The tool, then, is a lens with three focal lengths:**
- **Watch** — subscribe to jurisdictions and issues; receive the changelog
- **Trace** — start from any outcome and walk the edges backward: who sponsored, who voted, who funded, who benefited
- **Act** — see the pending decision, the deciders, the edges you have to them, and the clock ("the vote is Tuesday")

---

## 4. Visualizing Influence

This is the open frontier of the project, so this section explores rather than prescribes. The governing principle first:

> **Every visualization is a query over the repo. Every visible element resolves, on click, to a sourced file. Time scrubbing is git history.**

If a visual can't be traced back to commits, it's an illustration, not an instrument.

### 4.1 The problem with the obvious answer

The obvious answer — dump the graph into a force-directed layout — fails at exactly the scale where it matters. Force-directed graphs become hairballs above ~100 nodes; a single county dossier has more. Force layout also encodes *nothing*: node position is an accident of the physics simulation, so the picture carries no meaning beyond "these things connect." Influence has structure — direction, magnitude, domain, time — and each of those deserves a visual encoding. The county-as-graph is the right *data model*; it is rarely the right *picture*.

What follows is a grammar of views, each answering one question well.

### 4.2 The Sphere — "who is around me?" (ego-network, radial)

The user is the center. Concentric rings are jurisdiction layers: municipality → county → district → state. Within each ring, nodes are the people and organizations of that layer, **sized by influence weight, sorted by proximity to the user's subscribed issues**. This is the dossier as a picture: your 7 officials, 10 employers, 8 donors, 3 media outlets, arranged by how close their power sits to your life.

Radial layouts stay readable because position *means* something (ring = level, angle = sector: government / money / media / civil society). The Mapbox isochrone layer can literally underlay it — influence within a 10-minute walk.

### 4.3 The Flow — "where does the money go?" (Sankey)

Influence's most legible edges are flows with direction and magnitude: dollars from donors → campaigns → officials → votes → contracts → vendors. Sankey diagrams were built for exactly this — conservation of flow, width = magnitude. A county's money view: left edge is sources (donors, taxpayers), right edge is destinations (contractors, grantees), and the middle is the government. Loops — a vendor that is also a donor — are the finding. The visualization *is* the investigation: closed circuits glow.

### 4.4 The Heartbeat — "what is happening?" (diff timeline)

Git log as an EKG. Each jurisdiction is a horizontal track; each commit is a pulse; pulse height = magnitude of change (agenda items added, money moved, seats changed). A healthy, watched county has a rhythm. A flatline means either nothing is happening or *nobody is looking* — and the visualization should distinguish those honestly (data absence ≠ civic absence). Zoom out and the national heartbeat is the product demo: government, visibly alive, changing in real time.

### 4.5 The Board — "where are we?" (coverage choropleth)

The national county map, colored by data depth: dark = unmapped, lit = dossier exists, bright = live sync + active watchers. This is simultaneously an honest data-coverage disclosure and the game board — the Influence App's growth is literally the map lighting up, county by county. First-to-map missions render as beacons on dark territory.

### 4.6 The Delta — "what changed?" (diff highlighting, everywhere)

Not a separate view but a rule across all of them: **what changed this week glows.** New edge, new node, changed value — rendered in a highlight state that decays over time (bright today, dim next week, gone next month). The user's eye goes to the diff without reading anything. This is the visual grammar of "the diff is the product."

### 4.7 Quantifying influence — carefully

Sizing nodes "by influence" requires a number, and here the project must be disciplined, because a wrong number editorializes and a gamed number corrupts.

The defensible approach:

- **Edges are facts. Scores are views.** The repo stores only sourced, typed, weighted edges (dollars, appointments, employment counts). Any influence score is computed downstream, from a **published weight vector** — and the vector is configurable.
- **The natural metric is centrality over a typed multigraph** — PageRank or eigenvector centrality where edge types carry different weights (a $50k donation ≠ a newspaper mention ≠ an appointment power). Memgraph runs this natively.
- **Influence is not scalar — it is conditioned on domain.** The most influential node on zoning is not the most influential node on the school board. Issue-conditioned centrality (run the metric on the subgraph reachable from an issue) gives "influence *on what*," which is the only version that is actually useful.
- **The Left/Right dual lens is a weight vector, not a data fork.** Same graph, same edges, different published weights on what counts as influence. Two users see different rankings and can inspect *exactly why* — which is itself the civic education.

### 4.8 Stack notes

Nothing here requires invention: Cytoscape.js or react-force-graph for the ego/graph views (already planned), d3-sankey for flows, deck.gl or MapLibre for the choropleth board, plain git plumbing for the heartbeat (commit metadata is the dataset). All of them read from the same JSONL export of the repo. The visualizations are cheap *because* the substrate is disciplined.

---

## 5. What This Unlocks (the rendering stack)

One substrate, many renderings — each is a view over the same files:

1. **The dossier** — who holds power in your sphere (useful at first commit)
2. **The changelog** — what changed, per jurisdiction and per issue (compounds daily)
3. **Missions** — diffs with a deadline and a location ("the vote is Tuesday; nobody is watching")
4. **Localized video** — the county changelog as a 30-second script, every sentence traceable to a commit; 3,144 unique, factual, sourced videos a week, because rendering scales where reporting doesn't
5. **Per-user feeds** — ZIP resolution ∩ issue subscriptions
6. **The credential** — the influence score as a verifiable record of civic showing-up

---

## 6. The Game Layer

The Influence App already carries Ingress DNA — touchpoints as portals, NFC taps, missions, meetup events. But a direct port of Ingress would import its core mechanic, and that mechanic is wrong for this: Ingress is PvP territorial warfare between factions, and factionalized civic territory is the disease, not the cure. The translation has to be more surgical.

### 6.1 The adversary is darkness

The defining design decision: **this game is PvE, and the enemy is opacity.**

In Ingress you capture portals *from the other team*. Here, territory is not captured from anyone — it is **illuminated out of the unwatched dark**. A dark county is one where government runs with no one watching: no dossier, no sync, no diffs, no witnesses. The game is the collective project of lighting the map.

| Ingress | Influence |
|---|---|
| Portals at landmarks | Touchpoints at civic locations |
| Capture from the enemy team | Illuminate from darkness |
| Resonators decay without recharging | **Light decays without watching** — a county mapped once but unattended dims back toward dark |
| Control fields over territory | Illuminated counties — coverage, not control |
| Intel map | The coverage choropleth (§4.5) — literally a fog-of-war map |
| Portal under attack alerts | "A decision near you is about to merge unwatched" |
| Anomaly events | Election nights, budget season — scheduled diff storms |
| Faction chat | The pair — one Left, one Right, cross-aisle by construction |

The decay mechanic matters most. It converts the game from conquest (one-time, collectible) to **maintenance** (ongoing, civic). Sustained watching is the whole point; the game should be structurally incapable of rewarding anything else. It also composes exactly with the Delta rendering rule (§4.6): freshness glows, neglect dims — the game state and the data-honesty state are the same pixel.

### 6.2 Play = commits

The second structural decision: **the game state lives in the repo. Verified actions are signed commits.**

An NFC tap, a filed meeting report, a fact-check, a pair handshake — each becomes a commit to the mirror, signed by the player, carrying its proof payload (location, timestamp, attestations). The consequences cascade:

- **Score is a query, not a table.** A player's influence score is computable from `git log --author=<player>` — weighted by action type, decayed by time. No separate game database to corrupt, desync, or dispute.
- **Players are contributors, literally.** The people playing the game are, in git terms, contributors to the public mirror of their government. The civic contribution graph *is* the GitHub-style activity heatmap. "First to map your city" is, precisely, first commit for that jurisdiction.
- **Anti-cheat and data-trust are the same system.** The NFC signed payload and pair attestation that prove a meeting happened are the same provenance chain that makes the data citable by a journalist. Gaming the game would require forging the civic record — which is exactly the attack the verification layer exists to stop, and every forged claim is a diff on the permanent record.
- **Missions are diffs with deadlines.** The mission board needs no content team: an agenda item added (a diff) plus a meeting date (a deadline) plus a location (a touchpoint) *is* a mission. The sync engine is the game master.

### 6.3 Mechanics that translate — and one that must not

Worth porting: **keys → standing** (verified reports filed in a jurisdiction grant standing there — deeper data layers and missions unlock where you have actually shown up); **badges → credentials** (a district sweep, a budget season survived — verifiable, portable proof of civic presence); **anomalies → convergences** (election nights and budget adoptions are natural diff storms; the game should schedule around the government's own calendar, not invent events).

Not porting, ever: **factions as teams.** The Left/Right pair is deliberately the anti-faction — the same data, two lenses, one verified human on each side. The moment the game scores one side against the other, it stops being a civic instrument and becomes a partisan one. The score is a credential of showing up (competition against your own prior period), never a war contribution.

---

## 7. Open Explorations

Questions worth experimenting on, not answering in a document:

- **Bills as branches, literally?** Modeling a pending ordinance as a git branch of the affected files would make "what would this change?" a `git diff main..proposal`. Powerful, but demands modeling the *rules* as files, not just the roster. Probably a v2 experiment on one ordinance.
- **Public comment as pull request?** Could citizens propose corrections to the mirror (a wrong phone number, a missed meeting) as PRs — making Phase 2/3 contributors literal git contributors?
- **The noise floor.** How much churn does a real county produce weekly? The two-week seed experiment answers this empirically — it calibrates the heartbeat view, mission volume, and video cadence all at once.
- **Adversarial pressure.** The moment influence scores matter, actors will optimize for them. Facts-not-scores and published weight vectors are the first defense; what is the second?
- **Absence rendering.** How do we visualize "nobody is watching this" without it reading as "nothing is happening here"? The distinction is the recruitment engine.
- **The fun problem.** Ingress worked because walking to a portal felt like play, not duty. Which civic actions carry intrinsic game-feel (discovery, first-to-map, streaks, sweeps) and which are duty dressed up in points? The mechanics should concentrate on the former — duty-with-points reads as homework and churns players.
- **Score decay vs. credential permanence.** The light decays, but should a person's earned credential? Probably: *standing* decays (you must keep showing up), *badges* are permanent (you did the thing). Needs playtesting against real behavior.

---

## 8. The Position

Nobody is systematically watching county-level power in America. The data to do it is public, standardized more often than anyone realizes, and unassembled. Git is the missing piece not because it stores files but because it **makes change itself a first-class, inspectable, permanent object** — and change is the thing that power depends on going unnoticed.

Government as software. The repo as the mirror. The diff as the product. Influence as a computable, inspectable, *visible* thing — a tool.

Start with one county. Watch it for two weeks. Read the diffs. Build what they teach.
