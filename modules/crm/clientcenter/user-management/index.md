# User Management

The **User Management** section in Client Center allows authorized external users to add and manage other external users for the currently selected customer.

This section is intended for customer-side administration of external access. It allows users with sufficiently high access rights to control who can enter the Client Center and what level of access each external user has for that customer.

[screenshot: client-center/user-management/cc-user-management-overview-01-user-management-section.png]

## What users can do in User Management

In the User Management section, authorized users can typically:

- add a new external user for the current customer;
- assign an external role to that user;
- define a **Days Back Access** limit, when needed;
- review the list of existing external users for the customer;
- manage existing user access assignments.

These actions allow the customer to maintain external access directly in Client Center without working in ERP.net.

For more information about the access model behind this functionality, see [Access model and external roles](../concepts/access-model-and-external-roles.md).

## Role-based visibility in User Management

Access to User Management is role-based.

Only users with **L80 - Admin** or **L90 - Owner** can access this section.

Lower roles do not have access to user administration.

The **Owner** role has the same general access scope as **Admin**, but it is protected and cannot be revoked by Admin users.

For more information, see [Access model and external roles](../concepts/access-model-and-external-roles.md).

## User Management and customer-specific access

User Management always works in the context of the currently selected customer.

This is important because external access in Client Center is assigned **per customer**, not globally per user. A user can have access to one customer and no access to another, or different access levels for different customers.

The User Management section therefore manages the relationship between:

- the external user account;
- the selected customer;
- the assigned external role;
- the optional **Days Back Access** restriction.

For more information, see [User access and customer assignment](concepts/user-access-and-customer-assignment.md).

[screenshot: client-center/user-management/cc-user-management-overview-02-user-management-list.png]

## Adding and managing users

The User Management section combines two related activities:

- adding a new external user to the current customer;
- maintaining the access settings of users who are already assigned to that customer.

This includes assigning or changing the user's role and controlling how much historical data the user is allowed to see.

For task-oriented guidance, see [Add and manage external users](operations/add-and-manage-external-users.md).

## Relationship to multi-customer access

Because external access is customer-specific, the same person can be assigned to more than one customer.

This is what makes **multi-customer login** possible in Client Center. A single user account can be linked to several customers through separate access records, each with its own role and restrictions.

For more information, see [Multi-customer login](../concepts/multi-customer-login.md).

## In this section

### Operations

Use the Operations pages for task-oriented guidance:

- [Operations overview](operations/index.md)
- [Add and manage external users](operations/add-and-manage-external-users.md)

### Concepts

Use the Concepts pages to understand how User Management works:

- [Concepts overview](concepts/index.md)
- [User access and customer assignment](concepts/user-access-and-customer-assignment.md)

## Related sections

- [Getting Started](../getting-started/index.md)
- [Access model and external roles](../concepts/access-model-and-external-roles.md)
- [Multi-customer login](../concepts/multi-customer-login.md)
- [Troubleshooting](../troubleshooting/index.md)

## Summary

The User Management section allows authorized external users to manage Client Center access for the current customer.

It is available only to users with **Admin** or **Owner** access and is used to assign external roles, control customer-specific access, and maintain external user assignments directly in Client Center.
