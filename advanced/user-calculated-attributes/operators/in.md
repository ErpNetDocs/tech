---
uid: cao-IN
---

# IN - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Determines whether a specified value matches any value in a list. The operator is used in combination with SELECT and FILTER as condition. It can be used to search through values of string and guid types. It cannot be used to search through numeric values or dates.           |
| Parameter 1 Name      | param                                                      |
| Parameter 1 Type      | String or Guid                                    |
| Parameter 2 Name      | list of values                                                         |
| Parameter 2 Type      | the values must be equal to the param type                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | True or False depending on if param equals a member of the list of values.                                                          |


## Example

Extract all sales orders with document types DocumentTypeId = 'f207c991-6289-47f9-85ca-f85cd2864263' and DocumentTypeId = '4acbc342-c7e2-43b9-b63c-cb51d20e5ab4'. The calculated attribute would contain the following expressions:
```
10: SELECT REPO: Crm.Sales.SalesOrders EXP: 20
20: WHERE EXP:30
30: IN ATTRIB: DocumentTypeId CONST: f207c991-6289-47f9-85ca-f85cd2864263, 4acbc342-c7e2-43b9-b63c-cb51d20e5ab4
```

> [!NOTE]
> Single quotes are only necessary when the values which we compare to are strings.
