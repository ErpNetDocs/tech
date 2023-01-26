# Kit task type

The Kit task type is used when working with @composite-products. It can usually be seen in Warehouse Order Lines that are a result of the document generation of the sales order document flow when it contains composite products.

The purpose of the Kit task type is to report the kitting (dispatching) of the composite product to the parent line and to carry out control. 

The Kit task type lines do NOT create Warehouse Transactions, as the availability of the composite product itself is kept in the Inventory module. 
Though, the Kit line's purpose is very important because it creates DocumentFulfillments to the parent line. It informs it that all components of the composite product's kit are dispatched and therefore the parent line is fullfilled.

The control during the kitting process depends on the specified level. For more information, see @levels.

The Warehouse Order Lines with Kit task type can be executed using the WMS Worker or the Execute lines function.

## Result
The Kit task type lines do NOT create Warehouse Transaction, as the availability of the composite product is kept in the Inventory module. 
It creates only a DocumentFulfillment, as follows:

`````````
Document = WarehouseOrder

DocumentLineId = WarehouseOrderLineId

LineNo = WarehouseOrderLine.LineNo

FulfillmentType = Completed

IsFinal = false

LineType = Line

QuantityBase = WarehouseOrder.QuantityBase

StandardQuantity = WarehouseOrder.StandardQuantity

Product = WarehouseOrder.Product

Lot = WarehouseOrder.Lot

SerialNumber = WarehouseOrder.SerialNumber

ProductVariant = WarehouseOrder.ProductVariant

CreationUser = CurrentUser

CreationTimeUtc = NOW(Utc)

DestinationEntityName = n/a

`````````
