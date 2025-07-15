# New Order

Order creation through the Client Center is disabled by default. You need to enable the respective global JSON settings first.

Once that's done, users with **[external role](/modules/crm/sales/customers/external-access.md)** **L20 - Orders** and above will get access to the **New Order** page.

This is a multi-tab interface designed to handle the filling out and placement of new sales orders.

![pictures](pictures/new_order_panel.png)

### Structure

New Order consists of two primary tabs, but it can be configured to include two more:

1. **Order** - This is where the order is built. You can add products manually by entering their codes and specifying their quantities.
   
2. **My Products** - All customer products will appear here. You can add them to the order simply by specifying their quantities. They will appear in the **Order** tab.
   
3. **Customer's default distribution channel** - If the JSON setting for hiding this channel is disabled and the channel has products linked to it, you will be able to see one extra tab carrying that channel's name. Inside, you will see the respective products.

4. **Client Center's default distribution channel** - If the JSON setting for showing this channel is configured and the channel has products linked to it, you will be able to see one extra tab carrying that channel's name. Inside, you will see the respective products.

   In the event where the JSON configuration is not set, the system will automatically link the created sales order to a distribution channel with **code "CC"** and **name "Client Center"**. If such channel does not exist, it will be created.

## Step-by-step process

1. Add products to the order. There are several ways to do this:
   
    1.1.   From the **Order** tab, click the **Add** button. This will reveal the **Code** and **Qty** fields, where you can respectively provide the code of the product and how many instances of it you need ordered.
   
   When you click **Save**, the product will be added with all the respective information about it, such as Unit, Price, and Discount.

   1.2.   From the **My Products** tab, click on the **Quantity** field of a **customer product** row and specify the exact quantity you need ordered.

   This will **automatically** add it in the **Order** tab.

   1.3.   Depending on how your Client Center instance is **configured**, users may be able to add products linked to their customer's **default distribution channel**.

   These products will be available in a separate tab that carries the channel's name, e.g. "Online store". The process to add them is identical to the **My Products** tab.

   1.4.  If the Client Center itself has a default distribution channel **configured**, an additional tab will also be available carrying that channel's name.

   Products linked to the channel will be available for selection.

2. When you're done specifying the quantities of the desired products, you can always **edit** or **delete** some of them if needed.

3. To finish the order, click **Place Order**. You'll be asked to confirm.

> [!NOTE]
> 
> You can start an order and switch to a different page or choose to place it later. <br> <br>
> The latest active user session is kept for **20 minutes**, and the order is automatically saved and registered with status **"New"**.
   
