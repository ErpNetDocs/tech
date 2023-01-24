# Count task type

Count task types are used for warehouse reconciliation.

The reconciliation is performed as ad hoc (single) operation using the @wms-worker-reconcile menu of @wms-worker.

As a result the reconciliation generates Warehouse Transaction with Count task type. The Warehouse Transaction can be with IN or OUR direction, depending on the difference between the avalability before and after the reconciliation.

> [!NOTE]
> If the counted product uses varible measurement ratio, then Warehouse Transaction will be created in the default Measurement Unit of the product, instead of the Base Unit. This is needed, because the variable quantity measured during the reconciliation could be (and ususally is) different from the standard measurement ratios. But but this is a contradiction to the rule that Quantity and Standard Quantity values must always follow the measurement rations. For this reason, the Quantity is converted to the default Measurement Unit of the product.
