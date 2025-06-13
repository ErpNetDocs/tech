---
items: CalculatedAttributeExamples
---

# Check if an entity record has attached files

This example demonstrates how to create a calculated attribute that checks whether any files are attached to a specific record in the system — such as a document (e.g., Sales Order, Invoice), a definition record (e.g., Product definition, Lot definition), or other.

The result is a boolean value – `1` if there is at least one file attached, and `0` otherwise.

## Use Case

Sometimes it's necessary to visually indicate in the UI or trigger business logic based on whether an entity has associated files (e.g., documents, images, contracts). This calculated attribute can be used in views, reports, or workflows to enable such logic.

## Logic Overview

The attribute performs the following operations:

1. Selects the `Files` child collection of the extensible entity.
2. Filters the files to match the current entity’s `Id` against the `EntityItemId`.
3. Counts the filtered records.
4. Compares the count to 1 or more.
5. Returns `1` if there is at least one file, otherwise returns `0`.

## Expression

```
10 IIF EXP 20 CONST 1 CONST 0
20 GTE EXP 30 CONST 1
30 COUNT EXP 40
40 GETOBJVALUE EXP 50 CHILD Files
50 FIRST EXP 60
60 SELECT REPO Systems.Core.ExtensibleDataObjects EXP 70
70 WHERE EXP 80
80 EQUAL ATTRIB EntityItemId EXP 90
90 GETOBJVALUE INPUT 10 ATTRIB Id

```

## Explanation

- `GETOBJVALUE INPUT 10 ATTRIB Id`: gets the current entity's ID.
- `SELECT ... WHERE ...`: filters files in `Systems.Core.ExtensibleDataObjects` where `EntityItemId` equals the entity's ID.
- `COUNT`: counts the matching files.
- `GTE ... CONST 1`: checks if the count is greater than or equal to 1.
- `IIF`: returns 1 if the condition is true, otherwise 0.

