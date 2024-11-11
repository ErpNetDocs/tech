# Count task type

Count task types are used for warehouse reconciliation.

The reconciliation is performed as an ad hoc (single) operation using the [Reconcile](xref:wms-worker-reconcile) menu of [WMS Worker](xref:wms-worker).

## Result

As a result the reconciliation generates Warehouse Transaction with Count task type. The Warehouse Transaction can be with IN or OUT direction, depending on the difference between the avalability before and after the reconciliation.If the counted quantity is exactly the available quantity for this reconciled operation, then the warehouse transaction will be entered in the direction IN with zero quantity. This is useful for checking the reconciled results.

> [!NOTE]
> If the counted product uses varible measurement ratios, then Warehouse Transaction will be created in the default Measurement Unit of the product, instead of the Base Unit. <br/> This is needed, because the variable quantity measured during the reconciliation could be (and ususally is) different from the standard measurement ratios. But but this is a contradiction to the rule that Quantity and Standard Quantity values must always follow the measurement rations. For this reason, the Quantity is converted to the default Measurement Unit of the product.


