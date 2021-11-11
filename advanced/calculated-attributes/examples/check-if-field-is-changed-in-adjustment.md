---
items: CalculatedAttributeExamples
---

# Check if a value of a field is changed in the adjustment document

This attribute checks if the value of a field in the adjustment document is equal to the value of the same field in the original document.

This information helps us determine if the value of the field is being or has been changed in the adjustment document. 

Using this attribute, we can create a business rule which would allow us to **prohibit** the correction of the value of the field.

```
10: IIF EXP:20 CONST:False EXP:30
20: EQUAL REF:AdjustedDocument CONST:NULL                                  
30: IIF EXP:40 CONST:False CONST:True      
40: EQUAL ATTRIB:@Property1 EXP:50                              
50: GETOBJVALUE REF:AdjustedDocument ATTRIB:@Property1                     
```

**Explanation:**

- 10: Check if EXP:20 is true or false. If EXP:20 is true - the calculated attribute displays 'True', else - 'False'.
- 20: Check if there is **AdjustedDocument**. If there is no such reference, then the document is not an adjustment document.
- 30: Check if EXP:40 is true or false.
- 40: Check if the value of the custom property 'Property1' is equal to EXP:50.
- 50: Get the value of the 'Property1' of the adjusted document.
