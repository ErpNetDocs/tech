# Allow a credit limit override when a client pays in cash

If we know when the 'system type' from 'payment type' (sales order document) is set as 'in cash', we can use that information to create a Business rule that inserts a check mark in the field *Credit Limit Override*.

We can get that information using [this](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html) calculated attribute, which returns True or False.

To allow a credit limit override when a client pays in cash, we can create a Business Rule with the following data:

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

> [!Note] 
> '#IsInCash' is a [Calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html). 
> 
> For more information, see [Check if the system type of payment type in the sales order is 'In cash'](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-system-type-is-in-cash.html).
