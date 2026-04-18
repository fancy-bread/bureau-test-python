# Implementation Plan: Tooling Config — Pre-Commit Hooks

**Branch**: `003-precommit-hooks` | **Date**: 2026-04-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/003-precommit-hooks/spec.md`

## Summary

Add `.pre-commit-config.yaml` at the repository root with two hooks: `ruff` (linting) and a local `pytest` hook (test suite). Both hooks must pass against the current codebase. This is the T3 tooling/config test — the entire deliverable is a single YAML file; no Python source is added or modified.

## Technical Context

**Language/Version**: YAML (config file only — no Python implementation)
**Primary Dependencies**: `pre-commit` (environment assumption); `ruff-pre-commit` (remote hook); `pytest` (local hook)
**Storage**: N/A
**Testing**: `pre-commit run --all-files` exit code is the verification oracle
**Target Platform**: Linux/macOS (wherever bureau runs)
**Project Type**: tooling config — single YAML artifact
**Performance Goals**: N/A
**Constraints**: One file only in PR diff; all hook `rev` values pinned to explicit version tags
**Scale/Scope**: one config file, two hooks

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Specs as Test Cases | ✅ PASS | `pre-commit run --all-files` is a runnable acceptance check |
| II. Test-First | ✅ PASS | Not applicable — no implementation code; TDD does not apply to YAML config |
| III. Python Primary | ✅ PASS | Spec explicitly declares this is a config artifact, not Python code |
| IV. Minimal Scope | ✅ PASS | FR-008 prohibits any file changes beyond `.pre-commit-config.yaml`; US3 enforces |
| V. Verifiable Outputs | ✅ PASS | `pre-commit run --all-files` exit 0 is the oracle |

No violations. Gate passes. Note: Principle II (TDD) is explicitly inapplicable to YAML config output — this is documented in the constitution ("Python tooling and configuration specs produce YAML/TOML/config files").

## Project Structure

### Documentation (this feature)

```text
specs/003-precommit-hooks/
├── plan.md              ← this file
├── research.md          ← Phase 0 (hook versions to pin)
├── data-model.md        ← Phase 1 (config schema)
├── contracts/
│   └── precommit.md     ← config structure contract
└── tasks.md             ← Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
.pre-commit-config.yaml  ← the sole deliverable
```

**Structure Decision**: Single file at repo root. No subdirectories, no other changes. `.pre-commit-config.yaml` is the standard location expected by the `pre-commit` tool.

## Complexity Tracking

No constitution violations to justify.
