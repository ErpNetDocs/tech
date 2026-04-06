# How to use function "Add related"

The function allows you to add a related product in a document line based on predefined product relations of type **Merchandising** between the base product and the added product.

This enables quick addition of complementary or promotional products (e.g., accessories, gifts, add-ons) without manually searching for them. Generally this feature aims at increasing the total amount of the sale or offer.

Unlike product Replacement, this function does not modify the original product. Instead, it adds a new document line with the selected related product.

A related product is available only if there is an active product relation, where:

- **From Product** is the product in the current document line
- **To Product** is the related product
- **Product Relation Type** engaging the products is of System Type = **Merchandising**

A product can be referred to as a Merchandise (related) if there is a valid relation in terms of the dates of the relation itself:
- **From Date** is empty or earlier than or equal to today
- **To Date** is empty or later than or equal to today

If the relation has a defined **QtyFactor**, it is used to calculate the quantity of the added product.

As a **result** of the addition:

- A new document line is added below the current line;
- The selected related product is inserted in the new line, its quantity calculated by the Qty factor;
- The original product and line details remain unchanged
  
