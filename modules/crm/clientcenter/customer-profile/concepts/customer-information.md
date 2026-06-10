# Customer information

The **Customer Profile** page shows the basic registered company information for the currently selected customer in Client Center.

This information gives external users a direct view of the customer identity associated with the active Client Center context. It helps users confirm which customer they are currently working with and review key company identifiers without accessing ERP.net directly.

[screenshot: client-center/customer-profile/concepts/customer-information/cc-customer-profile-concepts-customer-information-01-customer-information-overview.png]

## What customer information is shown

Customer Profile displays the registered information for the active customer.

This typically includes company identification details such as:

- customer name;
- **UIN**;
- **VAT number**.

The exact information shown depends on the customer data available in ERP.net for the current customer record.

## Customer information is customer-specific

The information shown in Customer Profile always belongs to the **currently selected customer**.

When a user has access to more than one customer, the page updates after a customer switch and shows the registered information for the newly selected customer.

This ensures that Client Center always presents company information in the correct customer context.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

[screenshot: client-center/customer-profile/concepts/customer-information/cc-customer-profile-concepts-customer-information-02-customer-identifiers.png]

## Relationship to access roles

Basic customer information is available to all external roles in Client Center.

This means that users who can sign in to Client Center can access the core company information shown in Customer Profile, even when they do not have access to higher-level functions such as Billing or User Management.

This makes Customer Profile the common reference page for the active customer across all access levels.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

## Relationship to Home and navigation

Customer information is part of the overall customer context shown in Client Center.

Together with the Home page and the navigation structure, Customer Profile helps users understand which customer they are currently viewing and what sections are available for that customer.

For more information, see [Home and navigation](../../concepts/home-and-navigation.md).

## Relationship to customer files

Customer Profile combines company information with a separate area for customer-related files.

The customer information part of the page identifies the customer, while the **Files** panel shows files attached directly to the customer record when such files are shared for external access.

For more information, see [Files in Customer Profile](files-in-customer-profile.md).

## Summary

The customer information shown in Customer Profile provides the basic registered company details for the active customer in Client Center.

This information is always customer-specific, updates when the user switches to another customer, and is available as the common company reference view across Client Center.
