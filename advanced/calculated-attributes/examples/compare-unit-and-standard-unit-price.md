---
items: CalculatedAttributeExamples
---

# Compare unit price and standard unit price

The following calculated attribute calculates if the Unit Price in the Sales Order Lines is greater than the Standard Unit Price of the product and returns a message:

```
10: IIF EXP:20 CONST:'OK!' CONST:'Not OK!'
20: GT ATTRIB:UnitPriceValue ATTRIB:StandardUnitPriceValue
```

Explanation:

- 10: Checks if EXP:20 is true or false. If EXP:20 is True - the calculated attribute displays the 'OK!' message, else - 'Not OK!'.
- 20: Checks if ATTRIB:UnitPriceValue is greater than ATTRIB: StandardUnitPriceValue. If so - returns True, else - False.



The same validation may be achieved by using other operator:

```
10: IIF EXP:20 CONST:'Not OK!' CONST:'OK!'
20: LTE ATTRIB:UnitPriceValue ATTRIB:StandardUnitPriceValue
```

Explanation:

- 10: Checks if EXP:20 is true or false. If EXP:20 is True - the calculated attribute displays the 'Not OK!' message, else - 'OK!'.
- 20: Checks if ATTRIB:UnitPriceValue is less than or equal to ATTRIB:StandardUnitPriceValue. If so - returns True, else - False.
