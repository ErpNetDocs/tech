---
items: StringInterpolationExamples
---

# Entity expression examples

### Acquiring an entity object and referencing its data member

#### Input
```cs
'Hi, {Public_Users(a08baf52-de7a-4a39-a567-c6d7e2ab1dc8).Name}, welcome to our forum!'
```
#### Output
```cs
'Hi, John Doe, welcome to our forum!'
```

#### Breakdown
1. `'Hi, '`
2. `{Public_Users(a08baf52-de7a-4a39-a567-c6d7e2ab1dc8).Name}`
    * Acquires an object of type 'User' from the `Public_Users` entity with the provided 'Id'.
    * Follows the reference path:
        * `.Name`
    * Evaluates to 'John Doe'
3. `', welcome to our forum!'`

### Acquiring an entity object and deep-referencing its data member, including a format specifier

#### Input
```cs
'The parent group of this product is <{General_Products_Products(1908c05a-790a-42be-a8d8-e850798b5530).ProductGroup.Parent.Name:en}>.'
```
#### Output
```cs
'The parent group of this product is <Materials>.'
```

#### Breakdown
1. `'The parent group of this product is '`
2. `{General_Products_Products(1908c05a-790a-42be-a8d8-e850798b5530).ProductGroup.Parent.Name:en}`
    * Acquires an object of type 'Product' from the `General_Products_Products` entity with the provided 'Id'.
    * Follows the reference path:
        * `.ProductGroup`
            * `.Parent`
                * `.Name`
    * Evaluates to `MultilanguageString` object
    * Format specifier finds `:en` and applies it.
    * Returns  `"Materials"`
3. `'>.'`

### #Error# Not existing entity

#### Input
```cs
'Not_Existing_Entity(4ab5e1ee-c613-4f6c-aa02-eb478c99bc80)'
```

#### Output
```cs
"#Error: Entity 'Not_Existing_Entity' not found#"
```

#### Breakdown
1. `'Not_Existing_Entity(4ab5e1ee-c613-4f6c-aa02-eb478c99bc80)'`
2. Acquires an object from the `Not_Existing_Entity` entity with the provided 'Id' --> Fail. Entity does not exist
3. Returns error.

### #Error# Not existing entity object 'Id'

#### Input
```cs
'Public_Users(ba8469d7-4854-4ff1-a5ac-a0a60414b061)'
```

#### Output
```cs
'#Error: Entity object 'ba8469d7-4854-4ff1-a5ac-a0a60414b061' not found#'
```

#### Breakdown
1. `'Public_Users(ba8469d7-4854-4ff1-a5ac-a0a60414b061)'`
2. Acquires an object of type 'User' from the `Public_Users` entity with the provided 'Id' --> Fail. <br> Could not find an object with such an Id.
3. Returns error.    
