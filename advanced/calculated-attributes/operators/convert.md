---
uid: cao-CONVERT
items: Operators
---

# CONVERT 

| Specification    | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | The CONVERT operator converts a parameter to a specified type. <br>It is commonly used by other operators to ensure parameter values are of the same type, particularly when the type of both of these parameters is a standard .Net type. <br> Accurate input data is crucial for successful conversion; otherwise, data loss may occur without triggering an error. For instance, converting the string '3.12' to decimal will succeed, but attempting to convert 'abc' to a numeric type will fail. |
| Parameter 1 Name | param                                                        |
| Parameter 1 Type | decimal, int, string, or date                                 |
| Parameter 2 Name | type                                                         |
| Parameter 2 Type | string - 'System.Int32', 'System.String', 'System.Decimal', 'System.DateTime' and all standard .Net types |
| Parameter 3 Name | -                                                            |
| Parameter 3 Type | -                                                            |
| Return value     | Returns the param converted to the type.                     |


<br/>**Tip:** If you can change the type using the 'CONVERT' operator, you should typically use the 'cao-CAST' operator instead—and vice versa.


<br/>**Example:**

Let's convert the quantity value of a sales order line, which is a decimal number, to an integer number:

```
10: CONVERT ATTRIB: QuantityValue CONST: System.Int32                  
```
OUTPUT: <br> If 'QuantityValue = 12.14', the output will be '12'.


#### More examples:

- **[Convert a value of a custom property to a number](../examples/convert-property-to-number.md)**
