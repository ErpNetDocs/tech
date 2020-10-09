---
uid: cao-MULTIPLY
items: Operators
---

# MULTIPLY - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Multiply the specified numbers.           |
| Parameter 1 Name      | Number1                                                        |
| Parameter 1 Type      | numeric type - int, double or decimal                                    |
| Parameter 2 Name      | Number2                                                            |
| Parameter 2 Type      | numeric type - int, double or decimal                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Number1 * Number2                                                         |

> [!NOTE]
> Ensure that the numbers of both parameters are from the the same type. For example, Parameter 1 and Parameter 2 must be both integers, doubles, or decimals.

## Example

```
10: ADD ATTRIB:QuantityValue CONST:2.00                
```
OUTPUT: If 'QuantityValue = 3.00', the output will be '6.00'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*


#### More Examples
[Total Quantity And Scrap Quantity In Recipe Ingredients](../examples/TotalQuantityAndScrapQuantityInRecipeIngredients.md).

