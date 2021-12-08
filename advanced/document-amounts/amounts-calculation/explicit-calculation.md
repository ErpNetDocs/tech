# Explicit value calculation

The explicit amount entered through the *Input Amount* and *Input Amount Currency* fields is converted to the document currency. The result is the **end amount** of the additional amount.

**Example:**

There's a document with currency 'BGN' and an additional amount entered as explicit amount - 60 EUR. 

The additional amount is set to use round scale-up to the second digit after the decimal point. 

If the conversion rate is from EUR to BGN 1.96, the additional amount is:

[Input Amount] = ROUND(**60 * 1.96, 2) = 117.60 BGN**.

See **[Percent calculation](percent-calculation.md)** for comparison.
