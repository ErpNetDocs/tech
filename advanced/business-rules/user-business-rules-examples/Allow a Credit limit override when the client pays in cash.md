
# Allow a Credit Limit Override When the Client Pays in Cash

If we know when the 'System type' from 'Payment type' (Sales Order document) is set to be 'In cash', we can use that information to create a Business Rule that inserts a check mark in the field 'Credit Limit Override'.

In this particular case we can get that information using the calculated attribute 'Check If the System type of Payment type in the Sales Order is 'In Cash'', which returns True or False.

To allow a 'Credit Limit Override' when the client pays in cash, we can create a Business Rule with the following data:

|Repository
|:----
|Crm.Sales.SalesOrders

|**Events**
|:-----

|Event Type|Event Parameter|ExecutionPriority
|:----|:----|:----
|Change of State|RELEASING|Normal

|Conditions
|:-----

|Condition No|Attribute Name|Comparison Type|Value
|:-----|:-----|:----|:-----
|1|#IsInCash|=|True|

|Actions
|:-----

|Action No|Action Type|Parameter1 Type|Parameter1 Value|Parameter2 Type|Parameter1 Value
|:----|:----|:----|:----|:----|:-----
|1|SETVALUE|Attribute|CreditLimitOverride|Constant|True

> [!Note:] '#IsInCash' is a **Calculated Attribute**. >For more information, see '**Check If the System >type of Payment type in the Sales Order Is 'In >Cash'**'.
