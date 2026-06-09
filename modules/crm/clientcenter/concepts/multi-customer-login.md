# Multi-customer login

Client Center supports **multi-customer login**.

This allows one external user to access the data of more than one customer account with the same sign-in, as long as the user has been granted external access for each customer in ERP.net.

Instead of maintaining separate credentials for each customer, the user signs in once and can then work with the customer accounts that are assigned to that user through the **External Access** table.

[screenshot: client-center/concepts/multi-customer-login/cc-concepts-multi-customer-login-01-customer-switcher-overview.png]

## How multi-customer login works

Multi-customer login is based on the same access model used throughout Client Center.

If the same user is linked to multiple customers in ERP.net through separate **External Access** records, Client Center recognizes all of these customer assignments during sign-in.

After authentication, the user can work in the context of one of the assigned customers and switch between them without using a different account.

This means that multi-customer login does not introduce a separate access mechanism. It extends the standard customer-specific access model by allowing multiple customer assignments for the same user.

For more about the underlying access model, see [Access model and external roles](access-model-and-external-roles.md) and [External Access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html).

## Customer-specific access is preserved

Even when one user has access to multiple customers, access remains **customer-specific**.

For each customer, ERP.net evaluates the corresponding External Access record separately. This means that the same user can have a different role, different visibility, and different restrictions for each customer.

For example:

- the user can have **L40 - Billing** access for one customer;
- the same user can have **L20 - Orders** access for another customer;
- the same user can also have different **Days Back Access** limits for different customers.

The user does not receive one global role across all customers. Access is always determined by the currently selected customer context.

## Switching between customers

When a user has access to more than one customer, Client Center provides a way to switch between the available customer accounts.

After switching, the portal reloads the information for the selected customer and applies the corresponding external role and access restrictions for that customer.

This affects the entire Client Center context, including:

- the Home page content;
- the available navigation options;
- the visible orders and billing information;
- the customer profile data;
- the visible files and downloadable documents.

[screenshot: client-center/concepts/multi-customer-login/cc-concepts-multi-customer-login-02-customer-switcher.png]

## What changes after switching

Switching to another customer changes the working context of the current session.

This means that the user sees the data and pages available for the newly selected customer, not a combined view across all assigned customers.

In practice, after a customer switch:

- the visible documents belong to the selected customer;
- the navigation reflects the role assigned for that customer;
- customer-specific settings and restrictions are applied again;
- file visibility is recalculated based on the selected customer's accessible records.

This keeps the separation between customer accounts clear and prevents users from mixing data from multiple customers in the same view.

For more about navigation and page availability, see [Home and navigation](home-and-navigation.md).

## Relationship to roles

Multi-customer login does not override the external role model.

Instead, it applies the correct external role for the customer currently selected by the user.

This means that:

- a user can see billing pages for one customer and not for another;
- a user can have access to User Management for one customer and not for another;
- a user can see prices for one customer and only order lines without prices for another.

All page availability and document visibility continue to follow the assigned role for the active customer context.

For more information, see [Access model and external roles](access-model-and-external-roles.md).

## Relationship to User Management

Multi-customer login is closely related to how external users are assigned to customers.

A user becomes available in multiple customer contexts only when that same user account is assigned in ERP.net to multiple customers through separate External Access records.

This means that multi-customer login is not configured through a special setting in Client Center. It results from the way external user access is assigned and maintained.

For more information, see:

- [Add and manage external users](../user-management/operations/add-and-manage-external-users.md)
- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)

## Relationship to Home and Customer Profile

Because the active customer context changes after switching, the information shown in **Home** and **Customer Profile** also changes.

The user sees the data for the currently selected customer, including customer identifiers, customer-specific documents, and the pages available for that customer role.

This is especially important for users who work with several related companies or customer accounts and need to move between them without signing out and signing in again.

For more information, see:

- [Home and navigation](home-and-navigation.md)
- [Customer information](../customer-profile/concepts/customer-information.md)
- [Files in Customer Profile](../customer-profile/concepts/files-in-customer-profile.md)

[screenshot: client-center/concepts/multi-customer-login/cc-concepts-multi-customer-login-03-switched-customer-context.png]

## Session behavior

Client Center keeps the authenticated user session, but the selected customer determines which customer data is currently shown.

In other words, the session belongs to the user account, while the visible business data belongs to the active customer context selected within that session.

This is why a single sign-in can support several customer accounts without mixing their content.

## Summary

Multi-customer login allows one external user to access multiple customer accounts through a single sign-in.

This is possible when the same user is assigned to more than one customer in ERP.net through the **External Access** table.

The model preserves customer-specific access by applying the correct role and restrictions for the currently selected customer. As a result, users can switch between customer accounts while Client Center continues to enforce separate visibility, navigation, and document access for each one.
