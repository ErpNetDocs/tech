---
uid: cao-ADDDAYS
---
# ADDDAYS - Calculated Attribute Operator

| Specification | Value |
| ---- | ----- |
| Name | ADDDAYS |
| Description | Adds the specified number of days to the date. |
| Parameter 1 Name | Date |
| Parameter 1 Type | Date |
| Parameter 2 Name | NumDays |
| Parameter 2 Type | int |
| Parameter 3 Name |
| Parameter 3 Type |
| Return Value | Date + NumDays |

## Example

```
10: ADDDAYS ATTRIB:DocumentDate CONST:5                 
```
If 'DocumentDate = 2000-01-20', the output will be '2000-01-25'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrders*
