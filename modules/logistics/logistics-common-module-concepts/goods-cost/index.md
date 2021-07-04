# Goods Cost

Currently, the goods cost in @@name is calculated by the Transactions documents. 

For each Transaction the cost is defined either automatically when the document is released or by the parent document. This is determined by the <b>Cost Source</b> field. It has two possible values:

- ‘Store’ - this value sets out that the cost in the Transaction is defined when releasing the document by the accumulated cost in the store. This is used when issuing transactions are executed.

- ‘Document’ - the cost is defined by the data in the Transaction rows (<b>Unit Cost</b> and <b>Line Cost</b> fields). This data is usually inherited by the parent document and used when receipt operations are executed (the only exception is when the receipt operation comes from ‘Reconciliation’ - then, the value in <b>Cost Source</b> is ‘Store’).

‘Store Orders’ enable other modules to set goods cost. They contain not only the quantity but in specific cases, what the goods cost should be. This cost is copied to the Transactions. The <b>Cost Source</b> is set to <b>Document</b> in the Transactions executing the specific Store Order. This is how they participate in the cost definition.

For each store transaction (i.e. Transaction document) changing the cost, a specific Timestamp is saved. It indicates the time the operation starts influencing the cost. The field in the Transaction rows is called <b>Transaction Timestamp</b>. Generally, the transactions should be entered in the system in the right chronology. Usually, the <b>Transaction Timestamp</b> is set either by the ‘Transaction release’, or by the ‘Store Orders’ as follows:

- in the parent Store Order, a specific <b>Transaction Timestamp</b> is set. This value is inherited by the Transaction that executes the ‘Store Order’';

- if the parent Store Order has no <b>Transaction Timestamp</b> and the Transaction has today's date or future date, then the <b>Transaction Timestamp</b> is set to current date and time;

- if the parent Store Order has no <b>Transaction Timestamp </b> and the Transaction has past date, then the <b>Transaction Timestamp</b> is set to XX.XX.XXX 23:59:00, where XX.XX.XXXX is the document's date.

If necessary, the <b>Transaction Timestamp</b> may be set manually by the user, although there are certain limitations. For example, if the quantity in the row is 0, the date in  Document Date should be no different than the one in <b>Transaction Timestamp</b>. 

For more information, see the <b>Setting Transaction Timestamp</b> article.

## Cost types

When the Transactions are not entered in the system on time and damage the right chronology, this may generate incorrect costs. To fix this, @@name has developed a <b>Cost Correction</b> system, recalculating the cost as if it was entered in the right chronological order. 

There are two types of goods costs:

- Original Cost - defined right when entring the document. Depends on the entry order.

- Cost Adjustment – for the definition of this cost, a special recalculation is used. It compensates the wrong chronology of the transactions.

## Cost Currency

In the Transactions, the cost comes in four currencies: <b>base cost, product cost, store cost, and document cost</b>. For each row, the cost is calculated independently. 

- The base currency comes from the Enterprise Company definition of the current Transaction. 

- Product currency is part of the product definition and if there is no currency, then the base cost is used. 

- Store currency is in the store definition; if there is no currency - the base currency is used.

- The document currency is set in the <b>Document Currency</b> field. 

For each store transaction, the cost is calculated in all four currencies when defined automatically.

For more specific information about cost calculations see the following:

- <b>Cost Correction</b>

- <b>Original Cost Calculation</b>

