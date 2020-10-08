---
uid: cao-LEN
---

# LEN - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Returns the length of the string.           |
| Parameter 1 Name      | String                                                         |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | -                                                            |
| Parameter 2 Type      | -                                                            |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Returns the length of a string.                                                  |

> [!NOTE] 
> The spaces are included when calculating the length.

## Example
The following example returns the lenght of the Notes set in the Sales Order:
```
10: LEN ATTRIB:Notes
```
OUTPUT: 
<br/> If 'Notes = Apple', the output will be '5'.
<br/> If 'Notes = I am', the output will be '4'. 

> [!NOTE] 
> The repository of the attribute is Crm.Sales.SalesOrders
