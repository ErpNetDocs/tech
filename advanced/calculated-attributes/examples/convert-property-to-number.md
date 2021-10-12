---
items: CalculatedAttributeExamples
---

# Convert a value of a custom property to a number

The values of the custom properties are a specific type of value and the [CONVERT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/convert.html) operator does not know how to handle it properly. For this reason, if we want to covert a custom property's value to a number, we have to [CAST](https://docs.erp.net/tech/advanced/calculated-attributes/operators/cast.html) it first. 


## Example - Multiply standard price per lot by a coefficient stored in a property


Lets say, for example, we want to multiply the standard price per lot of the product by a coefficient stored as a product's custom property @CustomProperty1. 

> [!NOTE]
> The repository of the attributes is *General.Products.Products*

**RIGHT calculated attribute:**

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT EXP:30 CONST:System.Decimal
30: CAST ATTRIB:@CustomProperty1 CONST:System.String
```

Explanation:

- 10: Multiply the value of the 'Standard Price Per Lot' by EXP: 20.
- 20: Convert EXP:30 to a decimal number.
- 25: Cast the value of custom property 'CustomProperty1' to a string.

**WRONG calculated attribute:**

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT ATTRIB:@CustomProperty1 CONST:System.Decimal
```

Explanation:

- 10: Multiply the value of the 'Standard Price Per Lot' by EXP: 20.
- 20: Convert the value of custom property 'CustomProperty1' to a decimal number.

> [!NOTE]
> When we want to convert CustomPropertyValue to numeric value (for example, decimal), we need to [CAST](https://docs.erp.net/tech/advanced/calculated-attributes/operators/cast.html) it to a string first!
