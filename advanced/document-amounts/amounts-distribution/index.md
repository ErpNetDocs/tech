# Amounts distribution

After an additional sum is **[calculated](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html)**, the result is not saved directly in the document, but distributed among document rows with nonzero **[weight](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html)** where the additional amount is applied to. This distribution is then reflected in the document. 

After the amount is calculated and distributed, if you need to see the total value of the additional amount, you'll have to sum up all the values from its  distribution. This is easier than saving the total additional amount in the document. To see the VAT or the transport distributed to a specific product, you may often need just the amount distributed to a specific row.

If you save the total additional amount in the document, you'll have to distribute the amounts at the moment, which isn't effective. 

The following article(s) will descirbe different methods for distributing amounts through rows. 

## Common principle of distribution

The distribution principle is defined in the additional amount definition  (by *Distributed By* field). 

There are three basic methods

- by **[quantity](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-quantity.html)**,
- by **[amount](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-amount.html)**, 
- by **[product definition](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-product-definition.html)**. 
 
Every method suggests that a proportion of the amount distributed by the rows should be defined so the distribution can be executed.

If you have **n** rows on which you have to distribute additional amount, for every row, a weight is defined:

[**k1**], [**k2**] ... [**kn**]

These are different coefficients from those described in **[rows weighting](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html)**, but in some specific cases the latter may participate in the calculation of the distribution weights. 

Uf the amount of these coefficients is [**S**] (i.e. [**S**] = [**k1**] + [**k2**] + ... + [**kn**]) and this amount isn't equal to 0, <br> then the **i**-row of the proportion is [**ki**]/[**S**]:

[distribution to row **i**] = ROUND([amount] * [**ki**] / [**S**], [Round Scale]),

where *Round Scale* is property of the additional amount definition. 

This is a **standard distribution alogorithm**. A specific case is when [**S**] is **0**. 

Most of the time, the additional amount is distributed evenly throughout the row, using the following formula:

[row **i** distribution] = ROUND([amount] / [rows count], [Round Scale]),

but in some cases, there are more specific calculations, such as when the amount is distributed by amount or by product definition and the additional amount is percent.

Sometimes, the additional amount may not be distributed evenly among the rows. An attempt is then made to allocate the balance. It's impossible to distribute equal part of the balance to all rows - otherwise, there will be no balance. The balance is therefore distributed throughout the first several rows. 

You can't distribute less than:

[minimal balance distribution on a row] = 1 / 10[Round Scale].

**Example:**

You have **12** rows and the amount of **9.13 EUR** to distribute with the following weights: 

[**k1**] = [**k2**] = ... = [**k10**] = **1**, and [**k11**] = [**k12**] = **0**

**9.13 EUR** is distributed on the first 10 rows and you'll apply the formula to get the the distribution of 9.13 EUR / 10 ~ **0.91 EUR** (assuming you have _Round Scale_ = 2). In this case, you distribute only 10 * 0.91 = **9.10 EUR** and the amount left (**0.03 EUR)** needs to be distributed through the first 10 rows.

Since you can't distribute less than 1 / 102 = 0.01 EUR, only the first three rows increase by 0.01 EUR.

This is how the final distribution looks like: 

- on the first three rows, the amount of **0.92 EUR** is distributed;

- on the next seven rows, the amount of **0.91 EUR** is distributed;

- on the last two rows, no amount is distributed. 
 
If the round scale is more than 2, there's a chance that part of the amount will be lost. 

For example, if the additional amount is **10 EUR** and it's distributed equally throughout **3** rows and the round scale is **3.**, then for every row, the amount of ROUND(3.333333333333333, 3) = **3.333 EUR** will be distributed. 

When you save a document like this, the numbers after the second digit will be cut. 

In the database, you'll have **3.33 EUR** for each row. 

The total amount will be **9.99 EUR** and **0.01 EUR** will be lost.

-----------
### See more 

- **[Amount distribution by amount](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-amount.html)**
- **[Amount distribution by product definition](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-product-definition.html)**
- **[Amount distribution by quantity](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-quantity.html)**
