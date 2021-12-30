---
uid: amount-to-pay
---

# Amount to pay

Amount to pay is part of the sales orders and invoices. It is the final amount that the customer has to pay on the current document (sales order or invoice). It is calculated as the sum of the row amounts and all additional amounts in the current document which has checked in the Add To Customer attribute in their definitions.

#### Example 1:

There is an invoice with two rows:

- Row #10 - Product **1**, LineAmount: **2 PCS** x **12 EUR** = **24 EUR**
- Row #20 - Product **2**, LineAmount: 3 **PCS** x **7 EUR** = **21 EUR**

The document has an additional amount paid by the customer:

- VAT, Amount Percent: **20%** of the line amount of the rows = 0.2 x 45 EUR = **9 EUR**

So the Amount To Pay is: **54 EUR** = 24 EUR + 21 EUR +9 EUR.

## Relation To Tax Base And VAT (Invoices)

In most cases, the amount to pay matches the sum of tax base and VAT, like in ***Example 1***, but a difference is possible. It is possible if there are [Additional Amounts](~/tech/advanced/document-amounts/index.md) that are paid by the customer but are not set as base amounts for VAT additional amount.

#### Example 2 :

There is an invoice with a line amount of **45 EUR** and two [Additional Amounts](~/tech/advanced/document-amounts/index.md) which are paid by the customer:

- VAT, amount: 20% of **45 EUR** = **9 EUR**
- Penalty Interest - not a VAT base amount, Amount: **20 EUR**

So the Aount To Pay is **74 EUR** while the sum of Tax Base and VAT is **54 EUR**. 

***Example 3***:

The additional amount **VAT (special cases)** is set that its base amount type is **Tax Base**, *Add To Customer* and *Base On Lines* are *True*. **Tax Base** is not paid by the customer.

There is an invoice with two rows:

- Row #10 - Product **1**, LineAmount: **2 PCS** x **12 EUR** = **24 EUR**
- Row #20 - Product **2**, LineAmount: **3 PCS** x **7 EUR** = **21 EUR**

and [Additional Amounts](~/tech/advanced/document-amounts/index.md) as follows:

- **Tax Base**, Amount: **30 EUR**
- **VAT**, Amount Percent **20%** of **30 EUR** = **6 EUR**

In this case, the Amount To Pay is **45 EUR** while the sum of Base Tax and VAT is **36 EUR**.
