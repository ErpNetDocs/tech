---
uid: config-options-reference
---


# Config options reference

Config options are system settings with global and key importance for the operation of the database. Some of them can be set manually, while others are serviced automatically at system level.

> **_IMPORTANT:_** These settings are of great importance and must be changed with great care and only by trained consultants.

The options set for the database are visible in the Configurations navigator and can have different values in each database. 


## А list of configuration keys, their action and possible values: ##

## 1. AllowFirmPlannedParentForReleasedChild 
- a.Action: When the key has value and this value is "1" the following is allows: released subdocuments of FirmPlanned document are allowed.
- b.The user sets it manually.

## 2. CheckForNonVoidedReferencingDocumentsDisabled
- a.Action: When the key has value and this value is "1", verification for references between the documents is not performed when a document is made void. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 3. CheckForOverexecutionDisabled
- a.Action: When the key has value and this value is "1", verification for over execution of the parent order documents is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 4. CheckForOverinvoicedQuantityInSalesOrderLinesDisabled
- a.Action: When the key has value and this value is "1", verification for invoicing greater quantity than the sold quantity is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 5. CheckForTransactionMovementTypeDifferentThanParentStoreOrderMovementTypeDisabled
- a.Action: When the key has value and this value is "1", verification that the movement type of the store transaction is the same as the movement type(s) of the parent store order(s) is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 6. Default language
- a.Action: Defines the default language of multi-language fields. For example: en - English, bg - Bulgarian.
- b.The user sets it manually.

## 7. Default_Enterprise_Company_Location_Id/XXX
- a.Action: Defines the default company location. XXX is the ID of the enterprise company. The value is the ID of the default company location.
- b.Set automatically by the system of the user.

## 8. Documents/OnlySaveNewVersionsToHistory
- a.*This key is used for compatibility with older versions of the software. The old method of saving a document in the document history is to save the previous version before the current version is saved. The new method is to save the current version.*
- b.Action: When the key has value and this value is "1", the new method is applied. In all other cases, the old method is applied.
- c.The user sets it manually.

## 9. DontCheckForNegativeUnitPrice
- a.Action: When the key has value and this value is "1", verification for negative values in the Unit Price field is not performed. In all other cases, the verification is performed. 
- b.The user sets it manually.

## 10. Inv/CheckForNegativeAvailability
- a.Action: When the key has value "1", verification for negative stock balance is performed. The verification checks if the stock balance after the current operation would not become negative and also if the document date is not today's date, the validation checks for not negative stock balance for the dates in the transaction timestamps in the store transaction rows. If the key has an empty value (null) or its value is different than "1" the described validations are not performed.
- b.The user sets it manually.

## 11. InvoiceFiscalPrintChangeToState (DEPRECATED)
- a.Action: This key specifies the document state to which an invoice is switched to after the receipt is printed. The key value is the numeric value of the document states (0 = New, 10 = Planned, 20 = FirmPlanned, 30 = Released, 40 = Completed). In all other cases, the invoice is switched to Released state.
- b.The user sets it manually.

## 12. InvoiceFiscalPrintUseDistributedAmountsForUnitPrice
- a.Action: When the key has value and this value is "1", the unit price which is sent to the fiscal printer is calculated through the distributed amounts, which are added to the products. In all other cases, the unit price is calculated as follows: the unit price in the document line with VAT included and discounts in the row.
- b.The user sets it manually.

## 13. Last_Used_Enterprise_Company_Id
- a.Action: Defines the last used by the user enterprise company. The value is the id of the enterprise company.
- b.Set automatically by the system of the user.

## 14. Last_Used_Enterprise_Company_Location_Id/XXX
- a.Defines the last used by the user enterprise company location. The value is the id of the enterprise company location.
- b.Set automatically by the system of the user.

## 15. Кеу - SalesOrderFiscalPrintChangeToState (DEPRECATED)
- a.Action: This key specifies the document state to which a sales order is switched to after the receipt is printed. The key value is the numeric value of the document states (0 = New, 10 = Planned, 20 = FirmPlanned, 30 = Released, 40 = Completed). In all other cases, the sales order is switched to Released state.
- b.The user sets it manually.

## 16. SalesOrderFiscalPrintUseDistributedAmountsForUnitPrice
- a.Action: When the key has value and this value is "1", the unit price which is sent to the fiscal printer is calculated through the distributed amounts, which are added to the products. In all other cases, the unit price is calculated as follows: the unit price in the sales order line with VAT included and discounts in the row.
- b.The user sets it manually.

## 17. SalesOrdersOverduePaymentOrdersCheckDisabled
- a.Action: When the key has value and this value is "1", on sales order document release overdue payment orders check is not performed. In all other cases, such check is performed.
- b.The user sets it manually.

## 18. SimpleFilterLayout
- a.Action: When the value of the key is "1", then the "Use simple layout for filter panels" option is check-marked and the visualization of the navigator filter panels for the specified user is in the format "Field OR Value". If the value of the key is "0", then the "Use simple layout for filter panels" option is not check-marked and the visualization of the navigator filter panels for the specified user is in the format "Field: Value".
- b.The user sets it manually through File tab → Settings → "Use simple layout for filter panels". But if the key is not configured for the particular user, then the system will use the default value. The default value depends on the system version:
    - until Version 2019.1 - the default value is "0";
    - in Version 2019.1 and later - the default value is "1"

## 19. CheckInvoiceLinesQuantityUnitDisabled
- a.Action: When the key has value and this value is "1", when an invoice is released the validation if the measurement unit of the invoice line and the invoiced sales order line are the same is not performed.
- b.The user sets it manually.

## 20. AllowBaseAmountsFromThirdDocument   
- a.Action: The action of the current key impacts how the additional amounts are distributed. If amount S and B are distributed on document D1 and amount S depends on amount B.
    - When the current key has value and this value is "1" the calculation of the additional amounts is performed as follows: 
           - Each B amount which is distributed on the rows of document D1 participates in the calculation of the base amount of amount S no matter which document defines the B amount.
    - When the current key has a value different from "1" or the key does not exist:
           - Amount B participate in the base amount of S amount only if the B amount is defined by the same document as S amount in the referent document of S amount. The preferred document of S amount is the document on which rows S amount is distributed.
- b.The user sets it manually.

## 21.  CreateReconciliationsByTimestamp
- a.Action: When this key has value and this value is "1", the function "Add the available products" in the reconciliation form and the manually added new rows would use the date of the transaction timestamp in the row, and not the date of the document, to calculate the stocks availability. The stocks availability may be looked at by one of the following methods:
      - Stock movements in the store by the document date;
      - Stock movements in the store by the date of the transaction timestamp.
- b.Usually, the "i" method is used to define stock availability (i.e. the quantities at a specified date), and method "ii" is used to define the stocks cost (at a specified time)
- c.The user sets it manually.

## 22.  CostCorrectionsCalculateCostTransferDocumentsCostByDocumentCurrencyReevaluation
- a.Action: the current key regulates the recalculation of the products costs by the documents which transfer costs (store transfers, work orders, sales returns). When the key has value and this value is "1", the recalculation is performed as follows: all costs of the issue and receipt store documents are converted to the currency of the master document (the document which transfers the cost). If not, usually the base currency of the issue and receipt store documents is used for the recalculation.
- b.The user sets it manually.

## 23. ActiveLanguages
- a.Action: Displays the languages which are active in the current database. If there is no value, all languages are active (currently 15 languages are supported).
- b.Automatically by the form for editing the languages list, which opens from the Edit Languages menu.

## 24.  CheckForTransactionInvalidLotDisabled
- a.Action: When this key has value and this value is "1", the validation for an invalid lot in the store transaction on document release is not performed. An invalid lot is a lot that is defined for a product, different than the product in the store transaction line. In all other cases, the validation is performed.
- b.The user sets it manually

## 25. VisualPasteDisabled - suspended
- a.Action: When this key has value and this value is "1", when rows are pasted in a grid they are pasted all at the same time (as it was in version 2.3). In all other cases when rows are pasted in a grid, they are pasted visually - row by row and field by field. Every value is searched between allowed values in drop-down lists.
- b.The user sets it manually

> [!NOTE]
> *This key is suspended in version 2019.1. In its place there are two new functions in forms and navigators:*
> *- Paste Rows*
> *- Paste Rows Without On-Screen Validation*

## 26.  RealTimeEventsDisabled 
- a.When this key has value and this value is "1", @@name would not proceed connection with the server which sends real-time events.
- b.The user sets it manually

## 27. RealTimeEventsTimeoutSeconds
- a.Action: Sets the timeout period for waiting for a server response for real-time events, in seconds. If the server does not raise an event in the specified time, the client sends a new request. The value is a number between 5 and 240. If null, the timeout time is 240 seconds (4 minutes).
- b.The user sets it manually

## 28. Require strong passwords
- a.Action: When this key has value and this value is "1", strong password validation is performed. Strong password requirements are as follows:
    - the password is at least 8 characters;
    - the password contains characters from 3 out of 4 groups: small letters, capital letters, Nonalphanumeric characters, numbers; 
    - the password does not contain the username;
    - the password does not contain "123", "1234", "12345", "123456".     
- b.The user sets it manually

## 29. DisableAccountKeyPropertyDotCheck    
- a.Action: When this key has value and this value is "1", when an item key is formed in the accounting voucher rows the validation for no '.' (dot) in the values of the key custom, properties are not performed. For the normal working process of the system, it is important no dots to be part of the values of the key custom properties because the dot is a system character used for item key compilation.
- b.The user sets it manually

## 30. AllowPlannedDocumentStateInClient
- a.Action: When this key has value and this value is "1", the document state menu would contain Planned state. In all other cases, the user would not be able to select the Planned state on any document.
- b.The user sets it manually

## 31. DisableProductCopyPropertiesFromOtherProduct
- a.Action: When this key has value and this value is "1", the Product configurator feature for copying the values to custom properties from the custom property which values are products is deactivated.
- b.The user sets it manually

## 32. PaymentTransactionFiscalPrintChangeToState (DEPRECATED)
- a.This key specifies the document state to which a payment transaction is switched to after the receipt is printed. The key value is the numeric value of the document states (0 = New, 10 = Planned, 20 = FirmPlanned, 30 = Released, 40 = Completed). In all other cases, the payment transaction is switched to Released state.
- b.The user sets it manually.

## 33. Crm/Sales/SalesOrders/ShowFillLotsInLines  
- a.Action: When this key has value and this value is "1", the sales order function "Fill lots in lines" is activated.
- b.The user sets it manually.

## 34. General/Contacts/LoadCalendarForLimitedTime    
- a.Action: When this key has value and this value is "1", the calendar in the Activities navigator loads data only for the displayed period (+/- 1 month) when the user scrolls through the calendar. 
- b.The user sets it manually.

## 35. DisableDocumentRecalculationOnIdle
- a.Action: When this key has value and this value is "1", in the document forms the recalculation of additional amounts, bonus programs, payment plans and etc in real-time would not be performed (Application.Idle event). In such cases, the document would be recalculated only before the COMMIT event and not in real-time while the user enters the
- b.data in the document form. The method referred by the current key is "Document.Recalculate" which performs different actions in the different entities.
- c.The user sets it manually.

## 36. DisableParentDocumentReset
- a.Action: When this key has value and this value is "1", on document state change the parent document state is not reset.
- b.The user sets it manually.

## 37. RevokedBusinessRules   
- a.Action: When this key has value, the validation and the action of the business rules, which codes are specified as a key value, is not performed. The codes of the business rules must be listed comma-separated (for example 27407, 26881 ..). Since version 2018.2, business rules' codes must be set with their full code including "R" (eg R27408, R26881 ...). If the key value is changed, the client application requires a restart.
- b.The user sets it manually.

## 38. DisableQueryingForSaveOnClose    
- a.Action: When this key has value and this value is "1", on closing of a form which is not saved, if there is a change in any table of the form, no information message for saving or undo of the changes appears.
- b.The user sets it manually.

## 39. UseLegacyLoadForLotsIssue        
- a.Action: When this key has value and this value is "1", for the calculation of the quantity "Available to promise by lots" is used the method that was developed before Version 2018.2. In all other cases, is used the current for Version 2018.2 method which is advisable and has a better performance.
- b.The user sets it manually.

## 40. ReservedLicenses (not implemented/ cancelled)
    
## 41. EnableCreateGroupForUser
- a.Action: When this key has value and this value is "1" or "true" (case-insensitive), when creating a new user into the database a new group with the user’s name will be created automatically as well. 
- b.The user sets it manually.
- c.The key is introduced in version: - 2019.1 (in implementation)

> [!Note]
> Before version 2019.1 a new user group was created automatically every time when a new user is created and this behaviour could not be disabled. Since version 2019.1 the behaviour is disabled by default and could be activated manually using the current registry key.

## 42. DocumentVersioningSystem
- a.Action: When the value of this key is "VH" the system will use the "old" document versioning system. If the key's value is "TC" the system will not create records using the "old" document versioning system and will instead use the [Track changes](https://docs.erp.net/tech/advanced/track-changes.html) system. The minimum level that is going to be tracked when the "TC" option is activated is "Track Changes Level 3". If for the particular document entity is chosen a specific level, then this level will be applied only if it is a higher level than level 3. (For more information about the track changes system and its levels, please see topic [Track changes](https://docs.erp.net/tech/advanced/track-changes.html) 
       
>[!Note]
> Please note that the current key affects only entities which are a successor of document entity (such as sales orders, store orders ...) and NOT entities such as product groups, bonus programs..

- b.The user sets it manually, but if the key is not configured for the particular database or its value is different from "VH" or "TC", then the system will use the default value. The default value depends on the system version:
    - Version 2019.1 - the default value is "VH";
    - Version 2020.1 and later - the default value is "TC";
- c.The key is introduced in version: - 2019.1

## 43. Crm/Pos/PrintGroupedSalesLinesType
- a.Action: When the value of this key is "ShortName" then items in the fiscal receipt are grouped by "ShortName" field in the product. When the value of this key is "ProductGroup" then items in the fiscal receipt are grouped by the product group of the product. When the value of this key is different or the key is missing then items in the fiscal receipt are not grouped.
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
    - "1" - the form that is going to be opened when the program is started will be the Start screen. This applies to all users into the database, regardless of the "UseStartScreen" option.
    - "2" - the starting form will be the Main menu. This applies to all users into the database, regardless of the "UseStartScreen" option/key.
    - "0", different from "1" and "2" or the key is not configured for the particular database - there is no global policy. Each user decides whether they want to use the start screen using "UseStartScreen" option/key.
- b.The user sets it manually.
- c.The key is introduced in version: - 2020.1

## 46. UseDefaultMailClient

- a.Action: When this key has a value for the particular user and this value is "1", then when creating an email the system will start the default Windows mail client. This will apply even if there is a mailbox defined for the user. 
- b. The user sets it manually (directly in the registry or using the option available in tab File => Settings => Use default Windows mail client).
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
- a.When this key has value and this value is "1", all users can use basic authentication, regardless of their setting.
- b.The user sets it manually
- c.The key is introduced in version: - 2023

## 49. Calendar/TimePresets
- a.When this key has value and conforms to the format below, it overrides the time presets in the [calendar control](https://docs.erp.net/webclient/introduction/my-apps/calendar.html#time-presets).
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

## 54. WMS/WMS-Worker/SingleBarcodeScanEntersQuantityOfOnePce
- a.Action: When the value of this key is:
    - "1" - When Scan single barcode then this is accepted like 1 PCE
    - "0" - Wnen Scan single barcode then No quantity is accepted, the WMS-Worker APP just finds the line and goes to execute mode for this line.
- b.The user sets it manually.
- c.The key is introduced in version: - 23.2
