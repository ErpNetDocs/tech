---
items: StringInterpolationExamples
---

# Data member expression examples

## Same level data member reference

### Input
```cs
'The document Id is {DocumentId}.'
```

### Output
```cs
'The document Id is 929bdc15-79d8-4a1f-9467-c237f040939d.'
```

### Breakdown
1. `'The document Id is '`
2. `{DocumentId}`
    * Evaluates to `"929bdc15-79d8-4a1f-9467-c237f040939d"`
3. `'.'`


*Assuming the domain object has a data member `DocumentId` which equals to '929bdc15-79d8-4a1f-9467-c237f040939d'.*

## Referencing data members deeper

### Input
```cs
'The customer is {Customer.Party.PartyName} and its number is {Customer.Number}.'
```

### Output
```cs
'The customer is John Doe and its number is C12345.'
```

### Breakdown
1. `'The customer is '`
2. `{Customer.Party.PartyName}`
    * Follows the reference path:
        * `Customer`
            * `.Party`
                * `.PartyName`
    * Evaluates to `'John Doe`
3. `' and its number is '`
4. `{Customer.Number}`
    * Follows the reference path:
        * `Customer`
            * `.Number`
    * Evaluates to `"C12345"`
5. `'.'`

*Assuming the domain object has: data member `Customer` with data members `Party.PartyName` equals to 'John Doe' and Number equals to 'C12345'.*

## Including a format specifier 

### Input
```cs
"The customer is {Customer.Party.PartyName:de}."
```

### Output
```cs
"The customer is John Doe."
```

### Breakdown
1. `'The customer is '`
2. `{Customer.Party.PartyName:de}`
    * Follows the reference path:
        * `Customer`
            * `.Party`
                * `.PartyName`
    * Evaluates to `MultilanguageString` object
    * Format specifier found `:de`. Apply it.
    * Returns  `'Max Mustermann'`
3. `"."`

## #Error# Not existing reference

### Input
```cs
'The customer is {Customer.Name}.'
```

### Output
```c
'The customer is #Error: Attribute 'Name' not found#.'
```

### Breakdown
1. `'The customer is '`
2. `{Customer.Name}`
    * Follows the reference path:
        * `Customer`
            * `.Name` --> Fail. Reference does not exist.
    * Returns error.
3. `'.'`
