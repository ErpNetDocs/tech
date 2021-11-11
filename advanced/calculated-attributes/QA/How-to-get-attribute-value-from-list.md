---
items: CalculatedAttributesQA
---

# How to get attribute value from list?

A typical mistake is when users try getting a value of an attribute from a list. 

For example, if you want to get the user who changed the document state:

```
10: GETOBJVALUE CHILD:StateChanges ATTRIB:UpdateUser
```

This is an **incorrect** expression.

The right expression would be to **filter** the child list and then get the first element of the list. 

**Example:**

```
10 GETOBJVALUE EXP:20 ATTRIB:UpdateUser
20 FIRST EXP:30 
30 FILTER CHILD:StateChanges EXP:40
40 EQUAL ATTRIB:SystemInitiated CONST:False
```

**Explanation:**

- 10: get the value of the **UserUpdate** field from object in expression 20
- 20: get the first record in the list in expression 30
- 30: filter the child list **StateChanges** by the filter in expression 40
- 40: check if the attribute **SystemInitiated** is equal to "False"
