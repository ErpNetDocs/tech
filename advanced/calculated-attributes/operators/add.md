---
uid: cao-ADD
items: Operators
---
# ADD 

| Specification | Value |
| ---- | ----- |
| Name | ADD |
| Description | The operator returns the sum (total) of two numbers. |
| Parameter 1 Name | Number1 |
| Parameter 1 Type | numeric type - int, double or decimal |
| Parameter 2 Name | Number2 |
| Parameter 2 Type | numeric type - int, double or decimal |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | Number1 + Number2 |

> [!NOTE]
> 
> Ensure that the numbers which are summed up are from the the same type. <br>
> For example, Parameter 1 and Parameter 2 must be both integers, doubles, or decimals.

## Example
The following example adds '0.25' to the the value of the Quantity field in sales order lines and returns the sum of the two numbers.
```
10: ADD ATTRIB:QuantityValue CONST:0.25                 
```
OUTPUT: If 'QuantityValue = 1', the output will be '1.25'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*


#### More examples:
- [Total quantity and scrap quantity in recipe ingredients](https://docs.erp.net/tech/advanced/calculated-attributes/examples/total-quantity-and-scrap-in-recipe-ingredients.html)
