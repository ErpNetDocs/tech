# Orders page

The **Orders** page shows the existing sales orders available to the currently selected customer in Client Center.

It provides list-based access to order documents and allows users to open an individual order to review its details. Depending on the user's external role, the visible information may include only basic order data or also commercial values such as **Price**, **Discount**, and **Amount**.

The Orders page is intended for working with already created orders. For creating new ones, use **New Order**.

[screenshot: client-center/orders/concepts/orders-page/cc-orders-concepts-orders-page-01-orders-list.png]

## What the Orders page shows

The Orders page displays the sales orders available to the active customer context.

Users can browse the list of orders and open a specific order document to review its content. The page follows the shared list behavior used in other Client Center list pages.

For more information about the common grid interaction model, see [Shared grid behavior](../../concepts/shared-grid-behavior.md).

## Role-based visibility

Access to the Orders page is controlled by the user's external role.

Users with **L20 - Orders** and above can access the Orders section, but the amount of visible commercial information depends on the assigned role.

In general:

- users with **L20 - Orders** can view orders without **Price**, **Discount**, and **Amount**;
- users with **L30 - Orders + Prices** and above can view the full commercial details;
- higher roles retain order access as part of the cumulative role model.

This means that the same Orders page can present different levels of detail to different external users.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

## Working with the order list

The Orders page presents orders in a list view.

Users can:

- browse the available orders;
- sort and filter the list;
- search for specific records;
- open an individual order document.

This allows users to locate a specific order and then move from the list view to the document details.

[screenshot: client-center/orders/concepts/orders-page/cc-orders-concepts-orders-page-02-orders-grid.png]

## Opening an order document

When a user selects an order from the list, Client Center opens the order document view.

The document view shows the details that are available for the user's role. Depending on the assigned access level, this may include product information only or the full commercial details of the order.

The page is intended for reviewing existing orders rather than editing them as draft documents through the order entry interface.

For creating a new order, see [Create an order](../operations/create-an-order.md).

## Order details

When an order document is opened, Client Center can show information such as:

- order identification details;
- product lines;
- quantities;
- commercial values, when allowed by role;
- attached files, when externally shared.

The exact visible fields depend on the role and the available document data.

Users with access to prices can review the full order values. Users without price visibility can still review the order content, but the commercial columns remain hidden.

## Files in an order

If an order contains attachments that are shared for both internal and external users, the order document shows a dedicated **Files** section.

This section displays the available files together with basic information such as file name, file extension, and size. Users can download the visible files directly from the order document.

If the order contains no externally shared attachments, the **Files** section does not appear.

For more information, see:

- [Download files from an order](../operations/download-files-from-an-order.md)
- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)

[screenshot: client-center/orders/concepts/orders-page/cc-orders-concepts-orders-page-03-order-document-files.png]

## Canceling an order

Client Center allows a submitted order to be canceled before it is released.

If the order is still eligible for cancellation, the cancel action is available in the order document. Once the order is released, it can no longer be canceled from Client Center.

For more information, see [Cancel an order](../operations/cancel-an-order.md).

## Relationship to New Order

The Orders page and **New Order** belong to the same functional area, but they serve different purposes.

- **Orders page** is used to review existing order documents;
- **New Order** is used to create and submit a new order.

This distinction is important because the Orders page focuses on already created records, while New Order provides the order entry behavior used during creation.

For more information, see [New Order behavior](new-order-behavior.md).

## Relationship to customer context

The Orders page always reflects the currently selected customer.

When a user has access to multiple customers, the visible orders belong only to the active customer context. After switching to another customer, the Orders page updates to show that customer's orders.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

## Summary

The Orders page gives users access to the existing sales orders for the current customer.

It allows them to browse the order list, open individual order documents, review the available details according to their role, download externally shared files, and cancel orders that have been submitted but not yet released.

For task-oriented guidance, see [Operations](../operations/index.md).
