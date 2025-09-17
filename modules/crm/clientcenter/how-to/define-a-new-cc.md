# How to set up a Client Center

This article provides a step-by-step guide on creating a Client Center website through @@name.

> [!WARNING]
> The information presented is relevant for **@@name version 24**. <br>
> As of **@@name version 26**, website configuration takes place under **System** -> **Configuration** -> **Web Sites**.

### Prerequisites 

To set up a website of **Client Center** type, navigate to the **Web Sites** panel within the **Core** section of the **Setup** module.

> [!NOTE]
> 
> You can observe and restart all sites through the **Instance Manager**.

### Website definition

Upon accessing the **New Web Site** form, you need to enter relevant data into the provided fields.

![picture](pictures/New_Web_Site_01_04.png)
 
1. The only mandatory field is **Web Site Type**. In this case, it should be set to **Client Center**. 

2. Make sure you've selected the appropriate **Enterprise Company**. 

3. Additionally, you may change the **Relative Url** of the website, which is set to "cc" by default. 

> [!NOTE]
> 
> You should define a distinct site with a unique **Relative URL** or **Host** for each **Enterprise Company**.

4. It's necessary to create a **trusted application** to ensure the security and integrity of the new website.
   
   To do so, click on **Run**, select the **Create/Update Trusted Application** option, and confirm with **OK**.

   ![picture](pictures/Create_Update_Trusted_app_01_04.png)

5. Once you complete this step, hit **Save and reload**.
   
   The new Client Center website will be created and you can access its internal application details through the form.

   ![picture](pictures/Trusted_app_open_01_04.png)

If you've passed all the steps successfully, you may proceed to **[define users](https://docs.erp.net/tech/modules/crm/clientcenter/how-to/setup-a-new-user-account-v26.html)** who can access the Client Center.

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.
