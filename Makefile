PROJ=macaddr-search
VENV_PATH=$$HOME/.virtualenvs/${PROJ}

SHELL := /bin/bash

.PHONY: build
build:
	$(PYTHON) setup.py install

.PHONY: clean-venv
clean-venv:
	rm -rf $(VENV_PATH)

.PHONY: requirements
requirements:
	pip install virtualenv; \
	virtualenv "$(VENV_PATH)"; \
	source "$(VENV_PATH)/bin/activate"; \
	pip install -r requirements.txt

.PHONY: setup
setup: clean-venv requirements
	echo "Run 'source ~/.virtualenvs/macaddr-search/bin/activate' to start using the search"
