# Implementation Plan: CI Workflow — PR Validation

**Branch**: `006-ci-workflow` | **Date**: 2026-04-20 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/006-ci-workflow/spec.md`

## Summary

Add `.github/workflows/ci.yml` — a GitHub Actions workflow that runs on every PR targeting `main`, installs dependencies, runs `pytest`, and runs `ruff check .`. Single YAML artifact. No Python source modified. TDD does not apply.

## Technical Context

**Language/Version**: YAML (GitHub Actions workflow syntax)
**Primary Dependencies**: `actions/checkout@v4`; `actions/setup-python@v5`; `pip install -e '.[dev]'`
**Storage**: N/A
**Testing**: `yamllint` YAML validation; structural inspection of workflow fields
**Target Platform**: GitHub Actions (`ubuntu-latest`, Python 3.14)
**Project Type**: CI/CD config — single YAML artifact
**Performance Goals**: N/A
**Constraints**: One implementation file in PR diff; Python version MUST be 3.14
**Scale/Scope**: one workflow file, one job, four steps

## Constitution Check

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Specs as Test Cases | ✅ PASS | Housekeeping spec — not a bureau test case; constitution Principle I applies to test tier specs |
| II. Test-First | ✅ PASS | Not applicable — YAML config output |
| III. Python Primary | ✅ PASS | No Python produced |
| IV. Minimal Scope | ✅ PASS | One file, four steps — nothing beyond what the spec requires |
| V. Verifiable Outputs | ✅ PASS | `yamllint` + grep assertions are the oracle |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/006-ci-workflow/
├── plan.md              ← this file
├── research.md          ← action versions
├── data-model.md        ← workflow structure
├── contracts/
│   └── workflow.md      ← expected workflow shape
└── tasks.md             ← ordered tasks
```

### Source Code (repository root)

```text
.github/
└── workflows/
    ├── pr-cleanup.yml   ← from spec 005 (unchanged)
    └── ci.yml           ← the sole deliverable
```

**Structure Decision**: Alongside the existing `pr-cleanup.yml`. No other changes.

## Complexity Tracking

No constitution violations to justify.
