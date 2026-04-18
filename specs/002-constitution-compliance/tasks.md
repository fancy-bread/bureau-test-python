# Tasks: Constitution Compliance — Temperature Conversion Module

**Input**: Design documents from `specs/002-constitution-compliance/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to

---

## Phase 1: Setup

**Purpose**: No new directory structure needed — `src/` and `tests/` exist from spec 001.

- [ ] T001 Confirm `src/` and `tests/` directories exist at repository root (no-op if spec 001 was implemented; create if not)

---

## Phase 2: User Story 1 — Celsius to Fahrenheit (Priority: P1)

**Goal**: `celsius_to_fahrenheit(celsius: float) -> float` exists in `src/temperature.py`, covered by three test cases, test committed before implementation.

**Independent Test**: `pytest tests/test_temperature.py::test_celsius_to_fahrenheit` exits 0.

### Tests — Write First, Verify They Fail ⚠️ TDD REQUIRED

> Tests for `celsius_to_fahrenheit` MUST be committed and failing before T004 begins.

- [ ] T002 [US1] Write `tests/test_temperature.py` with three test cases for `celsius_to_fahrenheit`: `(100.0 → 212.0)`, `(0.0 → 32.0)`, `(-40.0 → -40.0)`
- [ ] T003 [US1] Verify tests fail: run `pytest tests/test_temperature.py` and confirm `ImportError` or `AttributeError` (red phase confirmed); commit test file

### Implementation

- [ ] T004 [US1] Add `celsius_to_fahrenheit(celsius: float) -> float` to `src/temperature.py` using formula `(celsius * 9/5) + 32`; no imports; no other statements
- [ ] T005 [US1] Verify tests pass: run `pytest tests/test_temperature.py::test_celsius_to_fahrenheit` exits 0 (green phase confirmed); commit implementation

---

## Phase 3: User Story 2 — Fahrenheit to Celsius (Priority: P2)

**Goal**: `fahrenheit_to_celsius(fahrenheit: float) -> float` added to `src/temperature.py`, covered by three additional test cases, its tests committed before its implementation.

**Independent Test**: `pytest tests/test_temperature.py` exits 0 (all six cases pass).

### Tests — Write First, Verify They Fail ⚠️ TDD REQUIRED

> Tests for `fahrenheit_to_celsius` MUST be committed and failing before T007 begins.

- [ ] T006 [US2] Add three test cases for `fahrenheit_to_celsius` to `tests/test_temperature.py`: `(212.0 → 100.0)`, `(32.0 → 0.0)`, `(-40.0 → -40.0)`
- [ ] T007 [US2] Verify new tests fail: run `pytest tests/test_temperature.py` and confirm `fahrenheit_to_celsius` tests fail (red phase confirmed); commit updated test file

### Implementation

- [ ] T008 [US2] Add `fahrenheit_to_celsius(fahrenheit: float) -> float` to `src/temperature.py` using formula `(fahrenheit - 32) * 5/9`; no imports; no other statements
- [ ] T009 [US2] Verify all tests pass: run `pytest tests/test_temperature.py` exits 0 with all six cases (green phase confirmed); commit implementation

---

## Phase 4: User Story 3 — Minimal Scope Verification (Priority: P3)

**Goal**: Confirm `src/temperature.py` contains exactly two function definitions and nothing else.

**Independent Test**: `python -c "import ast, pathlib; tree = ast.parse(pathlib.Path('src/temperature.py').read_text()); stmts = tree.body; assert all(isinstance(s, ast.FunctionDef) for s in stmts), f'Extra statements: {[type(s).__name__ for s in stmts if not isinstance(s, ast.FunctionDef)]}'"`

- [ ] T010 [US3] Run AST scope check: verify `src/temperature.py` body contains exactly two `FunctionDef` nodes and zero other statement types
- [ ] T011 [US3] Run import check: verify `src/temperature.py` has zero import statements (`ast.Import` and `ast.ImportFrom` nodes absent)
- [ ] T012 [US3] Verify test count: confirm `tests/test_temperature.py` contains at minimum six test cases (one per input/output pair in the contract)

---

## Phase 5: Polish & Cross-Cutting Concerns

- [ ] T013 Run `pytest` at repo root to confirm no regressions in `tests/test_greeting.py` from spec 001
- [ ] T014 Verify TDD sequence for both functions via `git log --oneline -- tests/test_temperature.py src/temperature.py`

---

## Dependencies & Execution Order

- **T001**: No dependencies
- **T002**: Depends on T001
- **T003**: Depends on T002 — MUST confirm red before T004
- **T004**: Depends on T003 (red gate)
- **T005**: Depends on T004 — MUST confirm green before T006
- **T006**: Depends on T005
- **T007**: Depends on T006 — MUST confirm red before T008
- **T008**: Depends on T007 (red gate)
- **T009**: Depends on T008 — MUST confirm green before T010
- **T010–T012**: Depends on T009
- **T013–T014**: Depends on T012

### Parallel Opportunities

None within phases. The TDD red-green gates enforce strict sequencing. T010–T012 (US3 verification) can run in parallel with each other.

---

## Implementation Strategy

Two TDD cycles in sequence: C→F first, then F→C. US3 audits the final state. Complete in order: T001 → T002 → T003 (gate) → T004 → T005 → T006 → T007 (gate) → T008 → T009 → T010–T012 → T013–T014.

---

## Notes

- T003 and T007 are hard gates: bureau MUST NOT advance past them if tests pass prematurely
- T010 uses `ast.parse` — this is the Critic's verification tool, not an implementation task
- T013 confirms spec 001 is not broken by spec 002 (regression guard)
- The two TDD cycles are independent in content but sequential in order — spec 001's `greeting.py` pattern is the model
