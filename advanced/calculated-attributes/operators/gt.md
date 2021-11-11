---
uid: cao-GT
items: Operators
---

# GT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Checks if an attribute value is greater than another attribute's value (or a constant).           |
| Parameter 1 Name      | attribute1                                                         |
| Parameter 1 Type      | numeric (int, double, decimal) or datetime type                                    |
| Parameter 2 Name      | attribute2                                                          |
| Parameter 2 Type      | numeric (int, double, decimal) or datetime type                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | If attribute1 > attribute2, the returned value is 'True', if else - the operator returns 'False'.                                                          |

Make sure that the compared attributes are from the same type. 

For example, Parameter 1 and Parameter 2 must be both integers, or doubles, or decimals, or datetime.

**Example:**

```      
10: GT ATTRIB:LineNo CONST:30   
```
OUTPUT: 
<br/>If 'LineNo = 40', the output will be 'True'.
<br/>If 'LineNo = 30', the output will be 'False'.
<br/>If 'LineNo = 20', the output will be 'False'.


> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

#### More examples:

- **[Compare unit price and standard unit price](https://docs.erp.net/tech/advanced/calculated-attributes/examples/compare-unit-and-standard-unit-price.html)**


