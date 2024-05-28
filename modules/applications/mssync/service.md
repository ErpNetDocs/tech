# Service 

The **Service** section is exclusively for **ERP.net** admins. 

Here, they can request permissions for accessing **Office365** resources from an admin within their **enterprise company**. 

These permissions are essential for enabling synchronization between the company's **Office365** account and the **ERP.net Web Client**. 

 ![picture](pictures/Service_view_01_03.png)

### State 

In the **Service** section, you'll find the current **state** of the MsSync app.

There are also **logs** detailing all state changes, similar to those found in the **[Setup](https://docs.erp.net/tech/modules/applications/mssync/setup.html)** section. 
 
### Information panel 

This panel stores details about the **Operation mode** of the app, and reveals the **Client Id**, and **Tenant Id**, which play a role in establishing the two-way synchronization process.

![picture](pictures/Service_information_01_03.png)
 
## Connect to Microsoft Entra ID 

This button sends a request on behalf of ERP.net to access resources already available in your **Office365** account. 

![picture](pictures/Service_connect_01_03.png)

This permission not only enables modifications to existing resources but also allows the inclusion of new ones. 

Any changes made to resources in **ERP.net** are mirrored in **Office365**, and vice versa. 

![picture](pictures/Service_permission_01_03.png) 

## Give permissions

The "Give Permissions" ensures that the MsSync app has all the necessary permissions to function optimally. It's recommended that **an admin user** click the "Give Permissions" button after the very first start of the app. This action will automatically check and configure all required permissions specific to the various job types.

This process is essential for activating all available features and ensuring a seamless user experience.

![picture](pictures/service-give-permissions.png)

--

> [!NOTE]
> The screenshots taken for this article are from v24 of the platform.
