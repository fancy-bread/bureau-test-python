# Tasks: Tooling Config — Pre-Commit Hooks

**Input**: Design documents from `specs/003-precommit-hooks/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

**Note**: TDD does not apply to this spec. The deliverable is a YAML config file, not Python code. There is no red-green cycle. Verification gates replace TDD gates.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: User Story 1 — Linting Runs on Every Commit (Priority: P1)

**Goal**: `.pre-commit-config.yaml` exists with a pinned `ruff` hook; `pre-commit run --all-files` exits 0.

**Independent Test**: `pre-commit run ruff --all-files` exits 0.

- [ ] T001 [US1] Create `.pre-commit-config.yaml` at repo root with a `ruff` hook from `https://github.com/astral-sh/ruff-pre-commit`, pinned to the latest stable `rev` tag, scoped to `types: [python]`
- [ ] T002 [US1] Verify YAML parses: `python -c "import yaml; yaml.safe_load(open('.pre-commit-config.yaml'))"` exits 0
- [ ] T003 [US1] Verify ruff hook passes: `pre-commit run ruff --all-files` exits 0

---

## Phase 2: User Story 2 — Test Suite Runs on Every Commit (Priority: P2)

**Goal**: A local `pytest` hook added to `.pre-commit-config.yaml`; full hook suite passes.

**Independent Test**: `pre-commit run --all-files` exits 0 with both `ruff` and `pytest` hooks present.

- [ ] T004 [US2] Add a local `pytest` hook to `.pre-commit-config.yaml` with `language: system`, `pass_filenames: false`, `always_run: true`
- [ ] T005 [US2] Verify full hook suite: `pre-commit run --all-files` exits 0
- [ ] T006 [US2] Verify `pre-commit install` exits 0

---

## Phase 3: User Story 3 — Config-Only Output (Priority: P3)

**Goal**: PR diff contains only `.pre-commit-config.yaml`. No other files added or modified.

**Independent Test**: `git diff main --name-only` lists only `.pre-commit-config.yaml`.

- [ ] T007 [US3] Verify PR diff scope: `git diff main --name-only` returns exactly `.pre-commit-config.yaml` and nothing else
- [ ] T008 [US3] Verify pinned versions: inspect `rev` field in `.pre-commit-config.yaml` — MUST match `v\d+\.\d+\.\d+` pattern, not `latest` or a branch name
- [ ] T009 [US3] Verify `repos` length: `.pre-commit-config.yaml` contains exactly 2 entries in the `repos` list

---

## Dependencies & Execution Order

- **T001**: No dependencies — start here
- **T002**: Depends on T001
- **T003**: Depends on T002 (YAML must parse before running hooks)
- **T004**: Depends on T003 (ruff hook verified before adding pytest)
- **T005**: Depends on T004
- **T006**: Depends on T005
- **T007–T009**: Depends on T006; T007, T008, T009 can run in parallel [P]

### Parallel Opportunities

T007, T008, T009 are independent verification checks — they can run in parallel.

---

## Implementation Strategy

Linear: build the config incrementally (ruff first, then pytest), verify at each step, then audit scope. No TDD cycle — verification gates replace red-green.

Complete in order: T001 → T002 → T003 → T004 → T005 → T006 → T007/T008/T009 (parallel).

---

## Notes

- T007 uses `git diff main` not `git diff HEAD` — the comparison base is the target branch, matching what a PR diff would show
- The ruff `rev` in T001 should be the latest stable tag; bureau must look this up rather than hardcoding a stale version
- T002 (YAML parse check) is a lightweight gate before running `pre-commit` to avoid confusing error messages from a malformed config
