---
items: StringInterpolationExpressionTypes
---

# Constant expressions

These expressions don't perform any evaluation and will produce an output that's the same as the input.

There's **no** interpolation.

```cs
// Input
'test'
// Output
'test'

// Input
'Good morning!'
// Output
'Good morning!'
```

Multi-line input is also supported. The `\n` sequence is interpreted as a new line.
```cs
// Input
'line1\nline2'
// Output
@'line1
line2'

// Input
'line1\n\nline3'
// Output
@'line1

line3'
```

It's also possible to escape the control characters for beginning and end of an interpolation expression `{`, `}`, either by doubling `{{`, `}}`, or by using the escape character `\{`, `\}`.
```cs
// Input
'{{This one is escaped}}'
// Output
'{This one is escaped}'

// Input
'\{This one also\}'
// Output
'{This one also}'
```

> [!NOTE]
> 
> More details and examples are available in the **[Examples](https://docs.erp.net/tech/advanced/string-interpolation/examples/index.html)** section.
