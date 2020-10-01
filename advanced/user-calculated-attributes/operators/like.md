---
uid: cao-LIKE
---

# LIKE - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Searches for a specified pattern in a string. The '%' symbol is used to define 0 or more characters before and after the searched string. '_' is used to define specifically 1 character.          |
| Parameter 1 Name      | String1                                                       |
| Parameter 1 Type      | string                                    |
| Parameter 2 Name      | Mask                                                          |
| Parameter 2 Type      | string                                                          |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | True in case String1 matches Mask. False in case String1 does not match the Mask.                                                         |


## Examples

The following example return the number of lines in the current document (SalesOrder):

```
'a%' → Finds any values that start with "a".

'%a' → Finds any values that end with "a".

'%a%' → Finds any values that have "a" in any position.

'_a%' → Finds any values that have "a" in the second position.

'a_%_%' → Finds any values that start with "a" and are at least 3 characters in length.

'a%o' → Finds any values that start with "a" and ends with "o".
```

Calculated Attribute:

```
Repository: General.Products.Products

10 LIKE EXP 20 CONST %shoe_
20 CAST ATTRIB Name CONST System.String
```

Calculated Attribute Result:
```
ProductName = sports shoes → True
ProductName = shoes → True
ProductName = sports shoess → False
ProductName = sports shoe → False
ProductName = sports jacket → False
```
