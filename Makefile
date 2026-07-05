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

legal-us-code: ## Ingest the pinned U.S. Code Title 52 seed corpus
	python3 scripts/ingest_us_code.py --title 52

check: build validate  ## Build, then validate — the full gate
