# Move task type

Move task type to move goods from one warehouse location to another location within the same warehouse. 

The moving can be done as an ad hoc operation or can be performed as a part of a Warehouse Order.

As an ad hoc (single) operation it is performed using the @wms-worker-move menu of @wms-worker. 

While Warehouse Order Lines with Move task type can be executed using the Orders menu in @wms-worker or the Execute lines function of the Warehouse Order.

The moving results in creating 2 Warehouse Transaction - 1 for the goods issue of the previous location and 1 for the goods receipt into the destination location.
A Document Fulfillment will be created as well, but only if the moving is performed trough executing a Warehouse Order Line.

The Warehouse Transactions and the Document Fulfillment are created as follows:

* **Warehouse Transactions**

*  WarehouseTransaction1 for the goods issue
`````````
WarehouseTransaction.WarehouseOrder = WarehouseOrderLine.WarehouseOrder

WarehouseTransaction.WarehouseOrderLine = WarehouseOrderLine

WarehouseTransaction.ManagedWarehouse = WarehouseOrderLine.WarehouseOrder. ManagedWarehouse

WarehouseTransaction.ManagedWarehouseLocation = the Warehouse Location set during the line execution

WarehouseTransaction.LogisticUnit = WarehouseOrderLine.LogisticUnit

WarehouseTransaction.Product = the Product set during the line execution

WarehouseTransaction.ProductVariant = WarehouseOrderLine.ProductVariant

WarehouseTransaction.Lot = WarehouseOrderLine.Lot

WarehouseTransaction.SerialNumber = WarehouseOrderLine.SerialNumber

WarehouseTransaction.Direction = OUT

WarehouseTransaction.Quantity = the Quantity set during the line execution

WarehouseTransaction.QuantityUnit = WarehouseOrderLine.QuantityUnit

WarehouseTransaction.CatchQuantity = null

WarehouseTransaction.CreationUser = CurrentUser

WarehouseTransaction.CreationTimeUtc = NOW(Utc)
`````````
 

* WarehouseTransaction2
`````````
WarehouseTransaction.WarehouseOrder = WarehouseOrderLine.WarehouseOrder

WarehouseTransaction.WarehouseOrderLine = WarehouseOrderLine

WarehouseTransaction.ManagedWarehouse = WarehouseOrderLine.WarehouseOrder. ManagedWarehouse

WarehouseTransaction.ManagedWarehouseLocation = WarehouseOrderLine.ToWarehouseLocation

WarehouseTransaction.LogisticUnit = WarehouseOrderLine.LogisticUnit

WarehouseTransaction.Product = the Product set during the line execution

WarehouseTransaction.ProductVariant = WarehouseOrderLine.ProductVariant

WarehouseTransaction.Lot = WarehouseOrderLine.Lot

WarehouseTransaction.SerialNumber = WarehouseOrderLine.SerialNumber

WarehouseTransaction.Direction = IN

WarehouseTransaction.Quantity = the Quantity set during the line execution

WarehouseTransaction.QuantityUnit = WarehouseOrderLine.QuantityUnit

WarehouseTransaction.CatchQuantity = null

WarehouseTransaction.CreationUser = CurrentUser

WarehouseTransaction.CreationTimeUtc = NOW(Utc)
`````````
 

* **Document Fulfillment**
`````````
DocumentFulfillment.Document = WarehouseOrder

DocumentFulfillment.DocumentLineId = WarehouseOrderLineId

DocumentFulfillment.LineNo = WarehouseOrderLine.LineNo

DocumentFulfillment.FulfillmentType = Completed

DocumentFulfillment.IsFinal = false

DocumentFulfillment.LineType = Line

DocumentFulfillment.QuantityBase = the Quantity set during the line execution 

DocumentFulfillment.CreationUser = CurrentUser

DocumentFulfillment.DestinationEntityName = Wms_Warehouse_Transactions
`````````
