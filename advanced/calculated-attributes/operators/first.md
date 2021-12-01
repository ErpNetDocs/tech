---
uid: cao-FIRST
items: Operators
---

# FIRST 

| Specification | Value |
| ---- | ----- |
| Name | FIRST |
| Description | Returns the first element in a list. |
| Parameter 1 Name | list |
| Parameter 1 Type | list of objects |
| Parameter 2 Name |
| Parameter 2 Type |
| Parameter 3 Name |
| Parameter 3 Type |
| Return value | The first element in the list. |

> [!NOTE]
> 
> The criteria concerning which element is first may not meet your expectations. <br> If sorting matters to you, please use **FIRST** together with the **[SORT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/sort.html)** and **[ORDERBY](https://docs.erp.net/tech/advanced/calculated-attributes/operators/orderby.html)** operators.

**Example:**

Let's return the first met line of a document (sales order):

```
10: FIRST CHILD:Lines
```

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrders*

If you want to expand the example, you can sort the line in an ascending order by line number. 

This way, the atrribute will return the line with lowest line number:

```
10: FIRST EXP:20
20: SORT CHILD:Lines ATTR:LineNo CONST:ASC
```
