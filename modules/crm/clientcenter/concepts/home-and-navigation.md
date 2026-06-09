# Home and navigation

The **Home** page is the default landing page in Client Center after a successful sign-in.

It provides a summary view of the customer's activity and gives users direct access to the main sections available to them. The exact content and navigation options depend on the external role assigned to the user for the currently selected customer.

Home and navigation in Client Center are role-based and customer-specific. This means that the available sections are determined by the user's **external access role** and, when applicable, by the currently selected customer context.

[screenshot: client-center/concepts/home-and-navigation/cc-concepts-home-and-navigation-01-home-overview.png]

## Home as the starting point

Home serves as the main entry point to Client Center.

From there, users can orient themselves in the portal, review the information available for the active customer, and move to the sections they are allowed to access.

Depending on the assigned role, Home can provide access to:

- **Orders**;
- **Billing**;
- **User Management**;
- **Customer Profile**.

The Home page reflects the current customer context. If the same user has access to multiple customers, the information shown on Home belongs to the customer currently selected in the session.

For more about customer-specific access, see [Multi-customer login](multi-customer-login.md).

## Navigation is role-based

Client Center navigation is not identical for all users.

The available sections depend on the external role assigned to the user for the selected customer. As a result, two users signing in to the same Client Center can see different navigation options.

In general:

- users with basic access can reach Home and Customer Profile;
- users with order access can also reach Orders;
- users with billing access can also reach Billing;
- users with admin-level access can also reach User Management.

This is why navigation in Client Center should be understood as a reflection of the user's assigned access level rather than as a fixed portal menu.

For more information, see [Access model and external roles](access-model-and-external-roles.md).

[screenshot: client-center/concepts/home-and-navigation/cc-concepts-home-and-navigation-02-navigation-by-role.png]

## Main sections in Client Center

Client Center is organized into functional sections that become available according to the user's role.

### Orders

The **Orders** section gives users access to order-related information and actions. Depending on the role and configuration, users can review existing orders and use **New Order**.

For more information, see:

- [Orders overview](../orders/index.md)
- [Orders page](../orders/concepts/orders-page.md)
- [New Order behavior](../orders/concepts/new-order-behavior.md)

### Billing

The **Billing** section provides access to invoice and payment-related information.

Depending on the assigned role, users can view:

- **Invoices**;
- **Due Payments**;
- **Payment History**.

For more information, see:

- [Billing overview](../billing/index.md)
- [Invoices page](../billing/concepts/invoices-page.md)
- [Due Payments page](../billing/concepts/due-payments-page.md)
- [Payment History page](../billing/concepts/payment-history-page.md)

### User Management

The **User Management** section is available only to users with **Admin** or **Owner** access.

It allows them to add and manage external users for the corresponding customer.

For more information, see:

- [User Management overview](../user-management/index.md)
- [Add and manage external users](../user-management/operations/add-and-manage-external-users.md)

### Customer Profile

The **Customer Profile** section contains information about the current customer and, where applicable, customer-related files.

All users with Client Center access can view the basic customer information. Access to additional file-related functionality depends on role and file visibility settings.

For more information, see:

- [Customer Profile overview](../customer-profile/index.md)
- [Customer information](../customer-profile/concepts/customer-information.md)
- [Files in Customer Profile](../customer-profile/concepts/files-in-customer-profile.md)

## Home content depends on the current customer

When a user has access to more than one customer, the Home page always shows the information for the **currently selected customer**.

After switching to another customer, the Home page updates to reflect that customer's context. This includes the available sections, visible documents, and customer-specific information.

This keeps the portal consistent with the active customer selection and prevents information from multiple customers from being mixed in the same working view.

For more information, see [Multi-customer login](multi-customer-login.md).

## Relationship to file visibility

Navigation to a page or section does not automatically grant visibility to all files related to the documents shown there.

A user may be able to access Orders, Billing, or Customer Profile and still not see attached files unless those files are explicitly shared for external users.

This is why section availability and file visibility should be treated as separate parts of the Client Center access model.

For more information, see [File visibility and downloads](file-visibility-and-downloads.md).

[screenshot: client-center/concepts/home-and-navigation/cc-concepts-home-and-navigation-03-home-sections-and-files.png]

## Relationship to roles and restrictions

The external role determines not only whether a section is visible, but also how much information is shown inside that section.

For example:

- a user may have access to Orders without seeing prices, discounts, and amounts;
- a user may have access to Billing only when the assigned role includes billing rights;
- a user may see User Management only when the assigned role is **L80 - Admin** or **L90 - Owner**.

Additional restrictions such as **Days Back Access** can further limit which historical records are visible in the available sections.

For more information, see [Access model and external roles](access-model-and-external-roles.md).

## Summary

Home is the main starting page in Client Center, and navigation is generated according to the user's external role for the active customer.

This determines:

- which sections are available in the portal;
- what type of information the user can access;
- whether orders, billing pages, and user management are available;
- how the portal changes when the user switches to another customer.

As a result, Home and navigation in Client Center always reflect the current customer context and the level of access assigned to the signed-in user.
