# Feature Specification: CI Workflow — PR Validation

**Feature Branch**: `006-ci-workflow`
**Created**: 2026-04-20
**Status**: Draft
**Input**: Repo housekeeping — verify that what bureau produces on a PR branch is correct before merge

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Tests Pass on Every PR (Priority: P1)

A bureau run opens a PR. Before that PR can be merged, CI runs the test suite against the branch. If any test fails, the PR is blocked. This ensures no failing implementation reaches main.

**Why this priority**: The primary guarantee CI must provide. Bureau's Critic already checks this locally, but CI provides an independent second check under clean conditions.

**Independent Test**: Inspect `.github/workflows/ci.yml` — verify it triggers on `pull_request` and includes a step that runs `pytest`.

**Acceptance Scenarios**:

1. **Given** `.github/workflows/ci.yml` exists, **When** its triggers are inspected, **Then** it runs on `pull_request` events targeting `main`
2. **Given** the workflow, **When** its steps are inspected, **Then** it installs dependencies via `pip install -e '.[dev]'`
3. **Given** the workflow, **When** its steps are inspected, **Then** it runs `pytest` and fails the job if tests fail

---

### User Story 2 — Lint Passes on Every PR (Priority: P2)

CI also runs `ruff check .` on the branch. If any lint violation is found, the PR is blocked. This complements the pre-commit hook from spec 003 with a server-side enforcement.

**Why this priority**: Pre-commit hooks can be bypassed locally. CI lint is the authoritative gate.

**Independent Test**: Inspect `.github/workflows/ci.yml` — verify it includes a step that runs `ruff check .`.

**Acceptance Scenarios**:

1. **Given** the workflow, **When** its steps are inspected, **Then** it runs `ruff check .` after the test step
2. **Given** a PR with a lint violation, **When** CI runs, **Then** the lint step fails and blocks the PR

---

### User Story 3 — Config-Only Output (Priority: P3)

The PR diff contains exactly one new file: `.github/workflows/ci.yml`. No Python source files are added or modified.

**Acceptance Scenarios**:

1. **Given** the submitted PR, **When** the changed files are listed, **Then** only `.github/workflows/ci.yml` appears among implementation files
2. **Given** `.github/workflows/ci.yml`, **When** it is validated as YAML, **Then** it parses without error

---

### Edge Cases

- The workflow MUST use the same Python version as bureau's runtime (`3.14`) to catch version-specific issues.
- The workflow MUST set `PYTHONPATH=.` (or rely on `pyproject.toml`'s `pythonpath` setting) so `src.*` imports resolve correctly.
- On a repo with no tests yet (empty `tests/`), `pytest` MUST exit 0 — this is the case before any spec is implemented.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `.github/workflows/ci.yml` MUST exist after the PR is merged
- **FR-002**: The workflow MUST trigger on `pull_request` events targeting `main`
- **FR-003**: The workflow MUST check out the PR branch using `actions/checkout`
- **FR-004**: The workflow MUST set up Python 3.14 using `actions/setup-python`
- **FR-005**: The workflow MUST install dependencies via `pip install -e '.[dev]'`
- **FR-006**: The workflow MUST run `pytest` and fail the job on test failure
- **FR-007**: The workflow MUST run `ruff check .` and fail the job on lint violation
- **FR-008**: The workflow file MUST be valid YAML that parses without error

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `yamllint .github/workflows/ci.yml` exits 0
- **SC-002**: Workflow triggers on `pull_request` to `main`
- **SC-003**: Python version in workflow matches bureau runtime (`3.14`)
- **SC-004**: Both `pytest` and `ruff check .` steps are present and configured to fail the job on error
- **SC-005**: PR diff contains no unexpected implementation files

## Assumptions

- `actions/setup-python` supports Python 3.14 in the GitHub Actions environment
- `pyproject.toml`'s `pythonpath = ["."]` setting is sufficient for `pytest` to resolve `src.*` imports without setting `PYTHONPATH` explicitly in the workflow
- The workflow runs under the default `GITHUB_TOKEN` — no additional secrets required
