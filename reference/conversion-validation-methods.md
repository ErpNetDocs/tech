# Conversion validation methods


Conversion ratio providers like currency directories and products have methods **IsConvertible** and **IsConvertibleToBase**. 

They are used by the system in order to determine whether the input unit is valid and could be converted during the calculations.
 
1. **IsConvertibleToBase** checks if using a specified provider object one measurement unit or one currency unit can be converted to the base unit of the provider. If the provider is null, the unit cannot be converted to base and the method returns as false.
 
When the provider is a currency directory, the method uses the **GetRatioToBaseOrDefault** method for currency directories, which finds a ratio if one of the following requirements is fulfilled:

- the currency directory’s **ToCurrency** is the same as the selected currency

- the currency directory has lines where **FromCurrency** is the same as the selected currency
 
When the provider is a product, the method uses the **GetRatioToBaseOrDefault** method for products, which finds a ratio if one of the following requirements is fulfilled:

- the selected measurement unit is part of the product's base measurement category;

- the product has defined dimension for the selected measurement unit;

-  the selected measurement unit is part of a measurement category for which the product has defined dimension.
 
 2.  **IsConvertible** checks if using a specified provider object one measurement unit or one currency can be converted to another of the same type. If the provider is null, the units cannot be converted and the method returns false. 
  
The method is based on the **GetRatioThroughBaseOrDefault** method. If the units are equal or both of them are null, the method returns true. If only one of them is null, the method returns false.
If the units are different and not null, the method uses **GetRatioToBaseOrDefault** for each to get the ratios for conversion to the base unit of the provider. Then, both ratios are combined in a new one. If such a combined ratio is calculated successfully, the method returns true.
