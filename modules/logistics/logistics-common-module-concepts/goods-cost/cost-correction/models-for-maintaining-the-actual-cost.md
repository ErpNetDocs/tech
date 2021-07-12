# Models For Maintaining The Actual Cost

There are two main models to keep the goods cost up-to-date.

1.	Right from the start, when we enter (and release) the Transactions, the actual cost is re-calculated. The costs of all existing store transactions affected by the current Transaction are also calculated. This leads to a perfect situation where all transactions are correctly calculated no matter when they are entered in the system. In addition, the calculation is performed by the system and the user does not have to control it. The disadvantage of this model is the additional calculations for creating and releasing a Transaction, especially when that Transaction is old. This may lead to slow performance of the Logistics module.

2.	The corrections are created periodically by a user instead of immediately for each Transaction. This model provides the easier daily creation of a Transaction with a risk for incorrect costs not covered by <b>Cost Correction</b> (this happens only when store transactions are entered in a non-chronological manner).

## Dynamic Cost Correction

Maintaining the actual cost at all times with the first model is accomplished by using two specific procedures for generating <b>Cost Correction</b> from every Transaction. They have to be created when the Transaction is <b>released</b> and the generation of the <b>Cost Correction</b> updating the cost of the current Transaction is performed first.

Thus, when the Transaction is released, it will have its original cost, and the first generation will correct its values if necessary. We assume that the cost of all existing released Transactions before the creation of the current Transaction are correct (as the cost of the current Transaction may be affected by them). Once the first generation corrects the cost of the newly entered Transaction, the second generation corrects the cost of all other transactions that depend on the current Transaction. Thus, after its release, the cost of all Transactions in the system will be actual no matter the date they are entered. The older the transaction, the slower the performance of the two generation procedures will be (this means that more Transactions will be affected by the current transaction).

## Periodical Cost Correction

The second model for <b>Cost Correction</b> does not use automatic generation procedures for the Cost Corrections. Instead, the user manually enters documents for a specified period (month, quarter, etc.) and starts the <b>Basic Algorithm For Cost Correction Calculation</b> for all Transactions in the specified period.

For example, if Cost Corrections are performed monthly, the user creates a new <b>Cost Correction</b> document and sets the period from the first date to the last date of the month. Then, he starts the function "<b>Recalculate the corrections for the period</b>", which loads all store transactions where <i>Transaction Timestamp</i> is in the specified period. The function then adds the opening balances at the beginning of the period, and this data is executed by the <b>Basic Algorithm For Cost Correction Calculation</b>. So, the actions of the user are limited to entering the start and end dates, starting the function and releasing the document. This is performed for <b>past periods</b> (i.e. not for the current month) for which there will be no more new Transactions, and in which the Cost Corrections are already calculated and released. Otherwise, there may be incorrect cost in the current-period transactions.

The re-calculation of the cost of all transactions in a specified period may take more time than if the first model is used, but it eases the daily Transactions release significantly. Also, for Periodical <b>Cost Correction</b>, a more appropriate execution time may be picked (for example, during the night).

