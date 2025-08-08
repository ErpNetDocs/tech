# User Management 

The User Management page is an administrative hub for a customer's users in the **Client Center**. It complements the **[standard way of setting up external customer access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html)** by allowing individual users to be managed so that each sees exactly what they need once they log into the platform. 

The page is visible to all Client Center users with **[external access role](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html#roles)** **L80 - Admin** and above.

![pictures](pictures/user_management_page.png)

### Details

You can find the following information about each user in the table:

* **User** -  Name of the user in the format {Name} <{Login}> [{UserType:DB}] as defined in **[Systems.Security.Users](https://docs.erp.net/model/entities/Systems.Security.Users.html)**.
* **Role** - **[External access role](../index.md#role-based-access)** of the user. Each superior role includes the rights granted by roles with fewer permissions.
* **Access Back (days)** - The maximum number of past days the user is allowed to view data to which their role grants them access.
* **Notes** - Optional notes for the user.

## Add user

Admins and Owners can add any already registered user from within their customer's organization into the Client Center.

1. To begin, click **Add User**.
   
   ![pictures](pictures/user_management_adduser.png)
   
2. This will trigger a window where you need to provide the user's email address.

   ![pictures](pictures/user_add.png)

   If no email record is found, you will get an **error**.

   ![pictures](pictures/user_management_error.png)

3. Proceed to fill out necessary **Days Back Access** and **Role** fields. The name will be filled out automatically.

   When done, click **Save**.

   ![pictures](pictures/user_fields.png)

   The new user will be added to the table.

### Actions

You can change any of the details of an existing user with the help of the **Edit button**.

Alternatively, you may **remove** a user's access to the Client Center with the **Delete button**.

![pictures](pictures/user_actions.png)

This action will only revoke the external access, not delete the actual user.

![pictures](pictures/user_delete_warning.png)
