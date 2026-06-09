# Access model and external roles

Access to Client Center is determined through **external access roles**.

The access model is based on the relationship between a **user** and a **customer**. This relationship is defined in ERP.net through the **External Access** table. For each user-customer combination, ERP.net stores the role that defines what the user is allowed to see and do in Client Center.

This means that Client Center access is not assigned globally to the user. It is assigned **per customer**.

[screenshot: client-center/concepts/access-model-and-external-roles/cc-concepts-access-model-and-external-roles-01-role-overview.png]

## How the access model works

Client Center uses the ERP.net **External Access** table as the source of truth for customer-specific access.

Each record in the table defines:

- the **customer** whose data is accessible;
- the **user** account to whom access is granted;
- the **role** that determines the level of access;
- the optional **Days Back Access** limit;
- optional **notes**.

This model allows the same user to have different access levels for different customers.

For example, one user can have billing access for one customer and order-only access for another.

For more information about the underlying ERP.net model, see [External Access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html).

## Role inheritance

External access roles are hierarchical.

Each subsequent role includes the rights granted by the previous one. This means that higher roles extend lower roles rather than replacing them.

For example:

- a user with **L30 - Orders + Prices** also has the access granted by **L20 - Orders**;
- a user with **L40 - Billing** also has the access granted by **L30 - Orders + Prices**;
- a user with **L80 - Admin** includes all previous rights.

This cumulative model makes it easier to assign access progressively as customers need more visibility in Client Center.

## External access roles

The following table summarizes the access granted by each external role in Client Center.

| Role | Home | Orders | Billing | User Management | Customer Profile | Notes |
|---|---|---|---|---|---|---|
| **L10 - Basic** | ✅ | ❌ | ❌ | ❌ | ✅ | Basic access to the Home page and Customer Profile. |
| **L20 - Orders** | ✅ | ✅ | ❌ | ❌ | ✅ | Access to Orders and New Order, excluding **Price**, **Discount**, and **Amount**. |
| **L30 - Orders + Prices** | ✅ | ✅ | ❌ | ❌ | ✅ | Same as L20, but including **Price**, **Discount**, and **Amount**. |
| **L40 - Billing** | ✅ | ✅ | ✅ | ❌ | ✅ | Adds access to billing-related pages, including **Invoices**, **Due Payments**, and **Payment History**. |
| **L80 - Admin** | ✅ | ✅ | ✅ | ✅ | ✅ | Full access, including **User Management**. |
| **L90 - Owner** | ✅ | ✅ | ✅ | ✅ | ✅ | Same as **Admin**, but Owner access cannot be revoked by anyone, including Admins. |

[screenshot: client-center/concepts/access-model-and-external-roles/cc-concepts-access-model-and-external-roles-02-role-matrix.png]

## What each role changes in practice

The role assigned to the user determines which sections of Client Center are available and how much document detail is visible.

In practice:

- **L10 - Basic** is intended for users who only need general access to the portal and customer information;
- **L20 - Orders** adds access to order-related work, but hides commercial values such as price, discount, and amount;
- **L30 - Orders + Prices** provides access to the full order details;
- **L40 - Billing** adds access to invoice and payment-related information;
- **L80 - Admin** adds the ability to manage other external users in Client Center;
- **L90 - Owner** is the protected top-level role for the customer.

This role-based structure allows organizations to expose only the information appropriate for each external user.

## Customer Profile access

All external roles have access to **Customer Profile**.

Users can view information about their registered company, including company identifiers such as UIN and VAT number.

Additional file-related visibility in Customer Profile depends on both role level and file sharing configuration:

- users with **L40 - Billing** and above can access the dedicated **Files** panel;
- visible files must also be shared for both internal and external users.

For more information, see:

- [Customer information](../customer-profile/concepts/customer-information.md)
- [Files in Customer Profile](../customer-profile/concepts/files-in-customer-profile.md)
- [File visibility and downloads](file-visibility-and-downloads.md)

## User Management access

Only users with **L80 - Admin** or **L90 - Owner** can access **User Management**.

These roles can add users to Client Center and determine the level of access they have for the corresponding customer.

The **Owner** role is special because it cannot be revoked by anyone, including Admins.

For more information, see:

- [Add and manage external users](../user-management/operations/add-and-manage-external-users.md)
- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)

## Days Back Access

In addition to the external role, ERP.net can also restrict how much historical data the user is allowed to see through the **Days Back Access** field.

This field defines the maximum number of past days for which the user can view data, such as sales order records.

If the field is left empty, the system assumes unlimited access to past records within the user's assigned scope.

Days Back Access does not replace the role. It acts as an additional restriction on top of the role-based access model.

[screenshot: client-center/concepts/access-model-and-external-roles/cc-concepts-access-model-and-external-roles-03-external-access-table.png]

## Access is assigned per customer

Because access is defined per user-customer combination, the same user can appear multiple times in the External Access table.

Each record can assign a different role for a different customer.

This is what enables Client Center to support customer-specific access and is also the foundation for multi-customer login.

For more information, see [Multi-customer login](multi-customer-login.md).

## Relationship to Client Center navigation

The role determines which parts of the Client Center navigation are available to the user.

Depending on the assigned role, the user may see only the basic pages, or may also have access to orders, billing information, and user administration.

This is why different users can have different navigation options even when they sign in to the same Client Center.

For more about the structure of the portal, see [Home and navigation](home-and-navigation.md).

## Summary

The Client Center access model is based on **external roles assigned per customer** through the ERP.net **[External Access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html)** table.

This model determines:

- which sections of Client Center the user can access;
- whether order prices and amounts are visible;
- whether billing-related pages are available;
- whether the user can manage other external users;
- how much historical data is visible through **Days Back Access**.

The model is cumulative, customer-specific, and designed to expose only the information appropriate for each external user.
