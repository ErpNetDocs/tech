---
uid: cao-LEFT
---

# LEFT - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the first n characters of a string.          |
| Parameter 1 Name      | String                                                       |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | NumChars                                                           |
| Parameter 2 Type      | int                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Returns the first Numchars characters of the String.                                                          |


## Example
The following example returns the first 3 characters of the Notes set in the Sales Order:
```
10: LEFT ATTRIB:Notes CONST:3   
```
OUTPUT: 
<br/> If 'Notes = Apple', the output will be 'App'.
<br/> If 'Notes = I am', the output will be 'I a'. 

> [!NOTE] 
> The repository of the attribute is Crm.Sales.SalesOrders
