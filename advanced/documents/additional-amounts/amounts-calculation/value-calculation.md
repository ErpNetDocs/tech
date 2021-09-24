# Explicit Value Calculation

The explicit amount, entered through "Input Amount" and "Input Ampunt Currency" fields, is converted to the document currency. The result is the end amount of the additional amount.

For example: If there is a document with currency "EUR", and there is an additional amount entered as explicit amount - 60 EUR. This addiotional amount is defined to use "Round Scale" up to the second digit afterthe decimal point. If the conversion rate form EUR to EUR is 1.96, than the additional amount is:

[Input Amount] = ROUND(**60 * 1.96, 2) = 117.60EUR**.
