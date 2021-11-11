---
uid: cao-COUNT
items: Operators
---

# COUNT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the number of elements contained within a list.           |
| Parameter 1 Name      | list                                                         |
| Parameter 1 Type      | list - repository, child.                                    |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | int                                                          |
| Introduced in version | 2020.1                                                       |

**Example:**

Let's have a number of lines in a document (sales order) returned:

```
10: COUNT CHILD:Lines
```

> [!NOTE]
> 
> The repository of the attribute is Crm.Sales.SalesOrders.

If you want to expand the example and get the number of lines with quantity greater than or equal to 10, <br> the following attribute would do the job:

```
10: COUNT EXP:20
20: FILTER CHILD:Lines EXP:30
30: GTE ATTRIB:QuantityValue CONST:10.00
```
