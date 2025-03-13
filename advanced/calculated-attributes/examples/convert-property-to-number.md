---
items: CalculatedAttributeExamples
---

# Convert a value of a custom property to a number

The values of custom properties are a specific type of value that the **[CONVERT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/convert.html)** operator doesn't know how to handle. 

For this reason, if you want to CONVERT a custom property's value to a number, you have to **[CAST](https://docs.erp.net/tech/advanced/calculated-attributes/operators/cast.html)** it first. 


**Example:**

Let's say you want to multiply the standard price per lot of a product by a coefficient stored as a product's custom property @CustomProperty1. 

> [!NOTE]
> 
> The repository of the attributes is *General.Products.Products*

### CORRECT calculated attribute:

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT EXP:30 CONST:System.Decimal
30: CAST ATTRIB:@CustomProperty1 CONST:System.String
```

**Explanation:**

- 10: Multiply the value of the _Standard Price Per Lot_ by EXP: 20.
- 20: Convert EXP:30 to a decimal number.
- 25: Cast the value of custom property **CustomProperty1** to a string.

### FALSE calculated attribute:

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT ATTRIB:@CustomProperty1 CONST:System.Decimal
```

**Explanation:**

- 10: Multiply the value of the _Standard Price Per Lot_ by EXP: 20.
- 20: Convert the value of custom property **CustomProperty1** to a decimal number.

> [!NOTE]
> 
> Before converting a **CustomPropertyValue** to a numeric value, you need to **CAST** it to a string first!
