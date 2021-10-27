# Explicit value calculation

The explicit amount entered through the *Input Amount* and *Input Amount Currency* fields, is converted to the document currency. The result is the end amount of the additional amount.

#### Example:

There is a document with currency 'EUR' and an additional amount entered as explicit amount - 60 EUR. The additional amount is set to use round Scale up to the second digit after the decimal point. If the conversion rate is 1.96, then the additional amount is:

[Input Amount] = ROUND(**60 * 1.96, 2) = 117.60EUR**.

Check out [Percent calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/percent-calculation.html) for comparison.
