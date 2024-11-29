---
uid: voiding
items: events
---

# VOIDING

<br>

|Name|VOIDING
|:----|:----
|**Layer**| Back-end
|**Description**| Occurs during the voiding of a document.
|**Version**| Introduced: 2019.1 <br> Updated: -

This event is recommended only when the **[business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** repository is a **document header** - Crm.Sales.SalesOrders, Logistics.Inventory.StoreOrders...

VOIDING may prohibit voiding using **[FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html)** when certain conditions are met. For example, the rule could throw an error when a sales order that's already been FIRMPLANNED is being voided.
