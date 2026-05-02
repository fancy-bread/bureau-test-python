# bureau-test

End-to-end test harness for [bureau](https://github.com/fancy-bread/bureau) — the autonomous ASDLC runtime. Each spec in this repo is a test case: bureau runs against it, implements it, and the output is verified against acceptance criteria.

---

## What this repo is

Bureau takes a spec file and produces a pull request. This repo provides a controlled target environment for testing that full pipeline across four test tiers:

| Tier | Spec | What it tests |
|------|------|--------------|
| T1 — Smoke | `001-smoke-hello-world` | Does bureau complete a run end-to-end? |
| T2 — Constitution | `002-constitution-compliance` | Does bureau honor TDD sequence, type annotations, and minimal scope? |
| T3 — Escalation | `004-escalation-missing-schema` | Does bureau escalate with a structured blocker instead of guessing? |

---

## Setup

### Install bureau

Bureau is not yet published to PyPI. Install it from the source repo:

```bash
git clone https://github.com/fancy-bread/bureau.git
cd bureau
pip install -e .
```

Verify:

```bash
bureau --version
```

### Initialize bureau in this repo

Once bureau is installed, run `bureau init` from this repo root to scaffold `.bureau/config.toml`. This is required before any spec can be run:

```bash
cd bureau-test
bureau init
```

---

## Running a spec

```bash
bureau run specs/<spec-dir>/spec.md --repo ./
```

Bureau emits structured phase events to stdout and opens a PR on completion. For T4, the expected output is `run.escalated` — no PR is opened.

### Resume an interrupted run

```bash
bureau resume <run-id>
```

---

## Spec index

### 001 — Smoke: Hello World

**Branch**: `001-smoke-hello-world`  
**Goal**: Bureau produces `src/greeting.py` with `greet(name: str) -> str` and a passing test file. Test commit precedes implementation commit (TDD sequence verified via `git log`).  
**Pass condition**: `pytest` exits 0; `run.completed` in stdout; PR opened.

### 002 — Constitution Compliance: Temperature Conversion

**Branch**: `002-constitution-compliance`  
**Goal**: Bureau produces `src/temperature.py` with two pure functions across two TDD cycles. US3 verifies minimal scope via `ast.parse` — no imports, no validation, exactly two function definitions.  
**Pass condition**: `pytest` exits 0; zero constitution violations in PR summary; `ast.parse` scope check passes.

### 003 — Escalation: Missing Schema

**Branch**: `004-escalation-missing-schema`  
**Goal**: Bureau attempts to implement `generate_report()` but cannot determine the output format because `docs/report-schema.md` is missing. Bureau must halt during the planner phase with a structured escalation. **A completed run is a test failure.**  
**Pass condition**: `run.escalated` in stdout; `run.completed` absent; builder phase not reached; escalation body names the missing artifact and includes all required fields.

---

## Constitution

Project governance is in [.specify/memory/constitution.md](.specify/memory/constitution.md). Key principles:

- **Specs as test cases** — each spec is independently runnable by bureau
- **Test-first** — TDD is mandatory for Python implementation specs
- **Minimal scope** — no file changes beyond what the spec requires
- **Verifiable outputs** — every spec has a runnable acceptance oracle

---

## Repo structure

```
specs/
├── 001-smoke-hello-world/
├── 002-constitution-compliance/
└── 004-escalation-missing-schema/
    ├── spec.md        ← feature specification (the test case)
    ├── plan.md        ← implementation plan
    ├── tasks.md       ← ordered task list
    ├── contracts/     ← interface/output contracts
    └── checklists/    ← quality validation

src/                   ← Python source (produced by bureau)
tests/                 ← pytest test files (produced by bureau)
.bureau/               ← bureau runtime config (created by `bureau init`)
```
