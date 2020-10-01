---
uid: cao-FORMATSTRING
---

# FORMATSTRING - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Returns the specified object, formatted by the specified rules.           |
| Parameter 1 Name      | Param1                                                       |
| Parameter 1 Type      | object (any type)                                  |
| Parameter 2 Name      | Format                                                            |
| Parameter 2 Type      | string - the format argument must contain a valid .NET Framework format string, either as a standard format string (for example, "C" or "D") or as a pattern of custom characters for dates and numeric values (for example, "MMMM DD, yyyy (dddd)"). For more information about the supported format specifiers, see @(Format Specifiers).                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Param1 as a string formatted by the rule in Format.                                                          |


## Example

The following expression:

FORMATSTRING CONST:150 CONST:C3
returns "150.000 $" (and the decimal symbol separator and the currency symbol depends on the local regional settings).

For more information about the supported format specifiers, see @(Format Specifiers).
> [!NOTE]
> The Format is entered as a constant (CONST).

If we have a calculated attribute with the following expression (the repository is not important):


- FORMATSTRING CONST:2020-03-15 CONST: yyyy MM dddd
The output of the calculated attribute would be "2020 03 Sunday".
- FORMATSTRING CONST:150 CONST: n6
The output of the calculated attribute would be "150,000000" (the decimal symbol separator depends on the local regional settings).
- FORMATSTRING CONST:150 CONST: C
The output of the calculated attribute would be "150.00 $" (the currency depends on the local regional settings).
- c
The output of the calculated attribute would be "150.00 $" (the currency depends on the local regional settings).
