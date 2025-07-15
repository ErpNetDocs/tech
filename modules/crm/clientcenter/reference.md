# Settings and errors 

This article contains reference points for specific JSON settings and error codes within the **Client Center**.

## IsNewOrderEnabled setting

By default, the ability to **[create new orders](how-to/create-new-order.md)** in the Client Center is disabled. 

To enable it, you have to apply the necessary **JSON setting** in the website's definition.

Enter a **value** for the Settings field and **restart** the website using the Instance manager:

```
{"NewOrderDocumentType": "DocumentType.Id","IsNewOrderEnabled": true}
```

> [!NOTE]
> DocumentType.EntityName must be equal to "SalesOrders"


For example:

```
{"NewOrderDocumentType": "85493adb-ac4e-4b3c-89bc-590c4b22404c","IsNewOrderEnabled": true}
```

If only one of the JSON settings is set or the ID doesn't match any sales order document type, an **error exception code** CC008 or CC009 is displayed.

## IsOrdersEnabled setting

By default, the **Orders** section of the Client Center is **enabled**. 

To disable it, enter the following **value** in the Settings field and **restart** the website using the Instance manager:

```
{"IsOrdersEnabled": false} 
```

> [!NOTE]
>
> If "IsOrdersEnabled" is not present in the settings, the Orders section will still be visible.

## HideLines setting

Document lines are visible by default both in the **Billing** and the **Orders** sections of the Client Center.

To hide them, enter the following **value** for the Settings field and **restart** the website using the Instance Manager:

```
{"HideLines": true}
```

> [!NOTE]
> 
> If "HideLines" is not present in the settings, lines will remain visible.

## HideCustomerProducts

Customer products are visible by default in the **My Products** tab during the creation of a new order in the Client Center.

To hide the products and this tab, enter the following **value** for the Settings field and **restart** the website using the Instance Manager:

```
{"HideCustomerProducts": true}
```

## HideDistributionChannel

Products linked to a customer's default distribution channel are visible by default during the creation of a new order in the Client Center.

To hide the products and this tab, enter the following **value** for the Settings field and **restart** the website using the Instance Manager:

```
{"HideDistributionChannel": true}
```

## DefaultStore

You can set a default store for every new order created in the Client Center.

To do so, enter the following **value** for the Settings field and **restart** the website using the Instance Manager:

```
{"DefaultStore": ID}
```

where ID is the identifier of the store (e.g. 00002).

## SiteChannel: DistributionChannel.Code

Each Client Center has its own site, or distribution channel. 

This can be overridden by specifying the code of another distribution channel in the following setting:

```
"SiteChannel": DistributionChannel.Code
```

where DistributionChannel.Code is the code of the channel (e.g. "CC").

## Error exception codes

* **CC002**

  The logged user is not defined as a Person. Please define Person object for this user to use the Client Center.
  
* **CC003**

  Parent party of the logged user is empty. Please set parent party to the company on behalf of which the user is entering Client Center.
  
* **CC004**

  The parent party is not defined as a customer. It should be customer in order to use Client Center.
  
* **CC005**

  The Client Center is not setup correctly - Enterprise Company is not set in the definition of the web site. Please set Enterprise company accordingly.
  
* **CC006**

  The parent party does not have customer agreement for the enterprise company of the Client Center. Create customer agreement for this party.
  
* **CC007**
  
  ServicedByEnterpriseCompanyLocation is null. Please set ServicedByEnterpriseCompanyLocation to the asigned ParentParty.Customer for this user.
  
* **CC008**

  Not well formatted JSON string.
  
* **CC009**

  Incorrect setup of Client Center - the option NewOrderDocumentType is set, but DocumentType is null.
