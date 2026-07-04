# Contributing

Republic OS is a mirror maintained mostly by agents, but its rules are simple enough that anyone can work in it. This page covers the disciplines that keep the mirror trustworthy and the practical steps for adding to it.

## The disciplines

Three rules govern everything, and they are won by subtraction — by declining to destroy:

1. **Never overwrite.** A change is a new commit, not a clobbered file. Deletes are diffs.
2. **Never rewrite history.** No force-push, no squash. The past is load-bearing — it *is* the changelog.
3. **Always push off-box.** One copy is a single point of failure; more is not.

And one rule that makes every diff meaningful:

4. **The build is deterministic.** Entity files change only when the government changes. Never introduce pipeline noise (run timestamps, unstable ordering, reformatting) into an entity file. If `make build` run twice produces a diff, that is a bug.

## The shape of a change

Everything flows one direction:

```
official source ──► raw export (data/*.jsonl) ──► build.py ──► entity tree
```

- **Raw first.** A new source lands in `data/<source>.jsonl` committed *as-is*, before any transformation. The origin must always be recoverable.
- **Build, don't hand-edit.** Entity files under `data/jurisdictions/` are generated. To change them, change the source or the generator — never edit a generated file by hand, or the next build will overwrite it (and you'll have created noise, not signal).
- **Validate before committing.** `make check` runs the build and then validates all files. It must pass.

## Adding a source

1. Obtain the data as JSONL (one JSON object per line) and commit it to `data/<source>.jsonl` untouched.
2. Register it in [`data/sources/sources.yaml`](../data/sources/sources.yaml) and note it in [docs/sources.md](sources.md).
3. Extend [`scripts/build.py`](../scripts/build.py) to read it and emit entities. Follow the existing patterns:
   - Emit frontmatter keys in a **fixed order**; sort all iteration.
   - Carry **field-level `sources`** and a `confidence` level on every record.
   - Use **path-based IDs** with lowercase slugs and stable government identifiers where available.
   - Reconcile to existing entities by a shared key, or by normalized name where none exists.
4. If it's a new entity type, add a JSON Schema to [`/schemas`](../schemas) — a stricter profile over OKF (required fields, property types, enums), tolerating unknown keys.
5. Run `make check`. Fix anything it reports.
6. Commit with a message that describes the *civic* change, not just the code change (see the existing history for the tone).

## Reading a change

You do not need deep git knowledge to read the mirror — four commands cover it:

```bash
git log -- <path>     # the timeline of any official, body, or place
git diff <a>..<b>     # what changed between two states
git show <commit>     # one change, in full
git blame <path>      # where each fact came from
make changelog        # the same, rendered as a plain-language civic changelog
```

## A note on truth

When the mirror disagrees with an official record, the official record is right and the mirror has a bug. Report it as a finding — the gap between the model and reality is information, not embarrassment. This repository never claims to be the authority; it only makes the authority easier to read.
