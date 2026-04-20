# Feature Specification: PR Cleanup GitHub Actions Workflow

**Feature Branch**: `005-pr-cleanup-action`
**Created**: 2026-04-18
**Status**: Draft
**Input**: Repo housekeeping — bureau-test accumulates short-lived spec branches and PRs; manual cleanup is overhead

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Stale PRs Are Closed Automatically (Priority: P1)

A spec branch PR has been open without activity for several days. Without manual intervention, it is automatically marked stale and then closed, keeping the PR list focused on active work.

**Why this priority**: Stale PRs are the primary source of noise. Each bureau test run opens a PR; if not merged or closed promptly they accumulate.

**Independent Test**: Inspect `.github/workflows/pr-cleanup.yml` — verify it includes a step that closes stale PRs on a schedule.

**Acceptance Scenarios**:

1. **Given** `.github/workflows/pr-cleanup.yml` exists, **When** its trigger is inspected, **Then** it includes a `schedule` trigger with a valid cron expression
2. **Given** the workflow, **When** its jobs are inspected, **Then** it includes a step that marks PRs stale after a configurable number of days without activity
3. **Given** the workflow, **When** its jobs are inspected, **Then** it includes a step that closes PRs that have been stale for a configurable number of days

---

### User Story 2 — Merged Branch Refs Are Deleted Automatically (Priority: P2)

After a spec branch PR is merged, the remote branch ref is deleted automatically, preventing branch accumulation in the remote.

**Why this priority**: Each spec produces a branch. Merged branches left in the remote add noise to `git branch -r` and GitHub's branch list.

**Independent Test**: Inspect `.github/workflows/pr-cleanup.yml` — verify it includes a step or job that deletes merged branches.

**Acceptance Scenarios**:

1. **Given** the workflow, **When** its contents are inspected, **Then** it includes logic to delete remote branch refs after their PR is merged
2. **Given** the workflow file, **When** it is validated as YAML, **Then** it parses without error

---

### Edge Cases

- The `main` branch MUST be excluded from deletion regardless of merge state.
- PRs with the label `keep` or `wip` SHOULD be exempt from stale marking — this allows bureau runs in progress to be protected.
- The workflow MUST have `contents: write` and `pull-requests: write` permissions to close PRs and delete branches.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: `.github/workflows/pr-cleanup.yml` MUST exist after the PR is merged
- **FR-002**: The workflow MUST run on a `schedule` trigger using a valid cron expression (daily or more frequent)
- **FR-003**: The workflow MUST mark PRs stale after a period of inactivity (recommended: 7 days)
- **FR-004**: The workflow MUST close PRs that remain stale for a further period (recommended: 2 days)
- **FR-005**: The workflow MUST delete remote branch refs for merged PRs
- **FR-006**: The `main` branch MUST be exempt from deletion
- **FR-007**: The workflow MUST declare `contents: write` and `pull-requests: write` permissions
- **FR-008**: The workflow file MUST be valid YAML that parses without error
- **FR-009**: The PR diff MUST contain only `.github/workflows/pr-cleanup.yml` — no other files added or modified

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: `yamllint .github/workflows/pr-cleanup.yml` exits 0
- **SC-002**: Workflow contains a `schedule` trigger with a valid cron expression
- **SC-003**: Stale period and close period are explicitly configured (not left as defaults)
- **SC-004**: `main` branch exclusion is explicitly present in the workflow
- **SC-005**: PR diff contains exactly one file

## Assumptions

- The repo uses GitHub Actions
- The `actions/stale` action is used for stale PR management (standard, well-maintained)
- Branch deletion on merge can be handled by a separate job in the same workflow using the GitHub API or `gh` CLI, or via a dedicated action
- `yamllint` is available in the environment for validation
- The workflow runs under the default `GITHUB_TOKEN` — no additional secrets required
