---
uid: config-options-reference
---


# Config options reference

Config options are system settings with global and key importance for the operation of the database. Some of them can be set manually, while others are serviced automatically at system level.

> **_IMPORTANT:_** These settings are of great importance and must be changed with great care and only by trained consultants.

The options set for the database are visible in the Configurations navigator and can have different values in each database. 


## А list of configuration keys, their action, and possible values: ##

## 1. AllowFirmPlannedParentForReleasedChild 
- a.Action: When the key has value and this value is "1", the following is allowed: released subdocuments of the FirmPlanned document are allowed.
- b.The user sets it manually.

## 2. CheckForNonVoidedReferencingDocumentsDisabled
- a.Action: When the key hasa  value and this value is "1", verification for references between the documents is not performed when a document is made void. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 3. CheckForOverexecutionDisabled
- a.Action: When the key has a value and this value is "1", verification for over execution of the parent order documents is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 4. CheckForOverinvoicedQuantityInSalesOrderLinesDisabled
- a.Action: When the key has a value and this value is "1", verification for invoicing a greater quantity than the sold quantity is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 5. CheckForTransactionMovementTypeDifferentThanParentStoreOrderMovementTypeDisabled
- a.Action: When the key has value and this value is "1", verification that the movement type of the store transaction is the same as the movement type(s) of the parent store order(s) is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 6. Default language
- a.Action: Defines the default language of multi-language fields. For example: en - English, bg - Bulgarian.
- b.The user sets it manually.

## 7. Default_Enterprise_Company_Location_Id/XXX
- a.Action: Defines the default company location. XXX is the ID of the enterprise company. The value is the ID of the default company location.
- b.Set automatically by the system for the user.

## 8. Documents/OnlySaveNewVersionsToHistory
- a.*This key is used for compatibility with older versions of the software. The old method of saving a document in the document history was to save the previous version before the current version was saved. The new method is to save the current version.*
- b.Action: When the key has a value and this value is "1", the new method is applied. In all other cases, the old method is applied.
- c.The user sets it manually.

## 9. DontCheckForNegativeUnitPrice
- a.Action: When the key has value and this value is "1", verification for negative values in the Unit Price field is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 10. Inv/CheckForNegativeAvailability
- a.Action: When the key has value "1", verification for negative stock balance is performed. The verification checks if the stock balance after the current operation would not become negative, and also if the document date is not today's date, the validation checks for a non-negative stock balance for the dates in the transaction timestamps in the store transaction rows. If the key has an empty value (null) or its value is different from "1", the described validations are not performed.
- b.The user sets it manually.

## 11. InvoiceFiscalPrintChangeToState (DEPRECATED)
- a.Action: This key specifies the document state to which an invoice is switched after the receipt is printed. The key value is the numeric value of the document states (0 = New, 10 = Planned, 20 = FirmPlanned, 30 = Released, 40 = Completed). In all other cases, the invoice is switched to the Released state.
- b.The user sets it manually.

## 12. InvoiceFiscalPrintUseDistributedAmountsForUnitPrice
- a.Action: When the key has value and this value is "1", the unit price, which is sent to the fiscal printer, is calculated through the distributed amounts, which are added to the products. In all other cases, the unit price is calculated as follows: the unit price in the document line with VAT included and discounts in the row.
- b.The user sets it manually.

## 13. Last_Used_Enterprise_Company_Id
- a.Action: Contains the last enterprise company used by the user. The value is the ID of the enterprise company.
- b.Set automatically by the system for the user.

## 14. Last_Used_Enterprise_Company_Location_Id/XXX
- a.Action: Contains the last enterprise company location used by the user. The value is the ID of the enterprise company location.
- b.Set automatically by the system for the user.

## 15. Кеу - SalesOrderFiscalPrintChangeToState (DEPRECATED)
- a.Action: This key specifies the document state to which a sales order is switched to after the receipt is printed. The key value is the numeric value of the document states (0 = New, 10 = Planned, 20 = FirmPlanned, 30 = Released, 40 = Completed). In all other cases, the sales order is switched to the Released state.
- b.The user sets it manually.

## 16. SalesOrderFiscalPrintUseDistributedAmountsForUnitPrice
- a.Action: When the key has value and this value is "1", the unit price, which is sent to the fiscal printer, is calculated through the distributed amounts, which are added to the products. In all other cases, the unit price is calculated as follows: the unit price in the sales order line with VAT included and discounts in the row.
- b.The user sets it manually.

## 17. SalesOrdersOverduePaymentOrdersCheckDisabled
- a.Action: When the key has value and this value is "1", on sales order document release overdue payment orders check is not performed. In all other cases, such a check is performed.
- b.The user sets it manually.

## 18. SimpleFilterLayout
- a.Action: When the value of the key is "1", then the "Use simple layout for filter panels" option is check-marked and the visualization of the navigator filter panels for the specified user is in the format "Field OR Value". If the value of the key is "0", then the "Use simple layout for filter panels" option is not check-marked and the visualization of the navigator filter panels for the specified user is in the format "Field: Value".
- b.The user sets it manually through File tab → Settings → "Use simple layout for filter panels". But if the key is not configured for the particular user, then the system will use the default value. The default value depends on the system version:
    - until Version 2019.1 - the default value is "0";
    - in Version 2019.1 and later - the default value is "1"

## 19. CheckInvoiceLinesQuantityUnitDisabled
- a.Action: When the key has value and this value is "1", when an invoice is released, the validation that the measurement unit of the invoice line and the invoiced sales order line are the same is not performed.
- b.The user sets it manually.

## 20. AllowBaseAmountsFromThirdDocument   
- a.Action: The action of the current key impacts how the additional amounts are distributed. If amounts S and B are distributed on document D1, and amount S depends on amount B.
    - When the current key has a value and this value is "1", the calculation of the additional amounts is performed as follows: 
           - Each B amount, which is distributed on the rows of document D1, participates in the calculation of the base amount of amount S, no matter which document defines the B amount.
    - When the current key has a value different from "1" or the key does not exist:
           - Amount B participates in the base amount of S amount only if the B amount is defined by the same document as S amount in the referent document of S amount. The preferred document of S amount is the document on which rows S amount are distributed.
- b.The user sets it manually.

## 21.  CreateReconciliationsByTimestamp
- a.Action: When this key has value and this value is "1", the function "Add the available products" in the reconciliation form and the manually added new rows would use the date of the transaction timestamp in the row, and not the date of the document, to calculate the stocks availability. The stock's availability may be looked at by one of the following methods:
      - Stock movements in the store by the document date;
      - Stock movements in the store by the date of the transaction timestamp.
- b.Usually, the "i" method is used to define stock availability (i.e., the quantities at a specified date), and method "ii" is used to define the stock's cost (at a specified time)
- c.The user sets it manually.

## 22.  CostCorrectionsCalculateCostTransferDocumentsCostByDocumentCurrencyReevaluation
- a.Action: the current key regulates the recalculation of the product's costs by the documents that transfer costs (store transfers, work orders, sales returns). When the key has a value and this value is "1", the recalculation is performed as follows: all costs of the issue and receipt store documents are converted to the currency of the master document (the document that transfers the cost). If not, usually the base currency of the issue and receipt store documents is used for the recalculation.
- b.The user sets it manually.

## 23. ActiveLanguages
- a.Action: Displays the languages that are active in the current database. If there is no value, all languages are active (currently, 140 languages are supported).
- b.Automatically by the form for editing the languages list, which opens from the Edit Languages menu.

## 24.  CheckForTransactionInvalidLotDisabled
- a.Action: When this key has a value and this value is "1", the validation for an invalid lot in the store transaction on document release is not performed. An invalid lot is a lot that is defined for a product, different than the product in the store transaction line. In all other cases, the validation is performed.
- b.The user sets it manually

## 25. VisualPasteDisabled - suspended
- a.Action: When this key has a value and this value is "1", when rows are pasted in a grid, they are pasted all at the same time (as it was in version 2.3). In all other cases when rows are pasted in a grid, they are pasted visually, row by row and field by field. Every value is searched among the allowed values in drop-down lists.
- b.The user sets it manually

> [!NOTE]
> *This key is suspended in version 2019.1. In its place, there are two new functions in forms and navigators:*
> *- Paste Rows*
> *- Paste Rows Without On-Screen Validation*

## 26.  RealTimeEventsDisabled 
- a. When this key has a value and this value is "1", @@name would not proceed connection with the server that sends real-time events.
- b.The user sets it manually

## 27. RealTimeEventsTimeoutSeconds
- a.Action: Sets the timeout period for waiting for a server response for real-time events, in seconds. If the server does not raise an event in the specified time, the client sends a new request. The value is a number between 5 and 240. If null, the timeout time is 240 seconds (4 minutes).
- b.The user sets it manually

## 28. Require strong passwords
- a.Action: When this key has a value and this value is "1", strong password validation is performed. Strong password requirements are as follows:
    - the password is at least 8 characters;
    - the password contains characters from 3 out of 4 groups: small letters, capital letters, non-alphanumeric characters, numbers; 
    - the password does not contain the username;
    - the password does not contain "123", "1234", "12345", "123456".     
- b.The user sets it manually

## 29. DisableAccountKeyPropertyDotCheck    
- a.Action: When this key has value and this value is "1", when an item key is formed in the accounting voucher rows, the validation for no '.' (dot) in the values of the key custom properties is not performed. For the normal working process of the system, it is important that no dots are part of the values of the key custom properties because the dot is a system character used for item key compilation.
- b.The user sets it manually

## 30. AllowPlannedDocumentStateInClient
- a.Action: When this key has a value and this value is "1", the document state menu would contain the Planned state. In all other cases, the user would not be able to select the Planned state on any document.
- b.The user sets it manually

## 31. DisableProductCopyPropertiesFromOtherProduct
- a.Action: When this key has a value and this value is "1", the Product configurator feature for copying the values to custom properties from the custom property whose values are products is deactivated.
- b.The user sets it manually

## 32. PaymentTransactionFiscalPrintChangeToState (DEPRECATED)
- a.This key specifies the document state to which a payment transaction is switched after the receipt is printed. The key value is the numeric value of the document states (0 = New, 10 = Planned, 20 = FirmPlanned, 30 = Released, 40 = Completed). In all other cases, the payment transaction is switched to the Released state.
- b.The user sets it manually.

## 33. Crm/Sales/SalesOrders/ShowFillLotsInLines  
- a.Action: When this key has a value and this value is "1", the sales order function "Fill lots in lines" is activated.
- b.The user sets it manually.

## 34. General/Contacts/LoadCalendarForLimitedTime    
- a.Action: When this key has value and this value is "1", the calendar in the Activities navigator loads data only for the displayed period (+/- 1 month) when the user scrolls through the calendar. 
- b.The user sets it manually.

## 35. DisableDocumentRecalculationOnIdle
- a.Action: When this key has value and this value is "1", in the document forms, the recalculation of additional amounts, bonus programs, payment plans and etc, in real-time would not be performed (Application.Idle event). In such cases, the document would be recalculated only before the COMMIT event and not in real-time while the user enters the
- b.data in the document form. The method referred to by the current key is "Document.Recalculate" which performs different actions in the different entities.
- c.The user sets it manually.

## 36. DisableParentDocumentReset
- a.Action: When this key has a value and this value is "1", on document state change, the parent document state is not reset.
- b.The user sets it manually.

## 37. RevokedBusinessRules   
- a.Action: When this key has a value, the validation and the action of the business rules, whose codes are specified as a key value, is not performed. The codes of the business rules must be listed comma-separated (for example, 27407, 26881 ..). Since version 2018.2, business rules' codes must be set with their full code including "R" (eg, R27408, R26881 ...). If the key value is changed, the client application requires a restart.
- b.The user sets it manually.

## 38. DisableQueryingForSaveOnClose    
- a.Action: When this key has value and this value is "1", on closing of a form which is not saved, if there is a change in any table of the form, no information message for saving or undoing the changes appears.
- b.The user sets it manually.

## 39. UseLegacyLoadForLotsIssue        
- a.Action: When this key has value and this value is "1", for the calculation of the quantity "Available to promise by lots" is used the method that was developed before Version 2018.2. In all other cases, is used the current for Version 2018.2 method which is advisable and has a better performance.
- b.The user sets it manually.

## 40. ReservedLicenses (not implemented/ cancelled)

## 41. EnableCreateGroupForUser
- a.Action: When this key has value and this value is "1" or "true" (case-insensitive), when creating a new user in the database, a new group with the user’s name will be created automatically as well. 
- b.The user sets it manually.
- c.The key is introduced in version: - 2019.1 (in implementation)

> [!Note]
> Before version 2019.1, a new user group was created automatically whenever a new user was created, and this behaviour could not be disabled. Since version 2019.1, the behaviour is disabled by default and could be activated manually using the current registry key.

## 42. DocumentVersioningSystem
- a.Action: When the value of this key is "VH" the system will use the "old" document versioning system. If the key's value is "TC" the system will not create records using the "old" document versioning system and will instead use the [Track changes](https://docs.erp.net/tech/advanced/track-changes.html) system. The minimum level that is going to be tracked when the "TC" option is activated is "Track Changes Level 3". If for the particular document entity is chosen a specific level, then this level will be applied only if it is a higher level than level 3. (For more information about the track changes system and its levels, please see topic [Track changes](https://docs.erp.net/tech/advanced/track-changes.html) 
       
>[!Note]
> Please note that the current key affects only entities which are a successor of the document entity (such as sales orders, store orders ...) and NOT entities such as product groups, bonus programs..

- b.The user sets it manually, but if the key is not configured for the particular database or its value is different from "VH" or "TC", then the system will use the default value. The default value depends on the system version:
    - Version 2019.1 - the default value is "VH";
    - Version 2020.1 and later - the default value is "TC";
- c.The key is introduced in version: - 2019.1

## 43. Crm/Pos/PrintGroupedSalesLinesType
- a.Action: When the value of this key is "ShortName", then items in the fiscal receipt are grouped by the "ShortName" field in the product. When the value of this key is "ProductGroup", then items in the fiscal receipt are grouped by the product group of the product. When the value of this key is different or the key is missing, then items in the fiscal receipt are not grouped.
- b.The key is introduced in version: - 2019.1
           
## 44. UseStartScreen
- a.Action: When the value of this key is:
    - "1" - the form that is going to be opened when the program is started by the specified user will be the Start screen. 
    - "2" - the starting form will be the Main menu. <br>
    - "0", different from "1" and "2" or the key is not configured for the particular database and user - the system will use the default value. The default value for
    version 2020.1 is Main Menu.**Warning:** The current key's value will be taken into account only if there is no global policy specifying the use of the start screen for the whole database using the key "UseStartScreenPolicy"
- b.The user sets it manually.
- c. The key is introduced in version: - 2020.1

## 45. UseStartScreenPolicy 
- a.Action: When the value of this key is:
    - "1" - the form that is going to be opened when the program is started will be the Start screen. This applies to all users in the database, regardless of the "UseStartScreen" option.
    - "2" - the starting form will be the Main menu. This applies to all users in the database, regardless of the "UseStartScreen" option/key.
    - "0", different from "1" and "2", or the key is not configured for the particular database - there is no global policy. Each user decides whether they want to use the start screen using "UseStartScreen" option/key.
- b.The user sets it manually.
- c.The key is introduced in version: - 2020.1

## 46. UseDefaultMailClient

- a.Action: When this key has a value for the particular user and this value is "1", then when creating an email, the system will start the default Windows Mail client. This will apply even if there is a mailbox defined for the user. 
- b. The user sets it manually (directly in the registry or using the option available in the tab File => Settings => Use default Windows mail client).
- c.The key is introduced in version: - 2019.1

## 47. CodeNameFormat

- a.Action: The default display text format for entities that provide Code and Name. The value is an integer number from 1 to 4:
    - "1" - {Code}: {Name}
    - "2" - {Code}
    - "3" - {Name} ({Code})
    - "4" - {Name}
- b.The user sets it manually.
- c.The key is introduced in version: - 2022

## 48. AllowBasicAuthForAllUsers 
- a. When this key has a value and this value is "1", all users can use basic authentication, regardless of their settings.
- b.The user sets it manually
- c.The key is introduced in version: - 2023

## 49. Calendar/TimePresets
- a. When this key hasa  value and conforms to the format below, it overrides the time presets in the [calendar control](https://docs.erp.net/webclient/introduction/my-apps/calendar.html#time-presets).
```
<PresetName1>=<H>:<M>;<PresetName2>=<H>:<M>;...
```
e.g.,
```
Morning=10:00;Lunch=12:30;Afternoon=15:00;Dinner=19:00
```
- b.The user sets it manually
- c.The key is introduced in version: - 2023

## 50. InventoryControl/ReceiveDocumentType
- a.The key defines the document type of the created document when using the Receive function of Inventory Control
- b.The user sets it manually
- c.The key is introduced in version: - 23.2

## 51. InventoryControl/IssueDocumentType
- a.The key defines the document type of the created document when using the Issue function of Inventory Control
- b.The user sets it manually
- c.The key is introduced in version: - 23.2

## 52. InventoryControl/ScrapDocumentType
- a.The key defines the document type of the created document when using the Scrap function of Inventory Control
- b.The user sets it manually
- c.The key is introduced in version: - 23.2

## 53. InventoryControl/ReconcileDocumentType
- a.The key defines the document type of the created document when using the Reconcile function of Inventory Control
- b.The user sets it manually
- c.The key is introduced in version: - 23.2

## 54. /WMS/WMS-Worker/SingleBarcodeScanEntersQuantityOfOnePce - DEPRECATED v.25
- a.Action: When the value of this key is:
    - "1" - When scanning a single barcode, then this is accepted as 1 PCE
    - "0" - When scanning a single barcode, then no quantity is accepted, the WMS-Worker APP just finds the line and goes to execute mode for this line.
- b.The user sets it manually.
- c.The key is introduced in version: - 23.2

## 55. /WMS/WMS-Worker/OrderDisplayFormat
- a.Action: When this key is defined, the WMS Worker application will display the data you need, replacing the first row with Order information in the WO list and inside the WO.
  Depending on the entered key value - in the orders list and inside the WO, you can see the data you need from the current Warehouse order header.
  The value is entered as an interpolated string. You can also use format specifiers. <br>
  For example "My info - {@Property1: VD} ; my store: {Warehouse}" will be displayed as "My info - 01:yes ; my store: Warehouse1"
- b.If the key is not defined, the WMS Worker will display the default information, which comes from the To Party field in the WO header.
- c.The user sets it manually.

## 56. DataSourceTableOptimizationDisabled

- a.Action: When this key has a value and this value is "1", all tables in the data source of the printout will be extracted from the database. In all other cases, only the data that is actually used by the layout of the printout will be extracted.
- b.The user sets it manually

## 57. /TrackChanges/AttributeChangesRetentionMonths
- a.Action: When the key is defined and has a value, its value specifies the retention period, in months, of attribute changes history data (these are the records in the [Attribute Changes](xref:Systems.Core.AttributeChanges) table, which are generated by the [Track Changes](~/advanced/data-objects/track-changes.md) system). The retention period starts from the date the change was made, which is set in ObjectChangeset.TimeUtc field.<br>
When the key is not defined or has no value, the retention period is set to 36 months by default.<br>
If the [J35666 Delete attribute changes history](~/advanced/jobs/J35666.md) job is configured and active, the old history data for attribute changes, whose retention period is expired, will be deleted.
- c.The user sets it manually.
- d.The key is introduced in version: - 24

## 58. Acc/DisableAccountFilterLimit
- a.Action: When the key is not defined or has a value and this value is "0", data loading is not allowed in the Chronological Statement Navigator if a filter is applied for more than 10 accounts or no accounts. An error message will be displayed.<br>
  When the key has the value "1", the warning message will be displayed, and then data will be loaded.
- b.The user sets it manually

## 59. /AI/Assistant/DebugMode
- a.Action: When this key has a value of '1', it determines whether an AI assistant will operate in debug mode.
- b.The user sets it manually
- c.The key is introduced in version: - 24

## 60. /AI/Assistant/AdditionalInstructions
- a.Action: Additional instructions, passed to the AI assistant when it is launched from a single record form (definition). Defines additional guidance passed to the AI Assistant to tailor its behavior to a single record context. If no custom value is specified by the user, the system default instructions are applied.
- b.The user sets it manually
- c.The key is introduced in version: - 24, Changed in version: 26 - Since this version, it no longer contains instructions for all form types. It is now valid only for single-record forms. For navigator forms, a different key is used: "/AI/Assistant/AdditionalNavigatorInstructions"."

## 61. /WMS/WMS-Worker/ProductDisplayFormat
- a.Action: When this key is defined, the WMS Worker application will display the data you need, replacing the Product field in the Warehouse order line list.
  Depending on the entered key value - in the orders line list, you can see the data you need from the current Warehouse order line.
  The value is entered as an interpolated string. You can also use format specifiers. <br>
  For example "my product: {Product.PartNumber}; size: {Product.@Property1: VD}" will be displayed as "my product: 0000001 ; size: 01:big"
- b.If the key is not defined, the WMS Worker will display the default information, coming from the Product field and follow the default Web client display text format for Product, which is Product.Name.
- c.The user sets it manually.

## 62. /WMS/WMS-Worker/LocationDisplayFormat
- a.Action: When this key is defined, the WMS Worker application will display the data you need, replacing the Location field in the Warehouse order line list.
  Depending on the entered key value - in the orders list, you can see the data you need from the current Warehouse order line.
  The value is entered as an interpolated string. You can also use format specifiers. <br>
  For example "location: {Location} ; forklift - {Document.@Property2: VD}" will be displayed as "location: 01-02-A2 ; forklift: 01:yes"
- b.If the key is not defined, the WMS Worker will display the default information, which comes from the Location field.
- c.With the Suggest Routing function, the string for the location is called with a dollar sign: {$WarehouseLocation}
- d.The user sets it manually.

## 63. /Inv/ListAllStoresForTransfers
- a.Action: When the value of this key is: <br>
"1" - When the key is defined and its value is 1, all defined stores will be listed in the ToStore field in the Transfer function.<br>
"0" - When a key is defined and its value is 0, or there is no defined key, only the stores to which the user has permission will be listed.
- b.The user sets it manually.
- c.The key is introduced in version: - 24 SP5

## 64. /Documents/AllowCompleteWithSubdocumentsIncludingUnreleased
- a.Action: When the value of this key is: <br>
"1" - When the key is defined and set to 1, 'Complete with sub-documents, including unreleased' will be available as a Completed status option.<br>
"0" - When the key is defined and set to 0, or if no key is defined, 'Complete with sub-documents, including unreleased' will not be available as a Completed status option.<br>
- b.The user sets it manually.
- c.The key is introduced in version: - 25

## 65. /JobsManager/IgnoreSessionsForIdleSchedule
- a.Action: When the value of this key is: <br>
"1" - When the key is defined and set to 1, Jobs marked as Run On Idle will start automatically at the scheduled time, regardless of current server sessions.<br>
"0" - When the key is defined and set to 0 or a value different from 1, or if no key is defined, Jobs marked as Run On Idle will start automatically at the scheduled time only if the server sessions are less than 5.<br>
- b.The user sets it manually.
- c.The key is introduced in version: - 24 SP7

## 66. /Monitoring/AuditLogEntriesRetentionMonths
-	a.Action: When the key is defined and has a value, its value specifies the retention period, in months, of audit log entries (these are the records in the  [Audit Log Entries](xref:Systems.Monitoring.AuditLogEntries) table). The retention period starts from the date set in AuditLogEntries.Event_Time_Utc field.
When the key is not defined or has no value, the retention period is set to 12 months by default.<br>
If the [J38417 Delete old audit logs](~/advanced/jobs/J38417.md) job is configured and active - the audit log entries, whose retention period has expired, will be deleted.<br>
-	b.The user sets it manually.<br>
-	c.The key is introduced in version: - 25<br>

## 67. /id/UserNameAutoComplete
-	a.Action: When the value of this key is:<br>
"1" - When the key is defined and set to 1, the autocomplete option for the user/email field of the Desktop client login screen is turned on. This means that previously entered login credentials will be suggested when clicking into the field.<br>
"0" - When the key is defined and set to 0 or a value different from 1, or if no key is defined, the autocomplete option for the user/email field of the Desktop client login screen is turned off.<br>
-	b.The user sets it manually.<br>
-	c.The key is introduced in version: - 24 SP10<br>

## 68. /AI/Chat/ContextDepth
- a.Action: Context depth is the number of previous comments that will be included in the prompt. Defaults to `100`.
- b.The user sets it manually
- c.The key is introduced in version: - 25

## 69. /AI/Assistant/AdditionalNavigatorInstructions
- a.Action: Additional instructions, passed to the AI assistant when it is launched from a navigator or report form. Defines additional guidance passed to the AI Assistant to tailor its behavior in the navigator or report contexts. If no custom value is specified by the user, the system default instructions are applied.
The default instructions are:
````
If there is an attached file, consider that it might be a JSON file exported from our ERP system.

- The file contains a report/navigator.
- The report’s name is in the "title" key.
- The report’s description is in the "description" key.
- The records are inside the array named "objects".

Please load and understand the structure of the file. Actually read it, don't pretend to have read it.
Remember the contents of this file for future questions, as the next questions might relate to its data.
If you need to analyze the data, you may use Python code.
````
- b.The user sets it manually
- c.The key is introduced in version: - 26

## 70. /InventoryControl/OrderDisplayFormat
- a.Action: When this key is defined, the Inventory Control application will display the data you need, replacing the first row with Order information in the Store Orders list.
  Depending on the entered key value - in the orders list you can see the data you need from the current Store Order header.
  The value is entered as an interpolated string. You can also use format specifiers. <br>
  For example "{Parent}, Notes: {DocumentNotes:T}, {MasterDocument} will be displayed as "Invoice Order 00001 ; Notes: ASAP ; Sales Order 00001
- b.If the key is not defined, the Inventory Control will display the default information, which comes from the To Party field in the Store Order header.
- c.The user sets it manually.
