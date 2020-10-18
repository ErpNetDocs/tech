---
uid: cao-FILTER
items: Operators
---

# FILTER - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | FILTER |
| Description | Filters the specified list by the condition. |
| Parameter 1 Name | list |
| Parameter 1 Type | list of objects |
| Parameter 2 Name | condition |
| Parameter 2 Type | boolean |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | Returns sub-list, which meets the condition. |


## Example

The following example returns a list with all of lines in the current document (SalesOrder) whose quantity is '1.00':

```
10: FILTER CHILD:Lines EXP:30
30: EQUAL ATTRIB:QuantityValue CONST:1.00
```

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrders*
