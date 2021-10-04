---
items: StringInterpolationExpressionTypes
---

# Constant expressions

This kind of expressions doesn't perform any evaluation (i.e. no interpolation) and will produce an output same as the input.
```cs
// Input
"test"
// Output
"test"

// Input
"Good morning!" 
// Output
"Good morning!"
```

Multi-line input is also supported. The `\n` sequence is interpreted as a new line.
```cs
// Input
"line1\nline2"
// Output
@"line1
line2"

// Input
"line1\n\nline3"
// Output
@"line1

line3"
```

It's also possible to escape the control characters for beginning and end of an interpolation expression `{`, `}`. Either by doubling `{{`, `}}`, or by using the escape character `\{`, `\}`.
```cs
// Input
"{{This one is escaped}}"
// Output
"{This one is escaped}"

// Input
"\{This one also\}"
// Output
"{This one also}"
```

> [!NOTE]
> More details and examples are available in the [examples section](../examples/constant.md).