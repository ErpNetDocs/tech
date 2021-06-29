# Amount to pay

**Amount To Pay** is part of Sales Orders and Invoices. 
It is the final amount which the customer has to pay on the current document (Sales Order or Invoice). 
It is calculated as the sum of the row amounts and all additional amounts in the current document which has check in the "**Add To Customer**" attribute in their definitions.

### Example 1:

There is an Invoice with two rows:

- Row #10 - Product **1**, LineAmount: **2 PCS** x **12 EUR** = **24 EUR**
- Row #20 - Product **2**, LineAmount: **3 PCS** x **7 EUR** = **21 EUR**

The document has an additional amount paid by the customer:

- VAT, Amount Percent: **20%** of the line amount of the rows = 0.2 x 45 EUR = **9 EUR**

So the **Amount To Pay** is: **54 EUR** = 24 EUR + 21 EUR +9 EUR.

## Relation To Tax Base And VAT (Invoices)

In most cases the **Amount To Pay** matches the sum of Tax Base and VAT, like in **Example1**, but a difference is possible.
It is possible if there are [Additional Amounts](~/advanced/documents/additional-amounts.md) which are paid by the customer but are not set as base amounts for VAT additional amount.

### Example 2:

There is an Invoice with Line Amount of **45 EUR** and two [Additional Amounts](~/advanced/documents/additional-amounts.md) which are paid by the customer:

- VAT, amount: 20% of **45 EUR** = **9 EUR**
- Penalty Interest - not a VAT base amount, Amount: **20 EUR**

So the *Amount To Pay* is **74 EUR** while the sum of Tax Base and VAT is **54 EUR**. 

### Example 3:

The additional amount **VAT (special cases)** is set that its base amount type is **Tax Base**, **Add To Customer** and **Base On Lines** are **True.** **Tax Base** is not paid by customer.

There is an Invoice with two rows:

- Row #10 - Product **1**, LineAmount: **2 PCS** x **12 EUR** = **24 EUR**
- Row #20 - Product **2**, LineAmount: **3 PCS** x **7 EUR** = **21 EUR**

and [Additional Amounts](~/advanced/documents/additional-amounts.md) as follows:

- **Tax Base**, Amount: **30 EUR**
- **VAT**, Amount Percent **20%** of **30 EUR** = **6 EUR**

In this case the *Amount To Pay* is **45 EUR** while *the sum of Base Tax and VAT* is **36 EUR**.
