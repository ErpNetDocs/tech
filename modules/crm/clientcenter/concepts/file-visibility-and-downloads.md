# File visibility and downloads

File visibility in Client Center is controlled by two separate mechanisms that work together:

- the user's **external role**, which determines whether the user can access a page or section;
- the file's **Access Permissions** setting in ERP.net, which determines whether a specific attached file is visible to external users.

This means that access to a document page does not automatically guarantee access to all files attached to that document. A user may be able to open an order, invoice, or customer profile and still not see any files there if the attached files are not shared for external access.

[screenshot: client-center/concepts/file-visibility-and-downloads/cc-concepts-file-visibility-and-downloads-01-files-sections-overview.png]

## Where files can appear

In Client Center, files can appear in three main places:

- in individual **order documents**;
- in individual **invoice documents**;
- in the **Files** panel of **Customer Profile**.

In all three cases, the interface shows the available files in a dedicated section or panel. When visible, each file is presented with basic metadata such as its name, file extension, and size.

For task-oriented instructions, see:

- [Download files from an order](../orders/operations/download-files-from-an-order.md)
- [Download files from an invoice](../billing/operations/download-files-from-an-invoice.md)
- [Download files from Customer Profile](../customer-profile/operations/download-files-from-customer-profile.md)

## The core visibility rule

A file becomes visible in Client Center only when its **Access Permissions** field allows access to both internal and external users.

In practice, this means that attachments whose Access Permissions value is not set to **Internal users + external users** do not appear in Client Center, even if they are attached to an otherwise visible order, invoice, or customer record.

This rule applies consistently across Client Center. The page or document may be accessible, but the attached files remain hidden unless they are explicitly shared for external access.

For background on access permissions in ERP.net, see:

- [Access Permissions field](https://docs.erp.net/webclient/introduction/how-to/access-permission-field.html)
- [Manage Access Permissions](https://docs.erp.net/tech/modules/system/security/system-permissions/manage-access-permissions.html)

[screenshot: client-center/concepts/file-visibility-and-downloads/cc-concepts-file-visibility-and-downloads-02-access-permissions-in-erp.png]

## When a Files section is shown

Client Center does not show an empty Files section just because a document has attachments in ERP.net.

The Files section appears only when there is at least one attachment that is shared with external users and is therefore allowed to be shown in Client Center.

As a result:

- if a document has visible external files, the Files section appears;
- if a document has attachments but none of them are shared for external access, the Files section does not appear at all.

This behavior is the same for order documents and invoice documents.

## Orders and invoices

In **Orders** and **Invoices**, files are shown inside the respective document view.

If an order or invoice contains attachments that are shared with external users, those files appear in a dedicated Files section in the document details. If no such attachments exist, the section is not shown.

This behavior is described in more detail in:

- [Orders page](../orders/concepts/orders-page.md)
- [Invoices page](../billing/concepts/invoices-page.md)

## Customer Profile files

Customer Profile uses the same visibility principle, but the source of the files is different.

Instead of showing files attached to a specific order or invoice, the Files panel in **Customer Profile** shows files attached to the **customer record** itself and shared for both internal and external users. This is intended for customer-related company documents such as contracts, annexes, agreements, catalogs, and similar shared files.

Users with the required Client Center access can work with these customer-related documents directly from the profile page.

If there are no accessible customer files, the panel shows the message **No documents available.**

For Customer Profile-specific details, see:

- [Files in Customer Profile](../customer-profile/concepts/files-in-customer-profile.md)

[screenshot: client-center/concepts/file-visibility-and-downloads/cc-concepts-file-visibility-and-downloads-03-customer-profile-files-panel.png]

## Relationship to external roles

File visibility should be understood separately from page visibility.

A user's external role determines whether they can access a section such as Orders, Billing, or Customer Profile. The role does not by itself expose every file attached to the underlying records. File-level visibility is still controlled through Access Permissions.

For example:

- a user may have access to **Orders** but still see no files in a specific order document;
- a user may have access to **Billing** but still not see invoice attachments unless those files are shared for external users;
- a user may have access to **Customer Profile**, but the Files panel will only show customer files that are externally shared.

For more about section access and role levels, see [Access model and external roles](access-model-and-external-roles.md) and [External Access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html).

## Download behavior

When a file is visible in Client Center, it is available for download directly from the corresponding Files section or panel.

The same general behavior applies across Orders, Invoices, and Customer Profile: the user does not need a separate file browser inside Client Center. Files are exposed in context, next to the business document or customer information they belong to.

The exact user steps are documented in the corresponding operation pages rather than here:

- [Download files from an order](../orders/operations/download-files-from-an-order.md)
- [Download files from an invoice](../billing/operations/download-files-from-an-invoice.md)
- [Download files from Customer Profile](../customer-profile/operations/download-files-from-customer-profile.md)

## What this means in practice

When users report that files are missing from Client Center, the cause is usually not the document itself but the sharing configuration of the attachment.

In most cases, the document is present and accessible, but its attached files are not visible because they were not configured for external access.

This is why file visibility in Client Center should always be treated as a combination of:

- access to the relevant page or document;
- correct file sharing through Access Permissions.

For problem-oriented guidance, see [Files are not visible or downloadable](../troubleshooting/files-are-not-visible-or-downloadable.md).
