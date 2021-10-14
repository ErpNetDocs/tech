---
uid: cao-IN
items: Operators
---

# IN - Calculated attribute operator

| Specification | Value |
| --------------------- | ------------------------------------------------------------ |
| Description           | Determines whether a specified value matches any value in a list. The operator is used in combination with **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** and **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** as condition. It can be used to search through values of string and guid types. It cannot be used to search through numeric values or dates.           |
| Parameter 1 Name      | param                                                      |
| Parameter 1 Type      | String or Guid                                    |
| Parameter 2 Name      | list of values                                                         |
| Parameter 2 Type      | the values must be equal to the param type                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | True or False depending on if param equals a member of the list of values.                                                          |


> [!NOTE]
> 
> Single quotes are only necessary when the values which we compare to are strings.

## Example

The following example checks whether there are sales orders with notes 'Apple' and 'Pear' into the datatabase:
```
10: SELECT REPO:Crm.Sales.SalesOrders EXP:20
20: WHERE EXP:30
30: IN ATTRIB:Notes CONST:'Apple', 'Pear'
```

OUTPUT: 
<br/>If there is atleast one sales order with 'Notes = Apple', the output will be 'True'.
<br/>If there is atleast one sales order with 'Notes = Pear', the output will be 'True'.
<br/>If there are NO sales orders with 'Notes = Apple OR Pear', the output will be 'False'.
