---
uid: cao-FLOOR
items: Operators
---

# FLOOR - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | FLOOR |
| Description | Returns the largest integer less than or equal to the specified number. |
| Parameter 1 Name | Number1 |
| Parameter 1 Type | double or decimal |
| Parameter 2 Name |
| Parameter 2 Type |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | Returns the largest integer less than or equal to Number1. |

## Example

The following example gets the largest integer that is less than or equal to 'Quantity' of a Sales Order Line:

```
10: FLOOR ATTRIB:QuantityValue                  
```
OUTPUT: 
<br/>If 'QuantityValue = 14.85', the output will be '14'.
<br/>If 'QuantityValue = 14', the output will be '14'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
