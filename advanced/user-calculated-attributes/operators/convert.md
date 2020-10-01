---
uid: cao-CONVERT
---

# CONVERT - Calculated Attribute Operator

| Specification    | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | Returns an object of the specified type and whose value is equivalent to the specified object. This conversion requires absolutely correct input data - if the data is not in the correct form, data loss may occur.For example: if the user tries to convert the string value of '3.12' to decimal, the conversion would be successful.If the conversion of the string is not possible, this may lead to data loss, but no error would be returned. |
| Parameter 1 Name | param                                                        |
| Parameter 1 Type | decimal, int, string or date                                 |
| Parameter 2 Name | type                                                         |
| Parameter 2 Type | string - 'System.Int32', 'System.String', 'System.Decimal', 'System.DateTime' and all standard .net types |
| Parameter 3 Name | -                                                            |
| Parameter 3 Type | -                                                            |
| Return Value     | Returns the param converted to the type.                     |


## Example
```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT EXP:30 CONST:System.Decimal
30: CAST ATTRIB:@CustomProperty1 CONST:System.String
```

> [!NOTE]
> When conversion from CustomPropertyValue to numeric value (for example Decimal) is processed, first a [CAST](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-calculated-attributes/operators/cast.md#uid-cao-cast) must be applied - the CustomPropertyValue must be cast to string!

So, if a user needs to create a value from the standard price per lot of  the product multiplied by a coefficient stored as a product's custom  property @CustomProperty1, a calculated attribute can be created. If the repository of the product is General.Products.Products, its expressions would be as follows:

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT ATTRIB:@CustomProperty1 CONST:System.Decimal
```

This is incorrect attribute. The values of the custom properties are  specific type of value and the CONVERT operator does not know how to  convert it. So cast of the custom property value to string is required.  The correct version of the calculated attribute is:

```
10: MULTIPLY ATTRIB:StandardPricePerLotValue EXP:20
20: CONVERT EXP:30 CONST:System.Decimal
30: CAST ATTRIB:@CustomProperty1 CONST:System.String
```
