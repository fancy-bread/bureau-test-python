# Data Model: Smoke Test — Hello World Function

**Date**: 2026-04-18

## Entities

No persistent entities. No state transitions. No storage.

## Function Signature (Logical Model)

**greet**
- Input: `name: str` — the name to include in the greeting
- Output: `str` — a greeting string containing the name
- Invariant: output is always non-empty
- Special case: `name == ""` → treat as `"World"`
- Side effects: none
