# Order-related settings

This article describes the settings that affect order visibility and order creation in Client Center.

The settings are defined in the **Settings** field of the Client Center website definition in JSON format.

If a setting is not explicitly added in the website definition, its rule is not enforced.

> [!IMPORTANT]
> To apply a setting, restart the website using the Instance Manager.

## IsNewOrderEnabled

By default, the ability to create new orders in Client Center is disabled.

To enable it, enter the following value in the **Settings** field:

```json
{"NewOrderDocumentType":"DocumentType.Id","IsNewOrderEnabled":true}
```

> [!NOTE]
> `DocumentType.EntityName` must be equal to `SalesOrders`.

For example:

```json
{"NewOrderDocumentType":"85493adb-ac4e-4b3c-89bc-590c4b22404c","IsNewOrderEnabled":true}
```

If only one of the JSON settings is set, or if the specified ID does not match a sales order document type, error code **CC008** or **CC009** is displayed.

## OrderDocumentTypes

This setting defines which document types are shown in the **Orders** module.

To include a document type, enter its ID in the **Settings** field. Multiple document types can be specified by separating them with a comma.

```json
{"OrderDocumentTypes":["DocumentType1.Id","DocumentType2.Id","DocumentTypeN.Id"]}
```

If this setting is not included in the configuration, all document types in the module are displayed.

## HideCustomerProducts

Customer products are visible by default in the **My Products** tab when creating a new order in Client Center.

To hide the products and this tab, enter the following value in the **Settings** field:

```json
{"HideCustomerProducts":true}
```

## HideDistributionChannel

Products linked to a customer's default distribution channel are visible by default when creating a new order in Client Center.

To hide the products and this tab, enter the following value in the **Settings** field:

```json
{"HideDistributionChannel":true}
```

## DefaultStore

You can set a default store for every new order created in Client Center.

This is a prerequisite when you want to see the actual availability while adding product quantities to the order, as long as an **AvailabilityMax** setting is also in place.

To set a default store, enter the following value in the **Settings** field:

```json
{"DefaultStore":"Store.Code"}
```

where `Store.Code` is the code of the store, for example `00002`.

## AvailabilityMax

This setting defines the maximum product quantity to be displayed directly in the **Availability** column when creating a new order.

It is also a prerequisite for availability to be shown at all, provided **DefaultStore** is also present.

For example, if the threshold is set to `100`, but `200` pieces of a product are requested, the user will need to contact a sales representative to confirm whether the quantity is available.

The **AvailabilityMax** value is taken from the `ATPBase` field in the **Available To Promise** report, using the row where:

- **Store** = `DefaultStore`
- **Product** = current product
- **EnterpriseCompany** = current Client Center website enterprise company
- **FromDate** = latest date less than or equal to today

To enforce the rule, enter the following value in the **Settings** field:

```json
{"AvailabilityMax":number}
```

where `number` is an integer representing the maximum quantity that can be directly shown in the **Availability** column.

## SiteChannel

Each Client Center has its own distribution channel.

If a custom distribution channel is not explicitly defined, the Client Center is automatically assigned a distribution channel with code `CC` and name `Client Center`.

When products are linked to this channel, they appear in a tab with that channel's name in the **New Order** module.

The site channel can be overridden by specifying the code of another distribution channel in the **Settings** field:

```json
{"SiteChannel":"DistributionChannel.Code"}
```

where `DistributionChannel.Code` is the code of the channel, for example `CC`.
