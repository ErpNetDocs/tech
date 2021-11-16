---
uid: cao-LIKE
---

# LIKE 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Searches for a specified pattern in a string. <br> Used in combination with the wildcars '%' and '\_': <br/> The '%' symbol defines 0 or more characters before and after the searched string. <br/> '\_' is used to define 1 specific character.          |
| Parameter 1 Name      | String1                                                       |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | Mask                                                          |
| Parameter 2 Type      | string                                                          |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | **True** in case String1 matches Mask. **False** in case String1 doesn't match Mask.                                                         |


**Examples:**


- 'a%' → Finds any values starting with "a".

- '%a' → Finds any values ending with "a".

- '%a%' → Finds any values having "a" in any position.

- 'a%' → Finds any values having "a" in second position.

- 'a_%%' → Finds any values starting with "a" and at least 3 characters in length.

- 'a%o' → Finds any values starting with "a" and ending with "o".


The following example returns 'True' if the string contains 'Apple'. After 'Apple', there is exactly one character:

```
10 LIKE ATTRIB:Notes CONST:%Apple_
```

OUTPUT: 
<br/> If 'Notes = Apples', the output will be 'True'.
<br/> If 'Notes = Green apples', the output will be 'True'.
<br/> If 'Notes = apples', the output will be 'False'.
<br/> If 'Notes = Apple', the output will be 'False'.
<br/> If 'Notes = Green bananas', the output will be 'False'.


> [!NOTE] 
> 
> The repository of the attribute is *Crm.Sales.SalesOrders*.

