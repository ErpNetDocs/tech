# Determine Unit price and Line amount in Invoice Orders

The Invoice orders and their lines are created to generate Invoice documents with the aid of particular Sales order Lines are invoiced. For this reason, every Invoice order lines points to and fulfils exactly one Sales order line.
 
In some cases though, when the parent document is a Shipment, for example, the Unit price and Line amount could not be copied directly from the parent document. They could not be copied from the Sales order as well, because the line might be broken down (by lots for example) during the goods issue and the Line amount will not be the same. Therefore those amounts must be calculated.
 
# Calculation
 
Initially, when the Invoice order and its lines are created, the **Quantity** is copied from the parent documents line, the **Unit price** and the discounts are copied from the Parent Sales order line. The Quantity and Unit price values are used for the calculation of the **Line amount**.
 
 
***The algorithm is as follows***:
 
**[LineAmount] = Round([Quantity] * [Unit price] * (1 - [Line Standard Discount Percent]) * (1 - [Line Custom Discount Percent]))**
 
*The Line amount is rounded up to the second digit.
 
***Example:***
 
*SalesOrderLine1*: Quantity = 3 PCS , UnitPrice = 2.5694 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, LineAmount = 5.78 EUR
 
*ShipmentLine1*: Quantity = 2 PCS
 
*ShipmentLine2*: Quantity = 1 PCS
 
 
*InvoiceOrderLine1*: Quantity = 2 PCS, UnitPrice 
= 2.5694 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, LineAmount = 2*2.5694*(0.75) = 3.8541 ~ 3.85 EUR
 
*InvoiceOrderLine 2*: Quantity = 1 PCS, UnitPrice = 2.5694 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, LineAmount = 1*2.5694*(0.75) = 1.92705  ~ 1.93 EUR
 
Then when saving the document the Discrepancy System (for more information see **Discrepancy System**) initializes а depletion of the **rounded Line amount** which leads to a recalculation of the **Unit price:**
 
**[Unit price] = Round([LineAmount] / (1 - [Line Standard Discount Percent]) / (1 - [Line Custom Discount Percent]) / [Quantity] )**
 
 *The Unit price is rounded up to the fifth digit.
 
***Example:***

*InvoiceOrderLine1*: Quantity = 2 PCS, LineAmount = 3.85 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, UnitPrice = 3.85 / 0.75 / 2  = 2.5666666... ~  2.56667 EUR
 
*InvoiceOrderLine2*: Quantity = 1 PCS, LineAmount = 1.93 EUR, LineStandardDiscountPercent = 0.00 %, LineCustomDiscountPercent = 25.00 %, UnitPrice = 1.93 / 0.75 / 1 = 2.57333333... ~  2.57333 EUR

