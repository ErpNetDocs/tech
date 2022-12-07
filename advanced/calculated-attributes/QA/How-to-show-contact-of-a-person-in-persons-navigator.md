---
items: CalculatedAttributesQA
---

# How to show contact of a person in Persons navigator?

The specifics of this calculated attribute is that the contact mechanism type is **enum**. 

Its values and codes are as follows:

| Member name | Value | Description                       |
| :---------- | :---- | :-------------------------------- |
| Address     | 0     | Address value. Stored as 'A'.     |
| Mail        | 1     | Mail value. Stored as 'E'.        |
| Fax         | 2     | Fax value. Stored as 'F'.         |
| MobilePhone | 3     | MobilePhone value. Stored as 'M'. |
| Other       | 4     | Other value. Stored as 'O'.       |
| Telephone   | 5     | Telephone value. Stored as 'T'.   |
| WebSite     | 6     | WebSite value. Stored as 'W'.     |

Let's say you need to get a column with email addresses. 

If a person has more than one email, the attribute will return a random one. <br> If a specific email is needed, more filters could be applied. 

The calculated attribute would have the following expressions:

```
10 GETOBJVALUE EXP:20 EXP:15
15 GETOBJVALUE REF:ContactMechanism ATTRIB:Name
20 FIRST EXP:21 
21 FILTER EXP:30 EXP:22
22 EQUAL EXP:23 CONST: 1
23 CAST EXP:25 CONST: System.Int32
23 GETOBJVALUE REF:ContactMechanism ATTRIB:ContactMechanismType
30 SELECT REPO:General.Contacts.PartyContactMechanisms EXP:40
40 WHERE EXP:50 
50 EQUAL ATTRIB:PartyId EXP:60
60 GETOBJVALUE INPUT:10 ATTRIB:PartyId
```

**Explanation:**

- 10: from the object from EXP:20, get the attribute from EXP:15
- 15: get the value of the attribute name from the referent object **ContactMechanism**
- 20: get the first element from the list in EXP:21
- 21: filter the list in EXP:30 by the conditions in EXP:22
- 22: check if EXP:23 is equal to 1
- 23: cast EXP:25 which contains the **ContactMechanismType** to integer
- 25: get the value of the attribute **ContactMechanismType** from the referent object **ContactMechanism**
- 30: select from repository **General.Contacts.PartyContactMechanisms** and filter it by EXP:40
- 40: the filter is in EXP:50
- 50: check if the value of attribute PartyId is equal to EXP:60
- 60: get the value of attribute **PartyId** of the input object of expression 10

