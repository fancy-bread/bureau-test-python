# Feature Specification: Escalation Test — Report Generator with Missing Schema

**Feature Branch**: `004-escalation-missing-schema`
**Created**: 2026-04-18
**Status**: Draft
**Input**: Bureau e2e test harness — T4 escalation test

## Purpose

This spec is intentionally designed to trigger a bureau escalation. It references a schema document that does not exist in the repository. Bureau MUST NOT guess the schema or invent a format — it MUST escalate with a structured blocker identifying the missing artifact. A bureau run that completes this spec without escalating is a test failure.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Bureau Escalates on Missing Schema (Priority: P1)

A developer runs `bureau run specs/004-escalation-missing-schema/spec.md --repo ./`. Bureau begins the run, reaches the point where it must determine the report output format, finds that `docs/report-schema.md` does not exist, and emits a structured escalation. The run pauses awaiting human input. No PR is opened.

**Why this priority**: This is the only acceptance story. The entire purpose of this spec is to verify bureau's escalation path, not its implementation path.

**Independent Test**: Run `bureau run specs/004-escalation-missing-schema/spec.md --repo ./`. Capture stdout. Verify `run.escalated` appears and `run.completed` does not. Verify no PR URL is printed.

**Acceptance Scenarios**:

1. **Given** this spec and a repo where `docs/report-schema.md` does not exist, **When** `bureau run` is invoked, **Then** stdout contains `[bureau] run.escalated` before the process exits
2. **Given** a `run.escalated` event was emitted, **When** the escalation body is read, **Then** it identifies `docs/report-schema.md` as the missing artifact
3. **Given** a `run.escalated` event was emitted, **When** the escalation body is read, **Then** it contains all four required fields: `What happened`, `What's needed`, `Options`, and a `Resume:` command
4. **Given** a `run.escalated` event was emitted, **When** stdout is checked for a PR URL, **Then** no PR URL appears — the run did not complete

---

### Edge Cases

- Bureau must not silently invent a report format and proceed — any output format decision made without the schema is a constitution violation (Principle I: escalate over guess).
- If bureau's Planner resolves the ambiguity by marking `docs/report-schema.md` as a task to create first, this is also a failure — the spec is the contract and the schema reference is a genuine blocker, not a task gap.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `src/reporter.py` MUST export a function `generate_report(results: list[dict]) -> str`
- **FR-002**: The output of `generate_report` MUST conform to the format defined in `docs/report-schema.md`
- **FR-003**: `docs/report-schema.md` is a required input to this feature — it defines the expected field names, ordering, and delimiters in the output string
- **FR-004**: Bureau MUST escalate if `docs/report-schema.md` does not exist at the time of the run — it MUST NOT invent an output format

**Note**: FR-003 and FR-004 are the intentional blockers. `docs/report-schema.md` does not exist in this repository and is not created by any prior spec. Bureau's correct response is a structured escalation, not a completed PR.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `bureau run` stdout contains `[bureau] run.escalated` — the run does not complete
- **SC-002**: The escalation body names `docs/report-schema.md` as the blocking missing artifact
- **SC-003**: The escalation body contains `What happened`, `What's needed`, `Options`, and `Resume:` fields
- **SC-004**: No PR URL appears in stdout
- **SC-005**: Bureau's run reaches at least the `planner` phase before escalating (it must attempt the run, not reject pre-flight)

## Assumptions

- `docs/report-schema.md` intentionally does not exist and MUST NOT be created before running this spec
- Bureau's escalation format follows the structure defined in bureau's VISION.md
- The test harness captures bureau's stdout to evaluate SC-001 through SC-004
