# String interpolation in @@name

String interpolation is a process in which an input string is broken down into expressions (a.k.a. interpolation expressions). @@name tries to evaluate each interpolation expression and finally replaces each one with its string representation. String interpolation is available for each object.

## String interpolation abstract

Below is a pseudo-example of how the string interpolation works:

In the following input:
```
"Where there’s {EXPRESSION1}, there’s {EXPRESSION2}.".
```

`{EXPRESSION1}` and `{EXPRESSION2}` will be replaced with their string representations - `smoke` and `fire`.


Finally, the interpolated string is presented to the output:
```
"Where there’s smoke, there’s fire.".
```

Let's try a real world example:

Input:
```
Now is {$date}.
My name is {$user.Name}.
```

Note `{$date}` and `{$user.Name}`. They are real expressions.

Output: 
```
Now is 4.10.2021 17:49:55.
My name is John Doe.
```

## String interpolation by example

More advanced examples for a string interpolation:
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

Also, it's possible to interpolate far more complex ones:
```cs
// Input
@"Hello, {Public_Users(d30f16c9-a07a-41ca-9d63-e15c3e4db6b4).Name:en}!
My name is {$user.Name:en} and I work as a {$role.Name} in {$enterprisecompany.Company.Name:en}."

// Output (interpolated)
@"Hello, John Doe!
My name is Jane Doe and I work as a Manager in ABC Company Ltd."
```

> [!NOTE]
> More examples are available in the separate [examples](examples/index.md) section.

## Syntax
The overall syntax for **one** interpolation expression is:

`{<$>reference<(args)><.subref><:fmt>}`

where:
* The curly braces `{`, `}` define the start and the end of the interpolation expression.
* `$` - specifies that the expression is a `System Variable`.
* `ref` (**required**) - the identifier to the context of the interpolation expression.
* `(args)` - additional arguments must be passed when evaluating a `Entity` expressions. E.g. an `Id`.
* `.subref` - required when `ref` referes to an object, but a data member is needed. E.g. `Customer.Party.PartyName`, where `Customer` is the context (i.e. the `ref`) and the `.Party.PartyName` is the path to the data member - the subreference. In short, `.subref` defines a path that will be followed after evaluation of `ref`.
* `:fmt` - format specifier. Further formatting of the evaluated value. E.g. `Customer.Party.PartyName:en` will format the resulting `PartyName` `MultiFormatString` according to particular language, referenced with `en` (English).

> [!WARNING]
> If an interpolation expression could not be evaluated because of incorrect syntax or wrong (not existing) reference, the evaluation will fail and will return an error. E.g. `{Customer.Number}` will produce "C12345", but `{Customer.Numer}` (note the typo) will output "#Error: Attribute 'Customer.Number' not found#".

## Format specifiers
If the interpolation expression evaluates to an object, it's possible for future customization of the value to a desired format. Typically the target format depends on the concrete object type, e.g. for `Number` type the `C` format specifier acts as number to currency string conversion, but if the object type is `MultilanguageString` the format specifier will return the string of the current value.

> [!NOTE]
> See [Format specifiers](format-specifiers.md) for more information about the supported format specifiers and how to use them.
