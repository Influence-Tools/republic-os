# Republic OS — repeatable pipeline commands.
# The build is deterministic: `make build` twice yields a byte-identical tree.

.PHONY: build validate board legal-us-code check

build:        ## Regenerate the entity tree from raw exports in data/
	python3 scripts/build.py

validate:     ## Check every entity file: OKF, schema, and link integrity
	python3 scripts/validate.py

board:        ## Rebuild the Board (inlines fresh data into viz/board.html)
	python3 scripts/build_viz.py
	@echo
	@echo "board.html regenerated. To update the LIVE Artifact you must REPUBLISH"
	@echo "viz/board.html to its existing URL — editing the repo file does not"
	@echo "update a deployed Artifact. See docs/board.md."

changelog:    ## What changed in the government since the last commit (BASE/HEAD overridable)
	python3 scripts/generate_changelog.py $(BASE) $(HEAD)

TITLES ?= 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 54

legal-us-code: ## Ingest the pinned U.S. Code titles (override with TITLES="…")
	@for t in $(TITLES); do python3 scripts/ingest_us_code.py --title $$t; done

check: build validate  ## Build, then validate — the full gate
