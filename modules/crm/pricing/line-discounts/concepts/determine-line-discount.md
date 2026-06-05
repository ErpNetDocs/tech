---
uid: determine-line-discount
---

# Determine line discount

This topic explains how @@name determines a single applicable line discount for one requested discount level.

Line discounts allow multiple discounts to be defined under different conditions.

Typical examples include:
- a general line discount valid for all customers;
- a line discount valid only for a specific customer;
- a line discount valid only for a specific product;
- a line discount valid only for a specific quantity range of a product;
- a line discount valid only for a specific price list;
- a promotional line discount valid for a limited period.

In addition to these applicability conditions, line discounts can also be defined for different discount levels.

For example, a company can use level 1 for customer-specific discounts, level 2 for promotions, and level 3 for additional special discounts.

@@name determines line discounts separately for each discount level.

For information about how discounts from multiple levels are accumulated in sales order lines, see [Multi-level line discounts](multi-level-line-discounts.md).

To determine the applicable line discount in a specific business context, @@name evaluates the available line discounts against the context data and then selects the best match for the requested discount level.

The determination has two stages:
1. @@name filters the available line discounts by applicability.
2. If more than one line discount remains for the requested discount level, @@name selects the best match according to the selection criteria.

## Context data used to determine the line discount

@@name determines the applicable line discount based on data from the current sales context, typically provided by the current sales document and its lines.

In this topic, **sales documents** refers to:
- **Offers**
- **Sales Orders**
- **Invoices**

Some context data is required so that line discount determination is possible.  
Other context data is used when available to narrow the selection.

### Minimum required data

The following data must be available:

- **Product**
- **Quantity**
- **Date**
- **Customer** or **Ship To Customer**

The context **Date** is taken from the sales document as follows:

- in **Offers** and **Sales Orders**, from **Required Delivery Date**;
- in **Invoices**, from **Delivery Date**. If **Delivery Date** is empty, from **Document Date**.

### Additional context data

The following data is used when available to narrow the selection:

- **Discount Level**
- **Enterprise Company**
- **Enterprise Company Location**
- **Distribution Channel**
- **Price List**

The requested **Discount Level** determines which level is evaluated by the algorithm. Automatic application of higher discount levels depends on the selected price list. 
For information about how discounts from multiple levels are combined in sales order line, see [Multi-level line discounts](multi-level-line-discounts.md).

> [!NOTE]
> If the requested **Discount Level** is not specified, @@name determines the line discount for level 1.

In addition, the algorithm can consider the **current Line Discount** when preserving an already selected applicable line discount.

## Filtering conditions

@@name filters the available line discounts by comparing the conditions defined in each line discount with the corresponding context data.

A line discount remains in the candidate set only if all of the following conditions are met:

- **Active** is true.
- **Discount Level** is equal to the requested discount level.
- **From Date** is empty or is earlier than or equal to the context **Date**.
- **Thru Date** is empty or is later than or equal to the context **Date**.
- **Product** is empty or is equal to the context **Product**.
- **Min Quantity** is empty or is less than or equal to the context **Quantity**.
- **Max Quantity** is empty or is greater than or equal to the context **Quantity**.
- **Customer** is empty or is equal to the context **Customer** or **Ship To Customer**.
- **Customer Type** is empty or is equal to the customer types of the context **Customer** or **Ship To Customer**.
- **Product Group** is empty, is equal to the product group of the context **Product**, or is a parent of that product group.
- **Distribution Channel** is empty or is equal to the context **Distribution Channel**.
- **Price List** is empty or is equal to the context **Price List**, and the price list is valid on the context **Date**.
- **Target Group** is empty or at least one customer from the context **Customer** or **Ship To Customer** belongs to the target group.

If any specified condition does not match, the line discount is excluded from the candidate set.

## Selection logic

After filtering, @@name may find one, many, or no applicable line discounts for the requested discount level.

- If no line discount remains in the candidate set, no line discount is determined.
- If exactly one line discount remains, that line discount is selected.
- If more than one line discount remains, @@name selects one of them according to the following criteria, in this order:
  1. **Highest Priority**
  2. **Latest From Date**

This ensures deterministic selection when multiple line discounts are applicable for the same discount level.

> [!NOTE]
> Automatic line discount determination applies only when the **Apply Trade Conditions** field is enabled on the sales document and on the relevant document lines.

### Current line discount preservation

When more than one applicable line discount remains, @@name can also consider the **current Line Discount**.

If the current line discount is still applicable and is equally ranked with the newly selected line discount, @@name can preserve the current line discount instead of replacing it.

This helps avoid unnecessary changes when the current line discount is still equally valid.

## Result

The algorithm returns at most one applicable line discount for the requested discount level.

If no line discount satisfies the filtering conditions, no line discount is returned.

If discounts from multiple levels are present in the sales document line, this algorithm is executed separately for each level. For more information, see [Multi-level line discounts](multi-level-line-discounts.md).

## Troubleshooting line discount determination

When the selected line discount is not the expected one, check the following:

1. Whether the expected line discount satisfies all filtering conditions.
2. Whether the correct **Discount Level** is being determined.
3. Whether another applicable line discount outranks it by:
   1. **Priority**
   2. **From Date**
4. Whether the **Current Line Discount** was preserved because it is still applicable and equally ranked.
5. Whether the **Apply Trade Conditions** field is enabled on the sales document and on the relevant document lines.

Keep in mind that:
- empty condition values mean "applies to all";
- filtering is performed before ranking;
- multiple applicable line discounts can exist for the same discount level, but only one is selected;
- **Product Group** matching also considers parent product groups.

## See also

- [Create basic line discount](../create-basic-line-discount.md)
- [Configuring line discounts](../configuration.md)
- [Multi-level line discounts](multi-level-line-discounts.md)
