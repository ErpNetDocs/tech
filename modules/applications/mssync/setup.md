# Setup

Within this section, you can find data about your default **enterprise company** - the one logged in MsSync, which includes details like **location** and **time zone**. 

This section also showcases the **state** of the app, as visible in **[Home](https://docs.erp.net/tech/modules/applications/mssync/home.html)**.

Below, there's a list of your sync tasks, with **slider buttons** built into them for toggling synchronization for on and off.

![picture](pictures/Setup_view_01_03.png) 

Just under the **state** message, you'll find an additional **log** detailing the latest change which occured for MsSync's state.

![picture](pictures/Setup_logs_01_03.png) 

## Company details 

There's a panel containing data about your company, including its **name**, **location**, and **time zone**.

This information is automatically filled in by the system upon your login and is integral for the two-way synchronization process.

For example, if you're creating an event through Outlook, these details cannot be filled from there as they are not required by default. As long as the connection with MsSync is properly configured, the Outlook event that will appear in the ERP.net Calendar will automatically pick up your default enterprise company data.

![picture](pictures/Setup_company_info_01_03.png)  

> [!NOTE]
> 
> You can choose your enterprise company in your profile settings. <br><br> A single profile can contain more than one company. <br><br>

![picture](pictures/Setup_profile_info_01_03.png) 

> [!NOTE]
> 
> If no enterprise company is specified, you will get a notification error indicating which sync job is affected.

![picture](pictures/Setup_Notifications_01_03.png) 

## Sync jobs 

As in **[Home](https://docs.erp.net/tech/modules/applications/mssync/home.html)**, there’s a panel presenting available **sync jobs**. 

Here, alongside the **latest sync**, you'll notice two extra buttons: one for sync jobs **activation** and **deactivation**, and another for **refreshing** the module.

![picture](pictures/Setup_jobs_01_03.png) 

### Activate and deactivate synchronization 

This button **enables** or **disables** the sync job assigned to it. Simply toggle the slider button in the respective direction and the process will commence. 

On first-time activation, the system will sync data for the **past two weeks and the upcoming year**. 

Afterwards, synchronization will occur **every 15 minutes**.
 
![picture](pictures/Setup_slider_01_03.png) 

### Full refresh 

When you click on this button, synchronization for the respective job will refresh on-demand, reflecting the last two weeks and the upcoming year.
 
![picture](pictures/Setup_fullrefresh_01_03.png) 

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.

