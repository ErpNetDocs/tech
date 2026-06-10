# Files in Customer Profile

The **Files** panel in Customer Profile shows customer-related files that are attached directly to the customer record in ERP.net and shared for external access.

Unlike files in **Orders** or **Invoices**, which are attached to specific business documents, the files shown in Customer Profile belong to the customer record itself. This makes the panel suitable for company-level documents that are meant to be available across the customer relationship.

[screenshot: client-center/customer-profile/concepts/files-in-customer-profile/cc-customer-profile-concepts-files-in-customer-profile-01-files-panel-overview.png]

## What files are shown

The Files panel shows customer-related files that are attached directly to the current customer record.

These files can include documents such as:

- contracts;
- annexes;
- agreements;
- catalogs;
- other shared customer documents.

The exact files shown depend on what has been attached to the customer record in ERP.net and whether those files are configured for external visibility.

## How file visibility works

Files in Customer Profile follow the same general visibility rule used across Client Center.

A file becomes visible only when its **Access Permissions** field allows access to both internal and external users.

This means that a file attached to the customer record does not automatically appear in Client Center. It must also be shared for external access.

If a file is attached to the customer but its Access Permissions do not allow external visibility, the file remains hidden in Customer Profile.

For more information, see:

- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)
- [Access Permissions field](https://docs.erp.net/webclient/introduction/how-to/access-permission-field.html)
- [Manage Access Permissions](https://docs.erp.net/tech/modules/system/security/system-permissions/manage-access-permissions.html)

[screenshot: client-center/customer-profile/concepts/files-in-customer-profile/cc-customer-profile-concepts-files-in-customer-profile-02-file-visibility-rule.png]

## Relationship to access roles

Customer Profile is available across Client Center access levels, but the dedicated **Files** panel is available to users with **L40 - Billing** and above when eligible files exist.

This means that file visibility in Customer Profile depends on two conditions working together:

- the user must have the role level required to access the Files panel;
- the file itself must be shared for both internal and external users.

If either condition is not met, the customer file is not shown.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

## What the Files panel shows

When customer-related files are available for external access, the Files panel displays them together with basic file information, such as:

- file name;
- file extension;
- file size.

Users can review the list of available files and download the required document directly from the profile page.

These files are shown in the context of the active customer and are not tied to a specific order or invoice document.

## When no files are available

If no customer-related files are available for external access, Customer Profile shows the message **No documents available.**

This can happen when:

- the customer record has no attached files;
- the customer record has attached files, but none of them are shared for external users.

In this case, the page still shows the customer information, but no downloadable customer documents are available in the Files area.

[screenshot: client-center/customer-profile/concepts/files-in-customer-profile/cc-customer-profile-concepts-files-in-customer-profile-03-no-documents-available.png]

## Relationship to Customer information

The Customer Profile page combines two related but different parts:

- **Customer information**, which identifies the current customer;
- the **Files** panel, which shows customer-level documents that are available for external access.

Together, these parts provide both company identity information and access to shared customer documents in a single customer-facing page.

For more information, see [Customer information](customer-information.md).

## Relationship to Orders and Invoices

Files in Customer Profile are different from files shown in order and invoice documents.

- in **Orders**, files are attached to a specific order document;
- in **Invoices**, files are attached to a specific invoice document;
- in **Customer Profile**, files are attached to the customer record itself.

This distinction is important because the same Client Center user can work with document-specific files and customer-level files in different parts of the portal.

For more information, see:

- [Orders page](../../orders/concepts/orders-page.md)
- [Invoices page](../../billing/concepts/invoices-page.md)
- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)

## Relationship to customer context

The Files panel always reflects the currently selected customer.

When a user has access to multiple customers, the visible files belong only to the active customer context. After switching to another customer, the page updates to show the files attached to that customer's record, if such externally shared files are available.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

## Download behavior

When a file is visible in the Files panel, it can be downloaded directly from Customer Profile.

For task-oriented guidance, see [Download files from Customer Profile](../operations/download-files-from-customer-profile.md).

## Summary

The Files panel in Customer Profile shows customer-related files attached directly to the current customer record.

These files are visible only when the user's role allows access to the panel and the files are shared for both internal and external users. When no such files are available, Customer Profile shows the message **No documents available.**
