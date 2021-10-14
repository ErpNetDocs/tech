---
uid: cao-GETVALUE
items: Operators
---

# GETVALUE 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the value from the current object.          |
| Parameter 1 Name      | Value                                                        |
| Parameter 1 Type      | attribute value                                   |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | Value                                                         |

## Example

The following example returns the value of the notes of the current sales order line:
```
10: GETVALUE ATTRIB:Notes             
```
OUTPUT: If 'Notes = Apple', the output will be 'Apple'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLiness*

