---
items: CalculatedAttributeExamples
---

# Compare unit price and standard unit price

This attribute calculates if the unit price in the sales order lines is greater than the standard unit price of the product.

It returns the following message:

```
10: IIF EXP:20 CONST:'OK!' CONST:'Not OK!'
20: GT ATTRIB:UnitPriceValue ATTRIB:StandardUnitPriceValue
```

**Explanation:**

- 10: Checks if EXP:20 is true or false. If EXP:20 is true - the calculated attribute displays 'OK!' message, else - 'Not OK!'.
- 20: Checks if ATTRIB:UnitPriceValue is greater than ATTRIB: StandardUnitPriceValue. If so - returns 'True', else - 'False'.


The same validation may be achieved using another operator:

```
10: IIF EXP:20 CONST:'Not OK!' CONST:'OK!'
20: LTE ATTRIB:UnitPriceValue ATTRIB:StandardUnitPriceValue
```

**Explanation:**

- 10: Checks if EXP:20 is true or false. If EXP:20 is true - the calculated attribute displays 'Not OK!' message, else - 'OK!'.
- 20: Checks if ATTRIB:UnitPriceValue is less than or equal to ATTRIB:StandardUnitPriceValue. If so - returns 'True', else - 'False'.
