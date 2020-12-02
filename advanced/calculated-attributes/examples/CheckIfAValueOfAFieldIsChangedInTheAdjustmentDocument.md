---
items: CalculatedAttributeExamples
---

# Check If a value of a field Is changed in the Adjustment Document

With the current attribute, we can check if the value of a field in the adjustment document is equal to the value of the same filed in the original (adjusted) document. When we have such information, we can determine if the value of this filed is being or has been changed in the adjustment document. Using this attribute, we can for example, create a Business rule which would allow us to prohibit the correction of the value of this field.



```
10: IIF EXP:20 CONST:False EXP:30
20: EQUAL REF:AdjustedDocument CONST:NULL                                  
30: IIF EXP:40 CONST:False CONST:True      
40: EQUAL ATTRIB:@Property1 EXP:50                              
50: GETOBJVALUE REF:AdjustedDocument ATTRIB:@Property1                     
```



Explanation:

- 10: Check if EXP:20 is true or false. If EXP:20 is True - the calculated attribute displays 'True', else - 'False'.
- 20: Check if there is AdjustedDocument. If there is no reference to an  Adjusted document, then the document is not an Adjustment document.
- 30: Check if EXP:40 is true or false.
- 40: Check if the value of the custom property 'Property1' is equal to EXP:50.
- 50: Get the value of the 'Property1' of the adjusted document.
