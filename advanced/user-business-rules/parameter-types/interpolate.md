# Interpolate

Interpolate is a parameter type of the user business rules **[actions](../action-types/index.md)**, introduced in version 24.

It represents a string interpolation as input, which supports:
- [reference following](../../string-interpolation/expression-types/data-member.md)
- [system-variables](../../string-interpolation/system-variables.md)
- [format specifiers](../../string-interpolation/format-specifiers.md)
- [expanding entities](../../string-interpolation/expression-types/entity.md)
- [and much more](../../string-interpolation/index.md)

> [!WARNING]
> 
> The **interpolate** operator fully depends on the @@erpnet **[string interpolation functionality](../../string-interpolation/index.md)**. <br/> <br/>
> All expressions in `Parameter 1` must conform to the specification.

**Example:**

Using `Interpolate`, this text

```
Hello, {$user.Name}\r\n
Today is {$date}.\r\n
Your web store has a new order!\r\n
{{SUMMARY}}\r\n
Number: {DocumentNo}\r\n
From: {Customer.Party.PartyName}\r\n
Order date: {DocumentDate:dd-MM-yyyy}\r\n
Shipping address:{ShipToPartyContactMechanism.ContactMechanism.Name}\r\n
Order total: {#CalculatedAttributeTotalSalesOrderAmount:C}
```
 
will be returned as:

```
Hello, John Doe
Today is 2023-11-01.
Your web store has a new order!
{SUMMARY}
Number: 00329
From: Jane Doe
Order date: 10-05-2019
Shipping address: 21 Lombard St
Order total: $14.82
```

-------------
## See more

- **[String interpolation](../../string-interpolation/index.md)**
- **[Calculated attributes INTERPOLATE operator](../../calculated-attributes/operators/interpolate.md)**