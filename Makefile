install:
	poetry install

lint:
	poetry run ruff check gendiff

test:
	poetry run pytest tests/ -v

check:	lint test

.PHONY:	install test lint check
