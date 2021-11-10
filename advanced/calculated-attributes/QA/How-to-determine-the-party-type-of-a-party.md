---
items: CalculatedAttributesQA
---

# How to determine the party type of a party?

If we need to compare the **PartyType** to check if it is a company, person or other, the following calculation would do the job:

```
CAST ATTRIB:PartyType CONST:System.Int32
```

Casting the **PartyType** to integer would return the following values:

- 0 - Company
- 1 - Company Location
- 2 - Person
- 3 - Store
- 4 - Company Division
