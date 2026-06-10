# New Order is not available

Use this page when the **New Order** function is missing or unavailable in Client Center.

According to the Client Center documentation, order creation is **disabled by default**. Before users can create orders, the required JSON settings must be applied in the Client Center website definition.

## Check whether New Order is enabled

By default, the ability to create new orders in Client Center is disabled.

To enable it, the Client Center website definition must include the required JSON setting in the **Settings** field:

```json
{"NewOrderDocumentType": "DocumentType.Id","IsNewOrderEnabled": true}
```

The specified NewOrderDocumentType must reference a document type whose EntityName is SalesOrders.

Example:

```json
{"NewOrderDocumentType": "85493adb-ac4e-4b3c-89bc-590c4b22404c","IsNewOrderEnabled": true}
```

If this setting is not applied, **New Order** is not available.

For more information, see [Settings and errors](https://docs.erp.net/tech/modules/crm/clientcenter/reference.html) and [How to set up a Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/how-to/define-a-new-cc.html).

## Check whether both required settings are present and valid

The reference documentation states that if only one of the JSON settings is set, or if the specified ID does not match a sales order document type, Client Center shows error **CC008** or **CC009**.

According to the reference page:

- **CC008** means that the JSON string is not well formatted.
- **CC009** means that the setup is incorrect because the option `NewOrderDocumentType` is set, but `DocumentType` is null.

If one of these errors appears, review the JSON configuration in the Client Center website definition.

For more information, see [Error codes](error-codes.md).

## Check the user's external role

The **New Order** page is available to users with external role **L20 - Orders** and above, provided that the required settings are already enabled.

If the user does not have the required role, the function will not be available.

For more information, see:

- [Access model and external roles](../concepts/access-model-and-external-roles.md)
- [New Order](https://docs.erp.net/tech/modules/crm/clientcenter/orders/new-order.html)

## Check whether the website was restarted after the settings change

Whenever Client Center settings are applied or changed, the website must be **restarted** through the **Instance Manager**.

If the JSON settings were added or changed but **New Order** is still not available, verify that the website was restarted after the change.

For more information, see [How to set up a Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/how-to/define-a-new-cc.html).

## Related pages

- [Order-related settings](../configuration/order-related-settings.md)
- [Create an order](../orders/operations/create-an-order.md)
- [New Order behavior](../orders/concepts/new-order-behavior.md)
- [Error codes](error-codes.md)
- [Settings changes are not applied](settings-changes-are-not-applied.md)
