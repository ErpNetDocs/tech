# Coding systems 

*Coding systems* group together multiple **[Product Codes](https://github.com/ErpNetDocs/tech/blob/master/modules/general/products/product-codes.md)** according to different criteria. All product codes are grouped in coding systems. Product codes are codes other than the part numbers that bring meaning to the company such as supplier codes, customer codes, barcodes and more. 

A 'Default Measurement unit' could also be specified in coding systems. If a product code relating to a coding system with a default measurement unit is selected, then this unit must load in the document instead of the product's default unit. 

For example, if in the products definition 'Measurement unit = Pcs' is set, and for this product there is also a product code that relates to a coding system with a 'Default Measurement unit = Package', then we expect the following behavior: 

When a product in the sales order is selected through product code via barcode, then: 

-  Product’s part number loads in the field 'Product' in the particular sales order line; 

- 'Quantity unit = Package', which corresponds to the default measurement unit in the coding system’s definition; 

- 'Unit price' must be recalculated according to the **[Product Dimensions](https://github.com/ErpNetDocs/tech/blob/master/modules/general/products/product-dimensions/index.md)**. 
