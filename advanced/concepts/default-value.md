# Default attribute values

Default attribute values automatically fill fields when a new record is created. They can be restricted to a particular context—for example, a user, role, enterprise company, location, language, or record category.

## Concepts

ERP.net has two entities for field defaults. 

The existing [Data Entry Default Values](https://docs.erp.net/model/entities/Systems.Core.DataEntryDefaultValues.html) entity stores defaults for columns in data-entry forms; in the [Desktop Client](https://docs.erp.net/winclient/introduction/fields-management/default-values-management.html), users can save a field’s current value with optional conditions, such as the current user or document type. 

The newer [Entity Attribute Default Values](https://docs.erp.net/model/entities/Systems.Core.EntityAttributeDefaultValues.html) is a new entity and table for storing defaults for attributes of ERP.net repositories. It is the **preferred approach for creating new default-value settings**. Settings created through this approach can be used by both the Web Client and the Desktop Client. The existing **Data Entry Default Values** entity remains available; the new entity does not replace or migrate its records.

Comparative table between the two entities:
1. [DataEntryDefaultValues](https://docs.erp.net/model/entities/Systems.Core.DataEntryDefaultValues.html)
2. [Entity_Attribute_Default_Values](https://docs.erp.net/model/entities/Systems.Core.EntityAttributeDefaultValues.html)

| `Sys_Default_Values`- old table | `Sys_Entity_Attribute_Default_Values` - new table |
|---|---|
| `TableName` | `RepositoryName` |
| `ColumnName` | `AttributeName` |
| `DefaultValueField` | `DefaultInternalValue` |
| `ConditionUserLogin` | `ConditionUser` |
| `ConditionRole` | `ConditionRole` |
| `ConditionEnterpriseCompany` | `ConditionEnterpriseCompany` |
| `ConditionDocumentType` | `ConditionEntityCategory` |
| `ConditionFormName` | N/A |
| `ConditionUserMachine` | N/A |
| `PanelName` | Няма съвместимост |
| N/A | `DefaultTextValue` |
| N/A | `ConditionEnterpriseCompanyLocation` |
| N/A | `ConditionLanguage` |

## Why use a separate entity?

The existing model identifies a default primarily by **table and column** and has its own set of conditions. The new model identifies the **repository and attribute**, stores both the internal value and its display text, and provides conditions for context such as **location, language, and entity category**. These differences make the new entity a better fit for the new field-level Web Client workflow. 

The new conditions are **context conditions**, not conditions based on any arbitrary field in the record. For example, a sales order’s document type can determine which default applies. Changing the role, or Enterprise company, Language forces the system to match any other default-value record and set it properly according to the new context.

## Set a default in the Web Client

Users with **Global Layout Manager permissions and the Layout Admin role** can open a field’s three-dot menu and choose **Default attribute value → Set as default attribute value**. The options are not available to other users.

First, enter or select the value to save. The dialog then lets you select the context conditions under which that value should apply. This follows the familiar [Desktop Client idea](https://docs.erp.net/winclient/introduction/fields-management/default-values-management.html) of saving a field value with optional conditions, while using the new entity to store the Web Client setting.

The available conditions are:

| Condition | Meaning |
|---|---|
| User | Apply for the specified user. |
| Role | Apply when the current user has the specified role. |
| Enterprise company | Apply for the specified enterprise company. |
| Enterprise company location | Apply for the specified location. |
| Language | Apply for the specified current language. |
| Entity category | Apply when the record has the specified category; for the tested sales-order scenario, this is associated with document type. |

A condition that is not selected does not restrict the default. **If no conditions are selected, the setting is an unconditional default:** it can be applied immediately when a new record is created. Selecting conditions restricts it to a matching context.

Saving a different value for the **same attribute and the same set of conditions** updates the existing default-value record rather than creating another record. This was observed in the sales-order tests.

## Manage saved values

Choose **Default attribute value → Manage default attribute value** from the field menu to open the **Entity Attribute Default Values** navigator, where saved settings can be reviewed and edited.

## How context changes affect a default

Defaults are context-sensitive. In the tested Web Client behavior, changing the relevant enterprise company, location, role, or language causes the applicable default to be evaluated against the new context and the field value to change accordingly. Changing the document type also caused the applicable default to be reevaluated in both clients. By contrast, changing session context alone did not automatically refresh an already open Desktop Client document in the tests.

**Administrators should take care when configuring defaults for important fields:** a context change in the Web Client may change a value that was already displayed in the form. These observations were tested with sales orders and should be verified before being stated as universal behavior for every form.

## Existing defaults and precedence

The two entities can contain settings for the **same field**. Based on the sales-order tests:

- **Web Client:** when applicable settings exist in both entities, it uses the setting from **Entity Attribute Default Values**.
- **Desktop Client:** an applicable setting from **Data Entry Default Values** takes precedence, even if a setting in the new entity matches more conditions. If there is no applicable old setting, Desktop can use the new setting.
- A setting saved in the new entity can therefore also affect Desktop users, even when it was created through the Web Client.

**Before creating or changing a default, review applicable settings in both entities.** In particular, check for the same field with overlapping contexts; do not assume that a setting created through one client affects only that client. 

> [!IMPORTANT]
> Administrators should carefully review saved settings — records in both the existing DataEntryDefaultValues table and the new EntityAttributeDefaultValues table — and avoid configurations that could apply to the same field in the same context. Although tests of the feature show that Desktop client "prefers" values from the old table, administrators need not rely on the order in which matching values are found to select a particular default.
