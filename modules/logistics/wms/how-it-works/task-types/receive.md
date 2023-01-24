# Receive task type

Receive task type is used receipt of new goods into the warehouse. 

The Warehouse Order Lines with Receive task type can be executed using the @wms-worker or the Execute lines function.

When executed, the system creates 1 Warehouse Transaction and 1 Document Fulfillment as follows:

* **Warehouse Transactions**

`````````
WarehouseTransaction.WarehouseOrder = WarehouseOrderLine.WarehouseOrder
 
WarehouseTransaction.WarehouseOrderLine = WarehouseOrderLine
 
WarehouseTransaction.ManagedWarehouse = WarehouseOrderLine.WarehouseOrder.ManagedWarehouse
 
WarehouseTransaction.ManagedWarehouseLocation = the Warehouse Location set during the line execution
 
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
 
DocumentFulfillment.QuantityBase = the Quantity set during the line execution DocumentFulfillment.CreationUser = CurrentUser

DocumentFulfillment.DestinationEntityName = Wms_Warehouse_Transactions
`````````
