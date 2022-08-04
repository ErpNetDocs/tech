# Amounts distribution

After an additional sum is **[calculated](../amounts-calculation/index.md)**, the result is not saved directly in the document, but distributed among document lines with nonzero **[weight](../lines-weighting.md)** where the additional amount is applied to. This distribution is then reflected in the document. 

After the amount is calculated and distributed, if you need to see the total value of the additional amount, you'll have to sum up all the values from its  distribution. This is more conveniently than saving the total additional amount in the document. To see the VAT or the transport distributed to a specific product, you may often need just the amount distributed to a specific line.

The following article(s) will descirbe different methods for distributing amounts through lines. 

## Common principle of distribution

The distribution principle is defined in the additional amount definition  (by *Distributed By* field). 

There are three basic methods

- by **[quantity](by-quantity.md)**,
- by **[amount](by-amount.md)**, 
- by **[product definition](by-product-definition.md)**. 
 
Every method suggests that a proportion of the amount distributed by the lines should be defined so the distribution can be executed.

If you have **n** lines on which you have to distribute additional amount, a weight is defined for every line:

[**k<sub>1</sub>**], [**k<sub>2</sub>**] ... [**k<sub>n</sub>**]

These are different coefficients from those described in **[lines weighting](../lines-weighting.md)**, but in some specific cases the latter may participate in the calculation of the distribution weights. 

Uf the amount of these coefficients is [**S**] (i.e. [**S**] = [**k<sub>1</sub>**] + [**k<sub>2</sub>**] + ... + [**k<sub>n</sub>**]) and this amount isn't equal to 0, <br> then the **i**-line of the proportion is [**k<sub>i</sub>**]/[**S**]:

[distribution to line **i**] = ROUND([amount] * [**k<sub>i</sub>**] / [**S**], [Round Scale]),

where *Round Scale* is property of the additional amount definition. 

This is a **standard distribution alogorithm**. A specific case is when [**S**] is **0**. 

Most of the time, the additional amount is distributed evenly throughout the lines, using the following formula:

[line **i** distribution] = ROUND([amount] / [lines count], [Round Scale]),

but in some cases, there are more specific calculations, such as when the amount is distributed by amount or by product definition and the additional amount is percent.

Sometimes, the additional amount may not be distributed evenly among the lines. An attempt is then made to allocate the balance. It's impossible to distribute equal part of the balance to all lines - otherwise, there will be no balance. The balance is therefore distributed throughout the first several lines. 

You can't distribute less than:

[minimal balance distribution on a line = 1 / 10[Round Scale].

**Example:**

You have **12** lines and the amount of **9.13 EUR** to distribute with the following weights: 

[**k<sub>1</sub>**] = [**k<sub>2</sub>**] = ... = [**k<sub>10</sub>**] = **1**, and [**k<sub>11</sub>**] = [**k<sub>12</sub>**] = **0**

**9.13 EUR** is distributed on the first 10 lines and you'll apply the formula to get the the distribution of 9.13 EUR / 10 ~ **0.91 EUR** (assuming you have _Round Scale_ = 2). In this case, you distribute only 10 * 0.91 = **9.10 EUR** and the amount left (**0.03 EUR)** needs to be distributed through the first 10 lines.

Since you can't distribute less than 1 / 102 = 0.01 EUR, only the first three lines increase by 0.01 EUR.

This is how the final distribution looks like: 

- on the first three lines, the amount of **0.92 EUR** is distributed;

- on the next seven lines, the amount of **0.91 EUR** is distributed;

- on the last two lines, no amount is distributed. 
 
If the round scale is more than 2, there's a chance that part of the amount will be lost. 

For example, if the additional amount is **10 EUR** and it's distributed equally throughout **3** lines and the round scale is **3.**, then for every line, the amount of ROUND(3.333333333333333, 3) = **3.333 EUR** will be distributed. 

When you save a document like this, the numbers after the second digit will be cut. 

In the database, you'll have **3.33 EUR** for each line. 

The total amount will be **9.99 EUR** and **0.01 EUR** will be lost.

-----------
### See more 

[!list folder="." depth=0 style="bullet" limit=100]
