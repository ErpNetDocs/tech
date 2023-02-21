# Setup Client Center  

## Define website of type ClientCenter as follows: 
- Enterprise Company
- Relative URL
- Is Active - check marked
- Trusted application – you can create it directly from the website definition form by using the function Create/Update Trusted Application 

> [!NOTE]
> For each Enterprise Company, a different site with a different Relative URL or Host should be defined. 

## Define Trusted Application as follows:  
- Is Enabled - check marked 
- System User Allowed - check marked
- Impersonate As Community User Allowed - check marked
- Impersonate As Internal User Allowed - check marked
- System user - SYSTEM-APPLICATION-USER 
- Client type - Confidential
- Scope - Update   
  
> [!NOTE]
> Through the Instance Manager you can see and restart all sites.

## Setup User settings: 
1.	New User registers himself from the Client Center register form – that creates a new User definition as External Community User.  
2.	Define Person for this User.
3.	Define Parent Party for this Person. 
4.	Define Customer for this Parent Party as follows: 
    - Enterprise Company - the same EC as the client center Web site EC
    -	Serviced by Enterprise Company Location 

> [!NOTE]
> If any ot this User setting is missing in the Client Center will be displayed [Error Exeption](error-codes.md) from CC002 to CC007 depens on the missing setting.

## Allow New order settings:

By Default New order in Client center is Disabled. To allow the New order you have to set JSON settings in the Web site definition: 
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

> [!NOTE]
> If just one of the JSON settings is set or the Id doesn't match any sales order document type then an [Error Exeption](error-codes.md) CC008 or CC009 will be displayed in the Client Center.
