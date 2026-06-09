# Create an order

Use **New Order** in Client Center to create a new sales order for the currently selected customer.

Order creation through Client Center is disabled by default. Before users can create orders, the required Client Center settings must be enabled.

Users with external role **L20 - Orders** and above can access **New Order** when ordering is enabled for the site.

[screenshot: client-center/orders/operations/create-an-order/cc-orders-operations-create-an-order-01-new-order-overview.png]

## Before you begin

Make sure that:

- the user has external role **L20 - Orders** or higher;
- order creation is enabled in the Client Center settings;
- a valid order document type is configured for **New Order**;
- the correct customer is selected when the user has access to multiple customers.

Depending on the Client Center configuration, users may be able to add products from:

- the **Order** tab;
- the **My Products** tab;
- the customer's default distribution channel tab;
- the Client Center distribution channel tab;
- the **Promotional packages** panel.

For more information, see:

- [Orders overview](../index.md)
- [Order-related settings](../../configuration/order-related-settings.md)
- [New Order behavior](../concepts/new-order-behavior.md)
- [Multi-customer login](../../concepts/multi-customer-login.md)

## Create the order

### 1. Open New Order

Open the **Orders** section and select **New Order**.

When the module opens, it shows the current **Supplier**, **Customer**, and **Document No** for the order being created.

New Order uses a multi-tab interface. The main tab is **Order**, and depending on the configuration, additional tabs may also be available.

[screenshot: client-center/orders/operations/create-an-order/cc-orders-operations-create-an-order-02-open-new-order.png]

### 2. Add products to the order

Add the required products to the order.

You can do this in several ways, depending on the available tabs.

#### Add a product from the Order tab

In the **Order** tab, select **Add**.

This reveals the **Code** and **Qty** fields, where you can enter the product code and the quantity to be ordered.

Select **Save** to add the product to the order.

After the product is added, the order line is shown with its related information, such as **Unit**, **Price**, and **Discount**.

> [!NOTE]
> The value in the **Discount** column is associated with `LineStandardDiscountPercent`.

#### Add a product from My Products

If the **My Products** tab is available, enter the required quantity in the **Quantity** field for the selected customer product.

Once a quantity is entered, the product is automatically added to the **Order** tab together with its related information.

#### Add a product from a distribution channel tab

Depending on how Client Center is configured, users may also be able to add products from:

- a tab listing products linked to the customer's default distribution channel;
- a tab listing products linked to the Client Center distribution channel.

The process is the same as in **My Products**: enter the quantity in the **Quantity** field, and the product is added automatically to the **Order** tab.

[screenshot: client-center/orders/operations/create-an-order/cc-orders-operations-create-an-order-03-add-products.png]

### 3. Review product information if needed

If you need more details about a product, select its **code** or **name**.

This opens the **Product Info** popup, which can show additional product information, including a product picture when available.

Selecting the picture expands it and hides the remaining details.

### 4. Add notes if needed

To add additional instructions while creating the order, use **Add Notes** in the command bar of the **Order** tab.

If no note has been saved yet, the button is labeled **Add Notes**. After a note is saved, the button is labeled **Notes**.

Selecting the button opens a popup where you can enter or edit the note. Use **Save** to store the note or **Cancel** to close the popup without changes.

Notes are optional and do not block order creation when left empty.

> [!NOTE]
> Notes are stored in `General.Documents.Documents.DocumentNotes`.

[screenshot: client-center/orders/operations/create-an-order/cc-orders-operations-create-an-order-04-add-notes.png]

### 5. Add promotional packages if available

If the **Promotional packages** panel is available, it shows the promotional packages that are valid for the current customer and order context.

Only packages that are active, valid for the current date, and applicable to the current order conditions are displayed.

The panel shows the following fields:

- **Name**
- **Code**
- **Valid from**
- **Valid to**
- **Qty**

To add a promotional package, enter a quantity in **Qty** and use **Add prom. pack.**

The system automatically adds the corresponding package lines to the order according to the package definition and pricing conditions.

Lines added from a promotional package are visually distinguished and cannot be edited manually.

The **Order** panel also includes a **Promotional package** field that shows which package each added line originates from.

[screenshot: client-center/orders/operations/create-an-order/cc-orders-operations-create-an-order-05-promotional-packages.png]

### 6. Review availability and store-related behavior if applicable

Client Center can automatically set a store for sales orders after they are created.

Administrators can define this through the corresponding JSON setting. If no store is defined, the **Store** field remains empty.

When a store is specified and a maximum availability threshold is configured, the order can also show product availability information.

The **Availability** column can be shown through the **Column Chooser** and can display one of the following results:

- **Yes** in green, when the requested quantity is less than or equal to the available quantity;
- the actual available quantity in red, when the requested quantity is greater than the available quantity;
- **Call**, when the requested quantity is above the maximum value that can be revealed through the availability setting.

The **Call** value indicates that the customer must contact a sales representative to confirm whether the requested quantity is available.

For more information, see [Order-related settings](../../configuration/order-related-settings.md).

### 7. Modify or remove order lines if needed

Before placing the order, you can still edit or remove the quantities of the added products.

New Order automatically saves the latest state of the order.

This means that if the user leaves the page or decides to place the order later, the order is saved automatically and remains registered with status **New** until it is submitted.

### 8. Place the order

When the order is ready, select **Place Order**.

The system asks for confirmation that all details have been reviewed.

After the user confirms **Place Order**, the order date is automatically updated to the current date.

If the order is reopened later but not submitted, the date is not changed until the order is placed.

If all order lines are removed and the order is not submitted, the order remains in **New** state and its date is not updated.

[screenshot: client-center/orders/operations/create-an-order/cc-orders-operations-create-an-order-06-place-order.png]

## Result

After the order is placed:

- the order is submitted to ERP.net;
- the order date is updated to the current date at the moment of placement;
- the newly created order becomes available in the **Orders** page.

For more information about how orders appear after creation, see [Orders page](../concepts/orders-page.md).

## Related information

- [New Order behavior](../concepts/new-order-behavior.md)
- [Orders page](../concepts/orders-page.md)
- [Cancel an order](cancel-an-order.md)
- [Order-related settings](../../configuration/order-related-settings.md)
- [New Order is not available](../../troubleshooting/new-order-is-not-available.md)
