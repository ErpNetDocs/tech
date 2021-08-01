# Determine Payment due date in Invoices

Invoices in @name are entered manually or they are created based on Invoice Orders.


## Determine Payment due date when entering an Invoice manually

In this case the *Payment Due Date* is determined in the standard way - based on the data in the Invoice customer definition. This is a default value and it can be changed by the user.


***Example 1:***

The user enters an Invoice with a Document Date **15 Mar 2020 **. The customer definition says that its *Default Payment Term Days* is **7 days**. Then the *Payment Due Date* in the Invoice is 22 Mar 2020 .


## Determine Payment due date when entering an Invoice based on Invoice orders

There is a *Payment Due Date* in the Invoice Orders. When the user enters Invoices based on Invoice Orders, the *Payment Due Date* is copied from the Invoice Order or from the *Document Date* of the Invoice Order (depending on which date is greater). This is also valid in the cases when the Invoice is created with today's date. In this case the payment term is kept (as days count) as it is in the Invoice Order.


***Example 2:***

There is a Sales Order with *Document Date* 02 Nov 2020 and *Payment Due Date*  09 Nov 2020 (so the payment term is 7 days). These dates are copied to the Invoice Order From the Sales Order. Then in the client definition the *Default Payment Term Days* is changed from 7 days to 14 days. The user creates Invoice with Document date 22 Nov 2020 . The Payment Due Date in the Invoice is 29 Nov 2020 (i.e. keeping the term from the Invoice Order), in spite of the difference in the terms according to the customer's definition.


***Example 3:***

The same case as in ***Example 2*** , except for the *Document Date* of the Invoice Order. In the current example it is 11 Nov 2020 (this is possible if the Invoice Order is generated from Shipments). Then when creating the Invoice. *Payment Due Date* is considered to be 11 Nov 2020 (the greater date), which means that the payment term is actually **0 days** (the difference between the document date and the effective payment due date). I.e. when  entering an Invoice with *Document Date* 22 Nov 2020, its *Payment Due Date* is 22 Nov 2020 .


>  *Payment Due Date* in the Invoice depends of how the *Payment Due Date* and the *Document Date* in the Invoice Order are determined.


## Determine the Payment Due Date and the Document Date in the Invoice Orders

They are usually generated on Sales Orders and copy their term and date. There are two general document flows that create Invoice Orders:


- Sales Orders => Invoice Orders
These are orders directly created from Sales Orders. They include products that cannot be shipped. These are also orders for Sales Orders for Sales returns.
- Sales Orders => Shipment Orders => Shipments => Invoice Orders
These are orders for products and services that have to be shipped first.

When directly creating Invoice Orders from the Sales Orders, *Document Date* and  *Payment Due Date* are copied from the Sales Order.


The second document flow contains different mechanisms. Here, the document date in the Invoice Order is copied from the Shipment and the *Payment Due Date* is determined by a more complicated algorithm. This is because the Shipment does not have information for the payment term and it is provided by the Sales Orders which the Shipment is based on. The Sales Orders may be more than one. Then the *Payment Due Date* in the Invoice Order is determined by the earliest *Payment Due Date* in the Sales Orders (i.e. the smallest date) and if this term is later than the *Document Date* of the Invoice Order (copied from the Shipment), then the *Payment Due Date* is saved. If the *Payment Due Date* is before the *Document Date* - then the *Document Date* is saved as a *Payment Due Date*.
