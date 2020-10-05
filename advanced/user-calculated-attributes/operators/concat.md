---
uid: cao-CONCAT
---

# CONCAT - Calculated Attribute Operator                      

| Specification    | Value                     |
| ---------------- | ------------------------- |
| Description      | Concatenates two strings. |
| Parameter 1 Name | String1                   |
| Parameter 1 Type | string                    |
| Parameter 2 Name | String2                   |
| Parameter 2 Type | string                    |
| Parameter 3 Name | -                         |
| Parameter 3 Type | -                         |
| Return Value     | String1 + String2         |

## Example


The following example concatenates the word 'Red' with the value of the field 'Notes' in Sales Order Lines:

```
10: CONCAT CONST:Red ATTRIB:Notes                  
```
OUTPUT: If 'Notes  = Apple', the output will be 'RedApple'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrderLines*

If we want to expand the example we can add a space between the both strings:
```
10: CONCAT CONST:Red EXP:20 
20: CONCAT CONST:' ' ATTRIB:Notes
```
OUTPUT: If 'Notes  = Apple', the output will be 'Red Apple'.
