# Research: Tooling Config — Pre-Commit Hooks

**Date**: 2026-04-18
**Status**: Complete

## Findings

One unknown to resolve: which pinned versions to use for `ruff-pre-commit`.

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| `ruff-pre-commit` from `https://github.com/astral-sh/ruff-pre-commit` | Official ruff pre-commit mirror; maintained by the ruff team | `pre-commit-hooks` with a ruff entry — the dedicated mirror is preferred |
| `rev: v0.11.6` for ruff-pre-commit | Latest stable tag as of 2026-04-18 | `latest` — rejected by FR-005 (must pin) |
| Local hook for pytest | pytest has no official pre-commit mirror; local hook is the standard pattern | `additional_dependencies` on a remote hook — more fragile than local |
| `pass_filenames: false` on pytest hook | pytest should run the full suite, not receive individual filenames as args | Default (`true`) — would cause pytest to run only staged files, missing regressions |
| `language: system` for pytest local hook | Uses the environment's pytest installation, consistent with how the project runs tests | `language: python` with `additional_dependencies` — adds an isolated venv, unnecessary overhead |
