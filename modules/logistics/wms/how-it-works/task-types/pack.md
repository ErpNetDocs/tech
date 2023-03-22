# Pack task type

Pack task type's purpose is to add Contents to a [Logistic Unit (LU)](/modules/logistics/wms/logistic-units/index.md)
The moving can be done as an ad hoc operation  using the [Pack](xref:pack-menu) menu of [WMS Worker](xref:wms-worker). 

## Result

The packing results in creating 2 Warehouse Transaction for each line of the LU's Contents. The first Warehouse Transaction is needed to issue of content before it was a part of a LU. The second performes the receipt of the content as a part of the LU.

**WarehouseTransaction1 for the issue of the content before it was a part of a LU**
`````````
WarehouseOrder = NULL
 
WarehouseOrderLine = NULL

TaskType = Pack

Direction = OUT
 
ManagedWarehouse = the current Warehouse
 
ManagedWarehouseLocation = the Warehouse Location specified during the packing
 
LogisticUnit = NULL
 
Product = the Product specified during the packing
 
ProductVariant = the Variant specified during the packing
 
Lot = the Lot specified during the packing
 
SerialNumber = the SerialNumber specified during the packing
 
Quantity = the Quantity specified during the packing
 
QuantityUnit = the QuantityUnit specified during the packing

QuantityBase = the QuantityBase specified during the packing

StandardQuantity = If Product.AllowVariableMeasurementRatios == true, then get QuantityBase, else CONVERT(Qauntity, BaseMeasurementUnit)
 
CreationUser = CurrentUser
 
CreationTimeUtc = NOW(Utc)
`````````
 

**WarehouseTransaction2 for the receipt of the content as a part of the LU**
`````````
WarehouseOrder = NULL
 
WarehouseOrderLine = NULL

TaskType = Pack

Direction = IN
 
ManagedWarehouse = the current Warehouse
 
ManagedWarehouseLocation = the Warehouse Location specified during the packing
 
LogisticUnit = the LU specified or created during the packing
 
Product = the Product specified during the packing
 
ProductVariant = the Variant specified during the packing
 
Lot = the Lot specified during the packing
 
SerialNumber = the SerialNumber specified during the packing
 
Quantity = the Quantity specified during the packing
 
QuantityUnit = the QuantityUnit specified during the packing

QuantityBase = the QuantityBase specified during the packing

StandardQuantity = If Product.AllowVariableMeasurementRatios == true, then get QuantityBase, else CONVERT(Qauntity, BaseMeasurementUnit)
 
CreationUser = CurrentUser
 
CreationTimeUtc = NOW(Utc)
