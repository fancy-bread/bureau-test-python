# Feature Specification: Constitution Compliance — Temperature Conversion Module

**Feature Branch**: `002-constitution-compliance`
**Created**: 2026-04-18
**Status**: Draft
**Input**: Bureau e2e test harness — T2 constitution compliance test

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Convert Celsius to Fahrenheit (Priority: P1)

A developer imports `convert` from `src/temperature.py` and calls `celsius_to_fahrenheit(100.0)`, receiving `212.0`. The function is covered by a test written before the implementation exists.

**Why this priority**: Establishes the module, the TDD sequence, and the type annotation requirement. All other stories build on this one.

**Independent Test**: `pytest tests/test_temperature.py::test_celsius_to_fahrenheit` passes; `git log` shows the test commit precedes the implementation commit.

**Acceptance Scenarios**:

1. **Given** `celsius_to_fahrenheit` is called with `100.0`, **When** the result is returned, **Then** it equals `212.0`
2. **Given** `celsius_to_fahrenheit` is called with `0.0`, **When** the result is returned, **Then** it equals `32.0`
3. **Given** `celsius_to_fahrenheit` is called with `-40.0`, **When** the result is returned, **Then** it equals `-40.0`
4. **Given** the implementation file, **When** the function signature is inspected, **Then** it carries type annotations on both the parameter and return value

---

### User Story 2 — Convert Fahrenheit to Celsius (Priority: P2)

A developer calls `fahrenheit_to_celsius(212.0)` and receives `100.0`. This function is added to the same module under the same TDD discipline.

**Why this priority**: Tests that bureau applies TDD and minimal scope consistently across a second function in the same module, not just once.

**Independent Test**: `pytest tests/test_temperature.py::test_fahrenheit_to_celsius` passes.

**Acceptance Scenarios**:

1. **Given** `fahrenheit_to_celsius` is called with `212.0`, **When** the result is returned, **Then** it equals `100.0`
2. **Given** `fahrenheit_to_celsius` is called with `32.0`, **When** the result is returned, **Then** it equals `0.0`
3. **Given** `fahrenheit_to_celsius` is called with `-40.0`, **When** the result is returned, **Then** it equals `-40.0`
4. **Given** the implementation file, **When** the function signature is inspected, **Then** it carries type annotations on both the parameter and return value

---

### User Story 3 — Minimal Scope Verification (Priority: P3)

The final PR contains no functionality beyond what this spec requires. No input validation, no error handling for non-numeric input, no CLI entrypoint, no `__all__` export list, no logging, no docstrings beyond what the type annotations already express.

**Why this priority**: This story exists specifically to test bureau's minimal-scope discipline (Constitution Principle IV). An agent that "helpfully" adds validation or a CLI entrypoint fails this story even if the core functions are correct.

**Independent Test**: Review `src/temperature.py` — the file contains exactly two functions and nothing else. No `if __name__ == "__main__"`, no `try/except`, no `isinstance` checks, no imports.

**Acceptance Scenarios**:

1. **Given** the submitted `src/temperature.py`, **When** its contents are reviewed, **Then** it contains exactly two function definitions and no other top-level statements
2. **Given** the submitted `src/temperature.py`, **When** its imports are checked, **Then** it has zero import statements
3. **Given** the submitted `tests/test_temperature.py`, **When** its test count is checked, **Then** it covers at minimum the three input/output pairs for each function (six test cases total)

---

### Edge Cases

- Floating-point precision: `celsius_to_fahrenheit(-40.0)` and `fahrenheit_to_celsius(-40.0)` both return `-40.0` — this is the convergence point and MUST be tested.
- Non-numeric input is explicitly out of scope. No type guards or `ValueError` handling required or permitted.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `src/temperature.py` MUST export a function `celsius_to_fahrenheit(celsius: float) -> float`
- **FR-002**: `src/temperature.py` MUST export a function `fahrenheit_to_celsius(fahrenheit: float) -> float`
- **FR-003**: Both functions MUST carry Python type annotations on all parameters and return values
- **FR-004**: `tests/test_temperature.py` MUST exist and cover at minimum three input/output pairs per function (six cases total), including the `-40.0` convergence point
- **FR-005**: The test file for each function MUST be committed before the corresponding implementation (TDD sequence)
- **FR-006**: `src/temperature.py` MUST contain no import statements
- **FR-007**: `src/temperature.py` MUST contain no top-level statements other than the two function definitions

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pytest tests/test_temperature.py` exits 0 with all cases passing
- **SC-002**: `git log --oneline` shows test commits preceding implementation commits
- **SC-003**: Bureau's PR run summary reports zero constitution violations
- **SC-004**: `src/temperature.py` contains exactly two function definitions and zero import statements (verifiable with `ast.parse`)
- **SC-005**: Bureau's run completes in under 5 minutes

## Assumptions

- Python 3.14+ is the target runtime
- `src/temperature.py` is importable via `PYTHONPATH=.` as `src.temperature`
- pytest is available in the environment
- Floating-point arithmetic precision to one decimal place is sufficient for all test assertions
