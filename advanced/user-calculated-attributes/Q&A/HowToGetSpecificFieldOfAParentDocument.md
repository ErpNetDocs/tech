---
items: CalculatedAttributesQ&A
---

# How to get specific field of a parent document?

When in a calculation attribute there is a need of a value  of attribute of the parent document there are two options to get them:

1. The attribute is part of the parent Document table
2. The attribute is part of the specific entity of the parent document

If the attribute is part of the parent Document table, than we may get it  directly by GETOBJVALUE operator in the following expression:

```
10: GETOBJVALUE REF:Parent ATTRIB:DocumentNo
```

This expression would be valid for every document which has parent document.

But in the second case, when the attribute is part of the specific entity  of the parent document (meaning SalesOrder, StoreOrder,  StoreTransaction, Payment and etc.) than the user has to tell the  calculate attribute what is the parent document. This is done by casting the parent document to the entity which is required (in the example a  cast to Offer is used):

```
10: GETOBJVALUE EXP:20 ATTRIB:DocumentNo
20: CAST REF:Parent CONST:Aloe.EnterpriseOne.Model.Crm.Presales.Offer
```

It is supposed to show such calculated attribute in document form where the parent document is exactly Offer.