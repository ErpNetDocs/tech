---
uid: determine-product-price
---

# Determine product price

Product prices allow different prices for the same product to be defined under different conditions.

Typical examples include:
- a general product price valid for all customers;
- a product price valid only for a specific customer;
- a promotional product price valid for a limited period;
- a product price valid only for a specific price list;
- a product price valid only for a specific quantity range.

To determine the applicable product price in a specific business context, @@name evaluates the available product prices against the context data and then selects the best match.

The determination has two stages:
1. @@name filters the available product prices by applicability.
2. If more than one product price remains, @@name selects the best match according to the selection criteria.

## Context data used to determine the product price

@@name determines the applicable product price based on data from the current sales context, typically provided by the current sales document and its lines.

In this topic, **sales documents** refers to:
- **Offers**
- **Sales Orders**

Some context data is required so that product price determination is possible.  
Other context data is used when available to narrow the selection.

### Minimum required data

The following data must be available:

- **Product**
- **Quantity**
- **Quantity unit**
- **Required Delivery Date**

### Additional context data

The following data is used when available to narrow the selection:

- **Customer**
- **Ship To Customer**
- **Enterprise Company**
- **Enterprise Company Location**
- **Distribution Channel**
- **Price List**

In addition, the algorithm can consider the **current Product Price** when preserving an already selected applicable product price.

## Filtering conditions

@@name filters the available product prices by comparing the conditions defined in each product price with the corresponding context data.

A product price remains in the candidate set only if all of the following conditions are met:

- **Is Active** is true.
- **From Date** is empty or is earlier than or equal to the context **Date**.
- **Thru Date** is empty or is later than or equal to the context **Date**.
- **Product** is equal to the context **Product**.
- **Customer** is empty or is equal to the context **Customer**.
- **Ship To Customer** is empty or is equal to the context **Ship To Customer**.
- **Min Quantity** is empty or is less than or equal to the context **Quantity**.
- **Max Quantity** is empty or is greater than or equal to the context **Quantity**.
- **Enterprise Company** is empty or is equal to the context **Enterprise Company**.
- **Enterprise Company Location** is empty or is equal to the context **Enterprise Company Location**.
- **Distribution Channel** is empty or is equal to the context **Distribution Channel**.
- **Price List** is empty or is equal to the context **Price List**, and the price list is valid on the context **Date**.
- **Target Group** is empty or the context **Customer** or **Ship To Customer** belongs to the target group.

If any specified condition does not match, the product price is excluded from the candidate set.

## Selection logic

After filtering, @@name may find one, many, or no applicable product prices.

- If no product price remains in the candidate set, no product price is determined.
- If exactly one product price remains, that product price is selected.
- If more than one product price remains, @@name selects one of them according to the following criteria, in this order:
  1. **Lowest Price Type ordinal position**
  2. **Highest Priority**
  3. **Latest From Date**

This ensures deterministic selection when multiple product prices are applicable at the same time.

### Current product price preservation

When more than one applicable product price remains, @@name can also consider the **current Product Price**.

If the current product price is still applicable and has the same selection priority as the newly selected product price, @@name can preserve the current product price instead of replacing it.

This helps avoid unnecessary changes when the current product price is still equally valid.

## Result

The algorithm returns one applicable product price.

If no product price satisfies the filtering conditions, no product price is returned.

## Troubleshooting product price determination

When the selected product price is not the expected one, check the following:

1. Whether the expected product price satisfies all filtering conditions.
2. Whether another applicable product price outranks it by:
   1. **Price Type** ordinal position;
   2. **Priority**;
   3. **From Date**.
3. Whether the **Current Product Price** was preserved because it is still applicable and equally ranked.

Keep in mind that:
- empty condition values mean "applies to all";
- filtering is performed before ranking;
- multiple applicable product prices can exist at the same time, but only one is selected.

## See also

- [Create basic product price](../create-basic-product-price.md)
- [Price Lists](../configuration/price-lists.md)
- [Price Types](../configuration/price-types.md)

  
