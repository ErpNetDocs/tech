---
uid: determine-unit-price-and-line-amount-in-invoice-orders
---

# Determine Unit Price and Line Amount in Invoice Orders

The Invoice Orders and their lines are created to generate Invoice documents with which to be invoiced particular Sales Order Lines. For this reason, every Invoice Order Lines points to and fulfils exactly one Sales Order Line.

In some cases though, when the parent document is a Shipment, for example, the Unit Price and Line Amount could not be copied directly from the parent document. They could not be copied from the Sales Order as well, because the line might be broken down (by lots for example) during the goods issue and the Line Amount will not be the same. Therefore those amounts must be calculated.

# Calculation

Initially, when the Invoice Order and its lines are created the **Quantity** is copied from the parent documents line, the **Unit Price** and the discounts are copied from the Parent Sales Order Line. The Quantity and Unit Price values are used for the calculation of the **Line Amount**.



***The algorithm is as follows:***

**[LineAmount]** = Round(**[Quantity]** * **[Unit Price]** * (1 - **[Line Standard Discount Percent]**) * (1 - **[Line Custom Discount Percent]**))

*The Line Amount is rounded up to the second digit.



***Example:***

*SalesOrderLine1*: Quantity = 3 PCS , UnitPrice = 2.5694 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, LineAmount = 5.78 EUR

*ShipmentLine1:* Quantity = 2 PCS

*ShipmentLine2:* Quantity = 1 PCS

 

*InvoiceOrderLine1:* Quantity = 2 PCS, UnitPrice = 2.5694 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, LineAmount = 2*2.5694*(0.75) = 3.8541 ~ 3.85 EUR

InvoiceOrderLine2: Quantity = 1 PCS, UnitPrice = 2.5694 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, LineAmount = 1*2.5694*(0.75) = 1.92705 ~ 1.93 EUR

 

Then when saving the document the Discrepancy System (for more information see [Discrepancy System](https://olddocs.erp.net/tech/discrepancy-system-22380546.html)) initializes а depletion of the **rounded Line Amount** which leads to a recalculation of the **Unit Price**:

**[Unit Price]** = Round(**[LineAmount]** / (1 - **[Line Standard Discount Percent]**) / (1 - **[Line Custom Discount Percent])** / **[Quantity]** )

 *The Unit Price is rounded up to the fifth digit.



***Example:***

*InvoiceOrderLine1:* Quantity = 2 PCS, LineAmount = 3.85 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, UnitPrice = 3.85 / 0.75 / 2 = 2.5666666... ~ 2.56667 EUR

*InvoiceOrderLine2:* Quantity = 1 PCS, LineAmount = 1.93 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, UnitPrice = 1.93 / 0.75 / 1 = 2.57333333... ~ 2.57333 EUR