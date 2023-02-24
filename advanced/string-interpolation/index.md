# String interpolation

String interpolation is a process in which an input string is broken into (interpolation) expressions. 

@@name tries to evaluate each interpolation expression and replace it with its string representation. 

String interpolation is available for each object.

## Abstract

Below is a pseudo example of how string interpolation works:

In the following input:
```
'Where there’s {EXPRESSION1}, there’s {EXPRESSION2}.'.
```

`{EXPRESSION1}` and `{EXPRESSION2}` will be replaced with their string representations - `smoke` and `fire`.


Finally, the interpolated string is presented to the output:
```
'Where there’s smoke, there’s fire.'
```

Let's try a real-world example:

**Input:**
```
Now is {$date}.
My name is {$user.Name}.
```

Note `{$date}` and `{$user.Name}`. They're **real** expressions.

**Output:** 
```
Now is 4.10.2021 17:49:55.
My name is John Doe.
```

**More advanced examples:**

```cs
// Input
"The following string was interpolated on {$date:ddd}"

// Output (interpolated)
"The following string was interpolated on 21-09-27"
```

```cs
// Input
"https://myservice.com?database={$dbname}&id={Id}"

// Output (interpolated)
"https://myservice.com?database=mydbname&id=39acf964-4e92-4d35-846e-c8a38efff02d"
```

**It's possible to interpolate even far more complex strings:**

```cs
// Input
@"Hello, {Public_Users(d30f16c9-a07a-41ca-9d63-e15c3e4db6b4).Name:en}!
My name is {$user.Name:en} and I work as a {$role.Name} in {$enterprisecompany.Company.Name:en}."

// Output (interpolated)
@"Hello, John Doe!
My name is Jane Doe and I work as a Manager in ABC Company Ltd."
```

> [!NOTE]
> 
> More details and examples are available in the **[Examples](https://docs.erp.net/tech/advanced/string-interpolation/examples/index.html)** section.

## Syntax
The overall syntax for an interpolation expression is:

`{<$>reference<(args)><.subref><:fmt>}`

where:
* The curly brackets `{`, `}` define the start and the end of the interpolation expression.

* `$` - specifies that the expression is a `System Variable`.

* `ref` (**required**) - the identifier to the context of the interpolation expression.

* `(args)` - additional arguments must be passed when evaluating a `Entity` expressions. E.g. an `Id`.

* `.subref` - required when `ref` referes to an object, but a data member is needed. E.g. `Customer.Party.PartyName`, where `Customer` is the context (i.e. the `ref`) and the `.Party.PartyName` is the path to the data member - the subreference. In short, `.subref` defines a path that will be followed after evaluation of `ref`.

* `:fmt` - format specifier. Further formatting of the evaluated value. E.g. `Customer.Party.PartyName:en` will format the resulting `PartyName` `MultiFormatString` according to particular language, referenced with `en` (English).

> [!WARNING]
> 
> If an interpolation expression can't be evaluated because of incorrect syntax or wrong (non-existing) reference, the evaluation will **fail** and will return an error. '{Customer.Number}' will produce 'C12345', but '{Customer.Numer}' will output "#Error: Attribute 'Customer.Number' not found#".

## Format specifiers

If an interpolation expression evaluates to an object, future customization of the value to a desired format is possible. The target format depends on the object type. 

For a 'Number' type, the 'C' format specifier acts as number-to-currency string conversion, but if the object type is 'MultilanguageString', the format specifier will return the string of the current value.

------------
### See more

- **[Expression types](./expression-types/index.md)**
- **[Format specifiers](./format-specifiers.md)**
- **[System variables](./system-variables.md)**
- **[Escape sequences](./escape-sequences.md)**
- **[Examples](./examples/index.md)**
