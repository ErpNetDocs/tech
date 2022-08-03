# Amount distribution by product definition

Distribution by product definition is similar to the **[by amount distribution](by-amount.md)**, the only difference being that **[line weights](lines-weighting.md)** are used. When the additional amount has _Based On Lines_ = True, the distributional coefficients are multiplied by the lines' weights. 

The only difference is in the following calculation formula:

[**k<sub>i</sub>**] = ([**k<sub>i</sub>**] + [line amount **i**]) * [line weight **i**].

In addition to Example 3 from **[Percent value calculation](/advanced/document-amounts/amounts-calculation/percent-calculation.md)**, there's an additional amount commission with input percent of **5** and three lines (line #10 for **150 EUR**, line #20 for **40 EUR** and line #30 for 69 EUR) which have the following weights:

line #10: weight = **0.00**; <br>
line #20: weight = **1.00**; <br>
line #30: weight = **1.00**. <br>

The commission amount is **5.45 EUR** and its distribution is calculated by the following coefficients:

[**k<sub>1</sub>**] = [line amount #10] * [line weight #10] = 150 * 0.00 = **0**;<br>
[**k<sub>2</sub>**] = [line amount #20] * [line weight #20] = 40 * 1.00 = **40**;<br>
[**k<sub>3</sub>**] = [line amount #30] * [line weight #30] = 69 * 1.00 = **69**.

The amount of **5.45 EUR** is distributed in 40:69 ratio as follows:

[line #10 commission] = 5.45 EUR * 0 / 109 = **0 EUR**; <br>
[line #20 commission] = 5.45 EUR * 40 / 109 = **2 EUR**; <br>
[line #30 commission] = 5.45 EUR * 69 / 109 = **3.45 EUR**. 
