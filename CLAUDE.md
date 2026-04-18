# bureau-test Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-04-18

## Active Technologies
- YAML (config file only — no Python implementation) + `pre-commit` (environment assumption); `ruff-pre-commit` (remote hook); `pytest` (local hook) (003-precommit-hooks)

- Python 3.11+ + pytest (test runner only; implementation has no external dependencies) (001-smoke-hello-world)

## Project Structure

```text
src/
tests/
```

## Commands

cd src && pytest && ruff check .

## Code Style

Python 3.11+: Follow standard conventions

## Recent Changes
- 003-precommit-hooks: Added YAML (config file only — no Python implementation) + `pre-commit` (environment assumption); `ruff-pre-commit` (remote hook); `pytest` (local hook)
- 002-constitution-compliance: Added Python 3.11+ + pytest (test runner only; implementation has no external dependencies)

- 001-smoke-hello-world: Added Python 3.11+ + pytest (test runner only; implementation has no external dependencies)

<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
