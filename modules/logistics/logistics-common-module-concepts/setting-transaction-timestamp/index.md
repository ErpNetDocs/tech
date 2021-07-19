# Setting Transaction Timestamp

The current article describes the principles for defining a <i>Transaction Timestamp</i> in the Transactions rows. A timestamp is essential for goods cost definition. It represents the exact moment when a specific transaction starts affecting the goods cost. For more information, see <b>Goods Cost</b> and its sub-articles.

Usually, transaction timestamps are set automatically with no need for user intervention. This is executed in two general ways:

 1. On Transaction release, if there is no transaction timestamp, then it is set automatically by the date of the Transaction and/or by the current date and time.

 2. When the automatic set of the timestamp in the Transaction release does not set the correct date and time in accordance with to the business process, a transaction timestamp is defined in the Store Orders (or another document generating Transactions, such as Reconciliations). Thus, another module which controls and executes the orders is available to set a specific <i>Transaction Timestamp</i> defined by its business logic.

Users can change the <i>Transaction Timestamp</i> in one of two ways:

 1. By editing the Store Orders (their <i>Transaction Timestamps</i> will be copied to the executing Transactions). 
 
 2. By editing the Transactions directly (before their release or afterwards by <b>Adjustment Documents</b>).

No matter how the timestamp is set, it has to comply with the following restrictions: 

if the quantity in the Transaction row is different from 0, then the Document Date should match the date of the <b>Transaction Timestamp</b>.

More detailed description of the logic behind the automatic set of the <i>Transaction Timestamp</i> may be found in the following articles:

- <b>More Specific Cases Of Setting The Transaction Timestamp</b>

- <b>Setting Transaction Timestamp by Store Orders</b>

- <b>Setting Transaction Timestamp In Reconciliations</b>

- <b>Setting Transaction Timestamp On Transaction Release</b>
