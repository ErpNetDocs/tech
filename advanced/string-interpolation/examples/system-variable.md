---
items: StringInterpolationExamples
---

# System variable expression examples

## Interpolation of a globally resolved system variable

### Input
```cs
'Now is {$datetimeutc} (UTC)'
```

### Output
```cs
'Current database name is 01.01.2021 15:00:00 (UTC)'
```

### Breakdown
1. `'Now is '`
2. `{$datetimeutc}`
    * Evaluates to `"01.01.2021 15:00:00'`.
3. `'(UTC)`

## Externally resolved system variable

### Input
```cs
'Current database name is {$dbname}'
```

### Output
```cs
"Current database name is E1_PROD"
```

### Breakdown
1. `'Current database name is'`
2. `{$dbname}`
    * Evaluates to `'E1_PROD'` via an external resolver.

## Acquiring a data member from a system variable and applying a format specifier

### Input
```cs
'Current company location is {$enterprisecompanylocation.LocationName:en}.'
```

### Output
```cs
'Current company location is London, UK.'
```

### Breakdown
1. `'Current company location is '`
2. `{$enterprisecompanylocation.LocationName:en}`
    * Resolves the system variable `$enterprisecompanylocation` to a `CompanyLocation` object type.
    * Follows the reference path:
        * `.LocationName`
    * Evaluates to `MultilanguageString` object
    * Format specifier found `:en`. Apply it.
    * Returns  `"London, UK'`
3. `"."`

## #Error# Not existing system variable

### Input
```cs
'Yesterday was {$yesterday}.'
```

### Output
```cs
'Yesterday was #Error: System Variable '$yesterday' not found#.'
```

### Breakdown
1. `'Yesterday was'`
2. `{$yesterday}`
    * Resolves the system variable `$yesterday` --> Fail. Such a system variable does not exist.
    * Returns error.
3. `'.'`

## #Error# Not existing reference

### Input
```cs
'My name is {$user.RealName}.'
```

### Output
```cs
'My name is #Error: Attribute 'RealName' not found#.'
```

### Breakdown
1. `'My name is''
2. `{$user.RealName}`
    * Resolves the system variable `$user` to a `User` object type.
    * Follows the reference path:
        * `.RealName` --> Fail. Reference does not exist.
    * Returns error.
3. `'.'`
