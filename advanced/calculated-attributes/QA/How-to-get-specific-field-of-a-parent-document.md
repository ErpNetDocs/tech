---
items: CalculatedAttributesQA
---

# How to get specific field of a parent document?

When in a calculation attribute there is a need for a value of an attribute of the parent document, there are two options:

1. The attribute is part of the parent document table
2. The attribute is part of the specific entity of the parent document

If the attribute is part of the parent document table, then we may get it directly by **[GETOBJVALUE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/getobjvalue.html)** operator in the following expression:

```
10: GETOBJVALUE REF:Parent ATTRIB:DocumentNo
```

This expression would be valid for every document which has a parent document.

But in the second case, when the attribute is part of the specific entity of the parent document (meaning SalesOrder, StoreOrder, StoreTransaction, Payment, etc.) then the user has to tell the calculated attribute what the parent document is. This is done by casting the parent document to the required entity.

**Example:**

```
10: GETOBJVALUE EXP:20 ATTRIB:DocumentNo
20: CAST REF:Parent CONST:Aloe.EnterpriseOne.Model.Crm.Presales.Offer
```

It is supposed to show such calculated attribute in document form where the parent document is exactly offer.
