---
items: CalculatedAttributesQA
---

# How to get only the value or only the description of a custom property

This article explains how to extract either the **value** or the **description** of a custom property in calculated attributes. Depending on your needs (e.g., display purposes, filtering in `WHERE` clauses, or other), you can choose the appropriate method described below.


## Getting the Value of a custom property

There are two methods to retrieve only the **value** of a custom property:

### Method 1: Using FORMATSTRING

This method is ideal for display purposes or simple outputs.

```
FORMATSTRING ATTRIB: @Property1 CONST: V
```

- @Property1 – The custom property, where '@' is a prefix and 'Property1' is the cutom property's code.
- `V` – is the format specifier for description.

OUTPUT:
If 'Property1 = Value1: Description1', the output will be 'Value1'.

**Note:** This method may not be usable in WHERE clauses within a SELECT statement due to type compatibility. 

### Method 2: Using CAST

For use in WHERE clauses or type-sensitive operations, the value should be explicitly cast to the appropriate type.
```
CAST ATTRIB: @Property1 CONST: System.String
```

- Casts the custom property value to a `System.String` type for safe usage in filters and logical expressions.

OUTPUT:
If 'Property1 = Value1: Description1', the output will be 'Value1'.

## Getting the Description of a custom property

To get only the **description** of a custom property, use:
```
FORMATSTRING ATTRIB @Property1 CONST:D
```

- `D` – is the format specifier for description.

OUTPUT:
If 'Property1 = Value1: Description1', the output will be 'Description1'.

**Note:** This is currently the only supported method to retrieve the description of a custom property. It may not be usable in WHERE clauses within a SELECT statement due to type compatibility. In this case, you can use a comparison by the value of the property instead of the description. 

## Useful Links

- [FORMATSTRING operator](../operators/formatstring.md)
- [Format specifiers](../../string-interpolation/format-specifiers.md)
- [CAST operator](../operators/cast.md)
- [Convert property to number еxample](../examples/convert-property-to-number.md)
- [How to check if a custom property has value](../QA/How-to-check-if-a-custom-property-has-value.md)
