# WMS features 

This section highlights the latest improvements in WMS, bringing together new functionality, process enhancements, and usability updates across warehouse operations.

## Improved Inventory reconciliation from WMS

The **Add the reconciliation lines from the WMS module** function has been improved to offset equivalent reconciliation adjustments coming from WMS.

The function processes eligible **Warehouse Transactions** with **TaskType = Reconciliation** and groups them by **Product, ProductVariant, Lot, and SerialNumber**, while ignoring differences in **WarehouseLocation** and **LogisticUnit**.

For each group, the values of **Quantity, QuantityBase, and StandardQuantity** from all matching Warehouse Transactions are combined into a single net result. This allows opposite WMS adjustments for the same product to compensate each other even when they were performed in different warehouse locations or logistic units.

A separate Inventory Reconciliation line is still created and linked for every processed Warehouse Transaction. One line carries the calculated group totals, while the remaining linked lines contain zero quantities. These zero-value lines keep the corresponding Warehouse Transactions marked as already processed, so they are not included again in a later transfer.

The function can be used for reconciliation adjustments created through different WMS processes, including **Planned Reconciliation** and **Quick Reconcile**.

See:
- [Planned Reconcile](https://docs.erp.net/tech/modules/logistics/wms/planned-reconcile/index.html)
- [Transfer the result to inventory reconciliation](transfer-the-result-to-inventory-reconciliation.md)
