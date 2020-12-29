.PHONY: .venv
.venv:
	python3 -m venv .venv

.PHONY: requirements
requirements:
	python3 -m pip install --upgrade pip poetry
	poetry update
