---
uid: cao-SORT
items: Operators
---

# SORT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Sorts an input list according to a specified attribute and order.          |
| Parameter 1 Name      | list                                                         |
| Parameter 1 Type      | list                                    |
| Parameter 2 Name      | attribute                                                           |
| Parameter 2 Type      | any type                                                         |
| Parameter 3 Name      | order (optional)                                                          |
| Parameter 3 Type      | string - ASC or DESC                                                          |
| Return жalue          | Returns the input list from parameter1, sorted by the specified attribute and in the specified order. <br> If not specified, the default order is ascending (ASC)                                                         |


**Example:**

Take the last line of a sales order (ordered by **LineNo**), which has quantity >= 0:

SalesOrder=>
```
10: FIRST EXP:20
20: SORT EXP:30 ATTR:LineNo CONST:DESC
30: FILTER CHILD:Lines EXP:40
40: GTE ATTR:QuantityValue CONST:0
```
