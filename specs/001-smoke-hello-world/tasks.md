# Tasks: Smoke Test — Hello World Function

**Input**: Design documents from `specs/001-smoke-hello-world/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: Setup

**Purpose**: Create the source directory structure this repo lacks.

- [ ] T001 Create `src/` and `tests/` directories at repository root

---

## Phase 2: User Story 1 — Bureau Completes a Run End-to-End (Priority: P1)

**Goal**: `greet(name: str) -> str` exists in `src/greeting.py`, covered by a passing test suite, with the test commit preceding the implementation commit.

**Independent Test**: `pytest tests/test_greeting.py` exits 0; `git log --oneline -- src/greeting.py tests/test_greeting.py` shows the test file commit appearing after the implementation file commit would be a constitution violation — test commit MUST appear first.

### Tests — Write First, Verify They Fail ⚠️ TDD REQUIRED

> Tests MUST be committed and failing before T004 begins. Bureau MUST verify red state via `pytest` before advancing.

- [ ] T002 [US1] Write `tests/test_greeting.py` covering: named greeting (`greet("Alice")`), empty-string default (`greet("")` returns string containing "World"), return type assertion (`isinstance(result, str)`)
- [ ] T003 [US1] Verify tests fail: run `pytest tests/test_greeting.py` and confirm `ModuleNotFoundError` or `ImportError` (red phase confirmed)

### Implementation

- [ ] T004 [US1] Implement `src/greeting.py` with `greet(name: str) -> str` satisfying the contract in `contracts/greeting.md` (empty string → "World" default)
- [ ] T005 [US1] Verify tests pass: run `pytest tests/test_greeting.py` exits 0 (green phase confirmed)

---

## Phase 3: Polish & Cross-Cutting Concerns

- [ ] T006 Verify `git log --oneline -- tests/test_greeting.py src/greeting.py` shows test commit before implementation commit (TDD sequence audit)
- [ ] T007 Verify `python -c "from src.greeting import greet; print(greet('Bureau'))"` runs without error (importability check via PYTHONPATH=.)

---

## Dependencies & Execution Order

- **Phase 1** (T001): No dependencies — run immediately
- **T002**: Depends on T001 (directories exist)
- **T003**: Depends on T002 (tests written) — MUST confirm red before T004
- **T004**: Depends on T003 (red confirmed) — constitution gate
- **T005**: Depends on T004 (implementation written) — MUST confirm green
- **T006–T007**: Depends on T005 (green confirmed)

### Parallel Opportunities

None. Tasks are strictly sequential due to the TDD red-green gate.

---

## Implementation Strategy

This spec has a single user story and a strict TDD sequence. There is no MVP subset — the entire spec is the MVP. Complete in order: T001 → T002 → T003 (gate) → T004 → T005 → T006 → T007.

---

## Notes

- T003 is a hard gate: bureau MUST NOT advance to T004 if tests pass prematurely (would indicate the test file is wrong)
- T006 is the TDD audit task — bureau's Critic checks `git log` to verify sequence, not just file existence
- No parallelism in this spec by design: smoke tests should be deterministic and linear
