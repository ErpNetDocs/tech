---
items: StringInterpolationExpressionTypes
---

# Entity expressions

Resolves an object by its entity name and Id. 

```cs
// Input (the passed id exists)
'{Public_Users(7af30531-d15d-4004-a4bb-21052299f549).Name}'
// Output: 
'John Doe'

// Input (the passed id exists)
'{General_Products_Products(4282f8c5-2ba8-4adc-b112-c9f5ca2675f2).Name}'
// Output
'Product X'
```

If the entity name or the Id does not exist, the evaluation fails and the output will contain an error message.
```cs
// Input
'{General_Product(2fa67d60-be11-41ec-beac-976e666ece4f)}'
// Output
'#Error: Entity 'General_Product' not found#'

// Input (the passed id does NOT exist)
'{General_Products_Products(1cbbe47c-2f54-4fcf-be46-7eb7c5a139e8)}'
// Output
'#Error: Entity object '1cbbe47c-2f54-4fcf-be46-7eb7c5a139e8' not found#'
```

Also the error handling when passing not valid reference still apply. The evaluation will return an error.
```cs
// Input
'{Public_Users(7af30531-d15d-4004-a4bb-21052299f549).FullName}' 
// Output
'#Error: Attribute 'FullName' not found#'
```

> [!NOTE]
> 
> More details and examples are available in the **[Examples](https://docs.erp.net/tech/advanced/string-interpolation/examples/index.html)**.
