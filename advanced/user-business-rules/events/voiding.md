# VOIDING
#### EVENT SUMMARY
|Name|VOIDING
|:----|:----
|**Layer**| Back-End
|**Description**| Occurs during the voiding of a document.
|**Version**| Introduced: 2019.1 <br> Updated: -

The VOIDING event is introduced in version 2019.1.

It is recommended only when the Business Rule's Repository is a document header - Crm.Sales.SalesOrders, Logistics.Inventory.StoreOrders...

The VOIDING event may be used to prohibit voiding (by using **[FAIL](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-business-rules/action-types/fail.md)** action) when certain conditions are met or not met. For example, the rule may throw an error when voiding a Sales order that has already been **FIRMPLANNED**.
