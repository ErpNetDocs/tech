# Due Payments page

The **Due Payments** page shows the payment obligations that are currently due for the selected customer in Client Center.

It gives external users a focused view of unpaid or outstanding amounts, separate from the invoice list and separate from historical payment records. This helps users quickly identify what is currently due without reviewing all billing documents one by one.

[screenshot: client-center/billing/concepts/due-payments-page/cc-billing-concepts-due-payments-page-01-due-payments-list.png]

## What the Due Payments page shows

The Due Payments page displays the due payment obligations for the active customer context.

This page is intended to give users a direct view of the amounts that currently require attention. Instead of focusing on invoice documents as such, it focuses on what is due for payment.

The page follows the shared list behavior used in other Client Center list pages.

For more information about the common grid interaction model, see [Shared grid behavior](../../concepts/shared-grid-behavior.md).

## Role-based visibility

Access to the Due Payments page is controlled by the user's external role.

Users with **L40 - Billing** and above can access the Billing section, including Due Payments. Lower roles do not have access to this page.

Because the external access model is cumulative, users with **L80 - Admin** and **L90 - Owner** also retain access to due payment information.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

## Working with the due payments list

The Due Payments page presents the available due payment records in a list view.

Users can:

- browse the available due payments;
- sort and filter the list;
- search for specific records;
- review the currently outstanding payment information.

This allows users to focus directly on open payment obligations for the selected customer.

[screenshot: client-center/billing/concepts/due-payments-page/cc-billing-concepts-due-payments-page-02-due-payments-grid.png]

## Relationship to invoice documents

Due Payments is related to invoicing, but it is not the same as the **Invoices** page.

- **Invoices** focuses on the invoice documents themselves;
- **Due Payments** focuses on the payment obligations that are currently due.

This distinction is useful because a customer may need a quick operational view of what must be paid now, rather than a document-oriented view of all invoices.

In Client Center, the Due Payments page can also provide direct access to the corresponding invoice.

For more information, see [Invoices page](invoices-page.md).

## Expanded view and direct invoice access

The Due Payments page supports an expanded view of the payment information.

This allows users to inspect the due payment entry in more detail and, where applicable, navigate directly to the related invoice document.

The expanded view helps connect the payment obligation to the original billing document without requiring users to search for the invoice separately.

[screenshot: client-center/billing/concepts/due-payments-page/cc-billing-concepts-due-payments-page-03-expanded-view-and-invoice-link.png]

## Relationship to Payment History

Due Payments and **Payment History** represent different stages of the billing process.

- **Due Payments** shows what is currently due;
- **Payment History** shows payments that have already been completed.

Together, these pages give users visibility into both current obligations and past payment activity.

For more information, see [Payment History page](payment-history-page.md).

## Relationship to customer context

The Due Payments page always reflects the currently selected customer.

When a user has access to multiple customers, the due payments shown belong only to the active customer context. After switching to another customer, the page updates to show that customer's due payment information.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

## Summary

The Due Payments page gives users a focused view of the payment obligations that are currently due for the active customer.

It allows them to review outstanding amounts, work with the information through the shared grid model, and connect the due payment entry to the related invoice document when needed.
