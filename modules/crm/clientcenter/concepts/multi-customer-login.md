# Multi-customer login

A single user can have access to more than one customer in Client Center.

This is controlled through the user's [External Access](../../sales/customers/external-access.md) records in ERP.net.

To give a user access to more than one customer, create an external access record for each customer.

## Example

| User | Customer | Role | Notes |
|---|---|---|---|
| John | Nimero Ltd | L40 - Billing | Access to billing-related data. |
| John | Olivia-Green | L30 - Orders + Prices | Full access to Orders. |


When the same user is granted access to multiple customers, they can switch between them and work with each customer's data according to the assigned external access role.

<!-- Screenshot needed: cc-con-01-multi-customer-switch.png -->

If multiple customers are detected for the same user, upon first-time login, the user will be asked to select a customer they wish to log into.


For more information about external access roles, see [External Access](../../sales/customers/external-access.md#roles).

For more information about assigning users in Client Center, see [Add your first external user](../getting-started/add-your-first-external-user.md) and [Add and manage external users](../user-management/operations/add-and-manage-external-users.md).
