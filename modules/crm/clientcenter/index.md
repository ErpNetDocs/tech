# Client Center

The Client Center allows Erp.Net clients to assist their customers by allowing them to see and create sales orders, review due payments, as well as access and download invoices. It’s best used to provide faster support and increased speed of new orders. 

You can **[build and host](how-to/define-a-new-cc.md)** a CC instance from your global website environment, and access it using a custom relative url.

![picture](pictures/client_center_v26.png)

## Features and structure

Depending on their **assigned role**, users may see and interact with up to **five panels**. 

Each Client Center panel works with accurate and simplified data to implement a seamless platform experience, allowing customers to look at documents important to them **on-demand**.

### Home

This panel offers quick access to **orders** and **invoices**, as well as **due payments**.

It keeps a real-time metric of how many orders and invoices were produced for the current month.

![picture](pictures/home_v26.png)

> [!NOTE]
> 
> As of v.26, the Chat feature of the Home panel is **no longer available**.

### Orders

This panel is responsible for storing existing orders and facilitating the creation of new ones. 

It is comprised of two sections:

* **Orders**
* **New Order** 

### Billing

This panel keeps log of billing-related documents and allows for their close inspection, and in the case of invoices - external downloading.

It is comprised of three sections:

* **Invoices**
* **DuePayments**
* **Payment History**

### User Management

Users with Admin and Owner role access have the ability to manage existing users and add new ones to the current Client Center.

This is achieved through a dedicated **User Management** panel.

![picture](pictures/user_management.png)

### Customer Profile

This is where customers can see more information about their company, including UIN and VAT number.

![picture](pictures/customer_profile.png)

> [!NOTE]
>
> Depending on your business' size and reach, you can create and manage **multiple** Client Centers. <br> <br> This could be useful for departments dealing with unique sets of tasks and issues, as their customized version of the Client Center will remain completely tailored to the users they’re serving.

### Creating sales orders

The Client Center gives users the ability to **[create new sales orders](how-to/create-new-order.md)** with just the click of a button.

This feature is **disabled** by default for security reasons. Access should be granted only when it's necessary.

For more information on how to define and set up Client Center, please refer to our **[step-by-step guides](how-to/index.md)** and the **[JSON settings reference](reference.md)**

### Actions

Users are able to perform a couple of **actions** from within the Client Center to enhance their experience.

- **Additional columns** can be added through the **Column Chooser** to provide more information for due payments, past orders and invoices.

- In the **Orders** panel, already issued sales orders from the Client Center can be **cancelled** before they're finalized.

- Generated invoices for any orders can be downloaded and previewed outside of the platform.

> [!NOTE]
> 
> The screenshots taken for this article are from v.26 of the platform.
