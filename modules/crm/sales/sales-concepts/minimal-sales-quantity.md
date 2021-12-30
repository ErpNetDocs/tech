# Minimal sales quantity

There are two ways to set a minimal sales quantity of a product:
 
1. In the product definition. It is a minimal base quantity that has to be specified in any sale. The minimum is enforced upon releasing a sales order. If not set, this means that there is no minimum sales quantity enforcement.
2. In the product distribution channel definition. It is also a base quantity that has to be specified in any sale. It describes the minimal sales quantity of this product through the current channel.

If it is set in the product definition, the restriction takes place in every sales order.
 
If it is set in the product distribution channel, then it validates the sales order release, only if the distribution channel is selected in the document header. If there are two minimal sales quantities for a product - one in its definition and one set by the product distribution channel, then the more restrictive one is taken into account.
 
> [!NOTE] 
> The minimal quantity constraint does not take effect when the user enters a sales return.
 
The restriction is applied on the *Quantity Base* field in the *Sales Order* Lines. When such restriction exists it is applied to the calculated quantity in the base measurement unit. 
 
> [!NOTE]
> The restriction also calculates the total quantity base of the product in the *Sales Order* Lines, meaning that if the user enters the product in more than one line and the
> total quantity base covers the minimal sales quantity base, then the user would be able to release the sales order.
 
#### Example 1:
 
- **Product A** has a minimal sales quantity base of **3 PCS**. The product base measurement unit is **PCS**. It is declared that **1 KG** of **Product A** is equal to **2 PCS**. In the product definition a minimal sales quantity base of **3.00**.

There is a sales order with the following line:
 
- Line No = **10**, Product = **Product A**, Quantity = **1.40 KG**, Quantity Base = **2.80 PCS**.

When the user tries to release the sales order, he will receive an error message, that the quantity in the current document lines is less than the minimal sales quantity.
 
#### Example 2:
 
If in the sales order from ***Example 1*** the user adds 3 more lines as follows:
 
- Line No = **20**, Product = **Product B**, Quantity = **10 KG**, Quantity Base = **10 KG**.
- Line No = **30**, Product = **Product C**, Quantity = **3 PCS**, Quantity Base = **3 PCS**.
- Line No = **40**, Product = **Product A**, Quantity = **0.20 pcs**, Quantity Base = **0.20 PCS**.

In this case, the user will be able to release the sales order because Line No 10 and Line 40 has a total quantity base of **3.00 PCS**, which covers the minimal sales quantity base restriction, defined in the product definition.
 
#### Example 3:
 
Product **P** is part of distribution channel **DC#1**. Its base measurement unit is **PCS**. Product **P** has a minimal sales quantity base in its definition of **3.00 PCS**. Product **P** also has a minimal sales quantity base defined in the product distribution channel of 2.80 PCS.
 
The user enters a sales order with the **DC#1** set in its header and the following line:
 
- Line No = **10**, Product = **Product P**, Quantity = **2.90 PCS**, Quantity Base = **2.90 PCS**.

In this case, the sales order release will also return an error because of a minimal quantity violation. This is because the more restrictive minimal sales quantity (the one in the product definition) is taken into account.
