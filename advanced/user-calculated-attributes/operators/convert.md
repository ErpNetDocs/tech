---
uid: cao-CONVERT
items: Operators
---

# CONVERT - Calculated Attribute Operator

| Specification    | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | Returns an object of the specified type and whose value is equivalent to the specified object. <br /> <br /> This conversion requires absolutely correct input data - if the data is not in the correct form, data loss may occur. For example: if the user tries to convert the string value of '3.12' to decimal, the conversion would be successful. If the conversion of the string is not possible, this may lead to data loss, but no error would be returned. |
| Parameter 1 Name | param                                                        |
| Parameter 1 Type | decimal, int, string or date                                 |
| Parameter 2 Name | type                                                         |
| Parameter 2 Type | string - 'System.Int32', 'System.String', 'System.Decimal', 'System.DateTime' and all standard .net types |
| Parameter 3 Name | -                                                            |
| Parameter 3 Type | -                                                            |
| Return Value     | Returns the param converted to the type.                     |


## Example


The following example converts the value of the 'Quantity' of a Sales Order Line, which is a decimal number, to an integer number:

```
10: CONVERT ATTRIB:QuantityValue CONST:System.Int32                  
```
OUTPUT: If 'QuantityValue = 12.14', the output will be '12'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

#### More Examples
[Convert a Value of a Custom Property to a Number](../examples/ConvertPropertyToNumber.md)