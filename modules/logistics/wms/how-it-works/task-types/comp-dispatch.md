# Component Dispatch task type 
The Component Dispatch task type is used when working with @composite-products. 

Its purpose is to issue the composite product's components from the warehouse. 
It can usually be seen in Warehouse Order Lines that are a result of the document generation of the sales order document flow when it contains composite products.

## Result
The Component Dispatch lines do NOT create Document Fulfillments, as they represent the dispatching of 1 component of a whole kit. The fulfillment is trigerred by the dispatching of the whole kit and it is performed trough the [Kit](kit.md) task type line.

When executed, the system creates only a Warehouse Transaction, as follows:

`````````
WarehouseOrder = WarehouseOrderLine.WarehouseOrder
 
WarehouseOrderLine = WarehouseOrderLine

TaskType = ComponentDispatch

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
