# Settings and errors 

This article contains reference points for specific JSON settings and error codes within the **Client Center**.

If a setting is not explicitly added in the definition of the Client Center website, its rule will **not** be enforced.

To **[apply a setting](how-to/apply-platform-settings.md)**, you need to **restart** the website using the **Instance Manager**.

## IsNewOrderEnabled setting

By default, the ability to **[create new orders](how-to/create-new-order.md)** in the Client Center is disabled. 

To enable it, you have to apply the necessary **JSON setting** in the website's definition.

Enter the following **value** in the Settings field:

```
{"NewOrderDocumentType": "DocumentType.Id","IsNewOrderEnabled": true}
```

> [!NOTE]
> DocumentType.EntityName must be equal to "SalesOrders"


For example:

```
{"NewOrderDocumentType": "85493adb-ac4e-4b3c-89bc-590c4b22404c","IsNewOrderEnabled": true}
```

If only one of the JSON settings is set or the ID doesn't match any sales order document type, an **error code** CC008 or CC009 is displayed.

## IsOrdersEnabled setting

By default, the **[Orders](orders/index.md)** section of the Client Center is **enabled**. 

To disable it, enter the following **value** in the Settings field:

```
{"IsOrdersEnabled": false} 
```

## HideLines setting

Document lines are visible by default both in the **[Billing](billing/index.md)** and the **[Orders](orders/index.md)** sections of the Client Center.

To hide them, enter the following **value** in the Settings field:

```
{"HideLines": true}
```

## HideCustomerProducts setting

**[Customer products](https://docs.erp.net/tech/modules/crm/sales/definitions/define-customers.html)** are visible by default in the **My Products** tab during the creation of a new order in the Client Center.

To hide the products and this tab, enter the following **value** in the Settings field:

```
{"HideCustomerProducts": true}
```

## HideDistributionChannel setting

Products linked to a customer's default **[distribution channel](https://docs.erp.net/tech/modules/crm/marketing/distribution-channels/index.html)** are visible by default during the creation of a new order in the Client Center.

To hide the products and this tab, enter the following **value** in the Settings field:

```
{"HideDistributionChannel": true}
```

## DefaultStore setting

You can set a default store for every new order created in the Client Center.

To do so, enter the following **value** in the Settings field:

```
{"DefaultStore": "ID"}
```

where ID is the identifier of the store (e.g. 00002).

## SiteChannel setting

Each Client Center has its own **[distribution (site) channel](https://docs.erp.net/tech/modules/crm/marketing/distribution-channels/index.html)**. 

If a custom distribution channel is not explicitly defined, the Client Center is automatically assigned a distribution channel with code **"CC"** and name **"Client Center"**. When products are linked to this channel, they will appear as part of a tab carrying that channel's name in the **[New Order](orders/new-order.md)** module.  

Site channels can be overridden by specifying the **code value** of another distribution channel in the Settings field:

```
"SiteChannel": "DistributionChannel.Code"
```

where DistributionChannel.Code is the code of the channel (e.g. "CC").

> [!NOTE]
> 
> Settings are **[applied](how-to/apply-platform-settings.md)** in a key-value pair JSON format in the **Settings** field of the Client Center website definition. 

## Error exception codes

* **CC002**

  The logged user is not defined as a Person.
  
  Please define Person object for this user to use the Client Center.
  
* **CC003**

  Parent party of the logged user is empty.
  
  Please set parent party to the company on behalf of which the user is entering Client Center.
  
* **CC004**

  The parent party is not defined as a customer.
  
  It should be customer in order to use Client Center.
  
* **CC005**

  The Client Center is not setup correctly - Enterprise Company is not set in the definition of the web site.
  
  Please set Enterprise company accordingly.
  
* **CC006**

  The parent party does not have customer agreement for the enterprise company of the Client Center.
  
  Create customer agreement for this party.
  
* **CC007**
  
  ServicedByEnterpriseCompanyLocation is null.
  
  Please set ServicedByEnterpriseCompanyLocation to the asigned ParentParty.Customer for this user.
  
  
* **CC008**

  Not well formatted JSON string.
  
* **CC009**

  Incorrect setup of Client Center - the option NewOrderDocumentType is set, but DocumentType is null.

* **CC010**

  The logged-in user does not have a defined role.
  
  Please add the user to the Crm_Customer_External_Access table and assign an appropriate role.

