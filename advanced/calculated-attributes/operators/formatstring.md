---
uid: cao-FORMATSTRING
items: Operators
---

# FORMATSTRING - Calculated Attribute Operator

| Specification| Value|
| ---- | ----- |
| Description| Returns the specified object, formatted by the specified rules.|
| Parameter 1 Name| Param1|
| Parameter 1 Type| object (any type)|
| Parameter 2 Name| Format|
| Parameter 2 Type| constant - the format argument must contain a valid .NET format string, either as a standard format string (for example, "C" or "D") or as a pattern of custom characters for dates and numeric values (for example, "MMMM DD, yyyy (dddd)"). For more information about the supported format specifiers, see @(Format Specifiers).|
| Parameter 3 Name| - |
| Parameter 3 Type| - |
| Return Value| Param1 as a string formatted by the rule in Format.|


> [!NOTE]
> For more information about the supported format specifiers, see [Format Specifiers](../reference/format-specifiers.md).

## Example

Here are some examples of the diffrent formats and format specifiers:

```
10: FORMATSTRING CONST:DocumentDate CONST:yyyy MM dddd
```
OUTPUT: If 'DocumentDate = 2020-03-15', the output will be '2020 03 Sunday'.
<br/>(*the language of the day of the week depends on the local regional settings*)

```
10: FORMATSTRING ATTRIB:QuantityValue CONST:n6
```
OUTPUT: If 'QuantityValue = 150.00', the output will be '150,000000'.
<br/>(*the decimal symbol separator depends on the local regional settings*)

```
10: FORMATSTRING ATTRIB:LineAmountValue CONST:C
```
OUTPUT: If 'LineAmountValue = 150.00', the output will be '150.00 $'.
<br/>(*the decimal symbol separator and the currency symbol depends on the local regional settings*)


> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
