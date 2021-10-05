# Amount distribution by amount

When distributing by amount, to define the distribution proportions rows amounts are used. Two types of amounts are used:

- row amounts (only if the additional amount has "Based On Line" is True);
- the amounts that are distributed to the rows (only the ones which  participate in the base amount of the current additional amount).

So, to define the proportion of row **i**, its coefficient is calculated (initially) as follows:

[**ki**] = [distributed to row **i** amount1] + [distributed to row **i** amount2] + ... + [distributed to row **i** amountm].

So amount1, amount2 ... amountm are the additional amounts, to which we add the current additional amount  that is distributed (i.e. the amounts, that are listed in its definition in the "Document Amount Type Dependencies" panel). If there are no such amounts, than in this initial calculation we have [**ki**] = **0**. Also if "Base On Lines" is true (in the current additional amount), than to the initial value for [**ki**] the row amount is added.

[**ki**] = [**ki**] + [row **i** amount].

This is how each row coefficient is calculated. After that the distribution  is performed as usual, except for the case when the amount [**S**] is **0** and the additional amount is calculated as a percent. In this case the  amount is distributed equally through the rows and for each row the  calculation is performed like this:

[row **i** distribution] = ROUND([**ki**] * [Input Percent], [Round Scale).

The idea behind this special case is that if a percent is used for the  additional amount calculation, than this percent may be used for the  calculation of the distributed amount for each row (i.e. to multiply the percent by [**ki**], which is the base amount only for the **i** row). Hereby, we avoid the disadvantage of the even distribution - the amount distributed to a certain row maynot be equal to the input percent (this is huge problem, for example, in cases like VAT). *Example 2,* below, demonstrate such distribution.

*Example 1:*

There are the following additional amounts:

- Corporate Discount:

  - Input Percent: **-3%**;
  - Distributed By: **Amount**;
  - Round Scale: **2**;
  - Base On Line: **True**.

- Eastern Bonus:

  - Distributed By: **Amount**;
  - Round Scale: **2**;

  - Input Amount: **-10 EUR**.

- VAT:

  - Input Percent: **20%**;
  - Distributed By: **Amount**;
  - Round Scale: **2**;
  - Base On Line: **True**;
  - in "Document Amount Type Dependencies" panel is listed that the VAT is  applied also on "Cosporate Discount" and "Easter Bonus" additional  amounts;

The document has two rows: row \\#10 for **150 EUR** and row \\#20 for **40 EUR**. In [Percent Value Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/percent-calculation.md) is explained how the additional amounts are calculated:

[Corporate Discount] = -**5.70 EUR**

[Eastern Bonus] = **-10 EUR**

[VAT] = **34.86 EUR**

So for the distribution of Corporate Discount there are the following coefficients [**k1**] = **150** and [**k2**] = **40** (only the base line amounts are taken into account). So the [Corporate Discount] is distributed in 150:40 ratio as follows:

[Corporate Discount for row \#10] = -5.70 EUR * 150 / 190 = **-4.50 EUR**;
[Corporate Discount for row \#20] = -5.70 EUR * 40 / 190 = **-1.20 EUR**.

For the next amount - "Easter Bonus" - the distribution is in the same ratio 150:40. The result is:.

[Easter Bonus for row \#10] = -10 EUR * 150 / 190 = -7.894736842105263 EUR ~ **-7.89 EUR**;
[Easter Bonus for row \#20] = -10 EUR * 40 / 190 = -2.105263157894737 EUR ~ **-2.11 EUR**.

For the last additional amount, the coefficients are different, because the distributed amounts from the other additional amounts haveto be  added to the row amounts. So the coefficients are as follows:

[**k1**] = [Corporate Discount for row \#10] + [Easter Bonus for row \#10] + [line amount for row \#10] = -4.5 + -7.89 + 150 = 137.61;
[**k2**] = [Corporate Discount for row \#20] + [Easter Bonus for row \#20] + [line amount for row \#20] = -1.2 + -2.11 + 40 = 36.69.

So the VAT distribution is as follows:

[VAT for row \#10] = 34.86 EUR * 137.61 / 174.3 = 27.522 EUR ~ **27.52 EUR**;
[VAT for row \#20] = 34.86 EUR * 36.69 / 174.3 = 7.338 EUR ~ **7.34 EUR**.

*Example 2:*

There are **20%** VAT and three document rows - row \#10 with **100 EUR,** row \#20 with **-30 EUR** and row \#30 for **-70 EUR**. In this case the VAT is **0 EUR**, but it is not appropriate to distribute **0 EUR** on each row (no matter what the coefficients are), as by law each row  separately must have nonzero VAT. Even if for some reason (for example  specifing roundings) the VAT is not equal to **0**, than it is not appropriate to distribute it equally through the rows (as it will be if we distribute by quantity and we have [**S**] = **0**), because the amounts on each row are different. This is the reason why  in these cases a specific calculation of the distributed amounts is  applied:

[VAT for row \#10] = 100 EUR* 0.2 = **20 EUR**;
[VAT for row \#20] = -30 EUR * 0.2 = **-6 \**EUR\****;
[VAT for row \#30] = -70 EUR * 0.2 = **-14 \**EUR\****.

 

> **_NOTE:_**  note text Also there is a specific case when the additional amount is distributed by  amount. If some rows/coefficients in the document are positive and some  of them are negative - as it is discribed in [Percent Value Calculation](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/amounts-calculation/percent-calculation.md), in these cases except the total amount of the additional amount there  are also two subtotals - positive amount/part and negative amount/part.  The amount distribution is performed in two stages - at first the positive subtotals are distributed throught the rows with positive  amounts and then the negative subtotal is distributed throught the rows  with negative amounts.

*Example 3:*

There is an additional amount VAT with input percent **20%**  and three document rows - row \#10 with amount of **74 EUR**, row \#20 with amount of **26 EUR** and row \#30 with amount of **-45 EUR**. The VAT amount is **11 EUR** and the the subtotals are [positive VAT] = **20 EUR** and [negative VAT] = **-9 EUR**. Then at first the **20 EUR** are distributed on row \#10 and row \#20 in 74:26 ratio:

[VAT for row \#10] = 20 EUR * 74 / 100 = **14.80 EUR**;

[VAT for row \#20] = 20 EUR * 26 / 100 = **5.20 EUR**

And than the [negative VAT] subtotal is distributed on the last document row: [negative VAT] = **-9 EUR** = [VAT for row \#30]
