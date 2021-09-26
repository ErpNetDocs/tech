# Explicit Value Calculation

The explicit amount entered through the _'Input Amount'_ and _'Input Amount Currency'_ fields, is converted to the document currency. The result is the end amount of the additional amount.

Example:

There is a document with currency "EUR" and an additional amount entered as explicit amount - 60 EUR. The additional amount is set to use 'Round Scale' up to the second digit after the decimal point. If the conversion rate is 1.96, then the additional amount is:

[Input Amount] = ROUND(**60 * 1.96, 2) = 117.60EUR**.
