# Variable (Dynamic) Measurement Ratios 

*Variable (Dynamic) Measurement Rаtios* are a functionality that allows a compensation of stock differences. Stock differences occur if there are variances between the quantity in the base unit of measure and the quantity in the parallel unit of measure. Stock differences may, for example, be caused by natural weight variations in material withdrawals. 

The option *‘Allow Variable Measurement Ratios’* is available in the product’s definition. When this option is checked, the base quantity could be edited in the receiving order and transaction’s lines. Thereby, the user has the opportunity to manually adjust the right base quantity in the particular situation. Otherwise, if in the product definition is not set that it is allowed to use *Variable Measurement Ratios*, then the product dimensions must be followed properly while recalculating base quantity.


## Example: 

The client has ordered **1 pallet** of a product. We know that one pallet theoretically weights **1000 kg** and that information is set as a conversion ratio in the **[Product Dimensions](https://github.com/ErpNetDocs/tech/blob/master/modules/general/products/product-dimensions/index.md)**. But we also know that this weight may vary, so the product is allowed to use *'Variable Measurement Ratios'*. The base quantity in the Store transaction is calculated on a base of the conversion rate. But when the workers in the warehouse actually put the pallet on the scale it turns out that the pallet actually weights **1100 kg**. In this case they can manually set the value for the base quantity. This will not only assure that the information in the system is correct, but also will allow the company to invoice the right amounts.


**Note:** 

When using *Variable Measurement Ratios*, there are certain prohibitions. For example, creating payment orders from sales orders involving products with this setting is not allowed. The reason is, if those payment orders are created for uninvoiced amounts, the possible change of the quantity in the transaction and therefore in the invoice may cause the generation of excess documents.
