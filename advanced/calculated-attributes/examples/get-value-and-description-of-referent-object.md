---
items: CalculatedAttributeExamples
---

# Get value and description of referent object

When a value is set to a custom property of an object, a new record is added to the **General.PropertyValue** repository.
The new record has its own Id, and an EntityItemId, which is the id of the specific object. 

In a calculated attribute, you'll need to filter the value for the specific property (PropertyId) of the specific object (EntityItemId) and then get the value or description. 

**Example:**

Let's see how to get the description of a property of the customer and show it in the offer form. 

Such a calculated attribute would have the following parameters:

```
Repository Name:Crm.Presales.Offers
```

And the calculated attribute expressions are as follows:

```
10: GETOBJVALUE EXP:20 ATTRIB:Description 
20: FIRST EXP:30 
30: SELECT REPO:General.PropertyValues EXP:40
40: WHERE EXP:50 
50: AND EXP:60 EXP:70
60: EQUAL ATTRIB:PropertyId CONST:e7005814-6140-4708-a9d8-aaaeb5b151ed
70: EQUAL ATTRIB:EntityItemId EXP:80
80: GETOBJVALUE INPUT:10 ATTRIB:CustomerId
```

**Explanation:**

- 10: get the attribute description of the object in expression 20 
- 20: get the first record in the list from expression 30
- 30: select repository **General.PropertyValues** filtered by expression 40
- 40: the filter is expression 50
- 50: expression 60 AND expression 70
- 60: check if the attribute **PropertyId** is equal to the constant of **e7005814-6140-4708-a9d8-aaaeb5b151ed** (this is a guid)
- 70: check if the attribute **EntityItemId** is equal to expression 80
- 80: get the attribute **CustomerId** of the input object of expression 10

 
If you need the value of the property, the first expression may be set to <br> **GETOBJVALUE EXP:20 ATTRIB:PropertyValueField**.
