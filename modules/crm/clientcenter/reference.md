# Reference 

This article serves as a point of reference for specific procedures and concepts within the **Client Center**.

## Setup User settings: 
1.	New User registers himself from the Client Center register form – that creates a new User definition as External Community User.  
2.	Define Person for this User.
3.	Define Parent Party for this Person. 
4.	Define Customer for this Parent Party as follows: 
    - Enterprise Company - the same EC as the client center Web site EC
    -	Serviced by Enterprise Company Location 

If any of these User settings are missing in the Client Center will be displayed [Error Exception](error-codes.md) from CC002 to CC007 depending on the missing setting.

## Allow New order settings:

By Default New order in the Client center is Disabled. To allow the New order you have to set JSON settings in the Web site definition: 
Enter Value to the field Settings as follows and Restart the Site from the Instance manager:
```
{"NewOrderDocumentType": "DocumentType.Id","IsNewOrderEnabled": true}
```
> [!NOTE]
> DocumentType.EntityName == SalesOrders


For example:
```
{"NewOrderDocumentType": "85493adb-ac4e-4b3c-89bc-590c4b22404c","IsNewOrderEnabled": true}
```

If just one of the JSON settings is set or the Id doesn't match any sales order document type then an [Error Exception](error-codes.md) CC008 or CC009 will be displayed in the Client Center.



## Is Orders Enabled settings:

By default "Orders" section the Client center is Visible. To hide the "Orders" section you have to set JSON settings in the Web site definition: 
Enter Value to the field Settings as follows and Restart the Site from the Instance manager:

```
{"IsOrdersEnabled": true} 
```

If "IsOrdersEnabled" is not present in the settings, then the "Orders" section is visible.



## Hide Lines settings:

In the Client Center, "Lines" are visible by default in both "Invoices" and "Orders". To hide the "Lines", you need to configure JSON settings in the Website Definition:
Enter the value in the "Settings" field as specified below, and restart the site using the Instance Manager:

```
{"HideLines": true}
```

If "HideLines" is not present in the settings, the "Lines" will remain visible in both "Invoices" and "Orders".

# User error codes for Client Center
* CC002 - The logged user is not defined as a Person. Please define Person object for this user to use the Client Center.
* CC003 - Parent party of the logged user is empty. Please set parent party to the company on behalf of which the user is entering Client Center.
* CC004 - The parent party is not defined as a customer. It should be customer in order to use Client Center.
* CC005 - The Client Center is not setup correctly - Enterprise Company is not set in the definition of the web site. Please set Enterprise company accordingly.
* CC006 - The parent party does not have customer agreement for the enterprise company of the Client Center. Create customer agreement for this party.
* CC007 - ServicedByEnterpriseCompanyLocation is null. Please set ServicedByEnterpriseCompanyLocation to the asigned ParentParty.Customer for this user.
* CC008 - Not well formatted json string.
* CC009 – Incorrect setup of Client Center - the option NewOrderDocumentType is set, but DocumentType is null.
