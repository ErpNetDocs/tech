# How to define a user of a Client Center

This article provides a step-by-step guide on defining a new user and configuring their access to a Client Center website.

If you haven't created such a website already, please refer to **[this guide](define-a-new-cc.md)**.

### Prerequisites

Before a user can be granted access to a Client Center by an administrator, they must first have issued a request for a **local account**. 

Required fields are **Е-mail**, **Full Name**, and **Password**.

![picture](pictures/Setup_user_account_02_04.png)

## Set up a user account 

Once a customer has sent a request for an account, they will appear as an **External Community User** which you can begin to configure.

1. Navigate to the **Users** panel within the **[Security](/modules/system/security/index.md)** section of the **Setup** module.

2. Upon accessing the navigator, locate the user account and click on the **Edit** button located to the left of its **Login** details.

   ![picture](pictures/Setup_User_table_02_04.png)

3. Assign a **person** to the user. If such hasn't already been registered on the platform, you can create a new one on the spot.
   
   Either right-click on the **Person** field or click the **three-dot button**.

   In both cases, this will expand a dropdown menu where you need to select **Create new**.
   
   ![picture](pictures/Setup_user_create_person_01_04.png)

   You will be redirected to a separate form for the creation of a new person.

   There are three critical fields: **First Name**, **Last Name** and **Parent Party**.

   ![picture](pictures/Setup_user_create_person_fields_01_04.png)

4. Click on **Save and reload** to finish creating the new person.
   
   You will be brought back to the user definition form. Click on **Save and reload** again to apply all settings.

5. Make sure that the **Parent Party** of the **Person** (the one in which they are employed) is a customer of the current **Enterprise Company**.
   
   To do so, open it from the **Person** form and locate its **Customers** panel. If it's not visible, add it through the **Customize form** option.

   In the **Customers** panel, verify that two fields are filled:

   * **Enterprise Company** - the Parent Party is a customer of this company, for which the Client Center is created.

   * **Serviced By Enterprise Company Location** - the respective Enterprise Company must be serviced by a particular location.

   ![picture](pictures/customer.png)

6. Click on **Save and reload** to apply your changes.

7. Define the appropriate level of **[external access](/modules/crm/sales/customers/external-access.md)** for the user.

   This is necessary for them to be able to see the kind of documents and information suitable for their role in your organization.

   ![picture](pictures/external_access.png)

> [!Warning]
> If any of the user configuration settings are not properly applied, a respective **[error message](https://docs.erp.net/tech/modules/crm/clientcenter/reference.html#error-exception-codes)** will be shown. 

> [!TIP]
> If you've passed all the steps successfully, you may proceed to **[apply platform settings](apply-platform-settings.md)**. <br><br>

> [!NOTE]
> 
> The screenshots taken for this article are from v24 and v26 of the platform.
