# Price Types

Price types are defined in **Pricing** → **Price Types** in the **Set Up** section.

A price type is used to add an additional priority layer on top of the standard Priority field of product prices.
When multiple product prices are applicable in the same sales context, product prices with a defined price type take precedence over product prices without a price type.

The main settings of a price type define:
- its code and name;
- its position relative to other price types;
- whether it is active.

The **Ordinal Position** field defines the priority of the price type relative to the other price types.  
A lower value means a higher priority.

When more than one applicable product price has a defined price type, the price whose type has the lowest **Ordinal Position** is preferred. If the applicable price types have the same **Ordinal Position**, the standard **Priority** of the product price is used.

**For example**:   
*A company can define price types such as **Regular**, **Promotional**, and **Special**, and assign them different Ordinal Positions to reflect which prices should take precedence in a given commercial context.*

For an overview of product price applicability conditions, including price types, see [Configuring product prices](../index.md).

For more information about how @@name selects the final price when multiple product prices are applicable, see [Determine product price](../concepts/determine-product-price.md).

![Price Type](pictures/price-type.png)
