VENV = .venv
PYTHON = $(VENV)/bin/python
PYTHON_INIT ?= python3
POETRY_VERSION = 1.5.1
CODE =\
  comprehensive_microservice
TESTS =\
  tests

.PHONY: run clean init

_activate: $(VENV)/bin/activate

init:
	$(PYTHON_INIT) -m venv $(VENV)
	$(PYTHON) -m pip install poetry==$(POETRY_VERSION)
	$(PYTHON) -m poetry install
	$(PYTHON) -m pre_commit install

test: _activate
	$(PYTHON) -m pytest

mypy: _activate
	$(PYTHON) -m mypy $(CODE)

flake8: _activate
	$(PYTHON) -m flake8 $(CODE) $(TESTS)

format: _activate
	$(PYTHON) -m isort $(CODE) $(TESTS)
	$(PYTHON) -m black $(CODE) $(TESTS)

format-check: _activate
	$(PYTHON) -m isort -c $(CODE) $(TESTS)
	$(PYTHON) -m black --check $(CODE) $(TESTS)

pretty: format mypy flake8

lint: format-check mypy flake8

$(VENV)/bin/activate: pyproject.toml poetry.lock
	$(MAKE) init

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
