---
items: CalculatedAttributesQA
---

# How to check if a custom property has values?

When there is a need to check if a custom property of an object has value, usually we can just **[CAST](https://docs.erp.net/tech/advanced/calculated-attributes/operators/cast.html)** the custom property to a string and then check if it is equal to null. However, the syntax of the calculated attribute should be tailored to the specifics of the property type of the particular custom property. Here are examples for the different custom property types which are universal to all repositories. The custom property code which is verified is **CustomProperty1**.

> [!Note]
> 
> When a custom property is cast to string, only its value will be processed, and not its description.

### Property type is 'Text' 

If the property type of the particular custom property is 'Text', use the following expressions:

```
10: IIF EXP:20 CONST:'null' CONST:'not null'
20: EQUAL EXP:30 CONST:NULL
30: CAST ATTRIB:@CustomProperty1 CONST:System.String
```

**Explanation:**

- 10: if EXP:20 is true, return the text 'null, else - return 'not null'
- 20: if EXP:30 is empty, return true, else - return false
- 30: cast CustomProperty1 to string


### Property type is 'Number' or 'Date'

If the property type of the particular custom property is 'Number' or 'Date', use the following expressions:

```
10: IIF EXP:20 CONST:'null' CONST:'not null'
20: OR EXP:30 EXP:40
30: EQUAL EXP:50 CONST:NULL
40: EQUAL EXP:50 CONST:''
50: CAST ATTRIB:@CustomProperty1 CONST:System.String
```

**Explanation:**

- 10: if EXP:20 is true, return the text 'null', else - return 'not null'
- 20: if EXP:30 OR EXP:40 is true, return 'true', else - return 'false'
- 30: if EXP:50 is empty, return 'true', else - return 'false'
- 40: if EXP:50 is an empty string, return 'true', else - return 'false'
- 50: cast CustomProperty1 to string


### Property type is 'Picture'

If the property type of the particular custom property is 'Picture', use the following expressions:

```
10: IIF EXP:20 CONST:'null' CONST:'not null'
20: EQUAL EXP:30 CONST:0
30: SUM EXP:40 CONST:1
40: FILTER EXP:70 EXP:50
50: NOT EXP:60            
60: EQUAL ATTRIB:Picture CONST:NULL
70: SELECT REPO:General.PropertyValues EXP:80
80: WHERE EXP: 90 EXP:100
90: EQUAL ATTRIB:PropertyId CONST:86ba82c9-8843-e611-82a1-b010410e63e2
100: EQUAL ATTRIB:EntityItemId CONST:47e225e9-f4b6-e611-af28-00155d001f28
```

**Explanation:**

- 10: if EXP:20 is true, return the text 'null', else - return 'not null'
- 20: if EXP:30 is equal to 0, return 'true', else - return 'false'
- 30: count the records of the list returned by EXP:40
- 40: filter the list returned by EXP:70 by the condition of EXP:50
- 50: if EXP:60 is true, return 'false', else - return 'true'
- 60: if ATTRIB:Picture is equal to NULL, return 'true', else - return 'false'
- 70: select the records of table General.PropertyValues filtered by the clauses of EXP:80
- 80: if EXP:90 AND EXP:100 are true, return 'true', else - return 'false'
- 90: if ATTRIB:PropertyId is equal to 86ba82c9-8843-e611-82a1-b010410e63e2, return 'true', else - return 'false'
- 100: if ATTRIB: ATTRIB:EntityItemId is equal to 47e225e9-f4b6-e611-af28-00155d001f28, return 'true', else - return 'false'

> [!NOTE] 
> 
> **EntityItemId** is the ID of the actual entity (particular document, line, product) for which the value is specified.
