# Research: CI Workflow — PR Validation

**Date**: 2026-04-20
**Status**: Complete

## Findings

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| `actions/checkout@v4` | Current stable major | v3 — superseded |
| `actions/setup-python@v5` | Current stable major; supports 3.14 | v4 — superseded |
| `python-version: "3.14"` | Matches bureau's `requires-python = ">=3.14"` | 3.11 — misaligned with runtime |
| `pip install -e '.[dev]'` | Installs pytest, ruff, pre-commit from pyproject.toml dev deps | `pip install pytest ruff` — brittle, diverges from pyproject.toml |
| Single job `ci` | Tests and lint are fast; no benefit to parallelising at this scale | Separate jobs — unnecessary overhead |
| `pull_request` targeting `main` | Validates all PRs before merge | `push` — too late; also runs on merge commits |
| No `PYTHONPATH` override needed | `pyproject.toml` sets `pythonpath = ["."]` for pytest | Explicit `env: PYTHONPATH: .` — redundant |
