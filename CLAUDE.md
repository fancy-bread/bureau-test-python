# bureau-test Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-04-20

## Active Technologies
- YAML (config file only — no Python implementation) + `pre-commit` (environment assumption); `ruff-pre-commit` (remote hook); `pytest` (local hook) (003-precommit-hooks)
- Python 3.14+ (target implementation language — never reached in a passing run) + N/A (run does not complete) (004-escalation-missing-schema)
- YAML (GitHub Actions workflow syntax) + `actions/stale` (stale PR management); `gh` CLI or GitHub API (branch deletion) (005-pr-cleanup-action)
- YAML (GitHub Actions workflow syntax) + `actions/checkout@v4`; `actions/setup-python@v5`; `pip install -e '.[dev]'` (006-ci-workflow)

- Python 3.14+ + pytest (test runner only; implementation has no external dependencies) (001-smoke-hello-world)

## Project Structure

```text
src/
tests/
```

## Commands

cd src && pytest && ruff check .

## Code Style

Python 3.14+: Follow standard conventions

## Recent Changes
- 006-ci-workflow: Added YAML (GitHub Actions workflow syntax) + `actions/checkout@v4`; `actions/setup-python@v5`; `pip install -e '.[dev]'`
- 005-pr-cleanup-action: Added YAML (GitHub Actions workflow syntax) + `actions/stale` (stale PR management); `gh` CLI or GitHub API (branch deletion)
- 004-escalation-missing-schema: Added Python 3.14+ (target implementation language — never reached in a passing run) + N/A (run does not complete)


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
