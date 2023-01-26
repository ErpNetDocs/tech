# Dekit task type
The Dekit task type is used when working with @composite-products. It can usually be seen in Warehouse Order Lines that are a result of the document generation of the procurement document flow when it contains composite products.

The purpose of the Dekit task type is to report the dekitting (receiving) of the composite product to the parent line and to carry out control.

The Dekit task type lines do NOT create Warehouse Transactions, as the availability of the composite product itself is kept in the Inventory module. Though, the Dekit line's purpose is very important because it creates DocumentFulfillments to the parent line. It informs it that all components of the composite product are received and therefore the parent line is fullfilled.

The control during the dekitting process depends on the specified level. For more information, see @levels.

The Warehouse Order Lines with Dekit task type can be executed using the WMS Worker or the Execute lines function.
Note that Dekit lines can only be executed after all of its components' receive lines have completed execution.

## Result
The Dekit task type lines do NOT create Warehouse Transaction, as the availability of the composite product is kept in the Inventory module. 
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
