# Product codes

*Product codes* are mechanisms that allow products to be selected not by their part number (indicated in the product definition), but by alternative codes for this product. For example, using this mechanism,  products are selected via barcode. Product codes are used for the creation of new codes for existing products in the database.  All product codes are grouped in coding systems.

This mechanism is applied in the lines of logistics documents. It is implemented through a special field for the product code in the table and is a foreign key to the product codes table. By selecting the number from the drop-down list box you actually select the product for which the code is set. The field is commonly used when the documents are created manually by the user. When the documents are created automatically by the system (through procedures, for example) values in this field are carried by parental documents to sub-documents (if set), but are not automatically filled by the system (if not set).

### There are certain relations between the fields *Product*, *Product Code* and *Quantity Unit*:**

- If the field *Product Code* has a value or the value in the field is changed, then the value of the *Quantity Unit* is taken from the definition of coding system (if set) to which the code belongs;

- If the value in the field *Product* is changed, then the field *Product Code* must be empty, because the product is no longer selected through this mechanism.

### Suggestion: Avoid Overlapping Product Codes (e.g., no inclusion of codes like 12345 and 12345A)

To ensure clarity and prevent errors during product identification, product codes within the same coding system should be unique and not overlap with one another. For example, avoid using codes that are substrings or variations of each other, such as "12345" and "12345A." Overlapping codes can lead to confusion, misidentification of products, and potential system errors when processing logistics documents or scanning barcodes. A clear distinction between codes will prevent misassignments and ensure smoother data handling.

Benefits of Proper Product Code Numbering:

Improved Accuracy and Efficiency: Unique product codes minimize the risk of misinterpretation or conflicts when selecting products manually or through automated processes. This leads to fewer errors in stock management, inventory tracking, and order fulfillment.

Enhanced System Integrity: Avoiding overlapping product codes prevents data corruption or mismatch issues during document processing. It ensures that product details, such as quantity and unit, are correctly associated with the product.

Optimized Barcode Scanning: Clear, non-overlapping product codes facilitate faster and more accurate barcode scanning in logistics operations. This reduces the risk of incorrect product selection or delays in warehouse operations.

Better Scalability and Code Management: By adhering to a strict non-overlapping product code format, businesses can more easily scale their coding systems, introduce new products, and update existing ones without the need for complex code restructuring.

For best practices, consider referencing guidelines such as [GS1 standards](../../logistics/wms/gs1-barcodes.md) for product numbering and barcoding, which emphasize the use of globally unique identifiers and non-overlapping codes to ensure accuracy and traceability across supply chains.
