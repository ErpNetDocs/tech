---
uid: determine-line-amount-in-sales-orders
---

# Determine line amount in sales orders
The line amount in a sales order is formed by the following fields: ***Quantity***, ***Unit Price***, ***Line Standard Discount Percent*** and ***Line Custom Discount Percent***. The fields *Unit Price*, *Line Standard Discount Percent* and *Line Custom Discount Percent* represent the trade conditions in the row. They may be managed/filled as a nomenclature - as product prices, discounts, bonus programs and promotions.
The formula of the field line amount is rounded up to the second digit and is as follows:

**[LineAmount]** = Round(**[Quantity]** * **[Unit Price]** * (1 - **[Line Standard Discount Percent]**) * (1 - **[Line Custom Discount Percent]**))
 
#### Example 1 :

In the row there is quantity **7 PCS** and unit price **0.15472 EUR** and no discounts, then the line amount is:

**[Line Amount]** = Round(**7 * 0.15472** * (1 - 0) * (1 - 0)) = Round(**1.08304**) = **1.08**.
 
#### Example 2 :

In the row there is quantity **27 PCS** and unit price **0.15472 EUR**, the discounts are **19%** and **7%**, then the line amount is:

**[Line Amount]** = Round( **27 * 0.15472** * (1 - **0.19**) * (1 - **0.07**)) = Round(**1.08304**) = **1.08**.
 
There are also other row amount types which meaning and calculation are different than those of amount saved in the field LineAmount. 

For more information, see [Amount to pay](https://docs.erp.net/tech/modules/crm/sales/sales-concepts/amount-to-pay.html).

