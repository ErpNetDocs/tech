# Percent Value Calculation
Here, the percent from "Input Percent" is used. First, we should know the value of which amounts will be used to apply the percent calculation. This is defined in the additional amount definition in "Base On Line" field and "Document Amount Type Dependencies" panel (there is an alternative name to this panel - "Base Additional Amounts"). According to these definitions the base amount for the additional amount is calculated. This base amount is used to calculate the end value of the additional amount using the following formula:
 
**[Amount] = ROUND([Base Amount] * [Input Percent], [Round Scale])**.
 
The Base amount is defined as follows:

1. Sum the amounts of the current document to all additional amounts, which are listed in the "Document Amount Type Dependencies" panel ("Base Additional Amounts"). This requires the previous calculation of the other amounts before we start calculating the current additional amount.
2. If the Additional Amount is marked as "Base On Lines", then the sum from p.1 is added to the sum of the document rows, multiplied by their specific weights (if there are any; if there are no weights - then we multiply by 100%. For more information, see **[Rows Weighting](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/rows-weighting.md)**).

Here are some examples:

*Example 1*:
If we have the following additional amounts:

- Corporate Discount:
    - Default Percent is -3%;
    - Base On Lines is True;
    - there are no other additional amounts listed in the "Document Amount Type Dependencies" panel;
    - Round Scale is "2";
- Easter bonus:
    - No Default percent;
    - Amount Input Allowed is True;
    - Percent Input Allowed is False;
    - Round Scale is "2";
- VAT:
    - Default Percent is 20%;
    - Base On Lines is True;
    - in the "Document Amount Type Dependencies" panel is listed that the VAT is applied also on "Corporate Discount" and "Easter Bonus" additional amounts;
    - Round Scale is "2";
 
If we have two document rows - one with a line amount of 150 EUR and the second with 40 EUR line amount. Then we enter an additional amount "Easter Bonus" value of "-10 EUR". The calculations for the three additional amounts are as follows:
- Corporate Discount base amount is **150 EUR + 40 EUR = 190 EUR** (only the sum of the document rows); so the "Corporate Discount" is calculated: [Corporate Discount] = ROUND(**190 EUR * -0.03, 2**) = **-5.70 EUR**;
- the "Easter Bonus" is **-10 EUR** (there is no currency conversion because the amount is in EUR);
- VAT is calculated as follows: [base amount] = [document rows amounts] + [Corporate Discount] + [Easter Bonus]  = **190 EUR + -5.70 EUR+ -10 EUR = 174.3 EUR**; so **[VAT] = ROUND(174.3 EUR * 0.2, 2) = 34.86 EUR**
 
*Example 2*:

In the current example, we have only one additional amount - "Commission". Its definition has the following properties:
- Default Percent is 5%;
- Distribute By is "Product Definition". The weight of the specific product is 100%;
- Base On Lines is True;
- Add To Customer is False;
- Add To Line is False;
- Round Scale is "2".

The example document has three rows:
- row #10 with the amount of 150 EUR;
- row #20 with the amount of 40 EUR; the row contains the specific product;
- row #30 with the amount of 69 EUR; the row contains the specific product.

So the rows have the following specific weights:
- row #10: weight = **0.00**;
- row #20: weight = **1.00**;
- row #20: weight = **1.00**;
 
So the base amount for the "Commission" additional amount is calculated as follows:

[base amount] = **150 EUR * 0.00 + 40 EUR * 1.00 + 69 EUR * 1.00 = 109 EUR**

The final result for the amount is:

[Commission] = ROUND(**109 EUR * 0.05, 2**) = **5.45 EUR**
>[!NOTE]<br> When we have to calculate percent and the document amount is part of the base amount (meaning "Based On Lines" is True) and the document has rows with different signs (negative and positive amounts), then there is a specific way to calculate the additional amount. Besides the end result, two subtotals are calculated - [positive amount] and [negative amount]. They are calculated by separating the row types - rows with positive amounts and rows with negative amounts - and for every group of rows, the additional amount is calculated separately (as described earlier). So the final result is:<br>
 [additional amount] = [positive amount] + [negative amount]<br>
 These two subtotals eventually may be used in the additional amount distribution. For further information, see [Amounts Distribution](https://github.com/ErpNetDocs/tech/blob/011b4e20c2f19c3fe62779e947d92025ae20932b/advanced/documents/additional-amounts/amounts-distribution/index.md).

*Example 3*:

If we have the following properties in the additional amount, VAT:
- Default Percent is True;
- Round Scale is 2;
- Base On Lines is True;

The example document has the following rows:
- row #10 with the amount of 74 EUR;
- row #20 with the amount of 26 EUR;
- row #30 with the amount of -45 EUR;
 
So the base amount of the additional amount is:<br>

[VAT] = ROUND((**74 EUR+ 26 EUR + -45 EUR**) * **0.2**, 2) = ROUND(**55 EUR * 0.2**, 2) = **11 EUR**,

but we also have the additional subtotals:<br>

[positive VAT amount] = ROUND((**74 EUR + 26 EUR**) * **0.2**, 2) = ROUND(**100 EUR * 0.2**, 2) = **20 EUR**,<br>
[negativeVAT amount] = ROUND(**-45 EUR** * 0.2, 2) = **-9 EUR**.<br>
and their sum is equal to [VAT] (20 EUR + -9 EUR = 11 EUR)


