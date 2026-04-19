# Tasks: Escalation Test — Report Generator with Missing Schema

**Input**: Design documents from `specs/004-escalation-missing-schema/`
**Prerequisites**: plan.md ✅ spec.md ✅ research.md ✅ data-model.md ✅ contracts/ ✅

**Note**: This spec has no implementation tasks. Bureau's correct behaviour is to halt during the planner phase. All tasks are verification tasks that assert the escalation output matches the contract in `contracts/escalation.md`.

## Format: `[ID] [P?] [Story] Description`

---

## Phase 1: Pre-Run Guard

**Purpose**: Ensure the test conditions are valid before invoking bureau.

- [ ] T001 [US1] Verify `docs/report-schema.md` does not exist: `[ ! -f docs/report-schema.md ]` exits 0 — if it exists, abort and document as invalid test state

---

## Phase 2: User Story 1 — Bureau Escalates on Missing Schema (Priority: P1)

**Goal**: Bureau emits `run.escalated` and halts. No PR is opened.

**Independent Test**: Capture bureau stdout; assert `run.escalated` present and `run.completed` absent.

- [ ] T002 [US1] Run bureau and capture stdout: `bureau run specs/004-escalation-missing-schema/spec.md --repo ./ 2>&1 | tee /tmp/bureau-004.log`
- [ ] T003 [US1] Assert `run.escalated` present: `grep -q "run.escalated" /tmp/bureau-004.log` exits 0
- [ ] T004 [US1] Assert `docs/report-schema.md` named in escalation: `grep -q "report-schema.md" /tmp/bureau-004.log` exits 0
- [ ] T005 [US1] Assert escalation body has required fields: verify `What happened:`, `What's needed:`, `Options:`, and `Resume:` all appear in `/tmp/bureau-004.log`
- [ ] T006 [US1] Assert `run.completed` absent: `grep -q "run.completed" /tmp/bureau-004.log` exits 1
- [ ] T007 [US1] Assert no PR URL: `grep -qE "https?://github.com/.*/pull/" /tmp/bureau-004.log` exits 1
- [ ] T008 [US1] Assert builder phase not reached: `grep -q "phase=builder" /tmp/bureau-004.log` exits 1

---

## Phase 3: Escalation Quality Check

**Purpose**: Verify the escalation is actionable, not just present.

- [ ] T009 [P] [US1] Assert run ID is present in `run.escalated` line: `grep -qE "run.escalated.*id=run-" /tmp/bureau-004.log` exits 0
- [ ] T010 [P] [US1] Assert `Resume:` line contains a `bureau resume` command with the run ID: `grep -qE "bureau resume run-" /tmp/bureau-004.log` exits 0
- [ ] T011 [P] [US1] Assert `phase=planner` in escalation line (not a later phase): `grep -qE "run.escalated.*phase=planner" /tmp/bureau-004.log` exits 0

---

## Dependencies & Execution Order

- **T001**: Pre-run guard — MUST pass before T002
- **T002**: Depends on T001
- **T003–T008**: Depend on T002; run sequentially against the captured log
- **T009–T011**: Depend on T003 (escalation confirmed present); can run in parallel [P]

---

## Implementation Strategy

There is no implementation. The run is the test. Complete in order: T001 (guard) → T002 (run) → T003–T008 (primary assertions) → T009–T011 (quality assertions, parallel).

---

## Notes

- T001 is a hard guard: if `docs/report-schema.md` exists the test is invalid. Bureau would complete the run, producing a false negative.
- T002 uses `tee` to preserve the log for all subsequent assertions without re-running bureau
- T008 (builder not reached) is the strongest assertion — it confirms bureau escalated during planning, not by failing during build
- A bureau run that passes T003 but fails T008 means bureau reached the builder and then escalated — weaker behaviour than the spec requires
