# bureau-test Development Guidelines

Auto-generated from all feature plans. Last updated: 2026-04-19

## Active Technologies
- YAML (config file only — no Python implementation) + `pre-commit` (environment assumption); `ruff-pre-commit` (remote hook); `pytest` (local hook) (003-precommit-hooks)
- Python 3.11+ (target implementation language — never reached in a passing run) + N/A (run does not complete) (004-escalation-missing-schema)
- YAML (GitHub Actions workflow syntax) + `actions/stale` (stale PR management); `gh` CLI or GitHub API (branch deletion) (005-pr-cleanup-action)

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
- 005-pr-cleanup-action: Added YAML (GitHub Actions workflow syntax) + `actions/stale` (stale PR management); `gh` CLI or GitHub API (branch deletion)
- 004-escalation-missing-schema: Added Python 3.11+ (target implementation language — never reached in a passing run) + N/A (run does not complete)
- 003-precommit-hooks: Added YAML (config file only — no Python implementation) + `pre-commit` (environment assumption); `ruff-pre-commit` (remote hook); `pytest` (local hook)


<!-- MANUAL ADDITIONS START -->
<!-- MANUAL ADDITIONS END -->
