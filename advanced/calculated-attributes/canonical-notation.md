## Canonical notation

A calculated attribute definition consists of:

- a header record in **[Systems.Bpm.CalculatedAttributes](xref:Systems.Bpm.CalculatedAttributes)**.
- one or more expression rows in **[Systems.Bpm.CalculatedAttributeExpressions](xref:Systems.Bpm.CalculatedAttributeExpressions)**.

The header defines the calculated attribute itself.  
The expression rows define how its value is calculated.

### Header fields

| Field | Description |
| --- | --- |
| **Repository Name** | The entity type for which the calculated attribute is defined (evaluated per instance). |
| **Name** | The technical name of the calculated attribute. This name is used when the attribute is referenced in other formulas. |
| **Caption** | The user-facing name of the attribute. |
| **Hint** | Additional help text shown in the UI. |
| **Is Active** | Specifies whether the calculated attribute is active. |
| **Starting Expression No** | The number of the expression row whose result becomes the value of the calculated attribute. |
| **Script Language** | Specifies how the attribute is calculated. Supported values are `Integrated` and `JavaScript`. |
| **Script Text** | JavaScript code used when `ScriptLanguage` is set to `JavaScript`. |
| **Notes** | Optional internal notes. |

### Expression rows

When **Script Language** is set to **Integrated**, the calculated attribute is defined by expression rows.

Each row contains:

- **Expression No**
- **Operator**
- **up to three parameters**:
  - `Parameter1Type` + `Parameter1Value`
  - `Parameter2Type` + `Parameter2Value`
  - `Parameter3Type` + `Parameter3Value`

Each operator defines its own behavior and accepted parameters. For more information, see [Operators](operators/index.md).

### Canonical form

Each expression row can be written in the following canonical form:

```text
<ExpressionNo>: <Operator> <Parameter1Type>:<Parameter1Value> <Parameter2Type>:<Parameter2Value> <Parameter3Type>:<Parameter3Value>
```

If an operator uses fewer than three parameters, the unused parameters are omitted.

### Parameter types

The canonical notation uses typed parameters in the form `Type:Value`.

The meaning of `ParameterXValue` depends on the selected `ParameterXType`.

| Type | Value |
| --- | --- |
| `CONST` | A constant value, for example `10`, `'Text'`, `true`, or a date value. |
| `ATTRIB` | The name of an attribute, for example `DefaultPaymentTermDays`. |
| `REF` | The name of a reference, for example `Customer`. |
| `CHILD` | The name of a child collection, related to the current master object. |
| `EXP` | An expression number, for example `20`. |
| `INPUT` | An expression number whose input parameter will be used. |
| `REPO` | The name of a repository. |
| `SYS` | The name of a system variable. |

For more information about the supported parameter types, see [Parameter types](parameter-types/index.md).

### Example 1 - Get a related value

```text
10: GETOBJVALUE REF:Customer ATTRIB:DefaultPaymentTermDays
```

Explanation:

- **GETOBJVALUE** gets information from a related entity.
- `REF:Customer` specifies the related entity.
- `ATTRIB:DefaultPaymentTermDays` specifies the attribute to return.
- The result of expression `10` becomes the value of the calculated attribute.

### Example 2 - Chained navigation

```text
10: GETOBJVALUE REF:Product EXP:20
20: GETOBJVALUE REF:ProductType ATTRIB:Name
```

Explanation:

- Line `10` gets the related `Product` and applies expression `20` to it.
- Line `20` gets the `Name` attribute from the related `ProductType`.
- The result of line `10` is the final value when **Starting Expression No** is `10`.

### JavaScript

When **Script Language** is set to **JavaScript**, the value of the calculated attribute is determined by the contents of **Script Text**.

The script must return the calculated value.

The following example is equivalent to **Example 2 - Chained navigation**:

```js
const product = subject.Product;

if (!product || !product.ProductType) {
    return null;
}

return product.ProductType.Name;
```

The script gets the related `Product`, then gets its related `ProductType`, and finally returns the value of its `Name` attribute.

If the script returns `null`, the value of the calculated attribute is `null`.

For more information, see [Scripting in calculated attributes](scripting/index.md).
