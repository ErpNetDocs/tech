# Percent value calculation

Here, input percent will be used. 

You should know the value of the amounts which will be used to apply the percent calculation. It's defined by the additional amount definition in the *Base On Lines* field and the **Document Amount Type Dependencies** panel (also known as **Base Additional Amounts**). 

Тhe base amount for the additional amount is calculated and used to find the end value of that amount with the following formula:
 
**[Amount] = ROUND([Base Amount] * [Input Percent], [Round Scale])**.
 
Base amount is defined in two steps:

1. Sum the amounts of the current document to all additional amounts listed in the **Document Amount Type Dependencies** panel. <br>
This requires the previous calculation of the other amounts.

2. If the аdditional аmount is marked as _Base On Lines_, the sum from p.1 is added to the sum of the document rows, multiplied by their specific weights (if there are no weights, you multiply by 100%). 

For more information, see **[Rows weighting](https://docs.erp.net/tech/advanced/document-amounts/rows-weighting.html)**.


**Example 1:**

If you have the following additional amounts:

- Corporate discount:

    - Default Percent is -3%;
    - Base On Lines is True;
    - there are no other additional amounts listed in the **Document Amount Type Dependencies** panel;
    - Round Scale is '2';
    
- Easter bonus:

    - No default percent;
    - Amount input allowed is True;
    - Percent input allowed is False;
    - Round Scale is '2';
    
- VAT:

    - Default Percent is 20%; 
    - Base On Lines is True;
    - the **Document Amount Type Dependencies** panel states that VAT is applied to Corporate discount and Easter bonus;
    - Round Scale is '2';
 
If you have two document rows - one with a line amount of 150 EUR and another with 40 EUR, <br> then you enter an additional Easter bonus value of -10 EUR. 

**The calculations for the three additional amounts are as follows:**

- Corporate discount base amount is **150 EUR + 40 EUR = 190 EUR** (only the sum of the document rows);</br> so [Corporate discount] is calculated = ROUND(**190 EUR * -0.03, 2**) = **-5.70 EUR**;

- Easter bonus is **-10 EUR** (there's no currency conversion because the amount is in EUR);
- VAT is calculated:</br>
[base amount] = [document rows amounts] + [Corporate discount] + [Easter bonus]  = **190 EUR + -5.70 EUR+ -10 EUR = 174.3 EUR**; so **[VAT] = ROUND(174.3 EUR * 0.2, 2) = 34.86 EUR**
 
 
**Example 2:**

You have only one additional amount - commission. Its definition has the following properties:

- Default Percent is 5%;
- Distribute By is 'Product Definition'. The weight of the specific product is 100%;
- Base On Lines is True;
- Add To Customer is False;
- Add To Line is False;
- Round Scale is '2'.

The example document has three rows:

- row #10 with the amount of 150 EUR;
- row #20 with the amount of 40 EUR; the row contains the specific product;
- row #30 with the amount of 69 EUR; the row contains the specific product.

So the rows have the following specific weights:

- row #10: weight = **0.00**;
- row #20: weight = **1.00**;
- row #20: weight = **1.00**;
 
The base amount for the commission  additional amount is calculated as follows:

[base amount] = **150 EUR * 0.00 + 40 EUR * 1.00 + 69 EUR * 1.00 = 109 EUR**

The final result for the amount is:

[Commission] = ROUND(**109 EUR * 0.05, 2**) = **5.45 EUR**

>[!NOTE]
>
> When you have to calculate percent and the document amount is part of the base amount (*Base On Lines* is True) and it has rows with different signs (negative and positive amounts), then there is a specific way to calculate the additional amount. Besides the end result, two subtotals are calculated - [positive amount] and [negative amount]. This is achieved by separating the row types - rows with positive amounts and rows with negative amounts - and for every group of rows, the additional amount is calculated separately. 
> 
> Тhe final result is:
> 
> [additional amount] = [positive amount] + [negative amount]
> 
 These two subtotals may be used in the additional amount distribution. For further information, see **[Amounts distribution](https://docs.erp.net/tech/advanced/document-amounts/amounts-distribution/index.html)**.

**Example 3*:**

If you have the following properties in the additional amount, VAT:

- Default Percent is True;
- Round Scale is '2';
- Base On Lines is True;

the example document has the following rows:

- row #10 with the amount of 74 EUR;
- row #20 with the amount of 26 EUR;
- row #30 with the amount of -45 EUR;
 
and the base amount of the additional amount is:

[VAT] = ROUND((**74 EUR+ 26 EUR + -45 EUR**) * **0.2**, 2) = ROUND(**55 EUR * 0.2**, 2) = **11 EUR**,

But you also have the additional subtotals:

[positive VAT amount] = ROUND((**74 EUR + 26 EUR**) * **0.2**, 2) = ROUND(**100 EUR * 0.2**, 2) = **20 EUR**,<br>
[negativeVAT amount] = ROUND(**-45 EUR** * 0.2, 2) = **-9 EUR**.

and their sum is equal to [VAT](20 EUR + -9 EUR = 11 EUR)


