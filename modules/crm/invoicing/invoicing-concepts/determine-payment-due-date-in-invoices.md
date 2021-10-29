# Determine payment due date in invoices

Invoices in @@name are entered manually or they are created based on invoice orders.


## Determine payment due date when entering an invoice manually

In this case the *Payment Due Date* is determined in the standard way - based on the data in the invoice customer definition. This is a default value and it can be changed by the user.


***Example 1:***

The user enters an invoice with a document date **15 Mar 2020**. The customer definition says that its *Default Payment Term Days* is **7 days**. Then the *Payment Due Date* in the invoice is **22 Mar 2020**.


## Determine payment due date when entering an invoice based on invoice orders

There is a *Payment Due Date* in the invoice orders. When the user enters Invoices based on invoice orders, the *Payment Due Date* is copied from the invoice order or from the *Document Date* of the invoice order (depending on which date is greater). This is also valid in the cases when the invoice is created with today's date. In this case the payment term is kept (as days count) as it is in the invoice order.


***Example 2:***

There is a sales order with *Document Date* **02 Nov 2020** and *Payment Due Date*  **09 Nov 2020** (so the payment term is **7 days**). These dates are copied to the invoice order from the sales order. Then in the client definition the *Default Payment Term Days* is changed from 7 days to 14 days. The user creates invoice with *Document Date* **22 Nov 2020** . The Payment Due Date in the invoice is **29 Nov 2020** (i.e. keeping the term from the Invoice Order), in spite of the difference in the terms according to the customer's definition.


***Example 3:***

The same case as in ***Example 2*** , except for the *Document Date* of the invoice order. In the current example it is **11 Nov 2020** (this is possible if the invoice order is generated from shipments). Then when creating the invoice. *Payment Due Date* is considered to be **11 Nov 2020** (the greater date), which means that the payment term is actually **0 days** (the difference between the document date and the effective payment due date). I.e. when  entering an Invoice with *Document Date* **22 Nov 2020**, its *Payment Due Date* is **22 Nov 2020**.


>  *Payment Due Date* in theiInvoice depends of how the *Payment Due Date* and the *Document Date* in the invoice o rder are determined.


## Determine the Payment Due Date and the Document Date in the invoice orders

They are usually generated on sales orders and copy their term and date. There are two general document flows that create invoice orders:


- sales orders => invoice orders
These are orders directly created from sales orders. They include products that cannot be shipped. These are also orders for sales orders for sales returns.
- sales orders => shipment orders => shipments => invoice orders
These are orders for products and services that have to be shipped first.

When directly creating invoice orders from the sales orders, *Document Date* and  *Payment Due Date* are copied from the sales order.


The second document flow contains different mechanisms. Here, the document date in the invoice order is copied from the shipment and the *Payment Due Date* is determined by a more complicated algorithm. This is because the shipment does not have information for the payment term and it is provided by the sales orders which the shipment is based on. The sales orders may be more than one. Then the *Payment Due Date* in the invoice order is determined by the earliest *Payment Due Date* in the sales orders (i.e. the smallest date) and if this term is later than the *Document Date* of the invoice order (copied from the shipment), then the *Payment Due Date* is saved. If the *Payment Due Date* is before the *Document Date* - then the *Document Date* is saved as a *Payment Due Date*.
