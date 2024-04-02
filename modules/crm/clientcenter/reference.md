# Reference 

This article contains reference points for specific procedures, concepts and error codes within the **Client Center**.

## IsNewOrderEnabled settings

By default, the ability to preview and **[create new orders](how-to/create-new-order.md)** in the Client Center is **disabled**. 

To enable it, you have to apply **JSON settings** in the website's definition.

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

If only one of the JSON settings is set or the ID doesn't match any sales order document type, an **error exception code** CC008 or CC009 will be displayed.

## IsOrdersEnabled settings

By default, the **Orders** section of the Client Center is **enabled**. 

To disable it, you have to apply **JSON settings** in the website's definition.

Enter a **value** for the Settings field and **restart** the website using the Instance manager:

```
{"IsOrdersEnabled": false} 
```

If "IsOrdersEnabled" is not present in the settings, the **Orders** section will still be visible.

## HideLines settings:

Lines are visible by default in both the **Invoices** and the **Orders** sections of the Client Center.

To hide them, you have to apply **JSON settings** in the website's definition.

Enter the following **value** for the Settings field and **restart** the website using the Instance Manager:

```
{"HideLines": true}
```

If "HideLines" is not present in the settings, lines will remain visible in both **Invoices** and **Orders**.

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
