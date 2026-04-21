# Tasks: CI Workflow — PR Validation

**Input**: Design documents from `specs/006-ci-workflow/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

**Note**: TDD does not apply. Single YAML artifact. Verification gates replace TDD gates.

## Format: `[ID] [P?] [Story] Description`

---

## Phase 1: User Story 1 — Tests Pass on Every PR (Priority: P1)

**Goal**: `.github/workflows/ci.yml` exists, triggers on PRs to main, and runs pytest.

- [x] T001 [US1] Create `.github/workflows/ci.yml` with `on.pull_request.branches: [main]`, checkout, setup-python 3.14, `pip install -e '.[dev]'`, and `pytest` steps
- [x] T002 [US1] Verify YAML parses: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"` exits 0
- [x] T003 [US1] Verify trigger and pytest present: `grep -q "pull_request"` and `grep -q "pytest"` both exit 0

---

## Phase 2: User Story 2 — Lint Passes on Every PR (Priority: P2)

**Goal**: `ruff check .` step added to the workflow.

- [x] T004 [US2] Add `ruff check .` step to the `ci` job in `.github/workflows/ci.yml`
- [x] T005 [US2] Verify lint step present: `grep -q "ruff check"` exits 0

---

## Phase 3: Scope Audit

- [x] T006 [P] Verify Python version: `grep -q "3.14"` exits 0
- [x] T007 [P] Verify install command: `grep -q "pip install -e"` exits 0

---

## Dependencies & Execution Order

- **T001**: No dependencies
- **T002–T003**: Depend on T001; can run in parallel [P]
- **T004**: Depends on T002 (valid YAML before modifying)
- **T005**: Depends on T004
- **T006–T007**: Depend on T005; can run in parallel [P]
