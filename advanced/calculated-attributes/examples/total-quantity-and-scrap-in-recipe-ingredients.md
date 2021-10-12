---
items: CalculatedAttributeExamples
---

# Total quantity and scrap quantity in recipe ingredients

If the user wants to see the total quantity of the material in a recipe, which would include the used quantity and the scrap rate, he would add the following calculated attribute:

```
Repository Name:Production.Technologies.RecipeIngredients
Name:TotalUsedQuantity
```

And the calculated attribute expressions are as follows:

```
10: ADD ATTRIB:UsageQuantityValue EXP:20
20: MULTIPLY ATTRIB:UsageQuantityValue ATTRIB:ScrapRate
```

Explanation:

- 10: Add the result from expression 20 to the attribute UsageQuantityValue
- 20: Multiply UsageQuantityValue and ScrapRate

