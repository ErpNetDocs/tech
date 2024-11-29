---
items: UserBusinessRuleExamples
---

# Allow a credit limit override when a client pays in cash

If the system type of a payment type in a sales order document is set as 'In cash', you can create a **[business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** that inserts a check mark in the field *Credit Limit Override*.

You can get that information using **[this](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html)** calculated attribute, which returns 'True' or 'False'.

To set a rule to allow a credit limit override when a client pays in cash, use the following data:

|Repository|
|:----|
|Crm.Sales.SalesOrders

|Events|
|:-----|

|Event type|Event parameter|Execution priority
|:----|:----|:----
|Change of State|RELEASING|Normal

|Conditions|
|:-----|

|Condition No|Attribute name|Comparison type|Value
|:-----|:-----|:----|:-----
|1|#IsInCash|=|True|

|Actions|
|:-----|

|Action No|Action type|Parameter1 type|Parameter1 value|Parameter2 type|Parameter1 value
|:----|:----|:----|:----|:----|:-----
|1|SETVALUE|Attribute|CreditLimitOverride|Constant|True

> [!NOTE] 
> 
> '#IsInCash' is a **[calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)**. 
> 
> For more information, see **[Check if the system type of payment type in a sales order is 'In cash'](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html)**.
