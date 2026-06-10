# User access and customer assignment

Client Center manages external user access through **customer-specific assignments**.

This means that access is not granted globally to a user account. Instead, access is defined separately for each **user-customer** combination through the ERP.net **External Access** model.

This is the core concept behind User Management in Client Center. When a user is added in the portal, Client Center does not create a general portal role for that person. It creates or updates the access relationship between that user and the currently selected customer.

[screenshot: client-center/user-management/concepts/user-access-and-customer-assignment/cc-user-management-concepts-user-access-and-customer-assignment-01-external-access-overview.png]

## The access assignment model

Client Center uses the ERP.net **External Access** table to store and apply customer-specific access.

Each access assignment defines:

- the **user** account that receives access;
- the **customer** whose data becomes accessible;
- the assigned **external role**;
- the optional **Days Back Access** restriction;
- optional notes or additional assignment context.

Because the assignment is created per customer, the same user can have different access settings for different customers.

For more information about the underlying ERP.net model, see [External Access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html).

## Access is assigned per customer

Customer-specific assignment is one of the most important principles in Client Center.

A user can:

- have access to one customer and no access to another;
- have different external roles for different customers;
- have different **Days Back Access** limits for different customers.

This means that Client Center does not treat access as a single user-level permission set. Instead, it evaluates access according to the currently selected customer and the assignment defined for that exact user-customer pair.

This model allows external access to be precise and controlled, especially when the same person works with several customer accounts.

## Relationship to external roles

Each customer assignment includes an **external role**.

The role determines what the user can see and do for that customer in Client Center. For example, it controls whether the user can:

- access only basic portal information;
- view orders;
- see prices and amounts;
- access billing information;
- manage other external users.

The role is therefore one part of the customer assignment, not a separate global user property.

For more information, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

[screenshot: client-center/user-management/concepts/user-access-and-customer-assignment/cc-user-management-concepts-user-access-and-customer-assignment-02-role-and-customer-assignment.png]

## Relationship to Days Back Access

A customer assignment can also include a **Days Back Access** value.

This value limits how many past days of historical data the user can see for that specific customer. It acts as an additional restriction on top of the assigned external role.

If the field is left empty, the system assumes no explicit historical limit within the assigned scope.

Because this setting belongs to the customer assignment, the same user can have different historical visibility limits for different customers.

## Why an existing user account is required

Client Center assigns access to an existing user account.

This means that a person must already exist as a local user account in ERP.net before that person can be added to a customer through User Management in Client Center.

The portal does not create the base user identity as part of the customer assignment. It uses an existing account and links it to the selected customer with the required access settings.

This is why user administration in Client Center should be understood as **access assignment**, not as full identity creation.

## Relationship to User Management

The **User Management** section is the customer-facing interface for maintaining these customer-specific assignments.

When an authorized user adds or updates a user in Client Center, the portal is effectively managing:

- which existing user account is linked to the selected customer;
- which external role is assigned for that customer;
- whether a **Days Back Access** restriction is applied.

This makes User Management the functional layer, while customer assignment is the underlying access concept.

For task-oriented guidance, see [Add and manage external users](../operations/add-and-manage-external-users.md).

## Relationship to multi-customer login

Customer-specific assignment is also what makes **multi-customer login** possible.

If the same user account is assigned to multiple customers through separate access records, the user can sign in once and then switch between those customer contexts in Client Center.

Each customer context is evaluated separately. This means the same user can receive:

- one role for one customer;
- another role for another customer;
- different historical access limits for each one.

For more information, see [Multi-customer login](../../concepts/multi-customer-login.md).

[screenshot: client-center/user-management/concepts/user-access-and-customer-assignment/cc-user-management-concepts-user-access-and-customer-assignment-03-multi-customer-assignment.png]

## Relationship to page visibility

Customer assignment determines more than whether the user can sign in.

It also determines which parts of Client Center are visible for that customer, including:

- whether **Orders** is available;
- whether prices are visible;
- whether **Billing** is available;
- whether **User Management** is available;
- how much historical data is shown.

This is why the customer assignment should be viewed as the main rule that shapes the user's portal experience for the selected customer.

## Owner and Admin scope

Users with **L80 - Admin** and **L90 - Owner** can manage customer assignments through User Management.

The **Owner** role has special protection. It has the same general access scope as Admin, but Owner access cannot be revoked by Admin users.

This ensures that protected top-level access remains available for the customer even when other external user assignments are being maintained.

## Summary

Client Center manages external access through **customer-specific user assignments**.

Each assignment links an existing user account to a specific customer and defines:

- the external role;
- the customer scope of access;
- the optional **Days Back Access** restriction.

This model allows the same user to have different access levels for different customers and is the basis for both User Management and multi-customer login in Client Center.
