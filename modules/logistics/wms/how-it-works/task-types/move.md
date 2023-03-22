# Move task type

Move task type's purpose is to move goods from one warehouse location to another location within the same warehouse. 

The moving can be done as an ad hoc operation or can be performed as a part of a Warehouse Order. As an ad hoc (single) operation it is performed using the [Move](xref:wms-worker-move) menu of [WMS Worker](xref:wms-worker). While Warehouse Order Lines with Move task type can be executed using the Orders menu in [WMS Worker](xref:wms-worker) or the Execute lines function of the Warehouse Order.

## Result

The moving results in creating 2 Warehouse Transaction - 1 for the goods issue of the previous location and 1 for the goods receipt into the destination location.
A Document Fulfillment will be created as well, but only if the moving is performed trough executing a Warehouse Order Line.

The Warehouse Transactions and the Document Fulfillment are created as follows:

* **Warehouse Transactions**

**WarehouseTransaction1 for the goods issue**
`````````
WarehouseOrder = if it is an ad hoch operation, then NULL, else WarehouseOrderLine.WarehouseOrder
 
WarehouseOrderLine = if it is an ad hoch operation, then NULL, else WarehouseOrderLine

TaskType = Move

Direction = OUT
 
ManagedWarehouse = WarehouseOrderLine.WarehouseOrder.ManagedWarehouse
 
ManagedWarehouseLocation = the Warehouse Location specified during the line execution
 
LogisticUnit = the LogisticUnit specified during the line execution 
 
Product = the Product specified during the line execution 
 
ProductVariant = the Variant specified during the line execution 
 
Lot = the Lot specified during the line execution 
 
SerialNumber = the SerialNumber  specified during the line execution 
 
Quantity = the Quantity specified during the line execution
 
QuantityUnit = the QuantityUnit specified during the line execution 

QuantityBase = the QuantityBase specified during the line execution 

StandardQuantity = If Product.AllowVariableMeasurementRatios == true, then get QuantityBase, else CONVERT(Qauntity, BaseMeasurementUnit)
 
CreationUser = CurrentUser
 
CreationTimeUtc = NOW(Utc)
`````````
 

**WarehouseTransaction2 for the goods receipt**
`````````
WarehouseOrder = if it is an ad hoch operation, then NULL, else WarehouseOrderLine.WarehouseOrder
 
WarehouseOrderLine = if it is an ad hoch operation, then NULL, else WarehouseOrderLine

TaskType = Move

Direction = IN
 
ManagedWarehouse = WarehouseOrderLine.WarehouseOrder.ManagedWarehouse
 
ManagedWarehouseLocation = ManagedWarehouseLocation = the Destination Location set during the line execution
 
LogisticUnit = the LogisticUnit specified during the line execution 
 
Product = the Product specified during the line execution 
 
ProductVariant = the Variant specified during the line execution 
 
Lot = the Lot specified during the line execution 
 
SerialNumber = the SerialNumber  specified during the line execution 
 
Quantity = the Quantity specified during the line execution
 
QuantityUnit = the QuantityUnit specified during the line execution 

QuantityBase = the QuantityBase specified during the line execution 

StandardQuantity = If Product.AllowVariableMeasurementRatios == true, then get QuantityBase, else CONVERT(Qauntity, BaseMeasurementUnit)
 
CreationUser = CurrentUser
 
CreationTimeUtc = NOW(Utc)

`````````
 

* **Document Fulfillment**
`````````
Document = WarehouseOrder
 
DocumentLineId = WarehouseOrderLineId
 
LineNo = WarehouseOrderLine.LineNo
 
FulfillmentType = Completed
 
IsFinal = false
 
LineType = Line

Product = the Product specified during the line execution 
 
ProductVariant = the Variant specified during the line execution 
 
Lot = the Lot specified during the line execution 
 
SerialNumber = the SerialNumber  specified during the line execution
 
QuantityBase = the QuantityBase specified during the line execution 

StandardQuantity = If Product.AllowVariableMeasurementRatios == true, then get QuantityBase, else CONVERT(Qauntity, BaseMeasurementUnit)

CreationUser = CurrentUser

CreationTimeUtc = NOW(Utc)

DestinationEntityName = Wms_Warehouse_Transactions
`````````
