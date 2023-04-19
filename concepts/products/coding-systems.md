# Coding systems 

*Coding Systems* group together multiple [product codes](product-codes.md) according to different criteria. All product codes are grouped in coding systems. Product codes are codes other than the part numbers that bring meaning to the company such as supplier codes, customer codes, barcodes and more. 

A *default measurement unit* could also be specified in coding systems. If a product code relating to a coding system with a default measurement unit is selected, then this unit must load in the document instead of the product's default unit. 

For example, if in the products definition "Measurement Unit = Pcs" is set, and for this product there is also a product code that relates to a coding system with a "Default Measurement Unit = Package", then we expect the following behavior: 

When a product in the sales order is selected through product code via barcode, then: 

-  Product’s part number loads in the Product field in the particular sales order line; 

- "Quantity Unit = Package", which corresponds to the default measurement unit in the coding system’s definition; 

- "Unit Price" must be recalculated according to the [product dimensions](product-dimensions.md).

Test - notifications.

