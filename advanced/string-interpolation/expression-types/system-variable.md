---
items: StringInterpolationExpressionTypes
---

# System variable expressions

They are case InsENSitiVE and always start with `$`, providing additional data unrelated to a specific object or its state. For example, if you need to get the current date, you can do it directly via the system variable `$date`.

```cs
// Input
'{$date}'
// Output
'01.01.2021'

// Input
'{$datetimeutc}'
// Output
'01.01.2021 15:00:00'

// Input
'{$rooturl}'
// Output
'db.myerp.net'

// Input
'{$user.Name}'
// Output
'John Doe'

// Input
'{$user.Name}'
// Output
'John Doe'
```

> [!NOTE]
> 
> See **[System variables](https://docs.erp.net/tech/advanced/string-interpolation/system-variables.html)** for more information and all supported system variables.

If a system variable exists but is null, the expression will evaluate to an **empty string**.

```cs
// Input 
'{$role.Name}'
// Output
''
```

If a system variable doesn't exist or its further reference is invalid, the evaluation will return an **error**.

```cs
// Input 
'{$yesterday}'
// Output
'#Error: System Variable '$yesterday' not found#'

// Input (FullName does not exist)
'{$role.FullName}'
// Output
'#Error: Attribute 'FullName' not found#'
```

> [!NOTE]
> 
> More details and examples are available in the **[Examples](https://docs.erp.net/tech/advanced/string-interpolation/examples/index.html)** section.
