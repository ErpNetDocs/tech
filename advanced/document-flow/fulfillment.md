# Document fulfillment

Fulfillment is related to document generation and makes sure that all quantities and amounts from a parent document are transferred to a sub-document.

Differences in quantities and amounts between parent and sub-documents require fulfillment.
Documents in @@name usually require **total** fulfillment before their state can be set to 'Completed'.

## Fulfillment documents

A document is fulfilled with another document.

For example:

- A **shipment order** is fulfilled by creating a shipment.
- An **invoice order** is fulfilled by creating an invoice.

Different document entity types usually come in **pairs**: orders and execution of entity types.

More and more entity types come in **triples** - requisition, order and transaction.

> [!NOTE]
> 
> Order documents naturally require fulfillment, which is recorded as 'execution documents'.

### Discrepancies in quantities and amounts between the parent and the sub-document(s)

Quantities and amounts in a sub-document may not represent an exact execution of a parent document.

Differences between parent and sub-documents can arise for many reasons:

- Partial execution. 
 
For example, you shipped goods partially. 

In this case, the shipment **doesn't** fulfill the shipment order.

- Partial payment by customer.

- Adjustments to the parent document due to processing errors.
								
- Adjustments to the parent document by customer request.

- Adjustments to the sub-document.

All these cases require fulfillment **before** the document state can be set to 'Completed'.

### Fulfillment tracking

This process calculates what remains for fulfillment and how it's divided in terms of detail lines.

For example, a sales order from a customer requests shipment of 10 oranges.

8 oranges and 2 tangerines were shipped.

Did you fulfill the sales order?

The system tracks the fulfillment of a document, using several tracking techniques:

* Natural matching
* Parent line
* Fulfillment table

### Natural matching

Natural matching matches the parent and the sub-documents, based on natural attribute values.

> [!NOTE]
> 
> Natural attributes are attributes representing **real-world** things.
> This is in contrast with artificial attributes, which are required by the inner workings of the software system.

In the example above, natural matching will compare the values of:

* Product
* Product variant
* Lot
* Serial number

Let’s review the previous example in the light of natural matching.

**sales order:**

* line 1: oranges, 10 kg

**shipment:**
	
* line 1: oranges, 8 kg
* line 2: tangerines, 2 kg

Natural matching will **not** qualify the shipment of tangerines as execution of the sale of oranges, because it's a different product.
Even if the customer agrees to accept the tangerines, this can't be represented in the system.

Another example:

А customer orders a specific lot of a product, but they're ready to accept another lot:

**sales order:**

- 10 oranges, lot 202

**shipment:** 

- 10 oranges, lot 203

This shipment satisfies the customer in the real world.
However, using natural tracking, this will be considered a severe **difference**.
The system will propose a reversal of the shipment of lot 203 and shipment again of lot 202.
This is problematic and might confuse some users.

Even more problematic would be if two or more lines of a sales order contain oranges.

In this case, natural matching just **doesn't** work well.

While natural matching won't require special (artificial) tracking attributes or tables, it does not work well for some real-world scenarios. It's used in document generations, created in the earlier stages of @@name, but mostly abandoned in newer developments.

### Parent line

Parent line is a widely used algorithm in @@name for keeping track of executions.

The sub-document keeps reference of the parent line which is being executed.

Let's see an example.

**sales order:**

* line 1: oranges, 10 kg
* line 2: apples, 2 pcs

**shipment:**

* line 1: oranges, 8 kg, parent line = 1
* line 2: tangerines, 2 kg, parent line = 1
* line 3: pears, 2 pcs, parent line = 2

Here, you can see that:

Although you sent tangerines, they replace the oranges; <br>
You sent the missing quantity; <br>
You sent pears, instead of apples.

> [!NOTE]
> 
> The measurement unit of the sub-document line should be the same as the parent line.

Of course, all this has to be arranged with the customer.

Once done, you have to represent it in the system.

### Fulfillment table

As good as parent line algorithm is, it cannot be used in all places.
There are cases where it might be impossible to match all sub-document lines using only parent line.

For example, in the WMS, suppose you have the following:

**Warehouse requisition:**

* line 1: despatch oranges, 10 pcs
* line 2: despatch apples, 2 pcs

In the optimization phase, the WMS has created the following plan:

**Warehouse order:**

* line 1: pick oranges, 30 pcs (there are other orders that will be sorted out on the packing table)
* line 2: pick apples, 2 pcs
* line 3: move everything to packing table 3.

There's a problem establishing a direct relationship with the parent document.

The solution is to use **Fulfillment** table.
It's like a notebook in which you record how much of the quantity has already been created for the sub-document.
This allows the system to generate complicated sub-documents, without tracking the direct relationship between the created and the parent lines.

In this example, after the warehouse order is created, the fulfillment table will contain:

* Warehouse requisition XXX, execution of line 1: Qty:10
* Warehouse requisition XXX, execution of line 2: Qty:2

The fulfillment table simply contains executed quantities, without any regard of how they are executed.

It **does not** contain any reference to the sub-document(s).

The system tracks the execution, without specifically deciphering the sub-document(s) contents.

The fulfillment table algorithm allows the application of complex algorithm execution.
These algorithms **don't** need to represent the parent document lines 1:1 with the sub-document lines and thus can employ subtle optimization techniques.
