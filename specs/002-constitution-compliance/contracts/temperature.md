# Contract: temperature module

**Module**: `src.temperature`
**Exported symbols**: `celsius_to_fahrenheit`, `fahrenheit_to_celsius`

## celsius_to_fahrenheit

```python
def celsius_to_fahrenheit(celsius: float) -> float:
```

| Input | Expected Output |
|-------|----------------|
| `100.0` | `212.0` |
| `0.0` | `32.0` |
| `-40.0` | `-40.0` |

## fahrenheit_to_celsius

```python
def fahrenheit_to_celsius(fahrenheit: float) -> float:
```

| Input | Expected Output |
|-------|----------------|
| `212.0` | `100.0` |
| `32.0` | `0.0` |
| `-40.0` | `-40.0` |

## Module-Level Constraints

- Zero import statements
- Exactly two top-level function definitions, nothing else
- No `if __name__ == "__main__"` block
- No `try/except` blocks
- No `isinstance` or type guard calls
- No docstrings (type annotations are the documentation)

## Test Obligations

`tests/test_temperature.py` MUST cover all six input/output pairs above.
Tests for each function MUST be committed before that function's implementation.
