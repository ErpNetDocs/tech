---
uid: cao-OR
items: Operators
---

# OR 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Checks if any conditions are true. If so - the operator returns 'True'. <br> If all specified conditions aren't true, the operator returns 'False'.           |
| Parameter 1 Name      | Condition1                                                         |
| Parameter 1 Type      | boolean                                  |
| Parameter 2 Name      | Condition2                                                            |
| Parameter 2 Type      | boolean                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | Condition1 OR Condition2                                                     |


**Example:**

```      
10: OR EXP:20 EXP:30
20: EQUAL ATTRIB:LineNo CONST:10
30: EQUAL ATTRIB:LineNo CONST:20
```
OUTPUT: 
<br/>If 'LineNo = 10', the output will be 'True'.
<br/>If 'LineNo = 20', the output will be 'True'.
<br/>If 'LineNo = 30', the output will be 'False'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

> [!NOTE]
OR is not supported by SELECT but used by the FILTER operator.
More information: https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html 
