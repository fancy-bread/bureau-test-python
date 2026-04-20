# Data Model: PR Cleanup GitHub Actions Workflow

**Date**: 2026-04-18

## Workflow Structure

```
name: PR Cleanup
on:
  schedule: daily at 06:00 UTC
  workflow_dispatch: (manual trigger for testing)

permissions:
  contents: write
  pull-requests: write

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v9
        with:
          days-before-stale: 7
          days-before-close: 2
          exempt-pr-labels: keep
          stale-pr-message: <message>
          close-pr-message: <message>

  delete-merged-branches:
    runs-on: ubuntu-latest
    steps:
      - delete all merged remote branch refs except main
        using: gh api DELETE /repos/{owner}/{repo}/git/refs/heads/{branch}
        for each: merged PR branch that is not main
```

## Key Constraints

| Field | Value |
|-------|-------|
| `days-before-stale` | 7 |
| `days-before-close` | 2 |
| Exempt label | `keep` |
| Protected branch | `main` (never deleted) |
| Permissions | `contents: write`, `pull-requests: write` |
| Secrets required | None — `GITHUB_TOKEN` only |
