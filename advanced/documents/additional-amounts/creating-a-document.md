# Creating A Duplicate Document And a Dew Document From Current


The current article describes the principles and some specifics in creating a duplicate of an existing document. Also different usages of the algorithm are presented.
 
### Basic Principles
Creating a duplicate of a given document is actually creating a new document which contains identical **business** data with the original one, meaning that in the duplicate  all ***substantial*** and ***meaningful*** data is copied from the original document and there is an exception for some technical data (such as internal identification numbers - Primary Keys, IDs of reference links between different parts of one document and more).

This is the common algorithm used when creating a duplicate of a given document:

1. A new document is created with the same Document type and in its headers the ***substantial*** data from the original document is copied:<br>
      a.  the ***substantial*** data from the original document header is copied to the new document header;<br>
      b.  in each of the specific headers in the new document only the***substantial*** data from the corresponding specific headers of the original documents is copied.
2. If the original document has rows - for each row a new row is created in the duplicate document and the ***substantial*** data from the original row is copied to the new one.
3. If the original document has *rows of the rows* (i.e. a document row has dependent records in different part of the document) - for each main row from the original document its duplicate row in the new document is fixed and for each of its sub-rows of the main row a new sub-row in the duplicate document is created and from the original sub-row only the ***substantial*** data is copied.
4. If the original document has *rows of the rows of the rows*, the same procedure is applied until the original document structure is covered.

Thus, the new document - the duplicate - must contain the same number of records (headers, rows, rows of rows etc.) as the original document and these records must have the same structure as they are in the original document.

As document rows are considered not only the standard rows which most of the documents have, but also the document properties and the **[Additional Amounts](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/index.md)**. Also, if the specific document header has its own properties, then they are considered document rows. The records in ‘Document Amount Referenced Documents’ panel are considered *rows of rows* (rows of the additional amounts). Also, the records in ‘Document Line Amounts’ are considered as such (they are rows of the standard document rows). Currently, the attached files are not copied when creating a duplicate of a document.
 
***Example 1:***

There is a Purchase Invoice (it has document header and a specific header) and there are two additional amounts and 4 rows. For the first row values in three properties are specified, and the last row has value in only one property (the second and the third rows do not have properties). The properties of the Purchase Invoice rows are considered *rows of rows* within the document. So when creating a duplicate of this Purchase Invoice actually a new Purchase Invoice has to be created which also has one document header and a specific document header, and also has two additional amounts and 4 document rows. For the document rows there are the following records for their properties:
- row 1 - 3 properties;
- row 2 - no properties;
- row 3 - no properties;
- row 4 - 1 property.

Each record in the new document copies the ***substantial*** data from its corresponding record from the original Purchase Invoice.

Other examples for *rows of rows* are: ‘Depreciation plan line fixed value’ are rows of ‘Depreciation plan lines’, ‘Payment slip lines’ are rows of ‘Payment slip amounts’, ‘Operations’ are rows of ‘Work Order Items’. Also the Voucher rows have their specific properties playing the role of their sub-rows.

The copying of the ***substantial*** data from the original records to the duplicate records is executed as follows:
- values in fields, which are Primary Key or referent ID of a link to an upper record in the current document hierarchy, are not copied; the original values are kept which are created when creating the new document (the duplicate);
- for fields, which are processed specifically (they are described in the next section), the value in the original record is not copied and the specific logic for filling the duplicate record is followed;
- for the rest of the fields, the value in the original record is copied with no change in the corresponding field from the duplicate record.
 
***Example 2:***

In the first example when copying the data from the original records to the duplicate records, the following fields are skipped:
- in the document header: the value in the Id field is not copied, also fields, which are processed specifically (they are described in the next sections);
- in the specific header of the Purchase Invoice: values in fields PurchaseInvoiceId and DocumentId are not copied;
- in Additional Amounts: values in fields DocumentAmountId and DocumentId are not copied;
- in Purchase Invoice lines: values in fields PurchaseInvoiceLineId and PurchaseInvoiceId are not copied;
- in Purchase Invoice lines user properties: values in fields PurchaseInvoiceId and EntityItemId are not copied.
 
## Cases Of Specific Data Copying

The current section describes some specific fields processing during copying the data of the original records to their corresponding records in the duplicate document.
 
#### Document Headers
If the following is true for the original document: the document is a Master Document to its own, then in the field MasterDocumentId in the duplicate document its own Id (the Id of the duplicate) is filled. If not true - MasterDocumentId is  copied from the original document. In DocumentDate the current date is filled in and DocumentVersion is set to "1". In EnterpriseCompanyId and EnterpriseCompanyLocationId are filled the Enterprise Company and the Enterprise Company Location which are currently used by the user. CreationTime is filled in with current date and time and CreationUser is set to the current user. State field is set to New and ReadOnly and Void are set to false.

If the original document is voided, DocumentNo of the duplicate record takes the number of the original document. Otherwise DocumentNo is null.

The fields UserStatusId, AssignedToUserId, VoidTime, VoidUser, VoidReason, AccessKeyId and ParentDocumentId are always empty.
 
#### Document Headers And Rows Of A Voucher
If in the original document the DefaultReferencedDocumentId is the same as the Id of the document, then in the duplicate document this field is filled with the Id of the duplicate document. The same logic is applied for ReferencedDocumentId field in the Voucher's rows.
 
#### Payment Slip Amounts
IsPartyPayment is always set to true.
 
#### Transactions Rows
The fields LineBaseCost, LineDocumentCost, LineProductCost and LineStoreCost are always set to 0.
 
#### Ingredients
When creating the duplicates of the Work order rows with ingredients, there is a specific, which is not exactly for the specified fields in these records, but for how they fit in the document hierarchy:
- if the field WorkOrderItemId in the material record is filled in, then this record is considered a sub-record of the work order item record from the Work Order document, which Id is the value from WorkOrderItemId (i.e.for these records it is considered that they are rows of the work order items rows);
- if the WorkOrderItemId field is null, then the record is considered directly a document row (i.e. such records are rows only of the document header and not of other rows).
 
### The Duplicate Creation Algorithm Usage
The algorithm for duplicates creation currently is used as follows:
- Duplicate creation: this is a function of the document form; the number of the original document is kept as are the date and the parent document (no matter the specifics of copying the data from the document headers).
- Creating new from current: this is a function of the document form; the document number and the parent document are not kept and the document date is the current date (as in the specific behaviour).
- Creating correction: this is a function of the document form; when using it, a duplicate of the current document is created and in its document header the field AdjustingDocumentId is filled with the Id of the original document and all other scalar fields in the duplicate are reset.
- Creating a copy of the Sales order: this is a generation procedure in the Sales order which generates a copy of the parent Sales order; the standard duplicate creation is used and in the document header of the duplicate the standard logic of document creation is applied.

