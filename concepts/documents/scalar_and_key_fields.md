---
uid: Scalar and Key Fields
---

# Scalar-value and Key fields

Understanding how fields are classified in documents is critical for managing data integrity and ensuring accurate calculations in complex systems. Here we explore the roles of scalar-value, key, and non-participating fields in the discrepancy system, highlighting their impact on document creation, corrections, and recalculations. By clearly defining these field types, businesses can streamline processes and maintain consistency across interconnected documents.

# Scalar-value Fields
Scalar fields in documents represent the quantitative effects of those documents. These fields typically include quantities — such as counts of products, materials, or people — and monetary values. Theys are the foundation of the <b>discrepancy system</b>, providing the basic numerical data on which calculations are performed.
For example, consider a Store order for 100 units of a product. When a corresponding store transaction document is created, it will attempt to account for the entire 100 units. However, if a sub-document has already been generated for 42 units, the discrepancies system calculates the remaining quantity by subtracting the 42 units from the original 100, yielding a difference of 58 units. In this case, the system creates a new document for the remaining 58 units. 

Scalar-value fields also play a crucial role in [<b>Adjustments</b>](adjustments.md). When an adjustment is created, its scalar-value field values are added to the corresponding fields in the original document. This approach allows the correction document to effectively represent the difference between the released document’s current values and the adjusted values. 

## Determining Scalar-value Fields
Most fields that represent quantities or monetary amounts are classified as scalar. If a field represents such data, it is almost always considered scalar. However, there are notable exceptions where fields, although representing quantities or amounts, are derived from other scalar fields or external calculations and are therefore not declared scalar.

For example:

•	Shipments and Shipment Order Lines: Fields such as “Net, kg,” “Gross, kg,” “Volume, l,” and others reflect physical characteristics of goods. These values are derived from quantities in the lines, using product dimensions ratios or user input. Since these fields are recalculated for every document — whether manually entered, generated, corrected, or processed through the discrepancy system — they are not scalar;

•	Cost fields in Store transactions: system cost fields, such as cost in base currency, warehouse currency, product currency, and document currency, depend on the cost source. If the cost source is “document,” these fields are derived from the line amount after applying currency conversions. If the cost source is “warehouse,” the values depend solely on line quantities and current warehouse costs, which are external to the document. In both cases, these fields are systematically recalculated rather than declared scalar.

# Key Fields
Key fields are identifiers that distinguish parts of a document or groups of documents within a larger set. They serve as natural, analytical, or business keys, allowing the system to recognize distinct captions, lines, or other business components. Key fields are integral to the discrepancy system, as they enable the segmentation of documents into components and determine the extent to which each part has been fulfilled.

Returning to the example of a Store order for 100 units, where 42 units have already been received: scalar fields quantify the remaining 58 units, while key fields identify which warehouse, product, or other analytical categories are associated with these quantities. 
When released documents are updated through adjustment documents, key fields are protected against changes. This ensures that the document’s business logic and structure remain consistent, preventing conflicts that could arise from altering key identifiers.

## Defining Key Fields
A field is classified as key if it is essential for recognizing distinct business activities or if the field’s value must remain constant to ensure the integrity of the document’s purpose. Common key fields include Customer, Store, and product fields.

For example:
•	Store in Store Orders: This key field is used when documents from modules such as Procurement and Sales create Store Orders for receiving or issuing goods across multiple stores. If the parent document’s quantities are edited, the system checks existing warehouse orders to determine how much of the quantities have already been processed. Since these checks are performed separately for each store, the store field is key;

•	Store in Store Transactons: If a store order generates a store transaction specifying a store, this field becomes key. Altering it in the transaction document would violate the discrepancy system’s integrity, as key field differences are not permitted. This ensures that sub-documents remain consistent with their parent documents.

In addition to business logic, fields related to units of measure or currencies are always classified as key. This prevents inconsistencies between sub-documents and parent documents, simplifying scalar field calculations and corrections by avoiding the need for complex conversions.

## Key field classification involves several considerations:

**1.**	Is the field essential for distinguishing specific business processes or components? If yes, it is likely key.
**2.**	Should the parent document enforce a fixed value for the field in sub-documents? If yes, it is likely key.
**3.**	Can the field’s value be modified in a released document through adjustments? If yes, it is probably not key.
**4.**	Does the field indicate a unit of measure, currency, or other scalar-related metric? If yes, it must be key.

# Other Fields
Fields that are neither scalar nor key, such as notes or dates, do not participate in the difference system. These fields are excluded from discrepancy calculations and are not assigned analytical significance. They can be updated through corrections, but their updates follow a simpler principle: the latest adjustment sets the current value. Exceptions to this behavior occur when specific fields, such as cost fields in warehouse receipts, undergo recalculations triggered by status changes.
