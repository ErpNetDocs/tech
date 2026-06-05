# Access model and external roles

Individual access to Client Center is determined by the user's external access role.

External access roles are assigned in ERP.net through the **External Access** navigator.

For more information, see [External Access](../../sales/customers/external-access.md#roles).

Each subsequent role in the table below also includes the rights granted by the previous.

## Role-based access

| Role | Home | Orders | Billing | User Management | Customer Information | Notes |
|---|---|---|---|---|---|---|
| **L10 - Basic** | ✅ | ❌ | ❌ | ❌ | ✅ | Basic access to the **Home** and **Customer Profile** pages. |
| **L20 - Orders** | ✅ | ✅ | ❌ | ❌ | ✅ | Access to [Orders](../orders/index.md), excluding Price, Discount, and Amount. |
| **L30 - Orders + Prices** | ✅ | ✅ | ❌ | ❌ | ✅ | Like **L20 - Orders**, but including Price, Discount, and Amount. |
| **L40 - Billing** | ✅ | ✅ | ✅ | ❌ | ✅ | Adds access to [Invoices](../billing/concepts/invoices-page.md), [Due Payments](../billing/concepts/due-payments-page.md), and [Payment History](../billing/concepts/payment-history-page.md). |
| **L80 - Admin** | ✅ | ✅ | ✅ | ✅ | ✅ | Full access, including to [User Management](../user-management/index.md). |
| **L90 - Owner** | ✅ | ✅ | ✅ | ✅ | ✅ | Same as Admin, but Owner access cannot be revoked by anyone, including Admins. |

> [!NOTE]
> Any registered user can be added to a Client Center by another user with external access role **Admin** and above.
>
> To see how users are managed in Client Center, see [Add and manage external users](../user-management/operations/add-and-manage-external-users.md).

## Using Owner and Admin roles

Use **L90 - Owner** for the ERP.net administrator or the main internal person responsible for the Client Center.

A user with role **L90 - Owner** cannot be edited in Client Center.

For external users who need to manage other users in Client Center, use **L80 - Admin** instead of **L90 - Owner**.
