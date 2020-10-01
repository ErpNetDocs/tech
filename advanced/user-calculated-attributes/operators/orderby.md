---
uid: cao-ORDERBY
---

# ORDERBY - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Clause, that specifies a column or expression on which the query result set is sorted. Used as a clause of SELECT.           |
| Parameter 1 Name      | attribute                                                         |
| Parameter 1 Type      | any type                                 |
| Parameter 2 Name      | order (optional) //if not set, the default is ASC                                                            |
| Parameter 2 Type      | const - ASC or DESC                                                            |
| Parameter 3 Name      | inner clauses (optional)                                                            |
| Parameter 3 Type      | expression                                                           |
| Return Value          | Ordered result set of a query by the specified column or expression.                                                          |
| Introduced In Version | (In implementation) |

## Example

```
10: SELECT REPO:General.Products.Products EXP:20
20: TOP CONST:5 EXP:30
30: ORDERBY ATTR:PartNumber CONST:ASC EXP:40
40: WHERE ...
```
