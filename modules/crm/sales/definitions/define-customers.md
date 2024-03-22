# Customer definition

For the purposes of creating a sales order, you must define and manage **customers** to whom you'll be selling your products. 

This involves adding various details about them which you can later make use of while creating the order.

Below is a step-by-step guide on how to define customers and configure their settings.

### Navigation

From the **[CRM](https://docs.erp.net/tech/modules/crm/index.html)** module, click on **[Common](https://docs.erp.net/tech/modules/crm/crm-common/index.html)**. 

There, you'll find the **Customers** panel, where you can view all of the customers you have created, with details about each.

![Pictures](pictures/Customer_view_27_02.png)
 
## Set up 

Before you can actually create a customer, it's necessary to set up a **[party](https://docs.erp.net/tech/concepts/parties-concepts.html?q=party)**, representing an entity not yet designated as a customer but recognized by the system as an entitiy that participates in business relations or transactions.

Prior to customer creation, you can also consider adding a **customer type**, which can help organize customers based on common characteristics.

> [!NOTE]
> 
> The type you define can impact the customer creation process, potentially adding different fields for you to fill out.

## Create a customer 

There are **two** ways to create a customer,  both ensuring consistency in the final result when selecting the same customer type.

1. Navigate to the **Create** section within the **Customers** panel. Here, you'll find a list of various **customer types**.

   Upon selecting the respective type, a separate window will open, automatically reflecting the chosen customer type.

   You can proceed with the creation process by filling out the rest of the details.

![Pictures](pictures/Customer_Create_section_27_02.png)
 
2. Use the **New** button found above the **Customers** list. Upon clicking this button, you can select a **customer type** from a dropdown menu.
  
   Then, you will be taken to the standard customer creation form and proceed to add the necessary details.

![Pictures](pictures/Customer_create_new_button_27_02.png)

### New customer details
 
Once you access the **New Customer** window, you can start adding all the necessary details for your customer.

Most of the fields are optional. However, whatever information you provide at this point will simplify the process of creating a sales order document later, as it will **automatically** be added in the order creation form.

![Pictures](pictures/Customer_New_window_27_02.png)
 
The only mandatory field is **Party**. 

![Pictures](pictures/Customer_party_27_02.png)

Once you've filled out all the desired fields, click the **Save and reload** button to complete the creation of the new customer.

![Pictures](pictures/Customer_Save_and_reload_27_02.png)
 
#### Most common fields 

Here's a summary of commonly used fields, along with those less frequently utilized:

•	**Party** – In this field, select a party that you wish to designate as a customer.

•	**Active** – This checkbox allows you to **enable** or **disable** a customer. When unchecked, the customer will no longer be visible in various places on the platform.

•	**Date** – You can specify the start and end dates of the sales contract using the **From Date** and **Thru Date** fields.

•	**Credit Limit**– If a sale has been made for a certain amount but payment has not been issued, the system will notify you that the customer has exceeded their credit limit.

•	**Customer Status** – You have two options for selling:

If you're shipping directly to the customer that placed the order, check the **Allow Use As Primary Customer** box. 

If you've made a sale to one customer but are shipping products to another, check the **Allow Use As Ship To Customer** box.

> [!NOTE]
> 
> The **Credit Limit** field value can be overridden by authorized users.

#### Assign defaults 

Fields starting with "Default" allow you to specify template information for customers. 

For example, if the **Default Currency** is set to BGN, all sales with that customer will be automatically conducted in that currency. 

> [!NOTE]
> 
> You have the ability to **modify** each default value when creating the sales order itself.
