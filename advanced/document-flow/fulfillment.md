# Document fulfillment

Fulfillment is related to the document generation.
Fulfillment makes sure that all quantities and amounts from the parent document are transferred to the sub-document.

Differences in quantities and amounts between the parent and the sub-document require fulfillment.
Documents in @@name usually require complete fulfillment before their state can be set to Completed.

## Fulfillment documents

A document is fulfilled with another document.
For example:

* [Shipment order](xref:Logistics.Shipment.ShipmentOrders) is fulfilled by creating a [shipment](xref:Logistics.Shipment.Shipments).
* [Invoice order](xref:Crm.Invoicing.InvoiceOrders) is fulfilled by creating an [invoice](xref:Crm.Invoicing.Invoices).
* ...and so on.

As can be seen in the example, different document entity types usually come (at least) in pairs - orders and execution pairs of entity types.
Actually, more and more entity types come in triples - requisition, order and transaction; but that is a different discussion.

> [!note]
> Order documents naturally require fulfillment, which is recorded as execution documents.

## Discrepancies in quantities and amounts between the parent and the sub-document(s)

Quantities and amounts in a sub-document may not always represent an exact execution of the parent document.
Why there are differences between the parent and the sub-document?

Differences can arise for many reasons:

* Partial execution. For example, we shipped goods partially. In this case, the shipment does not completely fulfill the shipment order.
* Partial payment by customer.
* Adjustments to the parent document, because of processing errors.
* Adjustments to the parent document, by customer request.
* Adjustments to the sub-document.
* etc.

All these cases require fulfillment before the document state can be set to Completed.

## Fulfillment tracking

Fulfillment tracking is the process of calculating what remains to be fulfilled and how it is divided in the terms of detail lines.

For example, a sales order from a customer requests shipment of 10 oranges.
We shipped 8 oranges and 2 tangerines.
Did we fulfill the sales order?

The system tracks the fulfillment of a document, using several tracking techniques:

* Natural matching
* Parent line
* Fulfillment table

### Natural matching

Natural matching matches the parent and the sub-documents, based on natural attribute values.

> [!note]
> Natural attributes are attributes, representing real-world things.
> This is in contrast with artificial attributes, which are required by the inner workings of the software system.

In the example above, natural matching will compare the values of:

* Product
* Product variant
* Lot
* Serial number

So, let’s review the previous example in the light of natural matching.

sales order:

* line 1: oranges, 10 kg

shipment:
	
* line 1: oranges, 8 kg
* line 2: tangerines, 2 kg

Natural matching will not qualify the shipment of tangerines as execution of the sale of oranges, because it is a different product.
Even if the customer agrees to accept the tangerines, we cannot represent this in the system.

Another example.
The customer might order specific lot of the product, but they are ready to accept another lot:

* sales order: 10 oranges, lot 202
* shipment: 10 oranges, lot 203

This shipment satisfies the customer in the real world.
However, using natural tracking, this will be considered a severe difference.
The system will propose reversal of the shipment of lot 203 and shipment again of lot 202.
Obviously, this is problematic and might confuse the users.

Even more problematic, and more real-world example if two or more lines of the sales order contain oranges.
In this case, natural matching simply does not work well.

The benefit of natural matching is that it does not require special (artificial) tracking attributes or tables.
However, it does not work well for some real-world scenarios.

Natural matching is used in document generations, created in the earlier stages of @@name, but is mostly abandoned in newer developments.

### Parent line

Parent line is widely used algorithm in @@name for keeping track of the execution.

The idea is simple: The sub-document keeps reference to the parent line, which is being executed.

For example:

Sales order:

* line 1: oranges, 10 kg
* line 2: apples, 2 pcs

shipment:

* line 1: oranges, 8 kg, parent line = 1
* line 2: tangerines, 2 kg, parent line = 1
* line 3: pears, 2 pcs, parent line = 2

Here, we can see that, although we sent tangerines, they replace the oranges.
And we sent exactly the missing quantity.
And we sent pears, instead of apples.

> [!note]
> The measurement unit of the sub-document line should be the same as the parent line.

Of course, all this has to be arranged with the customer.
The important thing is that, once arranged with the customer, we have to represent in it in the system.
parent line system allows that.

### Fulfillment table

As good as parent line algorithm is, it cannot be used in all places.
There are cases, where it might simply be impossible or very hard to match all sub-document lines using only parent line.

For example, in the WMS, suppose we have the following:

Warehouse requisition:

* line 1: despatch oranges, 10 pcs
* line 2: despatch apples, 2 pcs

In the optimization phase, the WMS has created the following plan:

Warehouse order:

* line 1: pick oranges, 30 pcs (because there are also other orders and all will be sorted out on the packing table)
* line 2: pick apples, 2 pcs
* line 3: move everything to packing table 3.

Obviously, we have a problem here establishing a direct relationship with the parent document.

The solution is to use Fulfillment table.
The fulfillment table is like a notebook, in which we record how much of the quantity has already been created for the sub-document.
This allows the system to create complicated sub-documents, without tracking the direct relationship of the created lines with the parent lines.

In this example, after creating the warehouse order, the fulfillment table will contain:

* Warehouse requisition XXX, execution of line 1: Qty:10
* Warehouse requisition XXX, execution of line 2: Qty:2

The fulfillment table simply contains the executed quantities, without any regard of how they are executed.
It does not contain any reference to the sub-document(s).
The system tracks the execution, without specifically deciphering the sub-document(s) contents.

The fulfillment table algorithm allows the application of complex algorithms for execution.
These algorithms do not need to represent the parent document lines 1:1 with the sub-document lines and hence have the freedom to employ complex optimization techniques.
