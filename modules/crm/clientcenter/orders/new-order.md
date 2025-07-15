# New Order

Order creation through the Client Center is disabled by default. You need to enable the respective global JSON settings first.

Once that's done, users with **[external role](/modules/crm/sales/customers/external-access.md)** **L20 - Orders** and above will get access to the **New Order** screen.

This is a multi-tab panel dedicated to the filling out and placement of new sales orders.

![pictures](pictures/new_order_panel.png)

## Step-by-step process

1. Add products to the order. There are two ways to do this:
   
    1.1.   From the **Order** tab, click the **Add** button. This will reveal the **Code** and **Qty** fields, where you can respectively provide the code of the product and how many instances of it you need ordered.
   
   When you click **Save**, the product will be added with all the respective information about it, such as Unit, Price, and Discount.

   1.2.   From the My **Products** tab, click on the **Quantity** field of a **customer product** row and specify the exact quantity you need ordered.

   This will **automatically** add it in the **Order** tab.

   1.3.   Depending on how your Client Center instance is **configured** to work with distribution channels, users may be able to add products linked to their customer's **distribution channel**.

   These products will be available in a separate tab that carries the channel's name, e.g. "Online store". The process to add them is identical to the **My Products** tab.

   1.4.  If the sales order has a default distribution channel, an additional tab will also be available carrying that channel's name.

   Products linked to the channel will be available for selection.

2. When you're done specifying the quantities of the desired products, you can always **edit** or **delete** some of them if needed.

3. To conclude the order, click **Place Order**.

> [!NOTE]
> Users can start the creation of an order and switch to a different page or choose to place it later. <br>
> The order completion progress is kept for the current active user session, automatically saving and registering that order with status "New".
   
