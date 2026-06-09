# Payment History page

The **Payment History** page shows completed payment records for the selected customer in Client Center.

It gives external users visibility into past payment activity and complements the other billing-related pages by showing what has already been paid, rather than what is still due.

[screenshot: client-center/billing/concepts/payment-history-page/cc-billing-concepts-payment-history-page-01-payment-history-list.png]

## What the Payment History page shows

The Payment History page displays historical payment records for the active customer context.

This page is intended to provide a retrospective view of completed payments. Unlike **Due Payments**, which focuses on current payment obligations, Payment History focuses on payment activity that has already been recorded.

The page follows the shared list behavior used in other Client Center list pages.

For more information about the common grid interaction model, see [Shared grid behavior](../../concepts/shared-grid-behavior.md).

## Role-based visibility

Access to the Payment History page is controlled by the user's external role.

Users with **L40 - Billing** and above can access the Billing section, including Payment History. Lower roles do not have access to this page.

Because the external access model is cumulative, users with **L80 - Admin** and **L90 - Owner** also retain access to payment history information.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

## Working with the payment history list

The Payment History page presents completed payment records in a list view.

Users can:

- browse the available payment history records;
- sort and filter the list;
- search for specific records;
- review historical payment information for the selected customer.

This allows users to track past payment activity in a consistent list-based view.

[screenshot: client-center/billing/concepts/payment-history-page/cc-billing-concepts-payment-history-page-02-payment-history-grid.png]

## Relationship to Invoices and Due Payments

Payment History is part of the Billing section, but it serves a different purpose from the other billing pages.

- **Invoices** focuses on invoice documents;
- **Due Payments** focuses on current outstanding obligations;
- **Payment History** focuses on completed payment records.

Together, these pages provide complementary views of the customer's billing information.

For more information, see:

- [Invoices page](invoices-page.md)
- [Due Payments page](due-payments-page.md)

## Relationship to customer context

The Payment History page always reflects the currently selected customer.

When a user has access to multiple customers, the visible payment records belong only to the active customer context. After switching to another customer, the page updates to show that customer's payment history.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

## Summary

The Payment History page gives users access to completed payment records for the active customer.

It allows them to review past payment activity through the same shared grid model used across Client Center and complements the invoice and due payment views in the Billing section.
