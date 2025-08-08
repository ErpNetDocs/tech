# New Order

Order creation through the Client Center is disabled by default. You need to **enable** the respective **[global JSON settings first](../reference.md#isneworderenabled-setting)**

Once that's done, users with **[external role](../sales/customers/external-access.md#roles)** **L20 - Orders** and above will get access to the **New Order** page.

This is a multi-tab interface designed to handle the filling out and placement of new sales orders.

![pictures](pictures/new_order_panel.png)

### Structure

New Order consists of one primary tab, but it can be configured to include more:

1. **Order** - This is where the order is built. You can add products manually by entering their **code** and **quantity** or automatically through other tabs.

   ![pictures](pictures/order_tab.png)
   
2. **My Products** - All **[customer products](https://docs.erp.net/tech/modules/crm/sales/definitions/define-customers.html#customer-products)** are stored here. This tab can be hidden or enabled with an appropriate **[JSON setting](../reference.md#hidecustomerproducts-setting)**.
  
   You can add customer products to the order simply by specifying their quantities in the **Quantity** field. Once a quantity is set, the respective product will appear in the **Order** tab.

   ![pictures](pictures/my_products_tab.png)
   
3. A tab listing products linked to the **customer's default distribution channel** - It can be optionally revealed with a **[JSON setting](../reference.md#hidedistributionchannel-setting)** and always carries the name of that channel.

   You can specify product quantities in the **Quantity** field to add them to the order. Once a quantity is set, the respective product will appear in the **Order** tab.

   ![pictures](pictures/channel_customer_tab.png)

4. A tab listing products linked to the **Client Center's distribution channel** - It can be enabled with a **[JSON setting](../reference.md#hidecustomchannel-setting)** and always carries the name of that channel.

   Like in all other tabs, you can specify product quantities in the **Quantity** field to add them to the order.

   If a distribution channel is not set for your Client Center, the system will automatically link the sales order to a **[distribution channel](https://docs.erp.net/tech/modules/crm/marketing/distribution-channels/index.html)** with **code "CC"** and **name "Client Center"**. If such a channel does not exist, it will be created after the order is placed.

   ![pictures](pictures/channel_CC_tab.png)

## Create a new order

1. To begin, add products to the order. There are several ways to do this:
   
    1.1.   From the **Order** tab, click the **Add** button. This will reveal the **Code** and **Qty** fields, where you can respectively provide the code of the product and how many instances of it you need ordered.

   ![pictures](pictures/add_button.png)
   
   When you click **Save**, the product will be added with all the respective information about it, like **Unit**, **Price**, and **Discount**.

   ![pictures](pictures/added_product.png)

   1.2.   From the **My Products** tab, click on the **Quantity** field of a **[customer product](https://docs.erp.net/tech/modules/crm/sales/definitions/define-customers.html#customer-products)** row and specify the exact quantity you need ordered. 

   This will automatically add it in the **Order** tab with the respective information.

   ![pictures](pictures/quantity_myproducts.png)

   1.3.   Depending on how the Client Center is configured, users may add products linked to their customer's **[default distribution channel](https://docs.erp.net/tech/modules/crm/sales/definitions/define-customers.html#new-customer-details)**.

      The process to add them is identical to the **My Products** tab.

   ![pictures](pictures/quantity_distribution_channel_customer.png)

   1.4.  If the Client Center's **distribution channel** has products linked to it, they will be available for selection as well.

   ![pictures](pictures/quantity_distribution_channel_clientcenter.png)

2. When you're done adding the quantities of the desired products, you can always **edit** or **delete** some of them if needed.

   ![pictures](pictures/edit_delete_product.png)

3. To finish the order, click **Place Order**. You'll be asked to confirm if all order details have been reviewed.

   ![pictures](pictures/place_order_warning.png)

   Newly created orders are stored in the **[Orders](index.md)** page.

> [!NOTE]
> 
> You can start an order and switch to a different page or choose to place it later. <br> <br>
> The latest active user session is retained and the order is **automatically saved** and registered with status **"New"**.
   
