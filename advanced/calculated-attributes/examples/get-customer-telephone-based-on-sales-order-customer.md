---
items: CalculatedAttributeExamples
---

# Get customer telephone based on Sales Order customer

This calculated attribute can get the telephone number of the customer in the current sales order. The result is determined by following the customer relation to the related party contact mechanisms, keeping only the records with contact mechanism type Telephone, taking the first matching record, and returning its Name value.

You can also use this attribute in a business rule or another formula when you need to fill, display, or compare the customer telephone number based on the selected customer in a sales order.

If the expression fails for any reason or no telephone record is found, it returns an N/A.


```
Repository: Crm.Sales.SalesOrders
```

```
5:  IFERROR EXP:7 EXP:100
7:  GETOBJVALUE REF:Customer EXP:8
8:  GETOBJVALUE REF:Party EXP:10
10: GETOBJVALUE EXP:20 ATTRIB:Name
20: GETOBJVALUE EXP:30 REF:ContactMechanism
30: FIRST EXP:40
40: FILTER CHILD:ContactMechanisms EXP:50
50: EQUAL EXP:60 CONST:5
60: CAST EXP:70 CONST:System.Int32
70: GETOBJVALUE REF:ContactMechanism ATTRIB:ContactMechanismType
100: GETVALUE CONST:"N/A"
```

**Explanation:**  
5 (IFERROR): Returns EXP:7; if an error occurs, returns EXP:100 (N/A)  
7: From the current Crm.Sales.SalesOrders record, gets the referenced Customer object (Crm.Sales.Customers)  
8: From the Customer, gets the referenced Party (General.Contacts.Parties)  
40 (FILTER CHILD:ContactMechanisms): From the Party, takes its child collection ContactMechanisms (i.e., party contact-mechanism links) and filters it by condition EXP:50  
50 (EQUAL): Keeps only entries where EXP:60 = 5 (Telephone)  
60 (CAST): Casts EXP:70 (enum) to System.Int32 so it can be compared to the numeric constant 5  
70: Reads ContactMechanismType from the referenced ContactMechanism  
30 (FIRST): Takes the first matching contact mechanism link from the filtered list 

If there are multiple phone numbers, this will return just one (based on the underlying order)  
20: From that selected record, gets the referenced ContactMechanism object (General.Contacts.ContactMechanisms)  
10: Returns the Name of the Contact Mechanism (commonly stored as the phone number text)  
100: Fallback return value (N/A) if the whole evaluation fails.
