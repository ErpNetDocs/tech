---
uid: cao-CAST
items: Operators
---

# CAST 

| Specification | Value |
| ---- | ----- |
| Name | CAST |
| Description | The CAST operator converts a parameter to a specified type. <br/>It is commonly used by other operators to ensure parameter values are of the same type, particularly when the type one of these parameters is a custom @@name type (e.g., a specific enum).  |
| Parameter 1 Name | 	param |
| Parameter 1 Type | 	any type |
| Parameter 2 Name | 	type |
| Parameter 2 Type | const - 'System.Int32', 'System.String', 'System.Decimal', 'System.Double' and all standard .net types +  custom @@name types (e.g., a specific enum)  |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | Returns the param converted to the type. |


**Example:**

Let's convert the value of the state of a sales order with the type 'enum' to an integer number. 

Converting to an integer allows for comparison between the states (lower -> higher):
```
10: CAST ATTRIB: State  CONST: System.Int32      
```
OUTPUT: <br> If 'State = Released', the output will be '30'.

> **Tip:** If you can change the type using the `CAST` operator, you should typically use the `CONVERT` operator instead—and vice versa.

#### More examples:

- **[Check whether the releasing of the document is first or not](../examples/check-for-first-releasing.md)**
- **[Check if the system type of payment type in the sales order is 'In Cash'](../examples/check-if-system-type-is-in-cash.md)**
- **[Convert a value of a custom property to a number](../examples/convert-property-to-number.md)**

