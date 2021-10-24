# VOIDING
## Event summary
|Name|VOIDING
|:----|:----
|**Layer**| Back-End
|**Description**| Occurs during the voiding of a document.
|**Version**| Introduced: 2019.1 <br> Updated: -

The VOIDING event is introduced in version 2019.1.

It is recommended only when the business rule's repository is a document header - Crm.Sales.SalesOrders, Logistics.Inventory.StoreOrders...

The VOIDING event may be used to prohibit voiding (by using [FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html) action) when certain conditions are met or not met. For example, the rule may throw an error when voiding a Sales order that has already been **FIRMPLANNED**.
