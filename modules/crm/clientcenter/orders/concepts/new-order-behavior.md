# New Order behavior

**New Order** is the order entry function in Client Center.

It allows external users to create a sales order for the currently selected customer through a dedicated order entry interface. Unlike the [Orders page](orders-page.md), which is used to review existing orders, **New Order** is used to compose and submit a new order.

The availability and behavior of New Order depend on both the user's external role and the Client Center configuration.

[screenshot: client-center/orders/concepts/new-order-behavior/cc-orders-concepts-new-order-behavior-01-new-order-overview.png]

## When New Order is available

New Order is available only when order creation is enabled in the Client Center settings and a valid order document type is configured.

Users with external role **L20 - Orders** and above can access it when the required settings are in place.

If New Order is not enabled or not configured correctly, the function is not available in Client Center.

For more information, see:

- [Create an order](../operations/create-an-order.md)
- [Order-related settings](../../configuration/order-related-settings.md)
- [New Order is not available](../../troubleshooting/new-order-is-not-available.md)

## General structure of New Order

New Order uses a multi-tab interface.

The main tab is **Order**. Depending on the Client Center configuration, additional tabs may also be available to help users add products to the order.

When the page is opened, it shows the current:

- **Supplier**
- **Customer**
- **Document No**

This gives the user immediate context for the order being created.

The tabs and panels available in New Order depend on the configured data sources and settings for the site.

## Product entry sources

Products can be added to the order from more than one source.

Depending on the Client Center configuration, New Order can include:

- the **Order** tab;
- the **My Products** tab;
- a tab for the customer's default distribution channel;
- a tab for the Client Center distribution channel;
- the **Promotional packages** panel.

These entry points all contribute to the same order being created. Regardless of where a product is selected, the resulting order lines are shown in the **Order** tab.

[screenshot: client-center/orders/concepts/new-order-behavior/cc-orders-concepts-new-order-behavior-02-tabs-and-sources.png]

## Order tab behavior

The **Order** tab is the central place where the current order lines are shown.

Users can add products directly in this tab by selecting **Add** and entering the product code and quantity. After saving, the product line is added to the order and appears together with its related information, such as unit, price, and discount when those values are visible for the user's role.

The **Discount** column is associated with `LineStandardDiscountPercent`.

The Order tab also reflects lines added from the other product source tabs, so it acts as the consolidated view of the order content.

## My Products and distribution channel tabs

When the **My Products** tab is available, it shows products related to the customer.

Users add products by entering quantities in the **Quantity** field. Once a quantity is entered, the corresponding product is added automatically to the **Order** tab.

The same general behavior applies to tabs that show products from:

- the customer's default distribution channel;
- the distribution channel assigned to the Client Center.

These tabs provide alternative product sources, but they do not create separate orders. They feed product lines into the same current order.

## Product information popup

New Order can display additional product details through the **Product Info** popup.

When users select a product code or product name, Client Center opens a popup with additional information about the selected product. If a product picture is available, it is shown there as well.

Selecting the picture expands it and hides the remaining details.

This allows users to review product-related information without leaving the order entry flow.

## Notes behavior

New Order supports optional document notes.

Users can add notes through the **Add Notes** command in the command bar of the **Order** tab. After a note has been saved, the same command is shown as **Notes**.

Selecting the command opens a popup where the note can be entered or edited. The note can then be saved or the popup can be closed without applying changes.

Notes are stored in `General.Documents.Documents.DocumentNotes`.

[screenshot: client-center/orders/concepts/new-order-behavior/cc-orders-concepts-new-order-behavior-03-notes-and-product-info.png]

## Promotional packages

New Order can include a **Promotional packages** panel.

When available, the panel shows promotional packages that are valid for the current customer and order context. Only packages that are active, valid for the current date, and applicable to the current order conditions are shown.

The panel includes the following fields:

- **Name**
- **Code**
- **Valid from**
- **Valid to**
- **Qty**

Users can add a package by entering a quantity and selecting **Add prom. pack.**

The package then adds the corresponding lines to the order automatically according to the package definition and pricing conditions.

Lines added from promotional packages are visually distinguished and cannot be edited manually. The **Order** panel also shows a **Promotional package** field indicating which package each added line originates from.

## Availability behavior

New Order can show product availability information when the corresponding settings are configured.

Administrators can define a default store and an availability threshold in the Client Center settings. When a store is configured, availability can be shown in the **Availability** column, which can be added through the **Column Chooser**.

The column can display:

- **Yes** in green, when the requested quantity is less than or equal to the available quantity;
- the actual available quantity in red, when the requested quantity is greater than the available quantity;
- **Call**, when the requested quantity is above the maximum value that can be shown through the configured threshold.

The **Call** result indicates that the customer must contact a sales representative to confirm whether the requested quantity is available.

If no store is defined, the **Store** field remains empty and availability behavior may be limited accordingly.

For more information, see [Order-related settings](../../configuration/order-related-settings.md).

[screenshot: client-center/orders/concepts/new-order-behavior/cc-orders-concepts-new-order-behavior-04-promotional-packages-and-availability.png]

## Automatic save behavior

New Order automatically saves the latest state of the order.

This means that if the user leaves the page or decides to complete the order later, the order remains saved in ERP.net with status **New** until it is submitted.

This behavior allows users to return to the order later without losing the entered data.

If all order lines are removed and the order is not submitted, the order still remains in **New** state.

## Placement behavior

When the user selects **Place Order**, Client Center asks for confirmation before submitting the order.

After confirmation:

- the order is submitted to ERP.net;
- the order date is updated to the current date.

If the order is reopened later but not submitted, the date does not change until the order is placed.

This means that the effective order date in Client Center reflects the actual placement moment rather than the moment when the draft order was first created.

## Relationship to existing orders

New Order belongs to the Orders area, but it behaves differently from the page used to review existing orders.

- [Orders page](orders-page.md) is focused on already created order documents;
- **New Order** is focused on creating and submitting a new order.

This distinction is important because the list of existing orders and the order entry workflow serve different purposes, even though they are part of the same functional section.

## Relationship to customer context

New Order always works in the context of the currently selected customer.

When a user has access to more than one customer, the order is created for the active customer context selected in the current session. After switching to another customer, New Order works with that customer's context instead.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

## Summary

New Order is the Client Center function for creating and submitting a sales order.

Its behavior is shaped by the user's access role and by the Client Center configuration. Depending on the setup, users can add products from several sources, review additional product information, add notes, use promotional packages, check availability, and submit the order when ready.

For task-oriented instructions, see [Create an order](../operations/create-an-order.md).
