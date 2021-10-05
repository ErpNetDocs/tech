# Creating A duplicate document and a new document from current

The current article describes the principles and some specifics in creating a duplicate of an existing document. 

Different usages of the algorithm are also presented.
 
### Basic principles

А duplicate of a given document is a new document which contains identical **business** data as the original one, meaning that all ***substantial*** and ***meaningful*** information is copied from the original. There is some exception for technical details, such as internal identification numbers - Primary Keys, IDs of reference links between different parts of one document, and more.

This is the common algorithm for creating a duplicate:

1. A new document is created with the same Document type. Inside its headers, the ***substantial*** data from the original is copied.

      a.  the ***substantial*** data from the original document header is copied to the new document header;<br>
      b.  in each of the headers of the new document, only the* **substantial*** data from the original headers is copied.
      
2. In the duplicate, new rows are created for each original row, where ***substantial*** data is copied.

3. If the original document has *rows of the rows* (a row having dependent records in different parts of the document) - for each main row, its duplicate in the new document is fixed; for each sub-row of the main row, a new sub-row in the duplicate is created.</br> Only ***substantial*** data is copied from the original sub-row.

4. If the original has *rows of the rows of the rows*, the same procedure is applied until the original document structure is copied.

The new **duplicate** document must contain the same number of records (headers, rows, rows of rows) and structure as the original. 

Document rows are considered standard rows which most documents have, but properties and **[additional amounts](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/index.md)** also play a role. 

If a specific document header has its own properties, they are considered document rows. The records in the ‘Document Amount Referenced Documents’ panel are considered *rows of rows* (rows of the additional amounts). The records in ‘Document Line Amounts’ are considered rows of the standard document rows. 

For now, attached files are **not** copied when creating a duplicate of a document.
 
***Example 1:***

There is a Purchase Invoice with a document header and a specific header, two additional amounts, and four rows. For the first row values, three properties are specified. The last row has value in only one property. The second and third row do not have properties. 

The properties of the Purchase Invoice rows are considered *rows of rows* within the document. When creating a duplicate of this Purchase Invoice, a new Invoice is created, which also has one document header and one specific document header, two additional amounts, and four document rows. 

For the document rows, there are the following records:

- row 1 - 3 properties;
- row 2 - no properties;
- row 3 - no properties;
- row 4 - 1 property.

Each record in the new document copies the ***substantial*** data from its corresponding record in the original Purchase Invoice.

Other examples for *rows of rows* are: 

- ‘Depreciation plan line fixed value’ are rows of ‘Depreciation plan lines’
- ‘Payment slip lines’ are rows of ‘Payment slip amounts’
- ‘Operations’ are rows of ‘Work Order Items’. 
- The Voucher rows and their specific properties playing the role of their sub-rows.

This is the common method for copying ***substantial*** data from the original records to the duplicate records:

- values in fields which are Primary Key or referent ID of a link to an upper record in the current document hierarchy, are **not** copied; the original values are kept since they are created during the creation of the duplicate;

- for fields processed specifically, the value from the original record is **not** copied and the specific logic for filling the duplicate record is followed;

- for the rest of the fields, the value from the original record **is** copied with no change in the corresponding field for the duplicate.
 
***Example 2:***

In the first example, when copying data from original to duplicate records, the following fields are skipped:

- in the document header: the value of the Id field as well as fields processed specifically;
- in the specific header of the Purchase Invoice: values of fields PurchaseInvoiceId and DocumentId;
- in Additional Amounts: values of fields DocumentAmountId and DocumentId;
- in Purchase Invoice lines: values of fields PurchaseInvoiceLineId and PurchaseInvoiceId;
- in Purchase Invoice lines user properties: values of fields PurchaseInvoiceId and EntityItemId.
 
## Cases of specific data copying

The current section describes specific fields processing during data copying.
 
#### Document headers

If the document is a Master Document on its own, then in the MasterDocumentId field of the duplicate document, the original Id is filled. If this is not the case - MasterDocumentId is copied from the original document. 

In DocumentDate, the current date is filled in and DocumentVersion is set to "1". EnterpriseCompanyId and EnterpriseCompanyLocationId house the Enterprise Company and Location currently used by the user. 

CreationTime is filled in with the current date and time while CreationUser is set to the current user. 

State field is set to New and ReadOnly and Void are set to false.

If the original document is voided, DocumentNo of the duplicate record takes the number of the original document.</br>Otherwise, DocumentNo is null.

The fields UserStatusId, AssignedToUserId, VoidTime, VoidUser, VoidReason, AccessKeyId and ParentDocumentId are always empty.
 
#### Document headers and rows of a voucher

If the DefaultReferencedDocumentId in the original document is the same as the Id, then in the duplicate document this field is filled with the Id of the duplicate document. The same logic is applied for ReferencedDocumentId field in the Voucher's rows.
 
#### Payment slip amounts

IsPartyPayment is always set to true.
 
#### Transactions rows

The fields LineBaseCost, LineDocumentCost, LineProductCost and LineStoreCost are always set to 0.
 
#### Ingredients

When creating duplicates of the Work order rows with ingredients, there are some specifics which are not exactly related to the fields, but to how they fit in the document hierarchy:

- if the WorkOrderItemId field in the material record is filled in, then it is considered a sub-record of the work order item record from the Work Order document, the Id of which is the value of WorkOrderItemId.</br> These records are considered rows of the work order items rows;
- if the WorkOrderItemId field is null, then the record is directly considered a document row.</br> Such records are rows only of the document header and not of other rows.
 
### The duplicate creation algorithm usage

The algorithm for creating a duplicate works as follows:

- Duplicate creation is a function of the document form; the number of the original document is kept as are the date and the parent document (no matter the specifics of copying the data from the document headers).

- Creating new from current is a function of the document form; the document number and the parent document are not kept and the document date is the current date (as in the specific behaviour).

- Creating correction is a function of the document form; a duplicate of the current document is created and in its header, the field AdjustingDocumentId is filled with the Id of the original document; all other scalar fields in the duplicate are reset.

- Creating a copy of the Sales order is a generation procedure in the Sales order which produces a copy of the parent Sales order; the standard duplicate creation is used and in the header of the duplicate, the standard logic of document creation is applied.
