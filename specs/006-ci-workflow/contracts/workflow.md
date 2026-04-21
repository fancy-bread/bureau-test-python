# Contract: .github/workflows/ci.yml

**File**: `.github/workflows/ci.yml`
**Format**: GitHub Actions YAML

## Required Fields

| Field | Required Value |
|-------|---------------|
| `on.pull_request.branches` | Includes `main` |
| `jobs.ci.steps` checkout | `actions/checkout@v4` |
| `jobs.ci.steps` setup-python | `actions/setup-python@v5` with `python-version: "3.14"` |
| Install step | `pip install -e '.[dev]'` |
| Test step | `pytest` |
| Lint step | `ruff check .` |

## Verification Commands

```bash
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/ci.yml'))"
grep -q "pull_request" .github/workflows/ci.yml
grep -q "3.14" .github/workflows/ci.yml
grep -q "pip install -e" .github/workflows/ci.yml
grep -q "pytest" .github/workflows/ci.yml
grep -q "ruff check" .github/workflows/ci.yml
```

All MUST exit 0.
