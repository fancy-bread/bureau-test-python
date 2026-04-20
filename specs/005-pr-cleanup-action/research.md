# Research: PR Cleanup GitHub Actions Workflow

**Date**: 2026-04-18
**Status**: Complete

## Findings

| Decision | Rationale | Alternatives Considered |
|----------|-----------|------------------------|
| `actions/stale@v9` | Latest stable major; widely used, maintained by GitHub | Custom script — unnecessary complexity for standard stale management |
| Stale after 7 days, close after 2 days | Matches the fast iteration cadence of a test repo; bureau runs are short-lived | 14/7 defaults — too long for a CI test harness |
| Branch deletion via `gh api` DELETE call in a separate job | No maintained action exists for this; `gh` CLI is available on all GitHub-hosted runners | `peter-evans/delete-merged-branches` — archived/unmaintained |
| `on: schedule: cron: '0 6 * * *'` (daily at 06:00 UTC) | Daily is sufficient; avoids rate limit pressure | Hourly — overkill for a low-volume repo |
| `GITHUB_TOKEN` only | No secrets to manage; standard permissions sufficient for this repo | PAT — unnecessary overhead |
| Exempt label: `keep` | Short, memorable, unambiguous | `no-stale`, `wip` — `keep` is more explicit as a human override |
