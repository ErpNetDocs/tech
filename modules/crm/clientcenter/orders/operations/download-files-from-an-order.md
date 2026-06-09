# Download files from an order

Use this procedure to download files attached to an order in Client Center.

Order files are available only when the order contains attachments that are shared for both internal and external users in ERP.net. If no such files are available, the **Files** section does not appear in the order.

[screenshot: client-center/orders/operations/download-files-from-an-order/cc-orders-operations-download-files-from-an-order-01-order-files-section.png]

## Before you begin

Make sure that:

- the user has access to the **Orders** section;
- the correct customer is selected when the user has access to multiple customers;
- the required order is visible in Client Center;
- the order contains attached files that are shared for external access.

A file becomes visible in Client Center only when its **Access Permissions** field allows access to both internal and external users.

For more information, see:

- [Orders overview](../index.md)
- [Orders page](../concepts/orders-page.md)
- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)
- [Multi-customer login](../../concepts/multi-customer-login.md)

## Download a file from an order

### 1. Open the Orders section

Open **Orders** and locate the order whose files you want to download.

If needed, use the available grid functions to find the required order more quickly.

For more information about the shared list behavior, see [Shared grid behavior](../../concepts/shared-grid-behavior.md).

### 2. Open the order document

Select the order to open its details.

Review the document and locate the **Files** section.

If the order contains externally shared attachments, the section shows the available files together with basic information such as file name, file extension, and size.

[screenshot: client-center/orders/operations/download-files-from-an-order/cc-orders-operations-download-files-from-an-order-02-open-order-document.png]

### 3. Download the file

In the **Files** section, select the file that you want to download.

Client Center downloads the selected file directly from the order document.

### 4. Repeat if needed

If more than one file is available, repeat the action for each required file.

[screenshot: client-center/orders/operations/download-files-from-an-order/cc-orders-operations-download-files-from-an-order-03-download-file.png]

## If the Files section is not shown

If the **Files** section does not appear in the order document, this usually means that the order does not contain any attachments that are shared for external access.

This can happen when:

- the order has no attached files;
- the order has attached files, but their **Access Permissions** do not allow access for external users.

For more information, see:

- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)
- [Files are not visible or downloadable](../../troubleshooting/files-are-not-visible-or-downloadable.md)

## Result

After the file is selected, it is downloaded from the order document to the user's device.

## Related information

- [Orders page](../concepts/orders-page.md)
- [Create an order](create-an-order.md)
- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)
- [Files are not visible or downloadable](../../troubleshooting/files-are-not-visible-or-downloadable.md)
