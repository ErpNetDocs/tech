---
uid: cao-COUNT
items: Operators
---

# COUNT - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the number of elements contained in the list.           |
| Parameter 1 Name      | list                                                         |
| Parameter 1 Type      | list - repository, child.                                    |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | int                                                          |
| Introduced In Version | 2020.1                                                       |

## Example

The following example returns the number of lines in the current document (SalesOrder):

```
10: COUNT CHILD:Lines
```

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrders*

If we want to expand the example and if we want to get the number of  lines with quantity greater than or equal to 10, the following attribute would do the job:

```
10: COUNT EXP:20
20: FILTER CHILD:Lines EXP:30
30: GTE ATTRIB:QuantityValue CONST:10.00
```
