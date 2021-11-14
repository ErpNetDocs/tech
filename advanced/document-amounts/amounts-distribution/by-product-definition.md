# Amount distribution by product definition

Distribution by product definition is the same as distribution **[by amount](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-amount.html)**, the only difference being that **[row weights](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html)** are used. <br> When the additional amount has _Based On Lines_ = True, the distributional coefficients are multiplied by the rows' weightings. 

The only difference is in the following calculation formula:

[**ki**] = ([**ki**] + [row amount **i**]) * [weighting **i**].

In addition to Example 3 from **[Percent value calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/percent-calculation.html)**, there's an additional amount commission with input percent of **5** and three rows (row #10 for **150 EUR**, row #20 for **40 EUR** and row #30 for 69 EUR) which have the following weights:

row #10: weight = **0.00**; <br>
row #20: weight = **1.00**; <br>
row #30: weight = **1.00**. <br>

The commission amount is **5.45 EUR** and the distribution of this amount is calculated by the following coefficients:

[**k1**] = [row amount #10] * [row weight #10] = 150 * 0.00 = **0**;<br>
[**k2**] = [row amount #20] * [row weight #20] = 40 * 1.00 = **40**;<br>
[**k3**] = [row amount #30] * [row weight #30] = 69 * 1.00 = **69**.

The amount of **5.45 EUR** is distributed in 40:69 ratio as follows:

[row #10 commission] = 5.45 EUR * 0 / 109 = **0 EUR**; <br>
[row #20 commission] = 5.45 EUR * 40 / 109 = **2 EUR**; <br>
[row #30 commission] = 5.45 EUR * 69 / 109 = **3.45 EUR**. 
