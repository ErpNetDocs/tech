# User Business Rules

## ⚠️ Breaking Changes

**JavaScript user business rules** now expose enum values as **strings instead of numbers** by default.

String comparisons like `'Receipt'` or `'Released'` now work as expected. Scripts that compare enums to numeric values (for example `=== 1`) may no longer behave correctly.

Numeric enum handling can be temporarily restored via `/Scripting/UseNumericEnumConversionMode`, but migrating to string-based comparisons is strongly recommended.
