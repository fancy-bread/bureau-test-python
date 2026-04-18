# Implementation Plan: Constitution Compliance — Temperature Conversion Module

**Branch**: `002-constitution-compliance` | **Date**: 2026-04-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/002-constitution-compliance/spec.md`

## Summary

Add `src/temperature.py` with two pure functions — `celsius_to_fahrenheit(celsius: float) -> float` and `fahrenheit_to_celsius(fahrenheit: float) -> float` — covered by `tests/test_temperature.py` with six test cases. TDD sequence enforced: each function's tests committed before its implementation. No imports, no validation, no extras. A third acceptance story explicitly verifies bureau's minimal-scope discipline.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: pytest (test runner only; implementation has no external dependencies)
**Storage**: N/A
**Testing**: pytest
**Target Platform**: Linux/macOS (wherever bureau runs)
**Project Type**: library — single pure function module
**Performance Goals**: N/A
**Constraints**: Importable via `PYTHONPATH=.`; zero import statements in implementation file
**Scale/Scope**: one module, two functions, one test file with six cases

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Specs as Test Cases | ✅ PASS | US3 is explicitly a scope-audit story with programmatic verification (`ast.parse`) |
| II. Test-First | ✅ PASS | FR-005 mandates test commits precede implementation commits; tasks enforce TDD gates per function |
| III. Python Primary | ✅ PASS | Pure Python, no cross-language output |
| IV. Minimal Scope | ✅ PASS | FR-006/FR-007 explicitly prohibit extras; US3 verifies at PR review |
| V. Verifiable Outputs | ✅ PASS | `pytest` exit code + `ast.parse` scope check are the verification oracles |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/002-constitution-compliance/
├── plan.md              ← this file
├── research.md          ← Phase 0 (minimal — no unknowns)
├── data-model.md        ← Phase 1
├── contracts/
│   └── temperature.md   ← function contracts
└── tasks.md             ← Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
src/
├── greeting.py          ← from spec 001 (unchanged)
└── temperature.py       ← celsius_to_fahrenheit, fahrenheit_to_celsius

tests/
├── test_greeting.py     ← from spec 001 (unchanged)
└── test_temperature.py  ← six test cases for temperature functions
```

**Structure Decision**: Same flat layout as spec 001. `temperature.py` sits alongside `greeting.py` — no subdirectories, no package init, no cross-module dependencies.

## Complexity Tracking

No constitution violations to justify.
