# Improved Serial Number Sequences in Execute Store Orders (v26.2)

In version **26.2**, we introduced an important improvement in the Barcode panel when working with serial numbers during **Execute Store Orders**.

## What changed?

Previously, the **SEQUENCE START / SEQUENCE END** modes were limited to Receipt-only scenarios.

Now the system supports more flexible and realistic warehouse workflows:

- **Issue-only lines**  
  → existing serial numbers are correctly identified and applied.

- **Receipt-only lines**  
  → new serial numbers are generated as expected.

- **Mixed Receipt/Issue documents**  
  → when an Issue line is detected, the system automatically uses existing serial numbers.

## Current limitation

To generate new serial numbers on Receipt lines, all visible document lines must still be of movement type **Receipt**.

## Why this matters

This improvement allows warehouse operators to handle serial numbers faster and more reliably in real-world scenarios, while maintaining strict control over serial number generation.
