# Government as Code

## The premise

Government is an operating system that has run for 250 years without version control.

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
| The changelog | **Did not exist. This repository is it.** |

Everything on the right is public. Almost none of it is *legible*. The state of government is scattered across PDFs, agenda portals, filings, and meeting videos — published, technically, but not readable, not diffable, and above all not *watchable*. A change to a zoning code and a change to a codebase are the same category of event; only one of them triggers a notification.

We cannot read government's source directly. But we can mirror its observable public state into files, and version the mirror. Git then gives us, for free, the tooling software has had for decades.

## What git's primitives mean here

| Git | In this repository |
|---|---|
| The files | The current state — who holds which office, what a place is made of, who's running. |
| A commit | An observed change, timestamped: "this member's committee assignment changed." |
| `git log` | The timeline of any official, body, or place — forever. |
| `git diff` | The change itself, in plain terms. This is the product. |
| `git blame` | The provenance of any single fact, line by line. |
| `git show` | One change, in full, on the permanent record. |

You do not need to know git deeply to read this repository. Four commands cover it: `git log` (what happened), `git diff` (what changed), `git show` (one change in full), `git blame` (where a fact came from). The agents that maintain the mirror do the writing.

## The diff is the product

The honest caveat: the mirror's history starts the day we start watching. Git's value here is entirely forward-looking — from the first commit on, *nothing changes unnoticed*. Nobody can quietly pull an item off an agenda or revise a bio; that edit is itself a diff, timestamped and permanent.

This is why the [changelog](../CHANGELOG.md) matters more than any single record. A directory of officials is useful; a running account of *what your government changed this week* is a different kind of instrument. The changelog is generated directly from git — nobody writes it, it falls out of the files changing.

For this to work, the files must be **boring**. The build is deterministic: the same entity always at the same path, keys always in the same order, identical formatting every run. Volatile bookkeeping ("we checked, nothing changed") never touches the entity files — only real government changes produce a diff. This single discipline is most of the engineering. See [the data model](data-model.md) for how it's enforced.

## Principles

- **Government should be legible.** Structure is the precondition for understanding.
- **Official sources remain the authority.** This repository is a mirror, not the source of truth. Every record cites where it came from and how confident we are.
- **Changes should be visible.** The value is not the snapshot; it's the diff between snapshots.
- **Git preserves history.** A record deleted upstream becomes a diff here, not a hole. Civic memory that survives deletion is a byproduct of refusing to overwrite.
- **Agents need structured civic memory.** The mirror is built to be read and reasoned over by software as much as by people — stable IDs, simple schemas, field-level sources, machine-diffable format.

## Not the source of truth

Worth repeating, because it is the ethical center of the project: **Republic OS is a mirror.** When it disagrees with an official record, the official record is right and the mirror has a bug — which is itself a finding, surfaced as a diff. The goal is to make public power easier to read, not to become an alternative authority over it.
