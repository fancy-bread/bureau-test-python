# Data Model: Escalation Test — Report Generator with Missing Schema

**Date**: 2026-04-18

## Entities

No source entities. The observable output is a bureau run event stream.

## Expected Run Event Stream

| Event | Expected | Notes |
|-------|----------|-------|
| `run.started` | ✅ present | Bureau begins the run |
| `phase.started phase=planner` | ✅ present | Bureau enters planner phase |
| `run.escalated` | ✅ present | Planner identifies missing schema and halts |
| `phase.started phase=builder` | ❌ absent | Run does not reach builder |
| `run.completed` | ❌ absent | Run does not complete |
| PR URL | ❌ absent | No PR is opened |

## Escalation Body Structure

The `run.escalated` event MUST be followed by a body containing these four fields:

| Field | Required | Example |
|-------|----------|---------|
| `What happened:` | ✅ | Description naming `docs/report-schema.md` |
| `What's needed:` | ✅ | Description of what the schema must contain |
| `Options:` | ✅ | At minimum: (1) provide schema and resume, (2) abort |
| `Resume:` | ✅ | `bureau resume <run-id> --response "..."` |
