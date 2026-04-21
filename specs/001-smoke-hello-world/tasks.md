# Tasks: Smoke Test — Hello World Function

**Input**: Design documents from `specs/001-smoke-hello-world/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: Setup

- [ ] T001 Create `src/` and `tests/` directories at repository root if they do not exist

---

## Phase 2: User Story 1 — Bureau Completes a Run End-to-End (Priority: P1)

**Goal**: `greet(name: str) -> str` exists in `src/greeting.py`, covered by a passing test in `tests/test_greeting.py`.

**Independent Test**: `pytest tests/test_greeting.py` exits 0.

- [ ] T002 [US1] Write `tests/test_greeting.py` with tests for: `greet("Alice")` returns a string containing "Alice"; `greet("")` returns a string containing "World"; return type is `str`
- [ ] T003 [US1] Implement `src/greeting.py` with `greet(name: str) -> str` — if `name` is empty return `"Hello, World!"`, otherwise return `f"Hello, {name}!"`
- [ ] T004 [US1] Verify `pytest tests/test_greeting.py` exits 0

---

## Dependencies & Execution Order

- T001 → T002 → T003 → T004 (sequential)
