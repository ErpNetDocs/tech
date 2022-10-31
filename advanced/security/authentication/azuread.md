# Azure authentication

ERP.net supports Azure as an authentication provider. There are a couple of Azure and ERP.net settings that should be configured for this authentication method to work.

![picture](./pictures/azure1.png)

### Azure settings

1. Log into your Azure subscription via https://portal.azure.com.

2. Manage Azure Active Directory.

3. Register your application with your Azure Active Directory tenant by clicking **App registrations** -> **Register an application**.

![picture](./pictures/azure2.png)

4. Enter the required details. You can use anything for the name (for example: ERP.net Identity Server). <br> Leave “_Accounts in this organizational directory only (Default Directory only - Single tenant)_” checked.

5. In the Redirect URI field enter the callback path configured in IdentityServer4 for Azure AD auth. <br>
This will be **https://`<UIN>`.my.erp.net/id/signin-aad**, where:

- ``<UIN>`` is the ERP.net unique instance name
- ``/id`` is the relative path of the ID site
- ``/signin-aad`` is the endpoint responsible for AZURE AD redirects (/signin-aad is constant for all databases)

6. In the “_Select a platform_” drop-down menu, select Web.

![picture](./pictures/azure3.png)

7. Confirm the app registration creation by clicking **Register**.

8. Now, you have a new app registration. Navigate to “_App registrations_” and open your new app.

![picture](./pictures/azure4.png)

9. Make a note of your Application (client) ID and Directory (tenant) ID values - they should be copied in the corresponding fields in the Sec_Domain_Providers table.

![picture](./pictures/azure5.png)

10. Open “_Authentication_”, located in the left pane. <br>

If you have to add more redirect URIs (in case you have more than one instance of @@erpnet application server), you can add them via the “_Redirect URIs_” panel, by clicking **Add URI**. <br>

Additionally, check the ID tokens checkbox.

![picture](./pictures/azure6.png)

11. Finally, save your changes.

### ERP.net settings

1. In the "Setup / Security / Domains" section a "Domain providers" record should be created. <br>
There is a default domain in the databases and the Azure record should be added there.
 
![picture](./pictures/azure7.png) 

2. The users are referenced by their email:
 
![picture](./pictures/azure8.png)

3. There should be a license **SEC01 - Security - Sign in with Azure AD**