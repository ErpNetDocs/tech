# Transitional Documents

The main purpose of the transitional documents is to decrease the number of sub-documents in case there are often changes in the data from which sub-documents are created by the [Document Fulfillment](document-fulfillment.md) System and lots of sub-documents are created.

## Example 1:

When creating Payment Orders by Sales Order payment plan (see "Sales Order Payment Plan" article) there are preconditions for great multiplication of the number of sub-documents. For example, if the Sales Order has payment plan with three payments - **40 EUR**, **50 EUR**, **10 EUR** - then initially three Paymen Orders will be created (with no Invoice data) for each scheduled playment. When the amount of 60 EUR from the Sales Order is invoiced, two additional payment orders are created - one for **-40 EUR** and one for **-20 EUR** for planned payments №**1** and №**2**, which have no invoice data, and two more Payment Orders for **40 EUR** and **20 EUR** for planned payments №**1** и №**2** with invoice data. So the sub-documents are now seven. When the user release more invoices, more Payment Orders will be created.

If an Invoice is voided - even more Payment Orders will be created so the collective state of the sub-documents is reached when the voided Invoice is no longer reported.

So the transitional documents are ment to decrease the sub-documents number in such cases, and the changes are applied as corrections on already existing sub-documents (see [Adjustment Documents](adjustment-documents.md)). This is performed only if the existing documents are Released. If they have higher than Released Document State (see [Document States](document-states.md)), new documents are created for the discrepancies that occur.

In such case we call these sub-documents *transitional*. If a document is transitional is a property of the document type definition. Activating this property is available only when all active procedures which create the current document allow transitional document and are set to create Released document.Thus, at the first sub-document creation, the sub-documents will have Released document state and the next document changes can be applied as corrections.

Thereby, not only the sub-documents number is smaller, and the user does not have to process them (no need to change their state, to edit/correct them so they can reach the values in the parent document, to void additional documents and etc.). This is some kind of automatic processing of these documents by the system. The user has to work only on the parent document. This is where the name of these documents came from - *transitional* - as these documents do not need direct processing by the user.

## Example 2:

There is a Sales Oder for **100 pcs**. It creates transitional Store Order. The first Store Order has **100 pcs**. When we correct the parent Sales Order so the quantity is **70 pcs**, there are the following two cases:

the first is when the primary Store Order has **100 pcs** and it is not Realesed, but Firm Planned (this is possible if its state is returned to Firm Planned before the Sales Order correction or when the Store  Order is created before its type is set to transitional). In this case as there is no released document to correct, so a new Store Order is created with **-30 pcs**. Now there are two documents;
But if the primary Store Order is Released (the usual case), than the discrepancy of **-30 pcs** is applied as a document correction and the quantity in the primary Store Order is now **70 pcs**. Thereby, the sub-document is only one, as the discepancy documents are not independent documents, they are applied to the primary document as corrections.


## Example 3 (continue of Example 1):

There is a Sales Order with payment plan for 3 payments - **40 EUR**, **50 EUR** and **10 EUR**. The Payment Orders are set as transitional documents. Initially there are no Invoices on this Sales Order so there are three released Payment Orders:

payment №**1**, **40 EUR**, no Invoice data;
payment №**2**, **50 EUR**, no Invoice data;
payment №**3**, **10 EUR**, no Invoice data.
Then Invoice #**1** is created based on this Sales Order for **60 EUR**. So the first two payments have to be corrected. The first should have Invoice data, the second should have **20 EUR** with Invoice data, and the rest **30 EUR** do not have Invoice data yet. So for the additional four Payment Orders from Example 1, created to cover the discrepancies, the first two Payment Orders containing **-40 EUR** and **-20 EUR** are applied as corrections of the already existing Payment Orders for planned payments №**1** and №**2**, with no invoice data. And the second two orders with invoice data are created as new Released documents as there are no released Payment Orders with Invoice data yet. So now the Payment Orders are:

payment №**1**, **0 EUR**, no Invoice data;
payment №**1**, **40 EUR**, Invoice #1;
payment №**2**, **30 EUR**, no Invoice data;
payment №**2**, **20 EUR**, Invoice #1;
payment №**3**, **10 EUR**, no Invoice data;
If after that Invoice #1 is edited to **35 EUR**  (or voided and created again), than the Invoice amount may cover only part of the first payment and this will cause discrepancies/changes in the first four payments. As the Payment Orders are transitional, instead of creating four new documents, the existing Payment Orders will be adjusted:

payment №**1**, **5 EUR**, no Invoice data;
payment №**1**, **35 EUR**, Invoice #1;
payment №**2**, **50 EUR**, no Invoice data;
payment №**2**, **0 EUR**, Invoice #1;
payment №**3**, **10 EUR**, no Invoice data;
The previous example shows that there are cases when the sub-documents have zero-values in the scalar value fields. This is equal to removing the sub-documents (i.e. it does not order/execute anything any more). The fact that the sub-documents are not voided or erased completely is useful as in a following action they may be used to be adjusted again with zero-values (thereby they are recoved as active documents).
