# Contract: greet function

**Module**: `src.greeting`
**Exported symbol**: `greet`

## Signature

```python
def greet(name: str) -> str:
```

## Behavior Contract

| Input | Expected Output |
|-------|----------------|
| `"Alice"` | Contains `"Alice"` |
| `"World"` | Contains `"World"` |
| `""` | Contains `"World"` (empty string treated as default) |

## Constraints

- Return value MUST be a non-empty string
- Return value MUST contain the resolved name
- No side effects (no print, no I/O, no mutation)
- No external dependencies

## Test Obligations

The test file MUST cover:
1. A named input (e.g., `greet("Alice")`)
2. The empty-string default (e.g., `greet("")`)
3. Return type assertion (`isinstance(result, str)`)
