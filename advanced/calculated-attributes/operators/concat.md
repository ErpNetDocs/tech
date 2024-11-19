---
uid: cao-CONCAT
items: Operators
---

# CONCAT                   

| Specification    | Value                     |
| ---------------- | ------------------------- |
| Description      | Concatenates two strings. |
| Parameter 1 Name | String1                   |
| Parameter 1 Type | string                    |
| Parameter 2 Name | String2                   |
| Parameter 2 Type | string                    |
| Parameter 3 Name | -                         |
| Parameter 3 Type | -                         |
| Return value     | String1 + String2         |

**Example:**

Let's concatenate the word 'Red' with the value of the field _Notes_ in a sales order lines:

```
10: CONCAT CONST:Red ATTRIB:Notes                  
```
OUTPUT: <br> If 'Notes  = Apple', the output will be 'RedApple'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

If you want to expand the example, you can add a space ( CONST:' ') between the both strings:
```
10: CONCAT CONST:Red EXP:20 
20: CONCAT CONST:' ' ATTRIB:Notes
```
OUTPUT:<br> If Notes = Apple, the output will be = Red Apple
