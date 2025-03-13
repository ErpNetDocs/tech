---
uid: cao-CONVERT
items: Operators
---

# CONVERT 

| Specification    | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | Returns an object of specified type, the value of which is equivalent to the specified object. <br> This conversion requires **correct** input data - otherwise, loss may occur with no error returned. If you convert the string value of '3.12' to decimal, the conversion will be successful.  |
| Parameter 1 Name | param                                                        |
| Parameter 1 Type | decimal, int, string, or date                                 |
| Parameter 2 Name | type                                                         |
| Parameter 2 Type | string - 'System.Int32', 'System.String', 'System.Decimal', 'System.DateTime' and all standard .net types |
| Parameter 3 Name | -                                                            |
| Parameter 3 Type | -                                                            |
| Return value     | Returns the param converted to the type.                     |


**Example:**

Let's convert the quantity value of a sales order line, which is a decimal number, to an integer number:

```
10: CONVERT ATTRIB: QuantityValue CONST: System.Int32                  
```
OUTPUT: <br> If 'QuantityValue = 12.14', the output will be '12'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*.

> **Tip:** If you can change the type using the `CONVERT` operator, you should typically use the `CAST` operator instead—and vice versa.

#### More examples:

- **[Convert a value of a custom property to a number](../examples/convert-property-to-number.md)**
