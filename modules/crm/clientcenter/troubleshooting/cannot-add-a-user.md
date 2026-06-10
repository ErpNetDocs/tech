# Cannot add a user

Use this page when a user cannot be added through the **User Management** page in Client Center.

In Client Center, users with external access role **L80 - Admin** or **L90 - Owner** can add an already registered user to the current customer and assign an external access role.

## Check whether the current user has sufficient rights

The **User Management** page is visible only to Client Center users with external access role **L80 - Admin** and above.

Users with roles **Admin** and **Owner** can add already registered users to the Client Center.

If the current user does not have the required role, the add-user action will not be available.

For more information, see:

- [User Management](../user-management/index.md)
- [Access model and external roles](../concepts/access-model-and-external-roles.md)

## Check whether the user is already registered

Before a user can be added through **User Management**, that user must already be registered.

A user must first create a local account by using the Client Center log-in page and the local account creation form.

Required fields for local account creation are:

- **E-mail**
- **Full Name**
- **Password**

If the user has not created a local account yet, they cannot be added through **User Management**.

For more information, see [How to add new users and manage permissions (v.26)](https://docs.erp.net/tech/modules/crm/clientcenter/how-to/setup-a-new-user-account-v26.html).

## Check whether the correct email address is entered

When adding a user, Client Center requires the user's exact email address.

If no email record is found, Client Center shows an error and the user cannot be added.

Verify that the entered email address exactly matches an already registered local user account.

## Check whether the correct customer is selected

If multiple customers are used, make sure you are logged into the customer whose data you want to share with the user.

User access in Client Center is customer-specific. Adding a user from **User Management** adds that user for the currently selected customer.

If the wrong customer is selected, the intended access assignment will not be created for the correct customer.

For more information, see:

- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)
- [Multi-customer login](../concepts/multi-customer-login.md)

## Check whether the required fields are completed

When adding a user, the following values must be provided:

- the user's exact email address;
- **Days Back Access**;
- **Role**.

The user's name is filled out automatically.

If the required values are not completed correctly, the user assignment cannot be saved.

For more information, see [Add and manage external users](../user-management/operations/add-and-manage-external-users.md).

## Check for configuration-related errors

If Client Center shows an error while adding the user, review whether the relevant Client Center configuration settings are properly applied.

If configuration settings are not properly applied, a respective error message is shown.

For general Client Center error information, see [Error codes](error-codes.md).

## Related pages

- [User Management](../user-management/index.md)
- [Add and manage external users](../user-management/operations/add-and-manage-external-users.md)
- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)
- [Error codes](error-codes.md)
