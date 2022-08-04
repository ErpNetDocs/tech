---
uid: transitional-documents
---

# Transitional documents

Transitional documents are maintained to contain the most up-to-date information from a parent document. Once generated, they're adjusted with the latest changes after each change in a parent document.

Transitional documents are **hidden** from the **[document flow](index.md)** by default, since they're totally automated and not user-created. Another reason for remaining invisible is to keep the document flow **contiguous**.

Only **[deterministic generations](deterministic-generations.md)** can create such documents.

The main purpose of transitional documents is to **decrease** the number of sub-documents in cases when there are many changes in the data from which sub-documents are created by the **[document fulfillment system](fulfillment.md)**.

## Transitional document setup

To set up a document type as transitional:

1. Go to the document type definition and select 'transitional document'.
2. To generate documents of this type, use generations that **support** transitional document generation.

**Example 1:**

When creating payment orders by a **sales order payment plan**, there are preconditions for a great increase in the number of sub-documents. 

If a sales order has a payment plan with three payments:

**40 EUR**, **50 EUR**, **10 EUR**,

then three payment orders will be created (with no invoice data) for each scheduled playment. 

When the amount of **60 EUR** from the sales order is invoiced, two additional payment orders are created: 

one for **-40 EUR** and one for **-20 EUR**,<br>
for planned payments **№1** and **№2**, which have no invoice data, 

and two more payment orders for **40 EUR** and **20 EUR** <br>
for planned payments **№1** и **№2** with invoice data.

The sub-documents are now seven. When more invoices are released, more payment orders will be created.

If an invoice is **voided**, even more payment orders will be created. The 'collective' state of the sub-documents is reached when the voided invoice is no longer reported.

**What happens?**

Transitional documents are meаnt to **decrease** the sub-documents' number. Changes are applied as corrections on already existing sub-documents. See **[Adjustment documents](~/concepts/documents/adjustments.md)** for more information. 

Another condition is for the existing documents to be 'Released'. If they have a document **[state](~/concepts/documents/states.md)** higher than 'Released', new documents are created for the discrepancies that occur.

In such а case, you can call the sub-documents **transitional**.

If a document is transitional, it's a **property** of the document type definition. Activating this property is available only when all active procedures that create the current document **allow** transitional documents and are set to create а 'Released' document. 

On first sub-document creation, the sub-documents will have 'Released' document state. 

The next document changes can be applied as **corrections**.

Not only is the sub-documents' number smaller, but you don't need to process it. There's no need to change sub-documents' states, nor edit or correct them so they can reach the values of the parent document. 

This, by itself, becomes an automatic processing of the documents by the system. You have to work only on the parent document. This is where the name 'transitional' comes from, as these documents don't need direct processing by the user.

**Example 2:**

There's a sales order for **100 pcs**. It creates a transitional store order. 

The first store order has **100 pcs**.

When you correct the parent sales order so the quantity is **70 pcs**, there are the following two cases:

- When the primary store order has **100 pcs** and is 'Firm Planned'. There's no released document to correct, so a new store order is created with **-30 pcs**. As a result, you get two documents. 

- If the primary store order is 'Released' (the usual case), the discrepancy of **-30 pcs** is applied as a document correction and the quantity in the primary store order is now **70 pcs**. The sub-document is only one. As the discrepancy documents are not independent documents, they're applied to the primary document as corrections.

**Example 3** (continuing **Example 1**):

There's a sales order with a payment plan for 3 payments - **40 EUR**, **50 EUR**, and **10 EUR**. 

The payment orders are set as transitional documents. 

Initially, there are no invoices on this sales order so there are three released payment orders:

- payment №**1**, **40 EUR**, no invoice data;
- payment №**2**, **50 EUR**, no invoice data;
- payment №**3**, **10 EUR**, no invoice data.

Then, invoice #**1** is created based on this sales order for **60 EUR**. 

The first two payments need to be corrected. 

The first should have invoice data, the second should have **20 EUR** with invoice data, and the rest **30 EUR** don't have invoice data yet. For the additional four payment orders from **Example 1**, the first two payment orders containing **-40 EUR** and **-20 EUR** are applied as corrections of the already existing payment orders for planned payments №**1** and №**2**, with no invoice data. The second two orders with invoice data are created as new 'Released' documents, as there are no released payment orders with invoice data yet. 

The payment orders now are:

- payment №**1**, **0 EUR**, no invoice data;
- payment №**1**, **40 EUR**, invoice #1;
- payment №**2**, **30 EUR**, no invoice data;
- payment №**2**, **20 EUR**, invoice #1;
- payment №**3**, **10 EUR**, no invoice data;

After invoice #1 is edited to **35 EUR**  (or voided and created again), the invoice amount may cover only part of the first payment, which will cause discrepancies/changes in the first four payments. 

As the payment orders are transitional, the existing payment orders will be **adjusted**:

- payment №**1**, **5 EUR**, no invoice data;
- payment №**1**, **35 EUR**, invoice #1;
- payment №**2**, **50 EUR**, no invoice data;
- payment №**2**, **0 EUR**, invoice #1;
- payment №**3**, **10 EUR**, no invoice data;

The previous example shows cases when the sub-documents have **zero** values in the scalar value fields. This is equal to **removing** the sub-documents (it doesn't order/execute anything anymore). 

The fact that the sub-documents are not voided or erased completely is useful, since in a future action they may be used to be adjusted again with zero values (only to be recovered as active documents).
