---
items: CalculatedAttributesQA
---

# How to check if a field that points to a reference object has a value?

When you're creating a calculated attribute and want to get a value from a referent object, you need to check if the current record has a reference to this object at all - if a particular ID field has a **value** or not. 

The **recommended** way to perform this validation is to check whether there is a referent object:

```
20  EQUAL REF:AdjustedDocument CONST:NULL        
```

and **not** whether the ID fields itself is empty:

```
20  EQUAL ATTRIB:AdjustedDocumentId CONST:NULL
```

The first approach is better because:

a. the second approach may lead to **incorrect** results - there are cases  with wrong results when this approach is used in a **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** clause or in multiple nested calculated attributes.

b. the first approach **does not** require type conversions - you're directly checking if there is a reference object and you don't have to use **[CAST](https://docs.erp.net/tech/advanced/calculated-attributes/operators/cast.html)** or **[CONVERT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/convert.html)** operators to match the types before the comparison.

