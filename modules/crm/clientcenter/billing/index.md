# Billing

The **Billing** section in Client Center gives external users access to invoice and payment-related information for the currently selected customer.

Depending on the assigned external role, users can review invoices, due payments, and payment history. The Billing section is intended to provide customer-facing visibility into financial documents and payment status without requiring direct access to ERP.net.

[screenshot: client-center/billing/cc-billing-overview-01-billing-section.png]

## What users can do in Billing

In the Billing section, users can typically:

- review the list of available invoices;
- open an individual invoice document;
- review current due payments;
- review payment history;
- download files attached to an invoice, when such files are shared for external access.

The exact availability of these pages depends on the user's assigned **external role**.

For more information about access levels, see [Access model and external roles](../concepts/access-model-and-external-roles.md).

## Role-based visibility in Billing

Access to Billing is role-based.

Users with **L40 - Billing** and above can access the billing-related pages in Client Center. Lower roles do not have access to this section.

Because the external access model is cumulative, users with **L80 - Admin** and **L90 - Owner** also retain billing access.

This means that Billing is available only when the assigned role includes invoice and payment visibility for the selected customer.

## What Billing includes

The Billing section includes three main pages:

- **Invoices** – shows the invoice documents available to the current customer;
- **Due Payments** – shows payment obligations that are currently due;
- **Payment History** – shows completed payment records.

These pages are related, but they present different views of the customer's billing information.

For more information, see:

- [Invoices page](concepts/invoices-page.md)
- [Due Payments page](concepts/due-payments-page.md)
- [Payment History page](concepts/payment-history-page.md)

[screenshot: client-center/billing/cc-billing-overview-02-billing-pages.png]

## Invoice documents and attached files

When users open an invoice document, they can review its details and, when applicable, download attached files.

Files are visible only when the corresponding invoice attachments are shared for both internal and external users in ERP.net. If no such files are available, the **Files** section does not appear in the invoice.

For more information, see:

- [Download files from an invoice](operations/download-files-from-an-invoice.md)
- [Invoices page](concepts/invoices-page.md)
- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)

## Shared list behavior

The pages in Billing follow the same shared grid interaction model used in other list-based areas of Client Center.

This allows users to sort, filter, group, search, and organize billing records in a consistent way across invoices, due payments, and payment history.

For more information, see [Shared grid behavior](../concepts/shared-grid-behavior.md).

## In this section

### Operations

Use the Operations pages for task-oriented guidance:

- [Operations overview](operations/index.md)
- [Download files from an invoice](operations/download-files-from-an-invoice.md)

### Concepts

Use the Concepts pages to understand how the Billing section works:

- [Concepts overview](concepts/index.md)
- [Invoices page](concepts/invoices-page.md)
- [Due Payments page](concepts/due-payments-page.md)
- [Payment History page](concepts/payment-history-page.md)

## Related sections

- [Home and navigation](../concepts/home-and-navigation.md)
- [File visibility and downloads](../concepts/file-visibility-and-downloads.md)
- [Troubleshooting](../troubleshooting/index.md)

## Summary

The Billing section gives external users access to invoice and payment-related information for the active customer.

It provides separate views for invoices, due payments, and payment history, while using the same role-based access model and shared grid behavior as the rest of Client Center. When invoice attachments are shared for external access, users can also download them directly from the invoice document.
