---
uid: cao-INTERPOLATE
items: Operators
---

# INTERPOLATE

| Specification| Value|
| ---- | ----- |
| Description| Performs a string interpolation, according to the context of the input or explicitly passed object.|
| Parameter 1 Name| InterpolatedString|
| Parameter 1 Type| string|
| Parameter 2 Name| InterpolationContext (optional)|
| Parameter 2 Type| object (DomainObject) |
| Parameter 3 Name| - |
| Parameter 3 Type| - |
| Return value| Returns a string, result from the string interpolation.|

> [!WARNING]
> 
> The **interpolate** operator fully depends on the @@erpnet **[string interpolation functionality](../../string-interpolation/index.md)**. <br/> <br/>
> All expressions in `Parameter 1` must conform to the specification.


**Examples:**

> [!NOTE]
> 
> The repository of the calculated attribute is *Crm.Customers*.

Let's try with something simple. We'll get the country name of the enterprise company for each customer. In English.

```
10: INTERPOLATE CONST: Customer's enterprise company country of origin: {EnterpriseCompany.Company.Country.Name:en}
```
OUTPUT:<br/>
Enterprise company country of origin: Bulgaria

EXPLAINED:<br/>
The essential part of the CONST parameter is enclosed in curly braces `{}`. It means the following:
- `{` - start of a single interpolated string expression.
- `EnterpriseCompany` - follow the enterprise company reference of the customer.
- `.Company` - follow the company reference of the enterprise company.
- `.Country` - follow the country reference.
- `.Name` - get the Name attribute.
- `:en` - because it's a multilanguage string - show it in English.
- `}` - end of the interpolated string expression.

---

Now let's involve a system variable.

```
10: INTERPOLATE CONST: What year is it? {$datetime:yyyy}; Who am I? {$user.Name:en}.
```
OUTPUT: <br/>
What year is it? 2023; Who am I? John Doe
EXPLAINED:<br/>
- `$datetime` is the system variable for the current date and time.
- It's followed by the `:yyyy` format specifier, "extracting" just the year part.
- `$user` is the currently logged in user.
- And with `.Name` we're getting its Name attribute.
- `:en` in English.

This example wasn't very practical, but it demonstrates a powerful feature- the [system variables](../../string-interpolation/system-variables.md).

---

The next example is something quite useful. We'll define a calculated attribute, returning its data in JSON format. Just with a single line.

```
10: INTERPOLATE CONST: {{"Timestamp": "{$datetimeutc}", "Id": "{Id}", "Number": "{Number}", "Active": {Active}, "Name": "{Party.PartyName:en}", "SalesPerson": "{SalesPerson.Person.PartyName:en}"}}
```

OUTPUT: <br/>
```
{
   "Timestamp":"2023-01-18 12:46:37",
   "Id":"901d254b-7ad9-44e4-ab96-0668e9258311",
   "Number":"ab30162",
   "Active":true,
   "Name":"Test PK 1",
   "SalesPerson":""
}
```

------------
### See more

- **[String interpolation](../../string-interpolation/index.md)**