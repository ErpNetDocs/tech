# VOIDING
#### EVENT SUMMARY
|Name|VOIDING
|:----|:----
|**Layer**| Back-End
|**Description**| Occurs during the voiding of a document.
|**Version**| Introduced: 2019.1 <br> Updated: -

The VOIDING event is introduced in version 2019.1.

Occurs when a document is being voided. Note that the use of the event is meaningful only when the Business Rule's Repository is a document header - Crm.Sales.SalesOrders, Logistics.Inventory.StoreOrders ... .

The VOIDING event may be used, for example, to prohibit voiding (by using **[FAIL](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/action-types/fail.md)** action) when particular conditions are or are not met. For example, the rule may throw an error when voiding a Sales order that has already been FIRMPLANNED.
