VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip

# Self documenting commands
.DEFAULT_GOAL := help
.PHONY: help
help: ## show this help
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
	| awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%s\033[0m|%s\n", $$1, $$2}' \
	| column -t -s '|'

$(VENV)/bin/activate: requirements.txt
	python3 -m venv .venv
	$(PIP) install -U pip
	$(PIP) install -r requirements.txt

run: $(VENV)/bin/activate ## Run the web app
	gunicorn -b 0.0.0.0:5001 --reload wsgi:application

update: $(VENV)/bin/activate ## Update pip and pre-commit
	$(PIP) install -U pip
	$(PYTHON) -m pre_commit autoupdate

lint: $(VENV)/bin/activate ## Run pre-commit hooks
	$(PYTHON) -m pre_commit install --install-hooks
	$(PYTHON) -m pre_commit run --all-files

clean: ## Remove temporary files
	rm -rf .ipynb_checkpoints
	rm -rf **/.ipynb_checkpoints
	rm -rf __pycache__
	rm -rf **/__pycache__
	rm -rf **/**/__pycache__
	rm -rf .pytest_cache
	rm -rf **/.pytest_cache
	rm -rf .ruff_cache
	rm -rf .coverage
	rm -rf build
	rm -rf dist