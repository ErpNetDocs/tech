---
uid: cao-FILTER
items: Operators
---

# FILTER 

| Specification | Value |
| ---- | ----- |
| Name | FILTER |
| Description | Filters a specified list by a condition. |
| Parameter 1 Name | list |
| Parameter 1 Type | list of objects |
| Parameter 2 Name | condition |
| Parameter 2 Type | boolean |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | Returns sub-list which meets the condition. |

**Example:**

Let's return a list with all lines in a document (sales order) whose quantity is '1.00':

```
10: FILTER CHILD:Lines EXP:30
30: EQUAL ATTRIB:QuantityValue CONST:1.00
```

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrders*
