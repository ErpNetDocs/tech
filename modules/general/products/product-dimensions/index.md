# Product dimensions


*Product Dimensions* are used for conversion between different units of measurement for the same quantity. In order to make this possible, product dimensions must be set for the products as a ratio between multiplier and divider to the base unit. 

The formula for calculation of Quantity Base in the documents lines is as follows: 

**Quantity Base = Quantity * Product Dimension Dest Quantity / Product Dimension Source Quantity**


|Required fields|Description|
|:---- |:----
|Quantity|The quantity in the non-base unit.
|Source Quantity Unit|The non-base unit for which the conversion ratio is specified.
|Dest Quantity|The quantity in some of the base units.
|Dest Quantity Unit|The measurement unit of the dest quantity. Should be one of the units of the base measurement category of the product.
|Measurement Category|The measurement category of the source quantity unit. For each product, only one conversion ratio can be specified for a measurement category.


**Example:** 

We need to load two pallets of a product. But we know that each pallet contains 15 pieces. So the total pieces that we need to load are 30. This means that if we want to automate this calculation, we need to insert the following information to create a conversion ratio in the product dimensions: 

**Source quantity** -  1.00 

**Source quantity unit** -  Pallet 

**Dest quantity** - 15.00 

**Dest quantity unit** - Pcs  

**Measurement category** - Complectation (e.g.)

