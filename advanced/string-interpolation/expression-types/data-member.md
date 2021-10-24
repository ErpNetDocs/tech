---
items: StringInterpolationExpressionTypes
---

# DataMember expressions

Acquires a data member according to the object's context by the passed `reference`. 
```cs
// Input
'{DocumentId}'
// Output
'6d954d04-105b-4277-ad2c-6a9a80076a63'

// Input *Note the (two-level) reference path - (1)Customer.(2)Id
'{Customer.Id}'
// Output
'54feef7d-c397-44f1-8c23-580a62dd93f6'

// Input *Note the (three-level) reference path - (1)Customer.(2)Party.(3)PartyName
'{Customer.Party.PartyName}'
// Output
'John Doe'

// Input (Customer.SalesPerson evaluates to null)
'{Customer.SalesPerson}'
// Output:
''
```

The evaluation fails if the resolved data member doesn't exist. The output will contain an error message. In contrast, if the data member is null, the expression will evaluate to an empty string.
```cs
// Input (There is no 'Name' data member in Customer)
'{Customer.Name}'
// Output
'#Error: Attribute 'Name' not found#'.

// Input (Typo error)
'{Customr.Id}'
// Output
'#Error: Attribute 'Customr.Id' not found#'.
```

> [!NOTE]
> More details and examples are available in the [examples section](https://docs.erp.net/tech/advanced/calculated-attributes/examples/index.html).
