# Tasks: PR Cleanup GitHub Actions Workflow

**Input**: Design documents from `specs/005-pr-cleanup-action/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

**Note**: TDD does not apply. Deliverable is a single YAML file. Verification gates replace TDD gates.

## Format: `[ID] [P?] [Story] Description`

---

## Phase 1: Setup

- [x] T001 Create `.github/workflows/` directory at repository root

---

## Phase 2: User Story 1 — Stale PRs Closed Automatically (Priority: P1)

**Goal**: Workflow exists with a valid schedule trigger and `actions/stale` configured.

**Independent Test**: `yamllint .github/workflows/pr-cleanup.yml` exits 0; `grep -q "actions/stale"` exits 0.

- [x] T002 [US1] Create `.github/workflows/pr-cleanup.yml` with: `name`, `on.schedule` (daily cron), `on.workflow_dispatch`, `permissions.contents: write`, `permissions.pull-requests: write`, and a `stale` job using `actions/stale@v9` with `days-before-stale: 7`, `days-before-close: 2`, `exempt-pr-labels: keep`
- [x] T003 [US1] Verify YAML parses: `yamllint .github/workflows/pr-cleanup.yml` exits 0
- [x] T004 [US1] Verify stale action present: `grep -q "actions/stale"` exits 0
- [x] T005 [US1] Verify configured values: `grep -q "days-before-stale: 7"` and `grep -q "days-before-close: 2"` both exit 0

---

## Phase 3: User Story 2 — Merged Branches Deleted Automatically (Priority: P2)

**Goal**: Workflow includes a job that deletes merged remote branch refs, excluding `main`.

**Independent Test**: `grep -q "delete"` and `grep -q "main"` (exclusion) both exit 0 in the workflow file.

- [x] T006 [US2] Add a `delete-merged-branches` job to `.github/workflows/pr-cleanup.yml` that uses `gh api` to delete merged branch refs, explicitly skipping `main`
- [x] T007 [US2] Verify branch deletion step present and `main` excluded: inspect workflow for deletion logic with main guard

---

## Phase 4: Scope Audit

- [x] T008 Verify PR diff scope: `git diff main --name-only` returns exactly `.github/workflows/pr-cleanup.yml`
- [x] T009 [P] Verify `workflow_dispatch` trigger present: `grep -q "workflow_dispatch"` exits 0
- [x] T010 [P] Verify permissions block: `grep -q "contents: write"` and `grep -q "pull-requests: write"` both exit 0

---

## Dependencies & Execution Order

- **T001**: No dependencies
- **T002**: Depends on T001
- **T003–T005**: Depend on T002; can run in parallel [P]
- **T006**: Depends on T003 (valid YAML before adding second job)
- **T007**: Depends on T006
- **T008–T010**: Depend on T007; T009 and T010 can run in parallel [P]

---

## Notes

- T006 uses `gh api DELETE /repos/{owner}/{repo}/git/refs/heads/{branch}` — the `gh` CLI is pre-installed on `ubuntu-latest` runners
- The `main` guard in T006 is critical: deleting `main` would be catastrophic; an explicit `if: branch != 'main'` condition is required
- `workflow_dispatch` (T009) enables manual test runs without waiting for the cron schedule
