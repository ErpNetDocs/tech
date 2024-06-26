---
items: CalculatedAttributesQA
---

# How to get specific field of a parent document?

When calculating an attribute requires the value of an attribute of a parent document, there are two options:

1. The attribute is part of the parent document table
2. The attribute is part of the specific entity of the parent document (SalesOrder, StoreOrder, StoreTransaction, Payment, etc.)

In the first case, you may get the value directly by **[GETOBJVALUE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/getobjvalue.html)** operator in the following expression:

```
10: GETOBJVALUE REF:Parent ATTRIB:DocumentNo
```

This expression would be valid for every document which has a parent document.

In the second case, you need to tell the calculated attribute what the parent document is. <br> This is done by casting the parent document to the required entity.

**Example:**

```
10: GETOBJVALUE EXP:20 ATTRIB:DocumentNo
20: CAST REF:Parent CONST:Aloe.EnterpriseOne.Model.Crm.Presales.Offer
```

It's supposed to show such calculated attributes in the document form where the parent document is 'offer'.
