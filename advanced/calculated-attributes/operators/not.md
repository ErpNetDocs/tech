---
uid: cao-NOT
items: Operators
---

# NOT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Returns logical negation on an expression.           |
| Parameter 1 Name      | Condition                                                         |
| Parameter 1 Type      | boolean                                  |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | False - if Condition is True; True - if Condition is False                                                     |

***Example***

```      
10: NOT EXP:20
20: EQUAL ATTRIB:LineNo CONST:10   
```
OUTPUT: 
<br/>If 'LineNo = 10', the output will be 'False'.
<br/>If 'LineNo = 20', the output will be 'True'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*
