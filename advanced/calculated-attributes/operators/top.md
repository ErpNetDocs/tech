---
uid: cao-TOP
items: Operators
---

# TOP 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Clause returning only the first N elements           |
| Parameter 1 Name      | Number                                                       |
| Parameter 1 Type      | int                                    |
| Parameter 2 Name      | Clauses                                                          |
| Parameter 2 Type      | operator **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)**                                                      |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | The first Number elements.                                                      |

> [!NOTE]
> 
> This operator is used with **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)**.


**Example:**

```
10: SELECT REPO:General.Products.Products EXP:20
20: TOP CONST:5 EXP:30
30: WHERE ...
```
