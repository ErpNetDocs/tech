# Dispatch task type

The Dispatch task type's purpose is to issue goods from the warehouse. It is usually used in Warehouse Order Lines that are a result of the document generation of the sales order document flow.

The Warehouse Order Lines with Dispatch task type can be executed using the the Orders menu in [WMS Worker](xref:wms-worker) or the Execute lines function of the Warehouse Order.

## Result

When executed, the system creates 1 Warehouse Transaction and 1 Document Fulfillment as follows:

* **Warehouse Transactions**

`````````
WarehouseOrder = WarehouseOrderLine.WarehouseOrder
 
WarehouseOrderLine = WarehouseOrderLine

TaskType = Dispatch

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
