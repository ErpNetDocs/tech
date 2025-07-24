# External Access

The **External Access** table is responsible for granting external and internal users permissions to **specific customer data**.

In the case of the **[Client Center](/modules/crm/clientcenter/index.md)**, it allows customers' individual users to see exactly what they need once they log into the platform. 

![pictures](pictures/customers_external_access.png)

### Columns

The table consists of the following columns:

- **Customer** - The customer whose data will be accessed.
- **User** - The user to whom the access will be granted.
- **Role** - The role of the user, which defines the level of granted access.
- **Days Back Access** - The maximum number of past days the user is allowed to view data (e.g. sales order records).
  
  If left empty, it assumes unlimited.

- **Notes** - Optional notes for the external access.

### Roles

A user can be assigned one of 6 different roles for external customer access. 

Each subsequent role in the list below also includes the rights granted by the previous.

1. **L10 - Basic** - Provides basic access.
2. **L20 - Orders** - Grants access to sales orders, excluding Price, Discount and Amount. 
3. **L30 - Orders with Prices** - Provides access to sales orders and all of their details.
4. **L40 - Billing** - Gives access to billing-related documents, such as due payments, invoices and payment history.
5. **L80 - Admin** - Ensures full access to all customer data. 
6. **L90 - Owner** - The same as Admin. Once assigned, Owner access cannot be revoked by anyone, including Admins.

## Grant access

To give external access to a user, you need to insert them as a new entry into the table and fill out the respective fields.

The user must already be registered and prepared for the Client Center. You can learn more about this setup process **[here](/modules/crm/clientcenter/how-to/setup-a-new-user-account.md)**.

![pictures](pictures/grant_new_access.png)

Once saved, a user's external access settings can always be changed later.

> [!NOTE]
> 
> The screenshots taken for this article are from v26 of the platform.
