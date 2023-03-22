# Unpack task type

Unack task type's purpose is to unpack the Contents of an Logistic Unit [Logistic Unit (LU)](/modules/logistics/wms/logistic-units/index.md).

The packing is performed as an ad hoc operation using the [Unpack](xref:unpack-menu) menu of [WMS Worker](xref:wms-worker). 

## Result

The packing results in creating 2 Warehouse Transaction for each line of the LU's availability. The first Warehouse Transaction is needed to issue the products which are no longer the contents of a logistic unit, at the specified destination location.

**WarehouseTransaction1 for the issue of the content from the LU:**
`````````
WarehouseOrder = NULL
 
WarehouseOrderLine = NULL

TaskType = Unpack

Direction = OUT
 
ManagedWarehouse = the current Warehouse
 
ManagedWarehouseLocation = the Warehouse Location specified during the unpacking
 
LogisticUnit = the LU specified during the unpacking
 
Product = the available Product 
 
ProductVariant = the available Variant 
 
Lot = the available Lot
 
SerialNumber = the available SerialNumber
 
Quantity = QuantityBaseAvailable
 
QuantityUnit = BaseUnit 

QuantityBase = QuantityBaseAvailable

StandardQuantity = StandardQuantityAvailable
 
CreationUser = CurrentUser
 
CreationTimeUtc = NOW(Utc)
`````````
 

**WarehouseTransaction2 for the receipt the products that are no longer a part of the LU:**
`````````
WarehouseOrder = NULL
 
WarehouseOrderLine = NULL

TaskType = Unpack

Direction = IN
 
ManagedWarehouse = the current Warehouse
 
ManagedWarehouseLocation = the Destination location specified during the unpacking
 
LogisticUnit = NULL
 
Product = the available Product 
 
ProductVariant = the available Variant 
 
Lot = the available Lot
 
SerialNumber = the available SerialNumber
 
Quantity = QuantityBaseAvailable
 
QuantityUnit = BaseUnit 

QuantityBase = QuantityBaseAvailable

StandardQuantity = StandardQuantityAvailable
 
CreationUser = CurrentUser
 
CreationTimeUtc = NOW(Utc)
