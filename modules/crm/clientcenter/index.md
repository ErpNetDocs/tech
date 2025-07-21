# Client Center

The Client Center allows Erp.Net clients to assist their **[customers](/modules/crm/sales/customers/index.md)** by allowing them to see and create sales orders, review due payments, as well as access and download invoices. It’s best used to provide faster support and increased speed of new orders. 

You can **[build and host](how-to/define-a-new-cc.md)** a CC instance from your global website environment, and access it using a custom relative url.

![picture](pictures/client_center_v26.png)

## Structure

The Client Center has a hierarchical menu structure consisting of several **sections** and **pages**. Each works with accurate and simplified data to implement a seamless platform experience, allowing customers to look at documents important to them **on-demand**.

> [!Important]
>
> User access to the Client Center is determined through **external access roles**. You can learn more about them **[below](index.md#role-based-access)**.

### Home

This is the default landing page of the Client Center, offering quick access to all **orders**, **invoices**, and **due payments**.

It also keeps a real-time metric of how many orders and invoices were produced for the current month.

![picture](pictures/home_v26.png)

> [!Warning]
> 
> As of v.26, the Chat integration is **no longer available**.

### Orders

This section is responsible for storing existing orders and facilitating the creation of new ones. 

It is comprised of two pages:

* **[Orders](orders/index.md)**
* **[New Order](orders/new-order.md)**

> [!NOTE]
> 
> The New Order page is **disabled** by default for security reasons. <br>
> For more information on how to enable it, please refer to our **[step-by-step guides](how-to/index.md)** and the **[Settings and error reference](reference.md)**

### Billing

This section keeps a log of billing-related documents and allows for their close inspection.

It is comprised of three pages:

* **[Invoices](billing/invoices.md)**
* **[DuePayments](billing/duepayments.md)**
* **Payment History**

### [User Management](user-management/index.md)

This page is for managing the customer's existing users by determining the level of access they have to the Client Center.

It further allows the removal of existing users and addition of new ones.

![picture](pictures/user_management.png)

### Customer Profile

This page is where customers can see more information about their registered company, including UIN and VAT number.

![picture](pictures/customer_profile.png)

> [!Tip]
>
> Depending on your business' size and reach, you can create and manage **multiple** Client Centers. <br> <br> This could be useful for departments dealing with unique sets of tasks and issues, as their customized version of the Client Center will remain completely tailored to the users they’re serving.

## Role-based access 

Individual access to Client Center sections is determined strictly based on the **[external access role](../sales/customers/external-access.md#roles)** a user is assigned.

Each subsequent role in the table below also includes the rights granted by the previous.

| Role                   | Home | Orders              | Billing              | User Management | Customer Information | Notes                                                                                   |
|-------------------------|------|----------------------|----------------------|------------------|------------------------|-----------------------------------------------------------------------------------------|
| **L10 - Basic**         | ✅   | ❌                   | ❌                   | ❌               | ✅                     | Basic access.                           |
| **L20 - Orders**        | ✅   | ✅        | ❌                   | ❌               | ✅                     | Access to **Orders** without price data.                                                    |
| **L30 - Orders + Prices** | ✅ | ✅      | ❌                   | ❌               | ✅                     | Access to **Orders**, including price details.                                       |
| **L40 - Billing**       | ✅   | ✅      | ✅                   | ❌               | ✅                     | Adds access to **Invoices**, **DuePayments**, and **Payment History**.                  |
| **L80 - Admin**         | ✅   | ✅      | ✅                   | ✅               | ✅                     | Full access, including to **User Management**.                                                 |
| **L90 - Owner**         | ✅   | ✅      | ✅                   | ✅               | ✅                     | Same as Admin, but Owner access **cannot** be revoked by anyone, including Admins.      |


## Features

Users can perform a couple of actions from within the Client Center:

- Customize a page's layout with **[Grid Control](grid-control.md)** capabilities

- **Cancel** already issued sales orders before they're finalized.

- **Download** invoices to preview them outside of the Client Center.

> [!NOTE]
> 
> The screenshots taken for this article are from v.26 of the platform.
