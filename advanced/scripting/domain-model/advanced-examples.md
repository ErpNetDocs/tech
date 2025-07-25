# Advanced examples

This section demonstrates advanced scripting scenarios in the @@name Domain Model, providing solutions for more complex business requirements and illustrating powerful techniques you can use in your scripts.

## Object initializers

Object initializers let you create and configure entities (including related objects) in a single, concise statement.

### Before: Without object initializer

```js
// Create a customer and related entities step by step
var customer = Domain.Crm.Sales.CustomersRepository.createNew();
customer.Number = 321;
customer.Active = true;

var customerType = Domain.Crm.Sales.CustomerTypesRepository.createNew();
customerType.Name = 'VIP';
customer.CustomerType = customerType;

var party = Domain.General.Contacts.PersonsRepository.createNew();
party.FirstName = 'John';
party.LastName = 'Doe';
customer.Party = party;
```

### After: Using object initializer

```js
// Create and initialize everything in one statement
var customer = Domain.Crm.Sales.CustomersRepository.createNew({
    Number: 321,
    Active: true,
    CustomerType: Domain.Crm.Sales.CustomerTypesRepository.createNew({
        Name: 'VIP'
    }),
    Party: Domain.General.Contacts.PersonsRepository.createNew({
        FirstName: 'John',
        LastName: 'Doe'
    })
});
```

Object initializers make scripts more concise and easier to read, especially when working with complex or nested entities.

## Advanced queries and filtering

In advanced scenarios, you may need to retrieve entities based on multiple criteria, ranges, references to other entities, or special options.

### Shorthand equals syntax

ou can use the shorthand filtering syntax when you want to match by `equals`, without writing it explicitly.

- Regular syntax:

```js
var customers = Domain.Crm.Sales.CustomersRepository.query({
    active: { equals: true },
    customerType: { equals: customerType }
});
```

- Shorthand syntax:

```js
var customers = Domain.Crm.Sales.CustomersRepository.query({
    active: true,
    customerType: customerType
});
```

### Filter by multiple property Values

Retrieve all customers who are active and have a specific customer type.

```js
var customers = Domain.Crm.Sales.CustomersRepository.query({
    active: true,
    customerType: { equals: customerType }
});
```

### Search within date or number ranges

Find all customers whose `fromDate` is within a specific range:

```js
var customers = Domain.Crm.Sales.CustomersRepository.query({
    fromDate: [
        { greaterthanorequal: new Date(2025, 6, 1) },
        { lessthanorequal: new Date(2025, 6, 10) }
    ]
});
```

> [!NOTE]
>
> When using the JavaScript Date constructor, months are zero-based (i.e., January is 0, July is 6).
> So `new Date(2025, 6, 1)` creates a date for `01-07-2025`.

### Query by references

You can filter entities based on their relationship to other entities by passing a reference in your query filter.

This is useful when you want to retrieve records linked to a specific related object, such as finding all customers associated with a particular person.

```js
// Assume 'person1' is a Person entity obtained earlier in the script.
var customers = Domain.Crm.Sales.CustomersRepository.query({
    party: { equals: person1 }
});
```

This example will return all customer entities where the party property references the `person1` object.

You can also use reference filters with other related properties, such as retrieving all sales orders for a particular customer:

```js
// Assume 'customer' is a Customer entity.
var salesOrders = Domain.Crm.Sales.SalesOrdersRepository.query({
    customer: { equals: customer }
});
```

### Include or exclude `null` values

You can include or exclude entities where a specific property is not set (i.e., is `null`).

This is helpful when you want to combine results for both a particular value and records where the property is not set.

```js
// Find customers where 'number' is '0' or is not set (null).
var customers = Domain.Crm.Sales.CustomersRepository.query({
    number: [
        { equals: '0' },
        { includeNulls: true }
  ]
});
```

This query returns all customers whose number is `'0'`, as well as customers where the number property is not set at all.

### Limit the number of results returned

You can control how many entities are returned from a query by using the `fetch` option.

This is especially useful for paging or performance optimization.

```js
// Fetch only the first 3 active customers.
var customers = Domain.Crm.Sales.CustomersRepository.query(
    { active: true },
    { fetch: 3 }
);
```

This query will return up to three customer entities that are active.

> [!NOTE]
>
> If you do not specify the fetch option, the default maximum number of results returned is `1000`.

### Query comparison operators

When performing queries with the `query()` method, the following comparison operators are supported:

| Operator             | Description                                  | Syntax / Example                       |
| -------------------- | -------------------------------------------- | -------------------------------------- |
| `equals`             | Equal to                                     | `status: { equals: "Active" }`         |
| `in`                 | In a list of values                          | `country: { in: ["US", "CA"] }`        |
| `greaterthanorequal` | Greater than or equal to                     | `age: { greaterthanorequal: 21 }`      |
| `lessthanorequal`    | Less than or equal to                        | `age: { lessthanorequal: 100 }`        |
| `like`               | SQL-style pattern matching                   | `name: { like: "%Corp%" }`             |
| `contains`           | Contains substring                           | `description: { contains: "premium" }` |
| `startswith`         | Starts with substring                        | `email: { startswith: "support@" }`    |
| `endswith`           | Ends with substring                          | `filename: { endswith: ".pdf" }`       |

### Combined advanced query example

This example retrieves up to 10 active customers who:

- Belong to a specific customer type,
- Were created in July 2025,
- Are either related to a specific person or have no related party assigned.

```js
// Assume 'customerType' and 'person1' are entities obtained earlier
var customers = Domain.Crm.Sales.CustomersRepository.query(
    {
        active: true,
        customerType: { equals: customerType },
        fromDate: [
            { greaterthanorequal: new Date(2025, 6, 1) },  // 2025-07-01
            { lessthanorequal: new Date(2025, 6, 31) }     // 2025-07-31
        ],
        party: [
            { equals: person1 },
            { includeNulls: true }
        ]
    },
    {
        fetch: 10
    }
);
```

- **active: true** - Only customers marked as active.
- **customerType: { equals: customerType }** - Filter by a specific customer type entity.
- **fromDate** - Limits results to those created in July 2025.
- **party** - Includes customers linked to `person1` or with no party assigned `null`.
- **fetch: 10** - Limits the result set to 10 records.

> [!NOTE]
>
> The JavaScript Date constructor uses zero-based months (0 = January, 6 = July).

## Flexible type matching in queries and assignments

In many cases, you don't need to provide an exact type when assigning values or building query filters - @@name will automatically handle certain conversions for you.

### Dates

When working with date properties, you can provide values as JavaScript Date objects, or as ISO date strings (e.g., "2025-07-01"):

```js
// Both examples are valid for date filtering:
var customers1 = Domain.Crm.Sales.CustomersRepository.query({
    fromDate: { equals: new Date(2025, 6, 1) }
});

var customers2 = Domain.Crm.Sales.CustomersRepository.query({
    fromDate: { equals: "2025-07-01" }
});
```

### Multilanguage strings

For properties that expect a `MultilanguageString`, you can assign a plain string.

The system will automatically create a multilanguage value using the current language.

```js
// Assign a plain string; it will be set as a multilanguage value in the user's current culture.
person.FirstName = "John";
```