---
uid: cao-IIF
items: Operators
---

# IIF - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Depending on a specified condition, returns the second or the third argument.           |
| Parameter 1 Name      | Condition                                                        |
| Parameter 1 Type      | Boolean                                   |
| Parameter 2 Name      | TrueValue                                                   |
| Parameter 2 Type      | any type                                                         |
| Parameter 3 Name      | FalseValue                                                           |
| Parameter 3 Type      | any type                                                               |
| Return Value          | When Condition is True, returns TrueValue. When Condition is False, returns FalseValue  |

## Example

```      
10: IIF EXP:20 CONST:'Quantity is 1.00' CONST: 'Quantity is not 1.00'  
20: EQUAL ATTRIB:QuantityValue CONST:1.00
```
OUTPUT: 
<br/>If 'QuantityValue = 1.00', the output will be 'Quantity is 1.00'.
<br/>If 'QuantityValue = 2.00', the output will be 'Quantity is not 1.00'.


> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

#### More Examples
[Compare unit price and standard unit price](../examples/compare-unit-and-standard-unit-price.md)
<br/>[Check if a value of a field is changed in the adjustment document](../examples/check-if-field-is-changed-in-adjustment.md)
