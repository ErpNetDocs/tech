---
uid: cao-LEFT
items: Operators
---

# LEFT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the first n characters of a string (starting from left).|
| Parameter 1 Name      | String                                                       |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | NumChars                                                     |
| Parameter 2 Type      | int                                                          |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | Returns the first numchars characters of the string.         |


## Example

The following example returns the first 3 characters of the notes set in the sales order:
```
10: LEFT ATTRIB:Notes CONST:3   
```
OUTPUT: 
<br/> If 'Notes = Apple', the output will be 'App'.
<br/> If 'Notes = I am', the output will be 'I a'. 

> [!NOTE] 
> 
> The repository of the attribute is Crm.Sales.SalesOrders
