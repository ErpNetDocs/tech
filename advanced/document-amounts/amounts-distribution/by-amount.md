# Amount distribution by amount

When distributing by amount, rows amounts are used to define the distribution proportions. 

Two types exist:

- **row amounts** (only if the additional amount has _Base On Lines_ as 'True');
- **amounts distributed to the rows** (only the ones which  participate in the base amount of the current additional amount).

To define the proportion of row **i**, its coefficient is calculated as follows:

[**k<sub>i</sub>**] = [distributed to row **i** amount1] + [distributed to row **i** amount2] + ... + [distributed to row **i** amountm].

'amount1', 'amount2' ... 'amountm' are the additional amounts to which you add the current additional distributed amount (the amounts listed in its definition in the **Document Amount Type Dependencies** panel). 

If there are no such amounts, thеn in this initial calculation, you have [**k<sub>i</sub>**] = **0**. 

If _Base On Lines_ is 'True' (in the additional amount), the row amount is added to the initial value for [**ki</sub>**]:

[**ki<sub></sub>**] = [**k<sub>i</sub>**] + [row **i** amount].

This is how each row coefficient is calculated. 

Тhe distribution is performed as usual, except for when the amount [**S**] is **0** and the additional amount is calculated as a percent. 

In this case, the amount is distributed equally throughout the rows, and for each row, the calculation is performed like this:

[row **i** distribution] = ROUND([**k<sub>i</sub>**] * [Input Percent], [Round Scale).

If a percent is used for the additional amount calculation, it may be used for the calculation of the distributed amount for each row (to multiply the percent by [**k<sub>i</sub>**], which is the base amount only for the **i** row).

You may avoid the disadvantage of even distribution, but the amount distributed to a row may not be equal to the input percent. This is a huge problem for things like VAT.

**Example 1:**

There are the following additional amounts:

- Corporate discount:

  - Input Percent: **-3%**;
  - Distributed By: **Amount**;
  - Round Scale: **2**;
  - Base On Lines: **True**.

- Eastern bonus:

  - Distributed By: **Amount**;
  - Round Scale: **2**;
  - Input Amount: **-10 EUR**.

- VAT:

  - Input Percent: **20%**;
  - Distributed By: **Amount**;
  - Round Scale: **2**;
  - Base On Lines: **True**;
  - in the **Document Amount Type Dependencies** panel, VAT is also applied on the Corporate discount and Easter bonus;

The document has two rows: row \\#10 for **150 EUR** and row \\#20 for **40 EUR**. 

**[Percent value calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/percent-calculation.html)** explains how the additional amounts are calculated:

[Corporate Discount] = -**5.70 EUR**

[Eastern Bonus] = **-10 EUR**

[VAT] = **34.86 EUR**

For the distribution of corporate discount, there are the following **coefficients**: 

[**k<sub>1</sub>**] = **150** and [**k<sub>2</sub>**] = **40** (only the base line amounts are taken into account)

The [Corporate Discount] is distributed in 150:40 ratio as follows:

[Corporate Discount for row \#10] = -5.70 EUR * 150 / 190 = **-4.50 EUR**; <br>
[Corporate Discount for row \#20] = -5.70 EUR * 40 / 190 = **-1.20 EUR**.

For the next amount - 'Easter bonus' - the distribution is in the same 150:40 ratio. The result is:

[Easter Bonus for row \#10] = -10 EUR * 150 / 190 = -7.894736842105263 EUR ~ **-7.89 EUR**; <br>
[Easter Bonus for row \#20] = -10 EUR * 40 / 190 = -2.105263157894737 EUR ~ **-2.11 EUR**.

For the last additional amount, the coefficients are different. The distributed amounts from the other additional amounts have to be  added to the row amounts. The **coefficients** are as follows:

[**k<sub>1</sub>**] = [Corporate Discount for row \#10] + [Easter Bonus for row \#10] + [line amount for row \#10] = -4.5 + -7.89 + 150 = 137.61;
[**k<sub>2</sub>**] = [Corporate Discount for row \#20] + [Easter Bonus for row \#20] + [line amount for row \#20] = -1.2 + -2.11 + 40 = 36.69.

The **VAT distribution** is as follows:

[VAT for row \#10] = 34.86 EUR * 137.61 / 174.3 = 27.522 EUR ~ **27.52 EUR**; <br>
[VAT for row \#20] = 34.86 EUR * 36.69 / 174.3 = 7.338 EUR ~ **7.34 EUR**.

**Example 2:**

There are **20%** VAT and three document rows - \#10 with **100 EUR,** \#20 with **-30 EUR** and \#30 with **-70 EUR**. 

In this case, VAT is **0 EUR**, but it's inappropriate to distribute **0 EUR** on each row, no matter what the coefficients are. By rule, each separate row must have **nonzero** VAT. Even if for some reason the VAT is not equal to **0**, then it shouldn't be distributed equally throughout the rows (as it will be, if you distribute by quantity and have [**S**] = **0**). The amounts on each row are **different**. 

This is why a specific calculation of the distributed amounts is applied:

[VAT for row \#10] = 100 EUR* 0.2 = **20 EUR**; <br>
[VAT for row \#20] = -30 EUR * 0.2 = **-6 \**EUR\****; <br>
[VAT for row \#30] = -70 EUR * 0.2 = **-14 \**EUR\****. <br>

> [!NOTE] 
> 
> There's a specific case where the additional amount is distributed by **amount**. <br> If some rows/coefficients in the document are positive and others negative, as is described in **[Percent value calculation](https://docs.erp.net/tech/advanced/document-amounts/amounts-calculation/percent-calculation.html)**, except the total amount of the additional amount, there are also two **subtotals** - positive amount/part and negative amount/part. The amount distribution is performed in two stages: first, the positive subtotals are distributed among the rows with positive amounts and then, the negative subtotal is distributed among the rows with negative amounts. 

**Example 3:**

There's an additional amount VAT with input percent **20%** and three document rows:

row \#10 with amount of **74 EUR**, row \#20 with amount of **26 EUR** and row \#30 with amount of **-45 EUR**. 

The VAT amount is **11 EUR** and the the subtotals are [positive VAT] = **20 EUR** and [negative VAT] = **-9 EUR**. 

The **20 EUR** are distributed on row \#10 and row \#20 in 74:26 ratio:

[VAT for row \#10] = 20 EUR * 74 / 100 = **14.80 EUR**;

[VAT for row \#20] = 20 EUR * 26 / 100 = **5.20 EUR**

Then, the [negative VAT] subtotal is distributed on the last document row: 

[negative VAT] = **-9 EUR** = [VAT for row \#30]
