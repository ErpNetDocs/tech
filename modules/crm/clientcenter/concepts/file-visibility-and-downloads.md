# File visibility and downloads

This article explains how file attachments become visible in Client Center and how users can download them.

File attachments can be available in Client Center documents such as orders and invoices.

For the step-by-step actions, see [Download files from an order](../orders/operations/download-files-from-an-order.md), [Download files from an invoice](../billing/operations/download-files-from-an-invoice.md), and [Download files from Customer Profile](../customer-profile/operations/download-files-from-customer-profile.md).

## Access permissions

To be able to view and download file attachments in Client Center, configure the **Access Permissions** field of the respective attachment in ERP.net.

Open the respective order or invoice in ERP.net and expand the **Files** panel.

Then:

1. Right-click the attachment and select **Details**.
2. Click the downward arrow next to **Open** and select **Internal system data**.
3. Set **Access Permissions** to **Internal users + external users**.
4. Click **Save and reload**.

The steps above must be applied for every attachment that should be visible and downloadable in Client Center.

<!-- Screenshot needed: cc-con-08-file-access-permissions.png -->

## How files appear in Client Center

When an order or invoice contains attachments with the required access permissions, they appear in a dedicated **Files** section.

The section displays basic information for each file, including:

- file name;
- file extension;
- file size.

Clicking once on a file name triggers its download.

<!-- Screenshot needed: cc-con-09-files-section-in-document.png -->

## When files are not shown

File attachments whose **Access Permissions** field is not set to **Internal users + external users** do not appear in Client Center.

If none of a document's attachments have this setting configured, the **Files** section does not appear at all.
