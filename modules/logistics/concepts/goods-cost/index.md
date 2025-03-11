# Goods Cost

Currently, the goods cost in @@name is calculated by the transactions documents. 

For each transaction the cost is defined either automatically when the document is released or by the parent document. This is determined by the <b>Cost Source</b> field. It has two possible values:

- ‘Store’ - this value sets out that the cost in the transaction is defined when releasing the document by the accumulated cost in the store. This is used when issuing transactions are executed.

- ‘Document’ - the cost is defined by the data in the transaction rows (<b>Unit Cost</b> and <b>Line Cost</b> fields). This data is usually inherited by the parent document and used when receipt operations are executed (the only exception is when the receipt operation comes from ‘Reconciliation’ - then, the value in <b>Cost Source</b> is ‘Store’).

‘Store orders’ enable other modules to set goods cost. They contain not only the quantity but in specific cases, what the goods cost should be. This cost is copied to the transactions. The <b>Cost Source</b> is set to <b>Document</b> in the transactions executing the specific Store Order. This is how they participate in the cost definition.

For each store transaction (i.e. transaction document) changing the cost, a specific Timestamp is saved. It indicates the time the operation starts influencing the cost. The field in the transaction rows is called <i>transaction timestamp</i>. Generally, the transactions should be entered in the system in the right chronology. Usually, the <b>transaction timestamp</b> is set either by the ‘transaction release’, or by the ‘store orders’ as follows:

- in the parent store order, a specific <i>transaction timestamp</i> is set. This value is inherited by the transaction that executes the ‘store order’';

- if the parent store order has no <i>transaction timestamp</i> and the transaction has today's date or future date, then the <i>transaction timestamp</i> is set to current date and time;

- if the parent store order has no <i>transaction timestamp </i> and the transaction has past date, then the <i>transaction timestamp</i> is set to XX.XX.XXX 23:59:00, where XX.XX.XXXX is the document's date.

If necessary, the <i>transaction timestamp</i> may be set manually by the user, although there are certain limitations. For example, if the quantity in the row is 0, the date in  Document Date should be no different than the one in <i>transaction timestamp</i>. 

For more information, see the [Setting transaction timestamp](https://docs.erp.net/tech/modules/logistics/concepts/setting-transaction-timestamp/index.html) article.

## Cost types

When the transactions are not entered in the system on time and damage the right chronology, this may generate incorrect costs. To fix this, @@name has developed a [Cost correction]() system, recalculating the cost as if it was entered in the right chronological order. 

There are two types of goods costs:

- Original cost - defined right when entring the document. Depends on the entry order.

- Cost adjustment – for the definition of this cost, a special recalculation is used. It compensates the wrong chronology of the transactions.

## Cost currency

In the transactions, the cost comes in four currencies: <b>base cost, product cost, store cost, and document cost</b>. For each row, the cost is calculated independently. 

- The base currency comes from the Enterprise Company definition of the current transaction. 

- Product currency is part of the product definition and if there is no currency, then the base cost is used. 

- Store currency is in the store definition; if there is no currency - the base currency is used.

- The document currency is set in the <b>Document Currency</b> field. 

For each store transaction, the cost is calculated in all four currencies when defined automatically.

## Costing methods
@@name supports multiple costing methods to accommodate diverse business needs. For more information, see the [Costing methods](costing-methods.md) topic.


<br/>For more specific information about cost calculations see the following articles:
- **[Cost correction](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/cost-correction/index.html?q=Cost%20correction)** 

- **[Original cost calculation](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/index.html?q=Original%20cost%20calculation)** 

