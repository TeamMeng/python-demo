.PHONY: install fmt lint test testv cover check ci clean

install:
	pip install -r requirements.txt

fmt:
	ruff format .

lint:
	ruff check .

test:
	pytest -v

testv:
	pytest -v

cover:
	pytest --cov=. -v

check: fmt lint testv cover

ci: check

clean:
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
