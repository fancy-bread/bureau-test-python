# Feature Specification: Tooling Config — Pre-Commit Hooks

**Feature Branch**: `003-precommit-hooks`
**Created**: 2026-04-18
**Status**: Draft
**Input**: Bureau e2e test harness — T3 tooling/config test

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Linting Runs on Every Commit (Priority: P1)

A developer stages Python files and runs `git commit`. Before the commit lands, `ruff` checks the staged files for style and lint violations. If any violation is found, the commit is rejected with a clear error. If all checks pass, the commit proceeds.

**Why this priority**: This is the core deliverable — a pre-commit hook that enforces code quality automatically. Everything else depends on this being configured correctly.

**Independent Test**: Run `pre-commit run --all-files` from the repo root. The command exits 0 with the existing Python files in the repo (which are already clean). Verify `ruff` appears in the hook output.

**Acceptance Scenarios**:

1. **Given** `.pre-commit-config.yaml` exists at the repo root, **When** `pre-commit run --all-files` is executed, **Then** it exits 0 against the current codebase
2. **Given** `.pre-commit-config.yaml` exists, **When** its contents are read, **Then** it includes a `ruff` hook configured to run on Python files
3. **Given** `.pre-commit-config.yaml` exists, **When** `pre-commit install` is executed, **Then** it exits 0 and installs hooks into `.git/hooks/pre-commit`

---

### User Story 2 — Test Suite Runs on Every Commit (Priority: P2)

A developer stages changes and commits. Before the commit lands, the full test suite runs. If any test fails, the commit is rejected. This ensures no failing code enters the repository.

**Why this priority**: A linter catches style issues; a test runner catches correctness regressions. Together they form a complete pre-commit quality gate.

**Independent Test**: Run `pre-commit run --all-files`. Verify `pytest` appears in the hook output alongside `ruff` and that the existing tests pass.

**Acceptance Scenarios**:

1. **Given** `.pre-commit-config.yaml` exists, **When** its contents are read, **Then** it includes a hook that runs `pytest` against the test suite
2. **Given** `.pre-commit-config.yaml` exists and the test suite passes, **When** `pre-commit run --all-files` is executed, **Then** both the `ruff` and `pytest` hooks exit 0

---

### User Story 3 — Config-Only Output (Priority: P3)

The PR contains exactly one new file: `.pre-commit-config.yaml`. No Python source files are added or modified. No `requirements.txt`, no `setup.cfg`, no `pyproject.toml` changes. The pre-commit tool itself is not installed as part of this spec — it is assumed to be available in the environment.

**Why this priority**: This story tests bureau's ability to recognize that a tooling spec produces a config artifact, not code. Adding Python files or modifying `pyproject.toml` would be a constitution violation (minimal scope, Principle IV).

**Independent Test**: Review the PR diff — it contains only `.pre-commit-config.yaml` and nothing else.

**Acceptance Scenarios**:

1. **Given** the submitted PR, **When** the changed files are listed, **Then** only `.pre-commit-config.yaml` appears
2. **Given** `.pre-commit-config.yaml`, **When** it is validated as YAML, **Then** it parses without error
3. **Given** `.pre-commit-config.yaml`, **When** its `repos` entries are inspected, **Then** each hook references a pinned version (no `latest` or unpinned refs)

---

### Edge Cases

- `pre-commit run --all-files` runs hooks against all tracked files, not just staged ones — both hooks MUST pass against the current clean repo state.
- Pinned versions: hook `rev` values MUST be explicit version tags (e.g., `v0.6.0`), not branch names or `HEAD`.
- The pytest hook MUST set `pass_filenames: false` so pytest runs the full suite rather than receiving individual filenames as arguments.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `.pre-commit-config.yaml` MUST exist at the repository root after the PR is merged
- **FR-002**: The config MUST include a `ruff` hook (from `https://github.com/astral-sh/ruff-pre-commit`) that runs on Python files
- **FR-003**: The config MUST include a `pytest` hook (local hook using `pytest`) that runs the full test suite
- **FR-004**: The pytest hook MUST set `pass_filenames: false`
- **FR-005**: All hook `rev` values MUST be pinned to explicit version tags
- **FR-006**: The config MUST be valid YAML that parses without error
- **FR-007**: `pre-commit run --all-files` MUST exit 0 against the current codebase
- **FR-008**: The PR diff MUST contain only `.pre-commit-config.yaml` — no other files added or modified

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pre-commit run --all-files` exits 0
- **SC-002**: `pre-commit install` exits 0
- **SC-003**: Bureau's PR run summary reports zero constitution violations
- **SC-004**: PR diff contains exactly one file
- **SC-005**: Bureau's run completes in under 5 minutes

## Assumptions

- `pre-commit` is installed in the environment where bureau runs
- The existing Python files (`src/greeting.py`, `src/temperature.py`, `tests/`) are already ruff-clean
- `pytest` is available as a command in the environment
- Hook versions are current stable releases as of the spec date; bureau selects the latest pinned stable tag available
