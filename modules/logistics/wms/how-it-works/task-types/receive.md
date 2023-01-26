# Receive task type

Receive task type's purpose is to receipt new goods into the warehouse. It is usually used in Warehouse Order Lines that are a result of the document generation of the procurement document flow.

The Warehouse Order Lines with Receive task type can be executed using the [WMS Worker](xref:wms-worker) or the Execute lines function.

## Result

When executed, the system creates 1 Warehouse Transaction and 1 Document Fulfillment as follows:

* **Warehouse Transactions**

`````````
WarehouseOrder = WarehouseOrderLine.WarehouseOrder
 
WarehouseOrderLine = WarehouseOrderLine

TaskType = Receive

Direction = IN
 
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
