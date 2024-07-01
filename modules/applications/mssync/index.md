# Overview

MsSync is a website application designed to synchronize resources between **ERP.net** and **Office 365**. 

Each synchronization task is referred to as a **job**, allowing resources created in **Office 365** to be automatically reflected in the corresponding module in **ERP.net**, and the other way around.

An example of such a job is the **[Calendar](https://docs.erp.net/webclient/introduction/my-apps/calendar.html)**. 

![picture](pictures/Overview_view_nohighlights_01_03.png)
 
### Getting Started

First, you need to make sure that your organization uses **[Azure Athentication](advanced/security/authentication/azuread.md)** and that the organization's **[domain](/advanced/security/authentication/azuread.md#erpnet-settings)** is set up in ERP.NET.


Second, an ERP.net admin needs to login to **MSSync** and grant access to your domain using the **[Service](tech/modules/applications/mssync/service.md)**


Then, as a final step, each user that wants to use the synchronization must sign in **MSSync** to activate it. 

To access **MSSync**, it’s mandatory to sign in using the **'Sign in with Microsoft'** button with the **Microsoft account** provided by your organization. 

To establish the link, you will need to **read** and **accept** the permissions MSSync needs to obtain.

![picture](pictures/Overview_permission_01_03.png)
 
If you use local **ERP** credentials to log in, **MsSync** will still open, but will essentially deny you any kind of access to its resources. 

![picture](pictures/Overview_error_01_03.png)

> [!WARNING]
> 
> You must log in via an existing **Microsoft account** in order to reference your **Outlook** calendar. Otherwise, **MSSync** would be unable to determine which calendar to link to.

Then select your default enterprise company, location, and time zone and activate the desired synchronizations using the **[Setup](https://docs.erp.net/tech/modules/applications/mssync/setup.html)** menu.
 
## Main menu

The **MSSync** app consists of **three** sections: 

-	**[Home](https://docs.erp.net/tech/modules/applications/mssync/home.html)**
-	**[Setup](https://docs.erp.net/tech/modules/applications/mssync/setup.html)**
-	**[Service](https://docs.erp.net/tech/modules/applications/mssync/setup.html)**

In **Home**, you'll find personal profile details, general information about the current **state** of your application, as well as the latest **log data** for your activated sync jobs.

![picture](pictures/Overview_home_cropepd_01_03.png) 

In **Setup**, you can see information about your **enterprise company** - the one that is currently linked to **MSSync**. 

Additionally, you can toggle synchronization for a specific sync job **on** or **off**.

 ![picture](pictures/Overview_setup_01_03.png)

The **Service** section is meant for users with administrator access levels. It reveals more technical and sensitive details used in the communication between **MSSync** and **Office365**.

From here, admins can securely connect their **MSSync** instance to their **Microsoft Entra ID**. This is essential for activating all synchronization-related functionalities. 

![picture](pictures/Overview_service_01_03.png)

For more information about navigating, setting up, and configuring MsSync, see:

*	**[Home](https://docs.erp.net/tech/modules/applications/mssync/home.html)**
*	**[Setup](https://docs.erp.net/tech/modules/applications/mssync/setup.html)**
* **[Service](https://docs.erp.net/tech/modules/applications/mssync/setup.html)**

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.


