---
uid: cao-FORMATSTRING
items: Operators
---

# FORMATSTRING 

| Specification| Value|
| ---- | ----- |
| Description| Returns a specified object formatted by specified rules.|
| Parameter 1 Name| Param1|
| Parameter 1 Type| object (any type)|
| Parameter 2 Name| Format|
| Parameter 2 Type| constant <br> |
| Parameter 3 Name| - |
| Parameter 3 Type| - |
| Return value| Param1 as a string formatted by the rule in Format.|


> [!NOTE]
> 
> The format argument must contain a valid .NET format string, either as a standard string ("C" or "D") or as a pattern of custom characters for dates and numeric values ("MMMM DD, yyyy (dddd)"). <br>
> For more information about supported format specifiers, see **[Format specifiers](https://docs.erp.net/tech/advanced/string-interpolation/format-specifiers.html)**.

**Example:**

Let's see some formats and format specifiers:

```
10: FORMATSTRING CONST:DocumentDate CONST:yyyy MM dddd
```
OUTPUT: <br> If 'DocumentDate = 2020-03-15', the output will be '2020 03 Sunday'.
<br/>(*the language of the day of the week depends on the local regional settings*)

```
10: FORMATSTRING ATTRIB:QuantityValue CONST:n6
```
OUTPUT: <br> If 'QuantityValue = 150.00', the output will be '150,000000'.
<br/>(*the decimal symbol separator depends on the local regional settings*)

```
10: FORMATSTRING ATTRIB:LineAmountValue CONST:C
```
OUTPUT: <br> If 'LineAmountValue = 150.00', the output will be '150.00 $'.
<br/>(*the decimal symbol separator and the currency symbol depends on the local regional settings*)


> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
