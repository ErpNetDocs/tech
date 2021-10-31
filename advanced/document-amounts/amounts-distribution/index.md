# Amounts distribution

After the additional sum is calculated (see [Amounts calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/index.html)), the result is not saved directly in the document, but it is distributed through the document rows ( more precisely - through those rows which  the additional amount is applied to - the ones with nonzero weight, see [Rows weighting](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html)) and this distribution is saved in the document. So after the amount is  calculated and distributed, if the user needs to see the total value of  the additional amount, he has to  sum up all the values from its  distribution. This is easier than saving the total additional amount in  the document, because often the distributed to a specific row amount is  needed (for example - to see the VAT distributed to a specific product  or the transport distributed to a specific product, so that we can add  this amount to its value). If we save the total additional amount in the document, in these cases the user will have to distribute the amounts  at the moment, which is not very effective. 

The article (and the  subarticles) descirbes the methods for distributing the amounts throught the rows. Also, a procedure for amount distribution is described  when, because of roundings, the amount cannot be precisely distributed,  and other specific cases.

## Common principle of distribution

The distribution principle is defined in the additional amount definition  (by *Distributed By* field). There are three basic methods
- by quantity (see [Amount distribution by quantity](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-quantity.html)),
-  by amount (see [Amount distribution by amount](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-amount.html) and 
- by product definition (see [Amount distribution by product definition](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-product-definition.html)). Every method expects that a proportion of the amount distributed by the rows  should be defined so the distribution to be executed.

So if we have **n** rows on which we have to distribute additional amount, for every row a weight is defined - [**k1**], [**k2**] ... [**kn**]. In the common case, these are different coefficients than those described in [rows weighting](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html) (but in some specific cases the coefficients from [rows weighting](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html) may participate in the calculation of the distribution weights). So if the amount of these coefficients is [**S**] (i.e. [**S**] = [**k1**] + [**k2**] + ... + [**kn**]) and this amount is not equal to 0, than the **i**-row the proportion is [**ki**]/[**S**]:

[distribution to row **i**] = ROUND([amount] * [**ki**] / [**S**], [Round Scale]),

where *Round Scale* is property of the additional amount definition. This is a standart distribution alogorithm. Specific cases are when [**S**] is **0**. Usually, in those cases the additional amount is distributed evenly through the row, using the following formula:

[row **i** distribution] = ROUND([amount] / [rows count], [Round Scale]),

but in some cases there are some more specific calculations (for  example,when the amount is distributed by amount or by product  definition and the additional amount is percent).

Sometimes the  additional amount may not be able to be distributed exactly through the  rows. In these cases, an attempt is made to allocate the balance  throught the rows which the amount is distributed to. Normally, it is  impossible to distribute equal part of the balance to all rows  (otherwise there will be no balance). So the balance is distributed  throught the first several rows. Also, in this balance distribution we  cannot distribute less than:

[minimal balance distribution on a row] = 1 / 10[Round Scale].

***Example 1:***

If we have **12** rows and the amount of **9.13 EUR** to distribute with the following weights: [**k1**] = [**k2**] = ... = [**k10**] = **1**, and [**k11**] = [**k12**] = **0**. So **9.13 EUR** is distributed on the first 10 rows and, at first, we apply the formula to get the the distribution of 9.13 EUR / 10 ~ **0.91 EUR** (assuming we have Round Scale = 2). In this case, we distribute only 10 * 0.91 = **9.10 EUR** and the amount left (**0.03 EUR)** have to be distributed through the first 10 rows. As we cannot distribute less than 1 / 102 = 0.01 EUR, so only the first three rows are increase by 0.01 EUR.

This is how the final distribution is achieved: 

- on the first three rows the amount of **0.92 EUR** is distributed;

- on the next seven rows the amount of **0.91 EUR** is distributed;

- the last two rows no amount is distributed. 
 

If the round scale is more than 2 there is a chance part of the amount to be lost. For example, if the additional amount is **10 EUR** and it is distributed equally throught **3** rows and the round scale is **3.** In this case for every row the amount of ROUND(3.333333333333333, 3) = **3.333 EUR** is distributed. When we save a document like this, the numbers after  the second digit after the decimal point will be cut. So in the database we will have **3.33 EUR** for each row. So the total amount will be **9.99 EUR** and **0.01 EUR** will be lost.

For further information on how the distibuted amount is calculated by each method, see the following articles:

 

- **[Amount distribution by amount]**(https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-amount.html)
- **[Amount distribution by product definition]**(https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-product-definition.html)
- **[Amount distribution by quantity]**(https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/by-quantity.html)
