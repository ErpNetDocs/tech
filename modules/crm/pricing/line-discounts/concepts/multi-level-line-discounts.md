---
uid: multi-level-line-discounts
---

# Multi-level line discounts

This topic explains how line discounts from different discount levels work together in a sales order line.

For each discount level, @@name first determines at most one applicable line discount by using the [Determine line discount](determine-line-discount.md) algorithm.

After the line discounts for the individual levels are selected, their discount percentages can be accumulated in cascade in the **Line Standard Discount Percent** field.

Line discounts can be defined for three discount levels:

- **Level 1 Discount**
- **Level 2 Discount**
- **Level 3 Discount**

Each level can contain at most one selected line discount in a sales order line.

This means that multiple line discounts can affect the same sales document line, but only one line discount can be selected for each discount level.

## How multi-level line discounts are applied

Line discounts from different levels can be applied to sales document lines in the following ways:

- automatically – by determining the applicable line discount for the level;
- manually – by selecting a line discount in the document line;
- through user business rules.

Automatic application depends on the discount level and the current sales context.

Level 1 discounts can be determined without additional requirements.  
Level 2 and level 3 discounts are applied automatically only when a **Price List** is set in the sales order.

The maximum level that is applied automatically is controlled by the **Auto Apply Discount Level** field in the price list definition.

For example:

- if **Auto Apply Discount Level = 1**, @@name applies discounts up to level 1;
- if **Auto Apply Discount Level = 2**, @@name applies discounts up to level 2;
- if **Auto Apply Discount Level = 3**, @@name applies discounts up to level 3.

> [!NOTE]
> Increasing the auto apply discount level may have performance implications.

## How the final line discount percent is calculated

After the selected line discounts are applied to the sales document line, @@name calculates the final **Line Standard Discount Percent** by accumulating the discount percentages from all selected levels in cascade.

The calculation formula is:

```text
[Line Standard Discount Percent] =
1 - ((1 - [Level 1 Discount Percent]) *
     (1 - [Level 2 Discount Percent]) *
     (1 - [Level 3 Discount Percent]))
```
If a level discount percent is empty, it is treated as 0.

This means that the final line standard discount percent is not calculated by simple addition.  
Instead, each discount level is applied successively to the remaining amount after the previous level.

### Example 1

If there are no discounts in the line, then the line standard discount percent is:

```text
[Line Standard Discount Percent] =
1 - ((1 - 0) * (1 - 0) * (1 - 0)) = 0.00%
```

### Example 2

If the line contains the following discount percentages:

- **Level 1 Discount Percent** = 12%
- **Level 2 Discount Percent** = 5%
- **Level 3 Discount Percent** = 8%

then the line standard discount percent is:

```text
[Line Standard Discount Percent] =
1 - ((1 - 0.12) * (1 - 0.05) * (1 - 0.08)) = 23.088%
```

## Example business model

A company can use the discount levels for different purposes.

For example:

### Level 1 - according to the customer type and product group

- Customer Type Wholesale, Product Group Foods - 10%
- Customer Type Wholesale, Product Group Non-food items - 5%
- Customer Type Retail, Product Group Foods - 8%
- Customer Type Retail, Product Group Non-food items - 4%

### Level 2 - according to the target group or distribution channel

- Target Group VIP Customers, Product Group Foods - 6%
- Distribution Channel Online Store, Product Group Non-food items - 4%

### Level 3 - according to additional conditions

At this level, predefined line discounts can be assigned through user business rules.

The discount percent is defined in the line discount record itself, while the additional applicability conditions are defined in the user business rule.

For instance:

- a user business rule can assign a predefined level 3 line discount with 5% when a lot has less than 20 days remaining until expiration date;
- a user business rule can assign a predefined level 3 line discount with 2% when a sales order line amount is greater than 1000 BGN.

In this business model, level 1 and level 2 discounts are determined from line discount records that match the sales document context.

Level 3 discounts are assigned through user business rules based on conditions that are outside the standard line discount applicability fields.

A sales document can then apply discounts from the selected levels according to the price list configuration and any additional business rules.

If the price list selected in the sales order is configured with **Auto Apply Discount Level = 2**, @@name can apply level 1 and level 2 discounts automatically.

Level 3 discounts can also be assigned through user business rules when the relevant conditions are met.

## See also

- [Create a basic line discount](../create-basic-line-discount.md)
- [Configuring line discounts](../configuration.md)
- [Determine line discount](determine-line-discount.md)
