# Minimal Sales Price


There are two ways to set a Minimal Sales Price of a product:
 
1.  In the Product definition. It is a price for one standard lot and in the costing currency of the product. The minimum is enforced upon releasing a Sales Order. If not set, this means that there is no minimum sales price enforcement.
2.  In the Product Distribution Channel definition. It is also a price for one standard lot and in costing currency of the product. It describes the minimum sales price of this product through the current channel.

If it is set in the product definition, the restriction takes place in every Sales Order.
 
If it is set in the Product Distribution channel, then it validates the Sales Order release, only if the Distribution channel is selected in the document header. If there are two Minimal Sales Prices for a product - one in its definition and one set by the Product distribution channel, then the more restrictive price is taken into account.
 
>Note: The Minimal Price constraint does not take effect when the user enters a Sales Return.
 
The restriction is not directly applied to the Unit Price in the Sales Order. As the Unit Price in the Sales Order lines does not reflect discounts, the restriction calculates the final unit price through the line amount and is applied to the calculated results.
 
***Example 1***:
 
**Product A** has a Minimal Sales Price of **9.00 EUR**. The product Costing Currency is EUR and Standard Lot Size Base is 1 PCS.
 
There is a Sales Order with the following line:
 
- Line No = **10**, Product = **Product A** , Unit Price = **9.20 EUR**, Line Custom Discount Percent = **5%**; Quantity Base = **3 PCS**; Line Amount = **26.22 EUR**.

When the user tries to release the Sales Order, he will receive an error message, that the unit price is less than the minimum unit price of the product. This is because the unit price with the calculated discount is as follows: [Line Amount] / [Quantity Base] = **26.22 EUR** / **3 PCS = 8.74 EUR**. In this case, because of the custom discount the user has entered, the unit price of the product goes under the minimum sales price of the product.
 
***Example 2***:
 
Let’s use the product from ***Example 1***. The product is also part of the distribution channel **DC#1**. Product **A** also has a Minimal Sales Price defined in the product distribution channel of **9.40 EUR**.
 
The user enters a Sales Order with the **DC#1** set in its header and the following line:
 
- Line No = **10**, Product = **Product A** , Unit Price = **9.20 EUR**, Quantity Base = **1 PCS**.

In this case, the sales order release will also return an error because of a minimum sales price violation. This is because the more restrictive minimal sales price is taken into account and it is **9.40 EUR**. In this case, if the product is sold through the **DC#1** distribution channel and it cannot be sold for less than **9.40 EUR** per unit.

