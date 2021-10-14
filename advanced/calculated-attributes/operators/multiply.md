---
uid: cao-MULTIPLY
items: Operators
---

# MULTIPLY 

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
> 
> Make sure the numbers of both parameters are from the the same type. 
> 
> For example, Parameter 1 and Parameter 2 must be both integers, doubles, or decimals.

## Example

```
10:  MULTIPLY ATTRIB:QuantityValue CONST:2.00                
```
OUTPUT: If 'QuantityValue = 3.00', the output will be '6.00'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*


#### More examples

- **[Total quantity and scrap quantity in recipe ingredients](https://docs.erp.net/tech/advanced/calculated-attributes/examples/total-quantity-and-scrap-in-recipe-ingredients.html)**.

