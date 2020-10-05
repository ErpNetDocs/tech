---
uid: cao-FIRST
---

# FIRST - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | FIRST |
| Description | Returns the first element in the list. |
| Parameter 1 Name | list |
| Parameter 1 Type | list of objects |
| Parameter 2 Name |
| Parameter 2 Type |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | Returns the first element of list. |

> [!NOTE]
> The FIRST operator returns the first met element of the list, but the criateria about which element is actually first may not match your expectations. If the sorting of the elements matters, please use in combinations with the @cao-SORT and @cao-ORDERBY operators.

## Example

The following example returns the first met line of the current document (SalesOrder):

```
10: FIRST CHILD:Lines
```

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrders*

If we want to expand the example we can sort the line ascending by line number. This way the atrribute will return the line with lowest line number:

```
10: FIRST EXP:20
20: SORT CHILD:Lines ATTR:LineNo CONST:ASC
```
