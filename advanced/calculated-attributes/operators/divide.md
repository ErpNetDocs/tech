---
uid: cao-DIVIDE
items: Operators
---
# DIVIDE 

| Specification | Value |
| ---- | ----- |
| Name | DIVIDE |
| Description | Divides one number by a second number. |
| Parameter 1 Name | Number1 |
| Parameter 1 Type | numeric type - int, double or decimal |
| Parameter 2 Name | Number2 |
| Parameter 2 Type | numeric type - int, double or decimal |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | Number1 / Number2 |


Make sure that the numbers of both parameters are from the same type. 

For example, Parameter 1 and Parameter 2 must be both integers, doubles, or decimals.

**Example:**

```
10: DIVIDE ATTRIB:QuantityValue CONST:2.00                
```
OUTPUT: <br> If 'QuantityValue = 6.00', the output will be '3.00'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*


#### More examples:

- **[Calculate standart price per lot based on the ingredients and the operations in the recipe](https://docs.erp.net/tech/advanced/calculated-attributes/examples/calculate-standartpriceperlot.html)**
