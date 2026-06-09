# Invoices page

The **Invoices** page shows the invoice documents available to the currently selected customer in Client Center.

It provides list-based access to invoices and allows users to open an individual invoice to review its details. The page is intended to give external users visibility into billing documents without requiring direct access to ERP.net.

[screenshot: client-center/billing/concepts/invoices-page/cc-billing-concepts-invoices-page-01-invoices-list.png]

## What the Invoices page shows

The Invoices page displays the invoice documents available to the active customer context.

Users can browse the list of invoices and open a specific invoice document to review its content. The page follows the shared list behavior used in other Client Center list pages.

For more information about the common grid interaction model, see [Shared grid behavior](../../concepts/shared-grid-behavior.md).

## Role-based visibility

Access to the Invoices page is controlled by the user's external role.

Users with **L40 - Billing** and above can access the Billing section, including invoices. Lower roles do not have access to this page.

Because the external access model is cumulative, users with **L80 - Admin** and **L90 - Owner** also retain invoice access.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

## Working with the invoice list

The Invoices page presents invoice documents in a list view.

Users can:

- browse the available invoices;
- sort and filter the list;
- search for specific records;
- open an individual invoice document.

This allows users to locate a specific invoice and then move from the list view to the document details.

[screenshot: client-center/billing/concepts/invoices-page/cc-billing-concepts-invoices-page-02-invoices-grid.png]

## Opening an invoice document

When a user selects an invoice from the list, Client Center opens the invoice document view.

The document view shows the invoice details available for the current customer. This gives users direct access to the billing document together with any related information exposed in Client Center.

The page is intended for reviewing existing invoice documents rather than modifying them.

## Invoice details

When an invoice document is opened, Client Center can show information such as:

- invoice identification details;
- invoice lines;
- amounts and totals;
- attached files, when externally shared.

The exact visible fields depend on the available invoice data and the current customer context.

## Files in an invoice

If an invoice contains attachments that are shared for both internal and external users, the invoice document shows a dedicated **Files** section.

This section displays the available files together with basic information such as file name, file extension, and size. Users can download the visible files directly from the invoice document.

If the invoice contains no externally shared attachments, the **Files** section does not appear.

For more information, see:

- [Download files from an invoice](../operations/download-files-from-an-invoice.md)
- [File visibility and downloads](../../concepts/file-visibility-and-downloads.md)

[screenshot: client-center/billing/concepts/invoices-page/cc-billing-concepts-invoices-page-03-invoice-document-files.png]

## Relationship to Due Payments and Payment History

The Invoices page is one of the billing-related views in Client Center, but it is not the same as **Due Payments** or **Payment History**.

- **Invoices** focuses on the invoice documents themselves;
- **Due Payments** focuses on currently outstanding payment obligations;
- **Payment History** focuses on completed payment records.

These pages are related, but each presents a different aspect of the customer's billing information.

For more information, see:

- [Due Payments page](due-payments-page.md)
- [Payment History page](payment-history-page.md)

## Relationship to customer context

The Invoices page always reflects the currently selected customer.

When a user has access to multiple customers, the visible invoices belong only to the active customer context. After switching to another customer, the Invoices page updates to show that customer's invoice documents.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

## Summary

The Invoices page gives users access to the invoice documents for the current customer.

It allows them to browse the invoice list, open individual invoice documents, review the available billing details, and download externally shared files when such files are available.

For task-oriented guidance, see [Operations](../operations/index.md).
