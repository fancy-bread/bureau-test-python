# Contract: .github/workflows/pr-cleanup.yml

**File**: `.github/workflows/pr-cleanup.yml`
**Format**: GitHub Actions YAML

## Required Fields

| Field | Required Value |
|-------|---------------|
| `on.schedule[0].cron` | Valid cron expression, daily or more frequent |
| `on.workflow_dispatch` | Present (enables manual trigger) |
| `permissions.contents` | `write` |
| `permissions.pull-requests` | `write` |
| `jobs.stale` | Present — uses `actions/stale@v9` |
| `days-before-stale` | `7` |
| `days-before-close` | `2` |
| `exempt-pr-labels` | Includes `keep` |
| Branch deletion step | Present — skips `main` |

## Verification Commands

```bash
# YAML validates
yamllint .github/workflows/pr-cleanup.yml

# Required fields present
grep -q "actions/stale" .github/workflows/pr-cleanup.yml
grep -q "days-before-stale: 7" .github/workflows/pr-cleanup.yml
grep -q "days-before-close: 2" .github/workflows/pr-cleanup.yml
grep -q "workflow_dispatch" .github/workflows/pr-cleanup.yml
grep -q "contents: write" .github/workflows/pr-cleanup.yml
grep -q "pull-requests: write" .github/workflows/pr-cleanup.yml
```

All commands MUST exit 0.
