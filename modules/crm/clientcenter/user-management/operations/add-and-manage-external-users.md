# Add and manage external users

Use this procedure to add external users for the currently selected customer and manage their access in Client Center.

This operation is available only to users with **L80 - Admin** or **L90 - Owner** access.

User Management in Client Center works with customer-specific access. This means that the operation does not assign a global role to the user account. Instead, it creates or updates the access relationship between the user and the currently selected customer.

[screenshot: client-center/user-management/operations/add-and-manage-external-users/cc-user-management-operations-add-and-manage-external-users-01-user-management-overview.png]

## Before you begin

Make sure that:

- the user performing the operation has access to **User Management**;
- the correct customer is selected when the user has access to multiple customers;
- the external user account already exists as a local account in ERP.net.

If the external user account does not already exist, it must be created before it can be assigned to the customer in Client Center.

For more information, see:

- [User Management overview](../index.md)
- [User access and customer assignment](../concepts/user-access-and-customer-assignment.md)
- [Access model and external roles](../../concepts/access-model-and-external-roles.md)
- [Multi-customer login](../../concepts/multi-customer-login.md)

## Add an external user

### 1. Open User Management

Open **User Management** for the current customer.

The page shows the users who already have external access for that customer.

[screenshot: client-center/user-management/operations/add-and-manage-external-users/cc-user-management-operations-add-and-manage-external-users-02-open-user-management.png]

### 2. Start the add user action

Select **Add User**.

Client Center opens the user assignment flow for the current customer.

### 3. Enter the user email

Enter the email address of the user that you want to add.

The email must belong to an existing local user account in ERP.net. If the email is not found, the user cannot be added through Client Center.

### 4. Assign the external role

Select the external role that will define the user's access level for the current customer.

The available role levels determine what the user will be allowed to see and do in Client Center.

For more information about the role levels, see [Access model and external roles](../../concepts/access-model-and-external-roles.md).

### 5. Set Days Back Access if needed

If required, enter a value in **Days Back Access**.

This value limits how many past days of historical data the user can see for the selected customer.

If the field is left empty, the system assumes no explicit historical limit within the user's assigned scope.

### 6. Save the user assignment

Save the user assignment.

After the assignment is saved, the user receives external access for the current customer according to the selected role and any defined restrictions.

[screenshot: client-center/user-management/operations/add-and-manage-external-users/cc-user-management-operations-add-and-manage-external-users-03-add-user-form.png]

## Manage an existing external user

The User Management page can also be used to maintain users who are already assigned to the current customer.

Depending on the available actions, authorized users can review and update the access settings of existing external users, such as:

- the assigned external role;
- the **Days Back Access** limit;
- the customer-specific access assignment itself.

This allows customer administrators to keep the list of external users and their access levels up to date directly in Client Center.

## Owner and Admin behavior

Users with **L80 - Admin** and **L90 - Owner** can manage external users, but the **Owner** role has special protection.

The Owner has the same general access scope as Admin, but Owner access cannot be revoked by Admin users.

This ensures that the customer always retains protected top-level access to Client Center administration.

## Result

After the assignment is saved:

- the user is added to the current customer's external access list;
- the assigned role determines what the user can access in Client Center;
- any defined **Days Back Access** restriction is applied for that customer;
- if the same user is also assigned to other customers, the user can work with those customers according to the corresponding customer-specific assignments.

## If the user cannot be added

If the user cannot be added, common reasons include:

- the email address does not belong to an existing local user account;
- the current user does not have sufficient rights to manage users;
- the selected customer context is not the intended one.

For more information, see:

- [Cannot add a user](../../troubleshooting/cannot-add-a-user.md)
- [User access and customer assignment](../concepts/user-access-and-customer-assignment.md)

## Related information

- [User Management overview](../index.md)
- [User access and customer assignment](../concepts/user-access-and-customer-assignment.md)
- [Access model and external roles](../../concepts/access-model-and-external-roles.md)
- [Multi-customer login](../../concepts/multi-customer-login.md)
