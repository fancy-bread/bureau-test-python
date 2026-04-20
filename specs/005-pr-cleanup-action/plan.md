# Implementation Plan: PR Cleanup GitHub Actions Workflow

**Branch**: `005-pr-cleanup-action` | **Date**: 2026-04-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/005-pr-cleanup-action/spec.md`

## Summary

Add `.github/workflows/pr-cleanup.yml` — a scheduled GitHub Actions workflow that marks and closes stale PRs using `actions/stale`, and deletes merged branch refs using `actions/delete-branch-on-merge` or an equivalent step. The sole deliverable is one YAML file. No Python source is added or modified. TDD does not apply.

## Technical Context

**Language/Version**: YAML (GitHub Actions workflow syntax)
**Primary Dependencies**: `actions/stale` (stale PR management); `gh` CLI or GitHub API (branch deletion)
**Storage**: N/A
**Testing**: `yamllint` YAML validation; structural inspection of workflow fields
**Target Platform**: GitHub Actions (ubuntu-latest runner)
**Project Type**: CI/CD config — single YAML artifact
**Performance Goals**: N/A
**Constraints**: One file only in PR diff; `main` exempt from deletion; `GITHUB_TOKEN` only (no extra secrets)
**Scale/Scope**: one workflow file, two jobs or steps

## Constitution Check

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Specs as Test Cases | ✅ PASS | This is a housekeeping spec, not a bureau test case — constitution principle I applies to the test tier specs; this spec is repo infrastructure |
| II. Test-First | ✅ PASS | Not applicable — YAML config output, no Python implementation |
| III. Python Primary | ✅ PASS | No Python produced |
| IV. Minimal Scope | ✅ PASS | FR-009 limits diff to one file |
| V. Verifiable Outputs | ✅ PASS | `yamllint` exit code is the oracle |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/005-pr-cleanup-action/
├── plan.md              ← this file
├── research.md          ← action versions and branch deletion approach
├── data-model.md        ← workflow structure
├── contracts/
│   └── workflow.md      ← expected workflow shape
└── tasks.md             ← ordered tasks
```

### Source Code (repository root)

```text
.github/
└── workflows/
    └── pr-cleanup.yml   ← the sole deliverable
```

**Structure Decision**: Standard GitHub Actions path. No other directories modified.

## Complexity Tracking

No constitution violations to justify.
