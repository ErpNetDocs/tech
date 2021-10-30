---
uid: cao-LIKE
---

# LIKE 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Searches for a specified pattern in a string. It is usually used in a combination with the wildcars '%' and '\_': <br/> The '%' symbol is used to define 0 or more characters before and after the searched string. <br/> '\_' is used to define specifically 1 character.          |
| Parameter 1 Name      | String1                                                       |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | Mask                                                          |
| Parameter 2 Type      | string                                                          |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | True in case String1 matches Mask. False in case String1 does not match Mask.                                                         |


***Examples***


- 'a%' → Finds any values that start with "a".

- '%a' → Finds any values that end with "a".

- '%a%' → Finds any values that have "a" in any position.

- '_a%' → Finds any values that have "a" in the second position.

- 'a_%_%' → Finds any values that start with "a" and are at least 3 characters in length.

- 'a%o' → Finds any values that start with "a" and ends with "o".


The following example returns True if the the string contains 'Apple' and after 'Apple' there is exactly one character:

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
> The repository of the attribute is Crm.Sales.SalesOrders

