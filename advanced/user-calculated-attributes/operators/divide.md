---
uid: cao-DIVIDE
---
# DIVIDE - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | DIVIDE |
| Description | Divide one number by second number |
| Parameter 1 Name | Number1 |
| Parameter 1 Type | numeric type - int, double or decimal |
| Parameter 2 Name | Number2 |
| Parameter 2 Type | numeric type - int, double or decimal |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | Number1 / Number2 |

> [!NOTE]
> Ensure that the numbers which are summed up are from the the same type. For example, Parameter 1 and Parameter 2 must be both integers, doubles, or decimals.

## Example

```
10: ADD ATTRIB:QuantityValue CONST:2.00                
```
OUTPUT: If 'QuantityValue = 6.00', the output will be '3.00'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*


#### More Examples
[Calculate StandartPricePerLot Based on the Ingredients and the Operations in the Recipe](../examples/CalculateStandartPricePerLotBasedOnTheIngredientsAndTheOperationsInTheRecipe.md)
