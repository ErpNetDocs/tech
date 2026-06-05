# Billing visibility settings

This article describes the settings that affect invoice visibility in Client Center.

The settings are defined in the **Settings** field of the Client Center website definition in JSON format.

If a setting is not explicitly added in the website definition, its rule is not enforced.

> [!IMPORTANT]
> To apply a setting, restart the website using the Instance Manager.

## InvoiceDocumentTypes

This setting defines which document types are shown in the **Invoices** module.

To include a document type, enter its ID in the **Settings** field. Multiple document types can be specified by separating them with a comma.

```json
{"InvoiceDocumentTypes":["DocumentType1.Id","DocumentType2.Id","DocumentTypeN.Id"]}
```

If this setting is not included in the configuration, all document types in the module are displayed.

## HideLines

Document lines are visible by default in both the **Billing** and **Orders** sections of Client Center.

To hide them, enter the following value in the **Settings** field:

```json
{"HideLines":true}
```
