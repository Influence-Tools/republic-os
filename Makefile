# Republic OS — repeatable pipeline commands.
# The build is deterministic: `make build` twice yields a byte-identical tree.

.PHONY: build validate check

build:        ## Regenerate the entity tree from raw exports in data/
	python3 scripts/build.py

validate:     ## Check every entity file: OKF, schema, and link integrity
	python3 scripts/validate.py

check: build validate  ## Build, then validate — the full gate
