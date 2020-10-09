---
items: CalculatedAttributeExamples
---

# Total Quantity And Scrap Quantity In Recipe Ingredients

If the user wants to see what is the total Quantity of the  material in a Recipe which would include the Used Quantity and the Scrap Rate, he would add the following Calculated Attribute:



```
Repository Name: Production.Technologies.RecipeIngredients
Name: TotalUsedQuantity
```

And the Calculated Attribute expressions are as follows:

```
10: ADD ATTRIB:UsageQuantityValue EXP:20
20: MULTIPLY ATTRIB:UsageQuantityValue ATTRIB:ScrapRate
```



Explanation:

- 10: Add the result from expression 20 to the attribute UsageQuantityValue
- 20: Multiply UsageQuantityValue and ScrapRate

