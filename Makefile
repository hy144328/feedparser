.PHONY: .venv
.venv:
	python3 -m venv .venv

.PHONY: requirements
requirements:
	python3 -m pip install --upgrade -r requirements.txt
	poetry update

.PHONY: test
test:
	python3 -m pytest tests/copy2summary/
