# Document Fulfillment

## Description

Fulfillment is related to the document generation.
Fulfillment makes sure that all quantities and amounts from the parent document are transferred to the sub-document.

Differences in quantities and amounts between the parent and the sub-document require fulfillment.
Documents in @@name usually require complete fulfillment before their state can be set to Completed.

## Fulfillment documents

A document is fulfilled with another document.
For example:

* [Shipment Order](xref:Logistics.Shipment.ShipmentOrders) is fulfilled by creating a [Shipment](xref:Logistics.Shipment.Shipments).
* [Invoice Order](xref:Crm.Invoicing.InvoiceOrders) is fulfilled by creating an [Invoice](xref:Crm.Invoicing.Invoices).
* ...and so on.

As can be seen in the example, different document entity types usually come (at least) in pairs - orders and execution pairs of entity types.
Actually, more and more entity types come in triples - requisition, order and transaction; but that is a different discussion.

> [!note]
> Order documents naturally require fulfillment, which is recorded as execution documents.

## Discrepancies in quantities and amounts between the parent and the sub-document(s)

Quantities and amounts in a sub-document may not always represent an exact execution of the parent document.
Why there are differences between the parent and the sub-document?

Differences can arise for many reasons:

* Partial execution. For example, we shipped goods partially. In this case, the Shipment does not completely fulfill the Shipment Order.
* Partial payment by customer.
* Adjustments to the parent document, because of processing errors.
* Adjustments to the parent document, by customer request.
* Adjustments to the sub-document.
* etc.

All these cases require fulfillment before the document state can be set to Completed.

## Fulfillment tracking

Fulfillment tracking is the process of calculating what remains to be fulfilled and how it is divided in the terms of detail lines.

For example, a Sales Order from a customer requests shipment of 10 Oranges.
We shipped 8 Oranges and 2 Tangerines.
Did we fulfill the Sales Order?

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
* Product Variant
* Lot
* Serial Number

So, let’s review the previous example in the light of natural matching.

Sales Order:

* Line 1: Oranges, 10 kg

Shipment:
	
* Line 1: Oranges, 8 kg
* Line 2: Tangerines, 2 kg

Natural matching will not qualify the shipment of Tangerines as execution of the sale of Oranges, because it is a different Product.
Even if the customer agrees to accept the Tangerines, we cannot represent this in the system.

Another example.
The customer might order specific lot of the product, but they are ready to accept another lot:

* Sales Order: 10 Oranges, lot 202
* Shipment: 10 Oranges, lot 203

This shipment satisfies the customer in the real world.
However, using natural tracking, this will be considered a severe difference.
The system will propose reversal of the shipment of lot 203 and shipment again of lot 202.
Obviously, this is problematic and might confuse the users.

Even more problematic, and more real-world example if two or more lines of the Sales Order contain oranges.
In this case, natural matching simply does not work well.

The benefit of natural matching is that it does not require special (artificial) tracking attributes or tables.
However, it does not work well for some real-world scenarios.

Natural matching is used in document generations, created in the earlier stages of @@name, but is mostly abandoned in newer developments.

### Parent line

Parent line is widely used algorithm in @@name for keeping track of the execution.

The idea is simple: The sub-document keeps reference to the parent line, which is being executed.

For example:

Sales Order:

* Line 1: Oranges, 10 kg
* Line 2: Apples, 2 pcs

Shipment:

* Line 1: Oranges, 8 kg, Parent Line = 1
* Line 2: Tangerines, 2 kg, Parent Line = 1
* Line 3: Pears, 2 pcs, Parent Line = 2

Here, we can see that, although we sent Tangerines, they replace the Oranges.
And we sent exactly the missing quantity.
And we sent Pears, instead of Apples.

> [!note]
> The measurement unit of the sub-document line should be the same as the parent line.

Of course, all this has to be arranged with the customer.
The important thing is that, once arranged with the customer, we have to represent in it in the system.
Parent line system allows that.

### Fulfillment table

As good as parent line algorithm is, it cannot be used in all places.
There are cases, where it might simply be impossible or very hard to match all sub-document lines using only parent line.

For example, in the WMS, suppose we have the following:

Warehouse Requisition:

* Line 1: Despatch Oranges, 10 pcs
* Line 2: Despatch Apples, 2 pcs

In the optimization phase, the WMS has created the following plan:

Warehouse Order:

* Line 1: Pick Oranges, 30 pcs (because there are also other orders and all will be sorted out on the packing table)
* Line 2: Pick Apples, 2 pcs
* Line 3: Move everything to packing table 3.

Obviously, we have a problem here establishing a direct relationship with the parent document.

The solution is to use Fulfillment table.
The fulfillment table is like a notebook, in which we record how much of the quantity has already been created for the sub-document.
This allows the system to create complicated sub-documents, without tracking the direct relationship of the created lines with the parent lines.

In this example, after creating the Warehouse Order, the fulfillment table will contain:

* Warehouse Requisition XXX, Execution of Line 1: Qty:10
* Warehouse Requisition XXX, Execution of Line 2: Qty:2

The fulfillment table simply contains the executed quantities, without any regard of how they are executed.
It does not contain any reference to the sub-document(s).
The system tracks the execution, without specifically deciphering the sub-document(s) contents.

The fulfillment table algorithm allows the application of complex algorithms for execution.
These algorithms do not need to represent the parent document lines 1:1 with the sub-document lines and hence have the freedom to employ complex optimization techniques.
