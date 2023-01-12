---
items: CalculatedAttributeExamples
---

# Calculate standard price per lot based on ingredients and operations in a recipe

With this attribute, you can calculate the **StandardPricePerLot** set in a product’s definition as you save a recipe. **StandardPricePerLot** is determined by the prices of ingredients and operations used in the recipe. 

You can also use this attribute in a business rule to fill in the **PricePerLotValue** of the product in the recipe.


```
10: ADD EXP:20 EXP:25                 
20: SUM CHILD:Ingredients ATTRIB:PriceValue     
25: SUM CHILD:Operations EXP:30         
30: MULTIPLY EXP:40 EXP:45        
40: DIVIDE ATTRIB:StandardPricePerHourValue CONST:60.00   
45: CAST EXP:50 CONST:System.Decimal
50: ADD ATTRIB:RunTimeMinutes EXP:60 
60: ADD ATTRIB:WaitTimeMinutes EXP:70        
70: ADD ATTRIB:SetupTimeMinutes ATTRIB:MoveTimeMinutes
```

**Explanation:**

- 10: Add the value of EXP:20 to the value of EXP:25.
- 20: Sum all recipe's ingredients **PriceValues**.
- 25: Sum EXP:30 for all of the recipe's operations.
- 30: Multiply the value of EXP:40 and EXP:45.
- 40: Divide the **StandardPricePerHourValue** by 60.00 to get the **StandardPrice** per minute.
- 45: Cast EXP:50 to decimal.
- 50: Add the **RunTimeMinutes** values to EXP:60 => EXP:70 to get full execution time of the operation.

