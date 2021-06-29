---
uid: cao-EQUAL
items: Operators
---
# EQUAL - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | EQUAL |
| Description | Checks if two values are equal. If they are equal, the return value is True, else - the return value is False. |
| Parameter 1 Name | Value1 |
| Parameter 1 Type | numeric type - int, double or decimal; string; |
| Parameter 2 Name | Value2 |
| Parameter 2 Type | numeric type - int, double or decimal; string; |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | boolean (True or False) |

> [!NOTE]
> Ensure that the values which are compared up have the same type. For example, Parameter 1 and Parameter 2 must be both integers, or doubles, or decimals, or strings.

## Example

```      
10: EQUAL ATTRIB:LineNo CONST:30   
```
OUTPUT: 
<br/>If 'LineNo = 30', the output will be 'True'.
<br/>If 'LineNo = 10', the output will be 'False'.


> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

#### More Examples
[Check if the quantity is a whole number](../examples/check-if-quantity-is-whole-number.md)
<br/>[Check whether the releasing of the document is first or not](../examples/check-for-first-releasing.md)
<br/>[Get current availability of a product](../examples/get-current-availability-of-product.md)
