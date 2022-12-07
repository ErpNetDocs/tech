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


The calculated attribute would have the following expressions:

```
10:GETOBJVALUE	EXP:20	ATTRIB:Name	
20:GETOBJVALUE	EXP:30	REF:ContactMechanism
30:FIRST	EXP:40
40:FILTER	CHILD:ContactMechanisms	EXP:50	
50:EQUAL	EXP:60	CONST:1			
60:CAST	EX:70	CONST:System.Int32	
70:GETOBJVALUE	REF:ContactMechanism	ATTRIB:ContactMechanismType	
```

**Explanation:**

- 10: get the value of the Name attribute from EXP:20
- 20: get the referent object **ContactMechanism** of EXP:30
- 30: get the first value of the list returned by EXP:40
- 40: filter the list of records in the child table **ContactMechanisms** by the conditions in EXP:50
- 50: check if EXP:60 is equal to 1 (1 = email)
- 60: cast EXP:70 which contains the **ContactMechanismType** to integer
- 70: get the value of the attribute **ContactMechanismType** from the referent object **ContactMechanism**

**Notes**
If a person has more than one email, the attribute will return a random one. If a specific email is needed, more filters could be applied. 
If the person has no emails, the attribute will return an error. If you want to avoid that, you need to couny the records in the CHILD:ContactMechanisms first, and to try to get the email only if the records are more than one.
