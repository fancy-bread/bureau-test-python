# Implementation Plan: Smoke Test — Hello World Function

**Branch**: `001-smoke-hello-world` | **Date**: 2026-04-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `specs/001-smoke-hello-world/spec.md`

## Summary

Add a pure Python function `greet(name: str) -> str` in `src/greeting.py` with a corresponding test file at `tests/test_greeting.py`. The test file MUST be committed before the implementation (TDD sequence). This is the T1 smoke test verifying bureau can complete a run end-to-end on the simplest possible spec.

## Technical Context

**Language/Version**: Python 3.14+
**Primary Dependencies**: pytest (test runner only; implementation has no external dependencies)
**Storage**: N/A
**Testing**: pytest
**Target Platform**: Linux/macOS (wherever bureau runs)
**Project Type**: library — single pure function module
**Performance Goals**: N/A
**Constraints**: Importable via `PYTHONPATH=.`; no packaging setup required
**Scale/Scope**: one module, one function, one test file

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Specs as Test Cases | ✅ PASS | Acceptance scenarios are programmatically checkable |
| II. Test-First | ✅ PASS | Plan explicitly requires test commit before impl commit |
| III. Python Primary | ✅ PASS | Pure Python module, no cross-language output |
| IV. Minimal Scope | ✅ PASS | One function, one file, no abstractions beyond spec |
| V. Verifiable Outputs | ✅ PASS | `pytest` exit code is the verification oracle |

No violations. Gate passes.

## Project Structure

### Documentation (this feature)

```text
specs/001-smoke-hello-world/
├── plan.md              ← this file
├── research.md          ← Phase 0 (minimal — no unknowns)
├── data-model.md        ← Phase 1
├── contracts/
│   └── greeting.md      ← function contract
└── tasks.md             ← Phase 2 (/speckit-tasks)
```

### Source Code (repository root)

```text
src/
└── greeting.py          ← greet(name: str) -> str

tests/
└── test_greeting.py     ← pytest test module
```

**Structure Decision**: Single flat layout. No subdirectories needed — one source module, one test module. `PYTHONPATH=.` makes `src.greeting` importable without a package install.

## Complexity Tracking

No constitution violations to justify.
