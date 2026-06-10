# Files are not visible or downloadable

Use this page when files do not appear in Client Center or when a user cannot download files that are expected to be available.

In Client Center, file visibility depends on both the page the user can access and the sharing settings of the file itself.

## Check whether the file is shared for external access

A file is visible in Client Center only when its **Access Permissions** field allows access to both internal and external users.

Files whose **Access Permissions** value is not set to **Internal users + external users** do not appear in Client Center.

For more information, see:

- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)
- [Access Permissions field](https://docs.erp.net/webclient/introduction/how-to/access-permission-field.html)
- [Manage Access Permissions](https://docs.erp.net/tech/modules/system/security/system-permissions/manage-access-permissions.html)

## Check whether the user can access the relevant page

Files in Client Center can appear in:

- order documents;
- invoice documents;
- the **Files** panel in **Customer Profile**.

If the user cannot access the relevant section, the user will not be able to see or download its files.

For more information, see:

- [Access model and external roles](../concepts/access-model-and-external-roles.md)
- [Orders page](../orders/concepts/orders-page.md)
- [Invoices page](../billing/concepts/invoices-page.md)
- [Files in Customer Profile](../customer-profile/concepts/files-in-customer-profile.md)

## Check whether the Files section is expected to appear

In **Orders** and **Invoices**, the **Files** section appears only when there is at least one attachment that is shared for external access.

If a document has no attached files, or if none of its files are shared for external users, the **Files** section does not appear.

In **Customer Profile**, if no customer files are available for external access, the page shows the message **No documents available.**

For more information, see:

- [Download files from an order](../orders/operations/download-files-from-an-order.md)
- [Download files from an invoice](../billing/operations/download-files-from-an-invoice.md)
- [Download files from Customer Profile](../customer-profile/operations/download-files-from-customer-profile.md)

## Check whether the correct customer is selected

If the user has access to multiple customers, make sure the correct customer is selected.

Client Center always shows files in the context of the currently selected customer. After switching to another customer, the visible documents and files change accordingly.

For more information, see [Multi-customer login](../concepts/multi-customer-login.md).

## Check whether the file belongs to the expected object

Files shown in Client Center depend on where the file is attached in ERP.net.

- In **Orders**, the file must be attached to the order document.
- In **Invoices**, the file must be attached to the invoice document.
- In **Customer Profile**, the file must be attached to the customer record.

If the file is attached to a different object, it will not appear in the expected place in Client Center.

## Related pages

- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)
- [Orders page](../orders/concepts/orders-page.md)
- [Invoices page](../billing/concepts/invoices-page.md)
- [Files in Customer Profile](../customer-profile/concepts/files-in-customer-profile.md)
- [Download files from an order](../orders/operations/download-files-from-an-order.md)
- [Download files from an invoice](../billing/operations/download-files-from-an-invoice.md)
- [Download files from Customer Profile](../customer-profile/operations/download-files-from-customer-profile.md)
