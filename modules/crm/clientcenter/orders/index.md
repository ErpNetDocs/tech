# Orders

The **Orders** section in Client Center gives external users access to order-related information and actions for the currently selected customer.

Depending on the assigned external role and the Client Center configuration, users can review existing orders, create new orders, cancel submitted orders, and download files attached to order documents.

The Orders section is one of the main working areas in Client Center. It combines list-based access to existing orders with document-level actions and order-specific behavior such as **New Order**.

[screenshot: client-center/orders/cc-orders-overview-01-orders-section.png]

## What users can do in Orders

In the Orders section, users can typically:

- review the list of available orders;
- open an individual order document;
- create a new order when **New Order** is enabled;
- cancel an order before it is released;
- download files attached to an order, when such files are shared for external access.

The exact availability of these actions depends on both:

- the user's assigned **external role**;
- the Client Center configuration for the site.

For more information about access levels, see [Access model and external roles](../concepts/access-model-and-external-roles.md).

## Role-based visibility in Orders

Access to Orders is role-based.

Users with order access can work with order-related pages, but the amount of visible commercial information depends on the assigned role.

In general:

- users with **L20 - Orders** can access Orders, but do not see **Price**, **Discount**, or **Amount**;
- users with **L30 - Orders + Prices** and above can see the full commercial details of the order;
- users with **L40 - Billing**, **L80 - Admin**, and **L90 - Owner** retain order access as part of the cumulative access model.

This means that two external users may both have access to the Orders section, while still seeing different levels of detail inside the same functional area.

## Orders and New Order

The Orders section includes both access to existing order documents and, when enabled, the ability to create new ones through **New Order**.

These are related but not identical parts of the Orders experience:

- **Orders page** focuses on reviewing and opening existing orders;
- **New Order** focuses on creating a new order and submitting it to ERP.net.

The availability of **New Order** depends on Client Center settings such as whether ordering is enabled and whether a valid order document type is configured.

For more information, see:

- [Create an order](operations/create-an-order.md)
- [New Order behavior](concepts/new-order-behavior.md)
- [Order-related settings](../configuration/order-related-settings.md)

[screenshot: client-center/orders/cc-orders-overview-02-orders-and-new-order.png]

## Order documents and attached files

When users open a specific order, they can review the order details that are available to their role.

If the order includes attached files that are shared for both internal and external users, those files appear in the order's **Files** section and can be downloaded from there.

File visibility does not depend only on access to Orders. It also depends on the sharing configuration of the attachment itself.

For more information, see:

- [Orders page](concepts/orders-page.md)
- [Download files from an order](operations/download-files-from-an-order.md)
- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)

## Shared list behavior

The Orders page uses the same general grid interaction model as other list-based pages in Client Center.

This allows users to work with order lists through common list actions such as sorting, filtering, grouping, column selection, layout saving, and summaries.

For more information, see [Shared grid behavior](../concepts/shared-grid-behavior.md).

## In this section

### Operations

Use the Operations pages for task-oriented guidance:

- [Operations overview](operations/index.md)
- [Create an order](operations/create-an-order.md)
- [Cancel an order](operations/cancel-an-order.md)
- [Download files from an order](operations/download-files-from-an-order.md)

### Concepts

Use the Concepts pages to understand how the Orders section works:

- [Concepts overview](concepts/index.md)
- [Orders page](concepts/orders-page.md)
- [New Order behavior](concepts/new-order-behavior.md)

## Related sections

- [Home and navigation](../concepts/home-and-navigation.md)
- [Order-related settings](../configuration/order-related-settings.md)
- [Troubleshooting](../troubleshooting/index.md)

## Summary

The Orders section gives external users access to existing orders and, when enabled, to the creation of new orders.

What users can see and do depends on their external role, the selected customer context, and the site configuration. Together, these determine whether users can view prices, place orders, cancel submitted orders, and access attached files.
