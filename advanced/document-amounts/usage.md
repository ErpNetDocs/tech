# Additional amounts usage

Additional amounts are used for different reasons - adding amounts to the main business activity in the document or reporting secondary measurements for the business or outside activities.

## Calculating the amount to pay

Some additional amounts serve to calculate the amount to pay for the document. This is marked in the additional amount definition by adding a check to the *Add To Customer* field. Usually, these are amounts like VAT, VAT deviation, discounts, increases, decreases. 

For more information, see [Amount Тo Пay](https://docs.erp.net/tech/modules/crm/sales/sales-concepts/amount-to-pay.html).

## Calculating goods cost

Likewise, additional amounts may be used to add value to the goods cost in the [logistics](https://docs.erp.net/tech/modules/logistics/index.html).

For example, if transport is entered as an additional amount, when goods are purchased, the transport value will be **added** to the purchase price. When a stock transfer from one store to another is executed and it includes transport cost added to the issued products, the value of this transport should be **added** to the products cost **before** they are received in the second store. Adding transport to the purchase price or the store cost is done in the receiving store orders or store transactions. Then, when a row in the sub-document is created, the value of this row is **increased** by the distribution in the current row amount of the transport.

The same procedure is applied to **all** additional amounts marked as part of the store cost calculation. 

This is the *Add To Line* field in the definition of the additional amount.

### Calculating outside activities

Additional amounts may also be used to report external activities for the enterprise company.

For example, if a salesman in a company receives commissions or other additions to their salaries equal to a percent of the turnover they achieve, then the commision may be entered as an additional amount in the Sales Order, which is a percent of the [amount to pay](https://docs.erp.net/tech/modules/crm/sales/sales-concepts/amount-to-pay.html).

