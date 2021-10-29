# Product codes

*Product codes* are mechanisms that allow products to be selected not by their part number (indicated in the product definition), but by alternative codes for this product. For example, using this mechanism,  products are selected via barcode. Product codes are used for the creation of new codes for existing products in the database.  All product codes are grouped in coding systems.

This mechanism is applied in the lines of logistics documents. It is implemented through a special field for the product code in the table and is a foreign key to the product codes table. By selecting the number from the drop-down list box you actually select the product for which the code is set. The field is commonly used when the documents are created manually by the user. When the documents are created automatically by the system (through procedures, for example) values in this field are carried by parental documents to sub-documents (if set), but are not automatically filled by the system (if not set).

**There are certain relations between the fields "Product", "Product Code" and "Quantity Unit":**

- If the field "Product Code" has a value or the value in the field is changed, then the value of the "Quantity Unit" is taken from the definition of coding system (if set) to which the code belongs;

- If the value in the field "Product" is changed, then the field "Product Code" must be empty, because the product is no longer selected through this mechanism.
