# Special types

The @@name Domain Model provides a set of advanced types designed to address complex business requirements, including custom properties, multilingual data, precise amounts, and quantities.

All special types are defined in the `Domain.Types` namespace.

This section describes how to work with these types in your scripts.

## Custom properties

Entities can have user-defined (custom) properties that are accessible via the CustomProperties collection.

```js
// Access the value of a custom property by its code
var value = subject.CustomProperties['C1'].Value;

// Update the value of a custom property
subject.CustomProperties['C1'] = 'New custom value';
```

> [!NOTE]
> 
> You can find more information about custom properties [here](../../stored-attributes/index.md).

## Multilanguage strings

`MultilanguageString` enables storing and accessing text values in multiple languages.

```js
// Create a multilingual string with values for different languages
var str = new Domain.Types.MultilanguageString({
    en: 'Hello',
    bg: 'Здрасти',
    fr: 'Bonjour'
});
```

To retrieve the value for a specific language, use the corresponding language code:

```js
// Get the value in English
var englishValue = str['en']; // 'Hello'

// Get the value in Bulgarian
var bulgarianValue = str['bg']; // 'Здрасти'
```

> [!WARNING]
>
> `MultilanguageString` is immutable. Once created, its values cannot be changed.
> 
> If you need a different value, create a new instance with the updated translations.

> [!NOTE]
> 
> You can find more information about multi-language strings [here](../../../concepts/multi-language.md).

## Amount

The `Amount` type allows for accurate calculations with currency values.

```js
// Create an amount and perform arithmetic operations
// Example: EUR must be a valid currency object, e.g., retrieved from the subject, a repository or related entity.
var amount = new Domain.Types.Amount(10, EUR);
var total = Domain.Types.Amount.Multiply(amount, 5); // Result: 50 EUR
```

## Quantity

`Quantity` supports operations with amounts and units.

```js
// Create quantities and calculate ratios
// Example: Pcs must be a valid unit object, e.g., retrieved from the subject, a repository or related entity.
var quantity1 = new Domain.Types.Quantity(10, Pcs);
var quantity2 = new Domain.Types.Quantity(5, Pcs);
var ratio = Domain.Types.Quantity.Divide(quantity1, quantity2); // Result: 2
```