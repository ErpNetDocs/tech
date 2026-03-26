---
items: CalculatedAttributeExamples
---

# Get the total amount of the selected offer lines


This attribute determines the total amount of the lines in the current offer that are marked as selected. It sums the value of the LineAmountValue field only for the lines where IsSelected is set to True.  

The amount is recalculated upon saving the offer.  

You can also use this attribute when you need to determine the total amount of the selected lines in the offer or other entities.




```
Repository: Crm.Presales.Offers
```

```
10: SUM EXP:20 ATTRIB:LineAmountValue
20: FILTER CHILD:Lines EXP:30
30: EQUAL ATTRIB:IsSelected CONST:True
```

**Explanation:**  
10: Sum the values of LineAmountValue from the records returned by EXP:20.
20: Filter the child records from Lines by the condition in EXP:30.
30: Check whether IsSelected is equal to True.
