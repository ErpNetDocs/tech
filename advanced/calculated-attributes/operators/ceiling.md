---
uid: cao-CEILING
items: Operators
---

# CEILING                                                       

| Specification| Value|
| ---- | ----- |
| Description      | Returns the smallest integer that is greater than or equal to the specified number. |
| Parameter 1 Name | Number1|
| Parameter 1 Type | double or decimal|
| Parameter 2 Name | - |
| Parameter 2 Type | - |
| Parameter 3 Name | - |
| Parameter 3 Type | - |
| Return value     | The nearest integer which is larger than Number1.|                                                           |



***Example***



The following example gets the smallest integer that is greater than or equal to the quantity of a sales order line:

```
10:CEILING ATTRIB:QuantityValue                  
```
OUTPUT: 
<br/>If 'QuantityValue = 14.15', the output will be '15'.
<br/>If 'QuantityValue = 14', the output will be '14'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
