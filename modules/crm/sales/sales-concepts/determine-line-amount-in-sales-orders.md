# Determine Line Amount in Sales Orders
The Line Amount in a Sales Order is formed by the following fields: **"Quantity"**, **"Unit Price"**, **" Line Standard Discount Percent"** and **"Line Custom Discount Percent"**. The fields **"Unit Price", "Line Standard Discount Percent"** and **"Line Custom Discount Percent"** represent the trade conditions in the row. They may be managed/filled as a nomenclature - as product prices, discounts, bonus programs and promotions.
The formula of the field Line Amount is rounded up to the second digit and is as follows:

**[LineAmount]** = Round(**[Quantity]** * **[Unit Price]** * (1 - **[Line Standard Discount Percent]**) * (1 - **[Line Custom Discount Percent]**))
 
***Example 1***:

In the row there is Quantity **7 PCS** and Unit Price **0.15472 EUR** and no discounts, then the Line Amount is:

**[Line Amount]** = Round(**7 * 0.15472** * (1 - 0) * (1 - 0)) = Round(**1.08304**) = **1.08**.
 
***Example 2***:

In the row there is Quantity **27 PCS** and Unit Price **0.15472 EUR**, the discounts are **19%** and **7%**, then the Line Amount is:

**[Line Amount]** = Round( **27 * 0.15472** * (1 - **0.19**) * (1 - **0.07**)) = Round(**1.08304**) = **1.08**.
 
There are also other row amount types which meaning and calculation are different than those of amount saved in the field LineAmount. For more information see **[Amount To Pay](https://github.com/ErpNetDocs/tech/blob/master/modules/crm/sales/sales-concepts/amount-to-pay.md)**.

