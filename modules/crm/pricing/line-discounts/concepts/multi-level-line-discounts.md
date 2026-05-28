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

