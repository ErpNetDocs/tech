
# Convert a Value of a Custom Property to a Number

The values of the custom properties are  specific type of value and the CONVERT operator does not know how to  convert it properly. For this reason, if we want to covert a custom property's value to a number, we have to CAST [CAST](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-calculated-attributes/operators/cast.md#uid-cao-cast) it first. 


## Example -  Multiply standard price per lot by a coefficient stored in a property


Lets say, for example, we want to multiply the standard price per lot of the product by a coefficient stored as a product's custom  property @CustomProperty1. 

> [!NOTE]
> The repository of the attributes is *General.Products.Products*

<br/>

**RIGHT calculated attribute:**

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT EXP:30 CONST:System.Decimal
30: CAST ATTRIB:@CustomProperty1 CONST:System.String
```


> 
> Explanation:
>
> 10: Multiply the value of the 'Standard Price Per Lot' by EXP: 20.
>
> 20: Convert EXP:30 to a decimal number .
>
> 25: Cast the value of custom property 'CustomProperty1' to a string
> 


<br/>

**WRONG calculated attribute:**

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT ATTRIB:@CustomProperty1 CONST:System.Decimal
```

> 
> Explanation:
>
> 10: Multiply the value of the 'Standard Price Per Lot' by EXP: 20.
>
> 20: Convert the value of custom property 'CustomProperty1' to a decimal number.
>



> [!NOTE]
> When we want to convert CustomPropertyValue to numeric value (for example Decimal), we need to [CAST](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-calculated-attributes/operators/cast.md#uid-cao-cast)  it to a string first!
