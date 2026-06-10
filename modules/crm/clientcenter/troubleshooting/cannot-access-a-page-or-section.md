# Cannot access a page or section

Use this page when a user cannot open a section or page in Client Center, or when a page is missing from the available navigation.

In most cases, this is caused by one of the following:

- the user's assigned external role does not include access to that section;
- the user is not correctly associated with the customer in ERP.net;
- the logged-in user does not have a defined role;
- the Client Center user setup is incomplete.

## Check the user's external role

Access to Client Center sections is determined through **external access roles**.

Each subsequent role includes the rights granted by the previous one.

The following table summarizes the role-based access described in the Client Center documentation:

| Role | Home | Orders | Billing | User Management | Customer Information | Notes |
|---|---|---|---|---|---|---|
| **L10 - Basic** | ✅ | ❌ | ❌ | ❌ | ✅ | Basic access to the Home and Customer Profile pages. |
| **L20 - Orders** | ✅ | ✅ | ❌ | ❌ | ✅ | Access to Orders and New Order, excluding Price, Discount and Amount. |
| **L30 - Orders + Prices** | ✅ | ✅ | ❌ | ❌ | ✅ | Like L20 Orders, but including Price, Discount and Amount. |
| **L40 - Billing** | ✅ | ✅ | ✅ | ❌ | ✅ | Adds access to Invoices, Due Payments, and Payment History. |
| **L80 - Admin** | ✅ | ✅ | ✅ | ✅ | ✅ | Full access, including to User Management. |
| **L90 - Owner** | ✅ | ✅ | ✅ | ✅ | ✅ | Same as Admin, but the Owner role cannot be modified or removed by Admins. |

If the user's role is too low for the requested section, the page will not be available.

For more information, see [Access model and external roles](../concepts/access-model-and-external-roles.md).

## Check whether the user has a defined role

If Client Center shows error **CC010**, the logged-in user does not have a defined role.

According to the reference documentation, the resolution is:

- add the user to the `Crm_Customer_External_Access` table;
- assign an appropriate role.

For more information, see [Error codes](error-codes.md).

## Check whether the user is associated with the customer

Client Center uses the ERP.net **External Access** table to determine what type of access a user has to a particular customer.

If the user is not correctly associated with the customer, Client Center access may fail.

The following error codes from the reference documentation are related to user and customer setup:

| Error code | Meaning |
|---|---|
| **CC002** | The logged user is not defined as a Person. |
| **CC003** | Parent party of the logged user is empty. |
| **CC004** | The parent party is not defined as a customer. |
| **CC006** | The parent party does not have customer agreement for the enterprise company of the Client Center. |
| **CC007** | `ServicedByEnterpriseCompanyLocation` is null. |
| **CC010** | The logged-in user does not have a defined role. |

If one of these errors appears, review the user and customer setup in ERP.net.

> [!NOTE]
> Although **CC002** is still listed in the Client Center error reference, starting with version 26 it is no longer generally required for the logged user to be linked to a **Person** record.

For more information, see:

- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)
- [External Access](https://docs.erp.net/tech/modules/crm/sales/customers/external-access.html)
- [Error codes](error-codes.md)

## Check the current customer context

Client Center supports multi-customer login.

If the user has access to more than one customer, the available information and access depend on the currently selected customer.

If the expected section is missing, verify that the user is working in the intended customer context.

For more information, see [Multi-customer login](../concepts/multi-customer-login.md).

## Related pages

- [Error codes](error-codes.md)
- [Access model and external roles](../concepts/access-model-and-external-roles.md)
- [User access and customer assignment](../user-management/concepts/user-access-and-customer-assignment.md)
- [Multi-customer login](../concepts/multi-customer-login.md)
