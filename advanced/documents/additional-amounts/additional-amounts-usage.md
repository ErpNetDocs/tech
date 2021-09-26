# Additional Amounts Usage
The additional amounts are used for different reasons - adding amounts to the main business activity in the document or reporting secondary measurements of the business activity or outside activities.
### Calculating The Amount To Pay
Some of the additional amounts serve for calculating the amount to pay for the document. This is marked in the additional amount definition by adding a check to the ‘Add To Customer’ field. Usually these are amounts like VAT, VAT deviation, discounts, increases, decreases. For more information see **Amount To Pay**.
### Calculating Goods Cost
Likewise, the additional amounts may be used to add value to the goods cost in the **Logistics**.

For example, currently the transport is entered as an additional amount. Thus, when goods are purchased, the transport value is added to the purchase price. Also, when a Stock Transfer from one store to another is executed and it includes transport which cost is added to the issued products, the value of this transport should be added to the products cost before they are received in the second store. Adding the transport to the purchase price or to the store cost is done in the receiving Store Orders or Store Transactions. Then, when a row in the sub-document is created, the value of this row is increased by the distribution in the current row amount of the transport.

The same procedure is applied to all additional amounts which are marked as part of the store cost calculation. This is the ‘Add To Line’ field in the definition of the additional amount.
### Calculating Outside Activities
The additional amounts may also be used to report internal for the enterprise company activities.

For example, if the salesman in the company receives commissions or other additions to their salaries, which is equal to a percent of turnover they achieve. Then this commision may be entered as an additional amount (because it is not proper to be included in the rows of the document) in the Sales Order, which is a percent of the amount to pay.

