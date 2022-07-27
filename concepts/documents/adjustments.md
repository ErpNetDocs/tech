

# Adjustments documents

Using *adjustment documents* is a system to adjust released documents. As the released document states that the execution of the document has already started, therefore the released documents are read-only (see [Document states](states.md)). So when there is a need to change such a document, the usual way of editing it is not available and  a specific system is needed.

The *adjustment documents* are separate documents trough which a released document can be edited. They contain the main document that they are making corrections on. So one released document may have more than one correction. The *adjustment documents* are allowed two ([Document states](states.md)) - *New* and *Corrective*. The *Corrective* state is specific only for the *adjustment documents* and it is not allowed at the rest of the documents. When the document state is switched from New to Corrective, the changes in the adjustment document are applied to the main released document. Then the field "Adjustment number" is filled in with the consecutive number of the correction.

The *adjustment documents* contain only the changes which has to be applied. For example, if there is a released issuing Transaction with **10 PCS** and it turns out that now only **8 PCS** are issued, in this case, an adjustment issuing Transaction is executed with the quantity of **-2 PCS**. Thus, it can be considered that the adjustment document is the difference between the current values in the released document and the values, which have to be achieved after the correction. So the current data in every released document are a result of the original data (the document content when released for the first time) and the data added by all adjustment documents.

This mechanism is preferred over the direct redaction of the released documents because of easier tracking of the separated corrections that are executed (tracking of these changes is important). For example, in the previous example with the transactions, the user may easily see that the quantity has been decreased by **2 PCS** by the adjustment document. Otherwise, the user would have to compare the consecutive versions of the main document which may be a complicated and uncomfortable task, especially with large documents. Also, this mechanism allows the *adjustment documents* to be used for adjustment of [transitional documents](~/advanced/document-flow/transitional-documents.md) and sub-documents.

## Adjustment document application 

The mechanism, when an adjustment document (when the document state is switched to Corrective) is applied on the main released document, is as follows:

1. For each record in the adjustment document its corresponding record in the main document is searched. Matching the records is as follows:

   ​       a. if the record is in the adjustment document header, than the corresponding record is in the header of the main document;

   ​      b. if the record is in a row in the adjustment document then the record from the same row table in the main document is searched. The record should have the same *natural key* as the adjustment record; as natural key usually the document row number is used or another field (if there is no row number); for example, if in the adjustment document there is a row with number **30**, then in the main document a row in the same table and with the same number **30** is searched.

2. If no corresponding record is found in the main document (this is possible only if the current record is in the rows of the adjustment document), then the adjustment record is simply added to the corresponding table in the main document with no changes in it;

3. If a corresponding record is found in the main document, then the system reviews all the fields in the correction record and the following applies to each field:

   ​        a. if the field is a *key field* (see the article about Key and Scalar-Valued Fields), then it is checked if it has the same value in the main document and in the adjustment document; if there is a difference, the adjustment is rolled back, and the user is notified by an error message;

   ​        b. if the field is *scalar-valued* (see the article about Key and Scalar-Valued Fields), then the value of the adjustment record is ***added*** to the value of the main record;

   ​        c. if the field is neither *key* nor *scalar-valued*, then the value of the main record is ***replaced*** by the value of the adjustment record.

Thus, in the adjustment document, only the changes in the main document are marked. I.e. the user can decrease or increase the value of a scalar-valued field (quantity or amount) or change/replace the value of a field that is neither key nor scalar-valued.

> [!Note]
> Key fields cannot be adjusted by adjustment documents!

Also if the adjustment document has no record corresponding to a record in the main document, then the original document will not be changed after the correction takes place. For example, if in the main document there is a row with a number **30**, and in the adjustment document there is no such row, then row **30** from the main document will remain unchanged after the correction.

## What can be done by adjustment documents?

- Can adjust values of non-key fields (the scalar-valued fields are adjusted by adding the value in the adjustment document, and the rest of the fields are adjusted by replacing the value with the one from the adjustment document);
- New records can be added in row tables;
- All scalar-valued fields in a row can be reset (so the row will no longer affect the document behavior).

## What cannot be done by adjustment documents?

- A value of a key field cannot be changed;
- A row cannot be deleted.

## Special types of adjustment documents

There are some special types of adjustment documents in @@name, which are prepared by the system and the user does not have to fill the scalar values in them.

Such types are the *Nullify corrections*. They are accessible in all documents and are used to adjust all scalar-valued fields so they become **0**. By this correction, the document no longer "has value" (i.e. it does not order or fulfill any quantities or amounts). This is an alternative to document voidance.

For the Receiving orders there two special types of adjustments - *Correction according to stored quantities* and *Correction according to invoiced quantity*. The first type automatically calculates the necessary correction so the quantities in the Receiving Order become equal to the quantities from the current Receiving Order which are receipts in the store. This correction is used to eliminate the difference between the Receiving Order and its Transactions. The second type is used to equalize the quantities in the Receiving Order as they are in the Purchase invoices, created for the current Receiving order.
