# Minimal Sales Quantity

There are two ways to set a Minimal Sales Quantity of a product:
 
1. In the Product definition. It is a minimal base quantity that has to be specified in any sale. The minimum is enforced upon releasing a Sales Order. If not set, this means that there is no minimum sales quantity enforcement.
2. In the Product Distribution Channel definition. It is also a base quantity that has to be specified in any sale. It describes the minimal sales quantity of this product through the current channel.

If it is set in the product definition, the restriction takes place in every Sales Order.
 
If it is set in the Product Distribution channel, then it validates the Sales Order release, only if the Distribution channel is selected in the document header. If there are two Minimal Sales Quantities for a product - one in its definition and one set by the Product distribution channel, then the more restrictive one is taken into account.
 
>Note: The Minimal Quantity constraint does not take effect when the user enters a Sales Return.
 
The restriction is applied on the Quantity Base field in the Sales Order Lines. When such restriction exists it is applied to the calculated quantity in the base measurement unit. 
 
>The restriction also calculates the total Quantity Base of the product in the Sales Order Lines, meaning that if the user enters the product in more than one line and the total quantity base covers the Minimal Sales Quantity Base, then the user would be able to release the Sales Order.
 
***Example 1***:
 
- **Product A** has a Minimal Sales Quantity Base of **3 PCS**. The product base measurement unit is **PCS**. It is declared that **1 KG** of **Product A** is equal to **2 PCS**. In the product definition a Minimal Sales Quantity Base of **3.00**.

There is a Sales Order with the following line:
 
- Line No = **10**, Product = **Product A**, Quantity = **1.40 KG**, Quantity Base = **2.80 PCS**.

When the user tries to release the Sales Order, he will receive an error message, that the quantity in the current document lines is less than the minimal sales quantity.
 
***Example 2***:
 
If in the Sales Order from ***Example 1*** the user adds 3 more lines as follows:
 
- Line No = **20**, Product = **Product B**, Quantity = **10 KG**, Quantity Base = **10 KG**.
- Line No = **30**, Product = **Product C**, Quantity = **3 PCS**, Quantity Base = **3 PCS**.
- Line No = **40**, Product = **Product A**, Quantity = **0.20 pcs**, Quantity Base = **0.20 PCS**.

In this case, the user will be able to release the Sales Order because Line No 10 and Line 40 has a total Quantity Base of **3.00 PCS**, which covers the Minimal Sales Quantity Base restriction, defined in the product definition.
 
***Example 3***:
 
Product **P** is part of distribution channel **DC#1**. Its base measurement unit is **PCS**. Product **P** has a Minimal Sales Quantity Base in its definition of **3.00 PCS**. Product **P** also has a Minimal Sales Quantity Base defined in the product distribution channel of 2.80 PCS.
 
The user enters a Sales Order with the **DC#1** set in its header and the following line:
 
- Line No = **10**, Product = **Product P**, Quantity = **2.90 PCS**, Quantity Base = **2.90 PCS**.

In this case, the sales order release will also return an error because of a minimal quantity violation. This is because the more restrictive minimal sales quantity (the one in the product definition) is taken into account.


