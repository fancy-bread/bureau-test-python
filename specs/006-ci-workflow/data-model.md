# Data Model: CI Workflow — PR Validation

**Date**: 2026-04-20

## Workflow Structure

```
name: CI
on:
  pull_request:
    branches: [main]

jobs:
  ci:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.14"
      - run: pip install -e '.[dev]'
      - run: pytest
      - run: ruff check .
```

## Key Constraints

| Field | Value |
|-------|-------|
| Trigger | `pull_request` → `main` only |
| Python version | `3.14` |
| Install command | `pip install -e '.[dev]'` |
| Test command | `pytest` |
| Lint command | `ruff check .` |
| Secrets required | None |
