---
uid: cao-GETVALUE
items: Operators
---

# GETVALUE 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the value of an object.          |
| Parameter 1 Name      | Value                                                        |
| Parameter 1 Type      | attribute value                                   |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | Value                                                         |


**Example:**

Let's return the value of _Notes_ in a sales order line:
```
10: GETVALUE ATTRIB:Notes             
```
OUTPUT: <br> If 'Notes = Apple', the output will be 'Apple'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLiness*

