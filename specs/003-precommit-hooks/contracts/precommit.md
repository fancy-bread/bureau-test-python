# Contract: .pre-commit-config.yaml

**File**: `.pre-commit-config.yaml` (repository root)
**Format**: YAML

## Required Structure

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: <pinned-tag>          # e.g. v0.11.6
    hooks:
      - id: ruff
        types: [python]

  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
```

## Constraints

| Field | Requirement |
|-------|------------|
| `repos` length | Exactly 2 entries |
| ruff `rev` | Pinned version tag — MUST match `v\d+\.\d+\.\d+` pattern |
| pytest `pass_filenames` | MUST be `false` |
| pytest `always_run` | MUST be `true` |
| Other files in PR | None — `.pre-commit-config.yaml` is the only changed file |

## Verification Commands

```bash
# Validate YAML parses
python -c "import yaml; yaml.safe_load(open('.pre-commit-config.yaml'))"

# Run all hooks against current codebase
pre-commit run --all-files

# Install hooks
pre-commit install
```

All three MUST exit 0.
