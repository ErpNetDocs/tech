# Minimal sales price


There are two ways to set a minimal sales price of a product:
 
1.  In the product definition. It is a price for one standard lot and in the costing currency of the product. The minimum is enforced upon releasing a sales order. If not set, this means that there is no minimum sales price enforcement.
2.  In the product distribution channel definition. It is also a price for one standard lot and in costing currency of the product. It describes the minimum sales price of this product through the current channel.

If it is set in the product definition, the restriction takes place in every sales order.
 
If it is set in the product distribution channel, then it validates the sales order release, only if the distribution channel is selected in the document header. If there are two minimal sales prices for a product - one in its definition and one set by the product distribution channel, then the more restrictive price is taken into account.
 
> [!NOTE]: The minimal price constraint does not take effect when the user enters a sales return.
 
The restriction is not directly applied to the unit price in the sales order. As the unit price in the Sales Order lines does not reflect discounts, the restriction calculates the final unit price through the line amount and is applied to the calculated results.
 
#### Example 1 :
 
**Product A** has a minimal sales price of **9.00 EUR**. The product costing currency is EUR and standard lot size base is 1 PCS.
 
There is a sales order with the following line:
 
- Line No = **10**, Product = **Product A** , Unit Price = **9.20 EUR**, Line Custom Discount Percent = **5%**; Quantity Base = **3 PCS**; Line Amount = **26.22 EUR**.

When the user tries to release the Sales Order, he will receive an error message, that the unit price is less than the minimum unit price of the product. This is because the unit price with the calculated discount is as follows: [Line Amount] / [Quantity Base] = **26.22 EUR** / **3 PCS = 8.74 EUR**. In this case, because of the custom discount the user has entered, the unit price of the product goes under the minimum sales price of the product.
 
#### Example 2 :
 
Let’s use the product from ***Example 1***. The product is also part of the distribution channel **DC#1**. Product **A** also has a minimal sales price defined in the product distribution channel of **9.40 EUR**.
 
The user enters a sales order with the **DC#1** set in its header and the following line:
 
- Line No = **10**, Product = **Product A** , Unit Price = **9.20 EUR**, Quantity Base = **1 PCS**.

In this case, the sales order release will also return an error because of a minimum sales price violation. This is because the more restrictive minimal sales price is taken into account and it is **9.40 EUR**. In this case, if the product is sold through the **DC#1** distribution channel and it cannot be sold for less than **9.40 EUR** per unit.

