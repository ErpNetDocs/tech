---
uid: cao-IN
items: Operators
---

# IN 

| Specification | Value |
| --------------------- | ------------------------------------------------------------ |
| Description           | Determines if a specified value matches any value from a list. <br>  Used in combination with **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** and **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** as condition. <br> It can be used to search through values of string and guid types. <br> It cannot be used to search through numeric values or dates.           |
| Parameter 1 Name      | param                                                      |
| Parameter 1 Type      | String or Guid                                    |
| Parameter 2 Name      | list of values                                                         |
| Parameter 2 Type      | the values must be equal to the param type                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | True or False depending on whether a parameter equals a member from a list of values.                                                          |


> [!NOTE]
> 
> Single quotes are only necessary when the compared values are strings.
> 

**Example:**


Let's check whether there are sales orders with notes 'Apple' and 'Pear' in the datatabase:
```
10: SELECT REPO:Crm.Sales.SalesOrders EXP:20
20: WHERE EXP:30
30: IN ATTRIB:Notes CONST:'Apple', 'Pear'
```

OUTPUT: 
<br/>If there is at least one sales order with 'Notes = Apple', the output will be 'True'.
<br/>If there is at least one sales order with 'Notes = Pear', the output will be 'True'.
<br/>If there are NO sales orders with 'Notes = Apple OR Pear', the output will be 'False'.
