# Add your first external user

This article describes how to add the first external user to a Client Center.

If you have not created a Client Center website yet, first complete [Set up a Client Center](set-up-a-client-center.md).

For the internal ERP.net administrator who will administer the Client Center, see [Grant administrator access](grant-administrator-access.md).

## Create a local account

Before a user can be given access to a Client Center, they must first create a local account.

The local account creation form is available on the Client Center sign-in page.

The required fields are:

- **Email**
- **Full Name**
- **Password**

<!-- Screenshot needed: Client Center sign-in page with the local account creation form -->

## Set up access for the first external user

Access for the first external user is assigned in ERP.net through the **External Access** navigator.

For more information about external access roles, see [External Access](../../sales/customers/external-access.md).

Open the **External Access** navigator and create or edit the record for the customer and user who will use the Client Center.

Assign the user the **L80 - Admin** external access role.

This gives the user access to the Client Center and allows them to manage other users through the **User Management** page.

<!-- Screenshot needed: External Access record with role L80 - Admin -->

> [!IMPORTANT]
> If this step is omitted, the user will receive a lack-of-access error message when trying to sign in.

## Add other users in Client Center

After the first external user has been given **L80 - Admin** access, they can add other users through the **User Management** page in Client Center.

If you use multiple customers, first switch to the customer whose data you want to share with the user.

Then:

1. Open the **User Management** page.
2. Click **Add User**.
3. Enter the exact email address of the user.
4. Enter a value in **Days Back Access**.
5. Select the external access role to assign to the user.
6. Save the changes.

**Days Back Access** defines the maximum number of days in the past for which the user is allowed to view data.

The new user can then sign in with their credentials and start using the Client Center.

<!-- Screenshot needed: Add User form with Email, Days Back Access, and external access role -->

> [!IMPORTANT]
> To give the same user access to more of your customers, switch to another customer and repeat the steps above.

## Related information

For more information about user administration in Client Center, see [User Management](../user-management/index.md).
