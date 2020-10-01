---
uid: cao-SELECT
---

# SELECT - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the objects matching the clauses.           |
| Parameter 1 Name      | Repository                                                         |
| Parameter 1 Type      | repository                                    |
| Parameter 2 Name      | Clauses (optional, but highly advisable) // For more information see the 'FILTER AND WHERE filtering of a SELECT' section below)                                                           |
| Parameter 2 Type      | operators (@WHERE, @TOP)                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Returns a list of objects from Repository matching Clauses.                                                        |

> [!NOTE]
> The SELECT operator returns limited number of records - 20 000. This limit is only for the returned records count, so as setting much filters as possible are highly recommended (filters in the @WHERE clause).

## Example

The WHERE clause of the SELECT statement supports the following operators:


```
[AND](and.md)
TOP
EQUAL
GT
GTE
LT
LTE
```



If we want to expand the example and if we want to get the number of  lines with quantity greater than or equal to 10, the following attribute would do the job:

```
10: COUNT EXP:20
20: FILTER CHILD: Lines EXP:30
30: GTE ATTRIB: QuantityValue CONST: 10
```
