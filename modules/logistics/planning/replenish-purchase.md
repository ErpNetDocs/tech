# Replenishing suggestions for purchase orders

If a store is running low on product quantities, you can take advantage of **automatic replenishing suggestions** to restore the supply to its desired number.

By following the steps below, while issuing **purchase orders**, you'll be able to generate lines specifically for replenishing product quantities.

## Prerequisites

For the feature to work as expected, you need to have done two things in advance:

1.	Define a **product supply** suited for purchase orders.

Go to **General** **->** **Products** and select **Product Supply**. From there, add a new supply with the **plus** button.

![Picture](pictures/product_supply.png)
 
Make sure to go through each field carefully. 

![Picture](pictures/purchase_ord.png)
 
• **Product** - The product for which a supply (and purchase order) will be made.
•	**Procurement Type** - The type of action associated with this product (in this case, bought products imply **Buy**).
•	**Generate Document Type** - The type of document which will be issued according to the supply rules (leave this as **Purchase Order**).
- **Order Point Quantity Base** - Quantity the product must drop to for replenishment to be triggered.
- **Planning Maximum Inventory Quantity Base** - Maximum possible quantity of product in the store.
- **Planning Lead Time Days** - Days needed to supply or manufacture the product.
- **Order Minimum** - Minimum quantity of product that can be ordered at a time.
- **Order Maximum** - Maximum quantity of product that can be ordered at a time.
- **Order Multiple** - Tick this box to make the purchased product quantity multiple by lot size.
- **Order Lot Size Quantity Base** - The lot size value.
- **Order Policy** - The policy the replenishment system will follow (leave this as **OPS - Order Point System**). 
- **Manufacturing Policy** - Used when the procurement type is **Make**.
- **From Store** - Used when the procurement type is **Transfer**. 
- **Preferred Supplier** - Name of the supplier who must have produced the product (will be identical in the purchase order).
- **Enterprise Company** - Name of the enterprise company associated with the product supply (identical in the purchase order).

When done, **save** the product supply.
 
2.	Create a new purchase order from the **Logistics** **->** **Procurement** module. 

![Picture](pictures/logistics_procurement.png)

The status of the document should be **below** Released - most often **New**.

Make sure the product, supplier and store and are identical to the ones you defined for the product supply. 

![Picture](pictures/save_purchase.png)
 
## Use Suggest replenish

You can apply the **Suggest replenish** feature from within your existing purchase order document. 

Click the play button and select **Suggest replenish**.

![Picture](pictures/sug_rep.png)

If the order has lines, they will be **removed** and new ones will be automatically generated for suggested product quantity replenishing.

![Picture](pictures/lines.png)

