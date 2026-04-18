# Data Model: Tooling Config — Pre-Commit Hooks

**Date**: 2026-04-18

## Entities

No persistent entities. No state. No storage. The deliverable is a single YAML config file.

## Config Structure (Logical Model)

**.pre-commit-config.yaml**

```
repos:
  - repo: <ruff remote repo URL>
    rev: <pinned version tag>
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

## Key Constraints

- `repos` is a list with exactly two entries: one remote (ruff), one local (pytest)
- `rev` on the remote entry MUST be a version tag string (e.g., `"v0.11.6"`), not a branch name
- The local pytest hook MUST include `pass_filenames: false` and `always_run: true`
- No additional top-level keys beyond `repos` are required
