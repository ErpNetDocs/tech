# File visibility and downloads

This article explains how attached files become visible in Client Center and how users can download them.

In Client Center, attached files can be shown in order and invoice documents.

For the step-by-step actions, see [Download files from an order](../orders/operations/download-files-from-an-order.md), [Download files from an invoice](../billing/operations/download-files-from-an-invoice.md), and [Download files from Customer Profile](../customer-profile/operations/download-files-from-customer-profile.md).

## Prerequisites

To be able to view and download file attachments in Client Center, you must configure the **Access Permissions** field of the respective attachment through the **Files** panel in ERP.net.

For more information about this field, see [How to use the Access Permission field in the Files panel](../../../../webclient/introduction/how-to/access-permission-field.md).

Simply navigate to the respective order or invoice and expand the **Files** panel.

Then:

1. Right-click the attachment and select **Details**.
2. Click the downward arrow next to **Open** and select **Internal system data**.
3. Edit the details of the attachment by setting the value of the **Access Permissions** field to **Internal users + external users**.
4. Click **Save and reload** to apply the change.

The steps above must be applied for every attachment you wish to see and download from within your Client Center website.

<!-- Screenshot needed: cc-con-08-file-access-permissions.png -->

## How files appear in Client Center

Open an invoice or an order with attachments.

The attachment will appear in a dedicated **Files** section.

You can see its:

- name;
- file extension;
- size.

Click on a desired attachment name once to immediately download and save it on your device.

<!-- Screenshot needed: cc-con-09-files-section-in-document.png -->

## When files are not shown

File attachments whose **Access Permissions** field is not set to **Internal users + external users** will not appear in the **Files** section.

If none of the document's attachments have this setting configured, the **Files** section will not appear at all.
