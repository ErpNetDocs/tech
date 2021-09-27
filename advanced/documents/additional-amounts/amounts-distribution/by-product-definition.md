# Amount Distribution By Product Definition

The distribution by product definition is the same as the  distribution by amount, the only difference is that row weights are used (see [Rows Weighting](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/rows-weighting.md)). So the difference is that the when the additional amount has "Based On  Lines" = True, than the distributional coefficientss are multiplied by  the rows weightings. So the only difference is in the following  calculation formula:

[**ki**] = ([**ki**] + [row amount **i**]) * [weighting **i** (from [Rows Weighting](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/rows-weighting.md)].

For example (as addition of Example 3 from [Percent Value Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/percent-calculation.md)), there is an addition amount "Commission" with input percent of **5%** and three rows (row #10 for **150 EUR**, row #20 for **40 EUR** and row #30 for 69 EUR), which, in relation of [Rows Weighting](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/rows-weighting.md), have the following weights:

\- row #10: weight = **0.00**;
\- row #20: weight = **1.00**;
\- row #30: weight = **1.00**.

The Commission amount is **5.45 EUR** and the distribution of this amount is calculated by the following coefficients:

[**k1**] = [row amount #10] * [row weight #10] = 150 * 0.00 = **0**;
[**k2**] = [row amount #20] * [row weight #20] = 40 * 1.00 = **40**;
[**k3**] = [row amount #30] * [row weight #30] = 69 * 1.00 = **69**.

So the amount of **5.45 EUR** is distributed in 40:69 ratio as follows:

[row #10 commission] = 5.45 EUR * 0 / 109 = **0 EUR**;
[row #20 commission] = 5.45 EUR * 40 / 109 = **2 \**EUR\****;
[row #30 commission] = 5.45 EUR * 69 / 109 = **3.45 \**EUR\****.
