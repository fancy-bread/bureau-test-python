# Data Model: Constitution Compliance — Temperature Conversion Module

**Date**: 2026-04-18

## Entities

No persistent entities. No state. No storage.

## Function Signatures (Logical Model)

**celsius_to_fahrenheit**
- Input: `celsius: float` — temperature in degrees Celsius
- Output: `float` — temperature in degrees Fahrenheit
- Formula: `(celsius * 9/5) + 32`
- Side effects: none
- Imports: none

**fahrenheit_to_celsius**
- Input: `fahrenheit: float` — temperature in degrees Fahrenheit
- Output: `float` — temperature in degrees Celsius
- Formula: `(fahrenheit - 32) * 5/9`
- Side effects: none
- Imports: none

## Key Invariant

`fahrenheit_to_celsius(celsius_to_fahrenheit(x)) == x` for any `x` (round-trip identity, subject to float precision).
The `-40.0` convergence point — where both scales agree — MUST be tested for both functions.
