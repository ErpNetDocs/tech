---
items: CalculatedAttributesQA
---

# How to check whether a field that points to a reference object has a value?

Often when we are creating a calculated attribute and we  want to get a value from a referent object, first we need to check if the current record has a reference to this object at all. A.k.a. we need to check if a particular Id field has a value or not. 



The **recommended** way to perform this validation is to check whether there is a referent object:

```
20  EQUAL REF:AdjustedDocument CONST:NULL        
```

​        



and **NOT** whether the Id fields itself is empty:

```
20  EQUAL ATTRIB:AdjustedDocumentId CONST:NULL
```



The **first** **approach is recommended** because:

a. the second approach may lead to incorrect results - there are cases  with wrong results when this approach is used in a SELECT clause or in  multiple nested calculated attributes.

b. the first approach does  not require type conversions - we are directly checking of there is a  reference object and we don't have use CAST or CONVERT operators to  match the types before the comparison.

