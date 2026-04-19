# Contract: Bureau Escalation Output

**Observable surface**: bureau stdout
**Expected terminal event**: `run.escalated` (not `run.completed`)

## stdout Contract

A passing bureau run against this spec MUST produce output matching this structure:

```
[bureau] run.started  id=<run-id>  spec=specs/004-escalation-missing-schema/spec.md  repo=./
[bureau] phase.started  phase=planner
[bureau] run.escalated  id=<run-id>  phase=planner  reason=BLOCKER

  What happened:  <text containing "docs/report-schema.md">
  What's needed:  <text describing schema contents>
  Options:
    1. <option to provide schema and resume>
    2. <option to abort>

  Resume: bureau resume <run-id> --response "..."
```

## Assertions

| Assertion | Pass Condition |
|-----------|---------------|
| `run.escalated` present | `grep -q "run.escalated" <stdout>` exits 0 |
| `docs/report-schema.md` named | `grep -q "report-schema.md" <stdout>` exits 0 |
| `What happened:` present | `grep -q "What happened:" <stdout>` exits 0 |
| `What's needed:` present | `grep -q "What's needed:" <stdout>` exits 0 |
| `Options:` present | `grep -q "Options:" <stdout>` exits 0 |
| `Resume:` present | `grep -q "Resume:" <stdout>` exits 0 |
| `run.completed` absent | `grep -q "run.completed" <stdout>` exits 1 |
| PR URL absent | `grep -qE "https?://github.com/.*/pull/" <stdout>` exits 1 |
| Builder not reached | `grep -q "phase=builder" <stdout>` exits 1 |

## Pre-Run Guard

Before invoking bureau, the test harness MUST verify:

```bash
[ ! -f docs/report-schema.md ] || (echo "ERROR: docs/report-schema.md must not exist before running spec 004" && exit 1)
```

If the file exists, the test is invalid and MUST be aborted.
