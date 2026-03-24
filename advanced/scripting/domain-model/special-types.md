# Special types

The @@name Domain Model provides a set of advanced types designed to address complex business requirements, including custom properties, multilingual data, precise amounts, and quantities.

All special types are defined in the `Domain.Types` namespace.

This section describes how to work with these types in your scripts.

## Custom properties

Entities can have user-defined (custom) properties that are accessible via the CustomProperties collection.

You can retrieve or update the value of a custom property using a simple string assignment:

```js
// Access the value of a custom property by its code
var currentTier = subject.CustomProperties['CustomerTier'].Value;

// Update only the value of a custom property
subject.CustomProperties['CustomerTier'] = 'Platinum';
```

If you need to update both the value and the description simultaneously, you can instantiate a `CustomPropertyValue` object. For a standard, single-language description, you can simply pass two strings into the constructor:

```js
// Update both the value and description using standard strings
var tierProperty = new Domain.Types.CustomPropertyValue('Platinum', 'Highest ranking customer tier');
subject.CustomProperties['CustomerTier'] = tierProperty;
```

For advanced scenarios requiring localized descriptions, you can pass a `MultilanguageString` object directly into the `CustomPropertyValue` constructor instead of a plain string:

```js
// Create a multi-language description for the customer tier
const localizedDescription = new Domain.Types.MultilanguageString({
    en: 'Platinum Tier Customer',
    bg: 'Платинен клиент',
    fr: 'Client de niveau Platine',
    es: 'Cliente de nivel Platino',
    de: 'Platin-Stufe Kunde'
});

// Assign the value and the multi-language description
var tierPropertyMultiLang = new Domain.Types.CustomPropertyValue('Platinum', localizedDescription);
subject.CustomProperties['CustomerTier'] = tierPropertyMultiLang;
```

> [!NOTE]
> 
> You can find more information about custom properties [here](../../stored-attributes/index.md).

## Multilanguage strings

`MultilanguageString` enables storing and accessing text values in multiple languages.

```js
// Create a multilingual string with values for different languages
var productStatus = new Domain.Types.MultilanguageString({
    en: 'In Stock',
    bg: 'В наличност',
    fr: 'En stock',
    es: 'En stock',
    de: 'Auf Lager'
});
```

To retrieve the value for a specific language, use the corresponding language code:

```js
// Get the value in English
var englishValue = productStatus['en']; // 'In Stock'

// Get the value in Bulgarian
var bulgarianValue = productStatus['bg']; // 'В наличност'
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
