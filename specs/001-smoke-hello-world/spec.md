# Feature Specification: Smoke Test — Hello World Function

**Feature Branch**: `001-smoke-hello-world`
**Created**: 2026-04-18
**Status**: Draft
**Input**: Bureau e2e test harness — T1 smoke test

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Bureau Completes a Run End-to-End (Priority: P1)

A developer runs `bureau run specs/001-smoke-hello-world/spec.md --repo ./` against this repo. Bureau validates the spec, plans the implementation, builds it, the Critic verifies it, and a PR is opened. The run completes without escalation.

**Why this priority**: This is the foundational smoke test. If bureau cannot complete a run on the simplest possible spec, no other test case is meaningful.

**Independent Test**: Run `bureau run specs/001-smoke-hello-world/spec.md --repo ./`. Verify structured phase events appear on stdout, the run completes with `run.completed`, and a PR is opened referencing this spec.

**Acceptance Scenarios**:

1. **Given** this spec file exists and the repo has a valid `.bureau/config.toml`, **When** `bureau run specs/001-smoke-hello-world/spec.md --repo ./` is invoked, **Then** the run completes with `[bureau] run.completed` on stdout and a PR URL is printed
2. **Given** a completed bureau run, **When** the PR is reviewed, **Then** it contains a new file `src/greeting.py` with a `greet(name: str) -> str` function
3. **Given** a completed bureau run, **When** `pytest` is run against the repo, **Then** all tests pass including at least one test covering `greet()`
4. **Given** a completed bureau run, **When** the PR is reviewed, **Then** the test file was committed before the implementation file (TDD sequence verifiable via git log)

---

### Edge Cases

- What happens if `greet()` receives an empty string? The function MUST return a non-empty greeting (e.g., treat empty name as "World").
- What happens if `greet()` receives a non-string argument? Out of scope — no runtime type checking required beyond type annotations.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The repo MUST contain a Python module at `src/greeting.py` exporting a function `greet(name: str) -> str`
- **FR-002**: `greet(name)` MUST return a greeting string that includes the provided name (e.g., `"Hello, Alice!"`)
- **FR-003**: `greet("")` MUST return a valid greeting using `"World"` as the default name
- **FR-004**: A test file MUST exist at `tests/test_greeting.py` covering at minimum: a named greeting, an empty-string input, and the return type
- **FR-005**: The test file MUST be committed before the implementation file (TDD sequence)
- **FR-006**: The module MUST include a Python type annotation on the function signature

### Key Entities

- **greet function**: Pure function, no side effects, no I/O, no external dependencies

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `pytest tests/test_greeting.py` exits 0 with no failures
- **SC-002**: `git log --oneline` shows the test file commit appears before the implementation file commit
- **SC-003**: Bureau's run summary on the PR lists zero constitution violations
- **SC-004**: Bureau's run completes in under 5 minutes (smoke test must be fast)

## Assumptions

- The repo has a `.bureau/config.toml` present before bureau is invoked (not bureau's responsibility to create it)
- Python 3.11+ is the target runtime
- No `src/__init__.py` or packaging setup is required — the module is importable via `PYTHONPATH=.`
- pytest is available in the environment where bureau runs
