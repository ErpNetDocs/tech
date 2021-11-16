---
uid: cao-LTE
items: Operators
---

# LTE 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Checks if an attribute value is smaller than or equal to another attribute's value <br> (or a constant).          |
| Parameter 1 Name      | attribute1                                                        |
| Parameter 1 Type      | numeric (int, double, decimal) or datetime type                                  |
| Parameter 2 Name      | attribute2                                                            |
| Parameter 2 Type      | numeric (int, double, decimal) or datetime type                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | If attribute1 <= attribute2, the returned value is 'True', if else - the operator returns 'False'.                                                          |
 
Make sure the compared attributes have the same type. 

For example, Parameter 1 and Parameter 2 must be both integers, or doubles, or decimals, or datetime.

Learn more in **[Compare unit price and the standard unit price](https://docs.erp.net/tech/advanced/calculated-attributes/examples/compare-unit-and-standard-unit-price.html)**.


**Example:**

```      
10: LTE ATTRIB:LineNo CONST:30   
```
OUTPUT: 
<br/>If 'LineNo = 20', the output will be 'True'.
<br/>If 'LineNo = 30', the output will be 'True'.
<br/>If 'LineNo = 40', the output will be 'False'.


> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*


