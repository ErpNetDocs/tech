# Multiple line discounts

## Description

@@name allows multiple discounts at multiple levels to be defined. The discount level is specified in the discount’s definition.

The discounts from each level can be applied to the sales order lines automatically, manually, or by using user business rules. For each level you can select only one discount out of all discounts of the given level.

The discount percentages from all levels are accumulated in cascade in the Line Standard Discount Percent field in the sales order lines.

## Applying multiple line discounts in sales orders

Discounts from different levels are applied to the relevant fields of the sales order lines in three alternative ways:

- automatically – by calling the Determine line discount method
- manually – by selecting a discount from the drop-down list or from a navigator
- using user business rules.

Note that, discounts from level 2 and above are applied automatically ONLY if a price list is set in the sales order. 

The level up to which discounts are applied automatically depends on the selected value in the Auto Apply Discount Level field in the price list’s definition.

For example:
- if Auto Apply Discount Level = 1, then level 1 discount is applied
- if Auto Apply Discount Level = 2, then level 1 and level 2 discounts are applied
- if Auto Apply Discount Level = 3, then level 1, level 2 and level 3 discounts are applied.

> [!note]
> 
> Increasing the auto apply discount level may have performance implications.
> 

## Determine line standard discount percent

The line standard discount percent is calculated by accumulating in cascade all level discount percentages that were specified in the line. The formula is as follows:

**[Line Standard Discount Percent]** = 
1 – ((1 - IIF(**[Level 1 Discount Percent]** == NULL, 0.00, **[Level 1 Discount Percent]**) 
* (1 - IIF(**[Level 2 Discount Percent]** == NULL, 0.00, **[Level 2 Discount Percent]**) 
* (1 - IIF(**[Level 3 Discount Percent]** == NULL, 0.00, **[Level 3 Discount Percent]**))

#### Example 1 :

If there are no discounts in the line, then line standard discount percent is:

**[Line Standard Discount Percent]** = 1 - ((1 - 0) * (1 - 0) * (1 - 0)) = **0.00%**.

#### Example 2 :

If the line contains the following discounts - level 1 discount percent = 12%, level 2 discount percent = 5% and level 3 discount percent = 8%, then the line standard discount percent is:

**[Line Standard Discount Percent]** = 1 - ((1 – 0.12) * (1 – 0.05) * (1 – 0.08)) = **23.088%**.

## Multiple line discounts in reality

For example, you can define three levels of discounts, and for each of them you can have multiple discounts:

**Level 1** – according to the customer type
- Wholesale customers, product group Foods - 10%
- Wholesale customers, product group Non-food items - 5%
- Retail customers, product group Foods - 8%
- Retail customers, product group Non-food items - 4%

**Level 2** – according to the current promotion
- All customers, product group Foods / Chocolate - 15%
- All customers in Sofia, product group Non-food items - 4%
 
**Level 3** - according to specific conditions
- If the lot has less than 20 days of expiration date remaining - 5%
- If the line amount is greater then 1000 BGN - 2%

Then, you can choose Level 1 and Level 2 discounts to be applied automatically by setting up a price list in the sales order with auto apply discount level equal to 2.
Level 3 discount can be applied automatically as well by defining a user business rule that should be triggered if some specific conditions are met.

