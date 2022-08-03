# Creating a duplicate document and a new document from current

The current article describes the principles behind the process of creating a duplicate of an existing document. 

Different usages of the algorithm are also presented.
 
## Basic principles

А duplicate of a given document is a new document which contains **identical** business data as the original one, meaning that all substantial and meaningful information is **copied**. 

There's some exception for technical details like internal identification numbers - primary keys, IDs of reference links between different parts of a document, and more.

**This is the common algorithm for creating a duplicate:**

1. A new document is created with a particular document type. <br> Inside its headers, the substantial data from the original is copied.


      a.  substantial data from the original document header is copied to the new document header;<br>
      b.  in each header of the new document, only the substantial data from the original is copied.
      
2. In the duplicate, new rows are created for each original row, and the substantial data is copied there.

3. If the original document has a row with dependent records in different parts of the document, for each main row, its duplicate in the new document is fixed; for each sub-row of the main row, a new sub-row in the duplicate is created. Only substantial data is copied from the original sub-row.

4. If the original has rows of rows of the rows, the step 3 is applied until the original structure is copied.

The new duplicate document must contain **the same** number of records (headers, rows, rows of rows) and structure as the original. Document rows are considered standard rows which most documents have, but properties and **[additional amounts](../document-amounts/index.md)** also play a role. 

If a document header has its own properties, they are considered document rows. The records in the **Document Amount Referenced Documents** panel are considered rows of rows (rows of the additional amounts). The records in **Document Line Amounts** are considered rows of the standard document rows. 

For now, attached files are **not** copied when creating a duplicate of a document.
 
**Example 1:**

There's a purchase invoice with a document header and a specific header, two additional amounts, and four rows. **3** properties are specified for the first row values. The last row value has only **1** property. The second and third rows have **0** properties. 

The properties of the purchase invoice rows are considered **rows of rows** within the document. 

When creating a duplicate of this purchase invoice, a new one is created, which also has a document header and a specific document header, two additional amounts, and four document rows. 

For the document rows, there are the following records:

- row 1 - 3 properties;
- row 2 - no properties;
- row 3 - no properties;
- row 4 - 1 property.

Each record in the new document copies the **substantial data** from its corresponding record in the original.

Other examples for 'rows of rows' are: 

- Depreciation plan line fixed value - rows of depreciation plan lines
- Payment slip lines - rows of payment slip amounts
- Operations - rows of work order items 
- The voucher rows and their specific properties playing the role of their sub-rows.

**This is the common algorithm for copying substantial data from original to duplicate records:**

- Values in fields which are primary key or referent ID of a link to an upper record in the document hierarchy, are **not** copied; originals are kept, since they're generated during the creation of the duplicate;

- For fields processed specifically, the value of the original record is **not** copied, and the specific logic for filling the duplicate record is followed;

- For the rest of the fields, the original record value **is** copied in the corresponding field of the duplicate.
 
**Example 2:**

In the first example, when copying data from original to duplicate records, the following fields are skipped:

- in the document header: the value of the _Id_ field as well as fields processed specifically;
- in the specific header of the purchase invoice: values of fields _PurchaseInvoiceId_ and _DocumentId_;
- in additional amounts: values of fields _DocumentAmountId_ and _DocumentId_;
- in purchase invoice lines: values of fields _PurchaseInvoiceLineId_ and _PurchaseInvoiceId_;
- in purchase invoice lines user properties: values of fields _PurchaseInvoiceId_ and _EntityItemId_.
 
### Cases of specific data copying

The current section describes specific field processing during data copying.
 
#### Document headers

If a document is a master document on its own, the original ID is filled in the _MasterDocumentId_ field of the duplicate document. If this isn't the case - _MasterDocumentId_ is copied from the original document. 

In _DocumentDate_, the current date is filled in and _DocumentVersion_ is set to '1'. _EnterpriseCompanyId_ and _EnterpriseCompanyLocationId_ house the enterprise company and location currently used by the user. 

_CreationTime_ is filled in with the current date and time, while _CreationUser_ is set to the current user. 

_State_ field is set to 'New' and 'ReadOnly'. _Void_ is set to 'False'.

If the original document is voided, _DocumentNo_ of the duplicate record takes the number of the original document. Otherwise, _DocumentNo_ is **null**.

The fields _UserStatusId_, _AssignedToUserId_, _VoidTime_, _VoidUser_, _VoidReason_, _AccessKeyId_ and _ParentDocumentId_ are always **empty**.
 
#### Document headers and rows of a voucher

If _DefaultReferencedDocumentId_ in the original document is the same as the ID, this field is filled with the Id of the duplicate in the duplicate document. 

The same logic is applied for _ReferencedDocumentId_ in the Voucher's rows.
 
#### Payment slip amounts

_IsPartyPayment_ is always set to 'True'.
 
#### Transactions rows

The fields _LineBaseCost_, _LineDocumentCost_, _LineProductCost_ and _LineStoreCost_ are always set to '0'.
 
#### Ingredients

When creating duplicates of work order rows with ingredients, there are some specifics which aren't exactly related to the fields, but to how they fit in the document hierarchy:

- If the _WorkOrderItemId_ field in the material record is filled in, it's considered a sub-record of the work order item record from the main document, the Id of which is the value of _WorkOrderItemId_.</br> These records are considered **rows** of the work order items rows;

- If _WorkOrderItemId_ is null, the record is instantly considered a **document row**.</br> Such records are rows **only** of the document header and not of other rows.
 
### The duplicate creation algorithm usage

The algorithm for creating a duplicate works as follows:

- **Duplicate creation** is a function of the document form; the number of the original document is **kept**, as are the date and the parent document (no matter the specifics of copying data from document headers).

- **Creating new from current** is a function of the document form; the document number and the parent document are **not** kept, and the document date is the current date.

- **Creating correction** is a function of the document form; a duplicate of the current document is created and in its header, the field _AdjustingDocumentId_ is filled with the Id of the original document; all other scalar fields in the duplicate are **reset**.

- **Creating a copy of the sales order** is a generation procedure in а sales order which produces a copy of the parent sales order; the standard duplicate creation is used and in the header of the duplicate, the standard logic of document creation is applied.
