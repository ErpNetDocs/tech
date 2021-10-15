---
uid: transitional-documents
---

# Transitional documents

**Transitional documents** are documents, which are automatically maintained to always contain the most current information from the parent document.
They are automatically generated first and then, on each change in the parent document, are adjusted with the latest changes.

Transitional documents, by default, are hidden from the document flow.
Since they are totally automated and not user-created, they are usually of no interest to the user.
They are used just to keep the document flow contiguous, but are hidden to keep it clean.

Not all generations can create transitional documents. Only **deterministic** generations can create such documents.

The main purpose of the transitional documents is to decrease the number of sub-documents in case there are often changes in the data from which sub-documents are created by the [document fulfillment](https://docs.erp.net/tech/advanced/document-flow/fulfillment.html) system and lots of sub-documents are created.

## Transitional document setup

To set up a document type as transitional:

1. Go to the document type definition and select 'transitional document'.
2. To generate documents of this type, use only generations that support transitional document generation.

### Example 1:

When creating payment orders by sales order payment plan (see the **Sales order payment plan** article) there are preconditions for great multiplication of the number of sub-documents. For example, if the sales order has a payment plan with three payments - **40 EUR**, **50 EUR**, **10 EUR** - then initially three payment orders will be created (with no invoice data) for each scheduled playment. 
When the amount of 60 EUR from the sales order is invoiced, two additional payment orders are created - one for **-40 EUR** and one for **-20 EUR** for planned payments №**1** and №**2**, which have no invoice data, and two more payment orders for **40 EUR** and **20 EUR** for planned payments №**1** и №**2** with invoice data.
So the sub-documents are now seven. When the user release more invoices, more payment orders will be created.

If an invoice is voided - even more payment orders will be created so the collective state of the sub-documents is reached when the voided invoice is no longer reported.

So the transitional documents are meаnt to decrease the sub-documents number in such cases, and the changes are applied as corrections on already existing sub-documents (see [Adjustment documents](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/adjustment.md)). 
This is performed only if the existing documents are Released. If they have document state higher than Released (see [Document states](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/states.md)), new documents are created for the discrepancies that occur.

In such а case, we call these sub-documents **transitional**.
If a document is transitional is a property of the document type definition. Activating this property is available only when all active procedures which create the current document allow transitional document and are set to create а Released document. 
Thus, at the first sub-document creation, the sub-documents will have Released document state and the next document changes can be applied as corrections.

Thereby, not only the sub-documents number is smaller, and the user does not have to process them (no need to change their state, to edit/correct them so they can reach the values in the parent document, to void additional documents and etc.).
This is some kind of automatic processing of these documents by the system.
The user has to work only on the parent document. This is where the name of these documents came from - *transitional* - as these documents do not need direct processing by the user.

### Example 2:

There is a sales order for **100 pcs**. It creates transitional store order. The first store order has **100 pcs**.
When we correct the parent sales order so the quantity is **70 pcs**, there are the following two cases:

- the first is when the primary store order has **100 pcs** and it is not Releаsed, but Firm Planned (this is possible if its state is returned to Firm Planned before the sales order correction or when the store order is created before its type is set to transitional). In this case, as there is no released document to correct, so a new Store Order is created with **-30 pcs**. Now there are two documents;
- But if the primary store order is Released (the usual case), then the discrepancy of **-30 pcs** is applied as a document correction and the quantity in the primary store order is now **70 pcs**. Thereby, the sub-document is only one, as the discrepancy documents are not independent documents, they are applied to the primary document as corrections.

### Example 3 (continue of Example 1):

There is a sales order with a payment plan for 3 payments - **40 EUR**, **50 EUR**, and **10 EUR**. 
The payment orders are set as transitional documents. Initially, there are no invoices on this sales order so there are three released payment orders:

- payment №**1**, **40 EUR**, no invoice data;
- payment №**2**, **50 EUR**, no invoice data;
- payment №**3**, **10 EUR**, no invoice data.

Then invoice #**1** is created based on this sales order for **60 EUR**. 
So the first two payments have to be corrected. 
The first should have invoice data, the second should have **20 EUR** with invoice data, and the rest **30 EUR** do not have invoice data yet. 
So for the additional four payment orders from Example 1, created to cover the discrepancies, the first two payment orders containing **-40 EUR** and **-20 EUR** are applied as corrections of the already existing payment orders for planned payments №**1** and №**2**, with no invoice data. And the second two orders with invoice data are created as new Released documents as there are no released payment orders with invoice data yet. So now the payment orders are:

- payment №**1**, **0 EUR**, no invoice data;
- payment №**1**, **40 EUR**, invoice #1;
- payment №**2**, **30 EUR**, no invoice data;
- payment №**2**, **20 EUR**, invoice #1;
- payment №**3**, **10 EUR**, no invoice data;

If after that invoice #1 is edited to **35 EUR**  (or voided and created again), then the invoice amount may cover only part of the first payment and this will cause discrepancies/changes in the first four payments. As the payment orders are transitional, instead of creating four new documents, the existing payment orders will be adjusted:

- payment №**1**, **5 EUR**, no invoice data;
- payment №**1**, **35 EUR**, invoice #1;
- payment №**2**, **50 EUR**, no invoice data;
- payment №**2**, **0 EUR**, invoice #1;
- payment №**3**, **10 EUR**, no invoice data;

The previous example shows that there are cases when the sub-documents have zero-values in the scalar value fields. This is equal to removing the sub-documents (i.e. it does not order/execute anything anymore). The fact that the sub-documents are not voided or erased completely is useful as in a following action they may be used to be adjusted again with zero-values (thereby they are recovered as active documents).
