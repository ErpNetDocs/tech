# How to apply platform settings

Like all ERP websites, the Client Center can have its settings changed on an individual level. 

This includes specific visual and functional modifications. 

Below is a list of settings you can apply to the Client Center. An extensive list can be found in the **[Settings and errors reference](https://docs.erp.net/tech/modules/crm/clientcenter/reference.html)**

- The ability to reveal or hide the **[New Order module](https://docs.erp.net/tech/modules/crm/clientcenter/orders/new-order.html?q=new%20order)**.

- The ability to define which document types are shown in the **[Orders](https://docs.erp.net/tech/modules/crm/clientcenter/orders/orders.html)** and the **[Invoices](https://docs.erp.net/tech/modules/crm/clientcenter/billing/invoices.html)** modules.

### JSON format definition

Client Center settings are defined in the **Settings** field of the Web Site creation form.

They must be configured in a **key-value pair JSON format**. 

**Example:**

{<br>
"NewOrderDocumentType": "DocumentType.Id","IsNewOrderEnabled": false <br>
"IsOrdersEnabled": true 
}

where 

- *NewOrderDocumentType* takes the valid ID value of a new (sales) order.
-  _IsNewOrderEnabled_ defines if the module for order creation will be shown or hidden to the users when they log into the system (**true** meaning visible, **false** meaning restricted).
- *IsOrdersEnabled* determines whether the "Orders" section will be present in the Client center. (**true** meaning visible, **false** meaning restricted).

![picture](pictures/settings_code.png)

### Troubleshooting

Depending on how you define the settings, you can encounter the following scenarios:

1.	Both settings are set:

```
    	"NewOrderDocumentType": "07c7ef2f-abc1-47d9-9d40-bc1e0acd1e7c",
   	"IsNewOrderEnabled": true
```

This results in the menu button allowing for the creation of a new order to be shown, and the document type to be set as a sales order.

If the ID doesn’t match any document of type Sales order, you’ll get an error:

**008 - Not well formatted json string**

You need to erase all inputted values, save your progress, refresh the website, and insert the correct values.

2.	Only one of the settings is set:

```
   	  "IsNewOrderEnabled": true
```

Here, the system will generate another error:

**009 – NewOrderDocumentType is set, but DocumentType is null**

3.	No settings are set:

In this scenario, both settings assume two values by default:

```
    	"NewOrderDocumentType": "CRM_SALES_ORDER.Id",
        "IsNewOrderEnabled": false
```

The button used for creating a new order will not be shown. 

If you try to use a link leading to the direct creation of an order, you’ll see the following message:

**You are not authorized to view this page.**

For more information, see the **[reference](https://docs.erp.net/tech/modules/crm/clientcenter/reference.html)**.

### Automatic tracking

Whenever you apply or change settings for the Client Center, they’re **tracked** by the system in real-time and are reflected immediately.

### User-level security

By default, the Client Center uses a system user known as **System-Application-User**. This user has rights to apply or change settings only in accordance with the normal functioning of the website. For better security, another more restricted user can be used. 

By default, the **System-Application-User** has System rights, but reflects used licenses as well. 

It’s automatically assigned whenever a new website is created and whenever a trusted application is added through the UI.
