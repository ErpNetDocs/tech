# Settings changes are not applied

Use this page when Client Center settings have been changed, but the expected result is not visible.

Client Center settings are applied through the **Settings** field in the website definition. After a change is made, the website must be restarted for the change to take effect.

## Check whether the JSON is well formatted

Client Center settings are entered as a JSON string in the **Settings** field of the website definition.

If the JSON string is not well formatted, Client Center shows error **CC008**.

For more information, see [Error codes](error-codes.md).

## Check whether the website was restarted

After a change is made in the **Settings** field, the website must be restarted through the **Instance Manager**.

If the website was not restarted, the new settings will not be applied.

For more information, see [How to set up a Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/how-to/define-a-new-cc.html).

## Check whether the required setting is present

Some Client Center functions require specific settings to be explicitly added in the JSON configuration.

For example, **New Order** is disabled by default and requires the corresponding settings to be present before it becomes available.

If a required setting is missing, the expected behavior will not be applied.

For more information, see:

- [Order-related settings](../configuration/order-related-settings.md)
- [New Order is not available](new-order-is-not-available.md)

## Check whether the setting value is valid

Some settings require a valid value rather than just a setting name.

For example, when `NewOrderDocumentType` is used, it must reference a valid sales order document type.

If a required value is missing or invalid, Client Center may show a configuration-related error such as **CC009**.

For more information, see:

- [Error codes](error-codes.md)
- [Order-related settings](../configuration/order-related-settings.md)

## Related pages

- [Error codes](error-codes.md)
- [New Order is not available](new-order-is-not-available.md)
- [Order-related settings](../configuration/order-related-settings.md)
- [How to set up a Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/how-to/define-a-new-cc.html)
