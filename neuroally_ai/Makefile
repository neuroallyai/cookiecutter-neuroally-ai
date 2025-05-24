# Makefile for NeuroAlly AI
#
# This Makefile provides common commands for project development.
# It adapts to whether Conda is used (with Poetry) or Poetry is used directly.

# --- Variables ---
# Conda environment name (used if Conda support is enabled)
CONDA_ENV_NAME := neuroally_ai

# Python interpreter executable name (can be overridden, e.g., make PYTHON_INTERPRETER=python3.10 run-main)
PYTHON_INTERPRETER ?= python

# Shell to use for executing recipes
SHELL := /bin/bash

# Determine the command runner prefix based on Conda support
# Jinja templating here sets the correct prefix when Cookiecutter generates this Makefile.

# For Poetry-only: use Poetry directly.
POETRY_INSTALL_CMD := poetry install
POETRY_EXPORT_CMD  := poetry export
RUNNER             := poetry run
PYTHON_IN_ENV_CMD  := poetry run $(PYTHON_INTERPRETER)
ENV_ACTIVATION_MSG := "poetry shell (or activate the virtual environment manually)"


# Default target: Executed when 'make' is run without arguments.
.DEFAULT_GOAL := help

# Phony targets: Targets that are not actual files.
.PHONY: help install setup install-core install-dev install-all-extras env requirements clean lint format test docs serve-docs run

# --- Help ---
help:
	@echo "Makefile for NeuroAlly AI"
	@echo "---------------------------------------------------------------------"
	@echo "Available commands:"
	@echo ""
	@echo "  Environment & Dependencies:"
	@echo "    make setup             Alias for 'make install-core' followed by 'make install-dev'."
	@echo "    make install-core      Install core project dependencies using Poetry."
	@echo "    make install-dev       Install development dependencies (from 'dev' group)."
	@echo "    make install-all-extras Install all optional dependency groups from pyproject.toml."
	@echo "    make env               Show instructions to activate the virtual environment."
	@echo "    make requirements      Export current dependencies to various requirements.txt files."
	@echo ""
	@echo "  Code Quality & Testing:"
  # Assume linters are useful if any of these are true
	@echo "    make lint              Run linters (e.g., Ruff) and type checkers (e.g., Mypy)."
	@echo "    make format            Format code automatically (e.g., Black, Ruff format)."


	@echo "    make test              Run automated tests using pytest."

	@echo ""

	@echo "  Documentation:"
	@echo "    make docs              Build the project documentation (TODO: configure tool)."
	@echo "    make serve-docs        Serve the project documentation locally (TODO: configure tool)."

	@echo ""
	@echo "  Application & Cleaning:"
	@echo "    make run               Run the main application script (src/neuroally_ai/main.py)."
	@echo "    make clean             Remove temporary files, build artifacts, and caches."
	@echo ""
	@echo "Note: Ensure dependencies for linting, testing, and docs are installed"
	@echo "      (e.g., via 'make install-dev' or by installing specific Poetry groups like 'docs_tools')."

# --- Environment & Dependencies ---
install-core: ## Install core project dependencies
	@echo ">>> Installing core project dependencies..."
	$(POETRY_INSTALL_CMD) --no-interaction --sync
	@echo "✅ Core dependencies installed."

install-dev: ## Install development dependencies (from 'dev' group)
	@echo ">>> Installing development dependencies (ensure 'dev' group is defined in pyproject.toml)..."
	$(POETRY_INSTALL_CMD) --no-interaction --sync --with dev
	@echo "✅ Development dependencies installed."

setup: install-core install-dev ## Install core and development dependencies

install-all-extras: ## Install all optional dependency groups
	@echo ">>> Installing all optional dependency groups defined in pyproject.toml..."
	$(POETRY_INSTALL_CMD) --no-interaction --sync --all-extras
	@echo "✅ All optional dependencies installed."

env: ## Show environment activation instructions
	@echo "To activate your project environment:"
	@echo "  $(ENV_ACTIVATION_MSG)"
	@echo "Alternatively, to run a command within the environment, use: $(RUNNER) your_command"

requirements: ## Export dependencies to requirements files
	@echo ">>> Exporting dependencies to requirements files using Poetry..."
	$(POETRY_EXPORT_CMD) -f requirements.txt --output requirements.txt --without-hashes
	@echo "  Generated: requirements.txt (main dependencies)"
	$(POETRY_EXPORT_CMD) -f requirements.txt --output requirements-dev.txt --with dev --without-hashes
	@echo "  Generated: requirements-dev.txt (main + dev dependencies)"
	$(POETRY_EXPORT_CMD) -f requirements.txt --output requirements-all.txt --all-extras --without-hashes
	@echo "  Generated: requirements-all.txt (all dependencies including all optional groups)"
	@echo "✅ Dependencies exported."

# --- Code Quality & Testing ---

lint: ## Run linters and type checkers
	@echo ">>> Running linters and type checkers (e.g., Ruff, Mypy)..."
	@echo "    Ensure linting tools are in your 'dev' dependency group and installed."
	$(RUNNER) ruff check .
	$(RUNNER) ruff format --check .
	$(RUNNER) mypy src tests # Adjust paths as needed
	@echo "✅ Linting and type checking complete."

format: ## Format code automatically
	@echo ">>> Formatting code (e.g., Black, Ruff format)..."
	@echo "    Ensure formatting tools are in your 'dev' dependency group and installed."
	$(RUNNER) ruff format .
	$(RUNNER) ruff check . --fix --unsafe-fixes # Be cautious with --unsafe-fixes
	# $(RUNNER) black src tests # If you prefer Black separately
	@echo "✅ Code formatting complete."



test: ## Run automated tests
	@echo ">>> Running automated tests (e.g., pytest)..."
	@echo "    Ensure pytest is in your 'dev' dependency group and installed."
	$(RUNNER) pytest
	@echo "✅ Tests complete."


# --- Documentation ---

docs: ## Build documentation
	@echo ">>> Building documentation..."
	@echo "    Ensure your documentation tools (e.g., MkDocs, Sphinx) are in the 'docs_tools' group and installed."
	@echo "    TODO: Add your specific documentation build command below."
	# Example for MkDocs:
	# $(RUNNER) mkdocs build --clean
	# Example for Sphinx:
	# $(RUNNER) sphinx-build -b html docs docs/_build -E
	@echo "    (Documentation build command not yet implemented in Makefile)"
	@echo "✅ Documentation build placeholder executed."

serve-docs: ## Serve documentation locally
	@echo ">>> Serving documentation locally..."
	@echo "    Ensure your documentation tools and a local server are available."
	@echo "    TODO: Add your specific command to serve documentation below."
	# Example for MkDocs:
	# $(RUNNER) mkdocs serve
	# Example for Sphinx (after building to docs/_build/html):
	# @echo "    Serving documentation at http://localhost:8000"
	# $(PYTHON_IN_ENV_CMD) -m http.server --directory docs/_build/html 8000
	@echo "    (Documentation serve command not yet implemented in Makefile)"
	@echo "✅ Documentation serve placeholder executed."


# --- Application & Cleaning ---
run: ## Run the main application script
	@echo ">>> Running main application script (src/neuroally_ai/main.py)..."
	$(PYTHON_IN_ENV_CMD) src/neuroally_ai/main.py
	@echo "✅ Main application script finished."

clean: ## Remove temporary files, build artifacts, and caches
	@echo ">>> Cleaning up project..."
	find . -type f -name "*.py[co]" -delete -o -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d \( -name ".pytest_cache" -o -name ".mypy_cache" -o -name ".ruff_cache" -o -name ".tox" -o -name ".nox" \) -exec rm -rf {} +
	rm -rf build/ dist/ .eggs/ *.egg-info/ coverage.xml htmlcov/ site/ docs/_build/
	rm -f .coverage .coverage.*
	# Add any other project-specific cleaning commands
	@echo "✅ Cleanup complete."