# Setting transaction timestamp

The current article describes the principles for defining a <i>transaction timestamp</i> in the transactions rows. A timestamp is essential for goods cost definition. It represents the exact moment when a specific transaction starts affecting the goods cost. For more information, see [Goods cost](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/index.html?q=Goods%20cost) and its sub-articles.

Usually, transaction timestamps are set automatically with no need for user intervention. This is executed in two general ways:

 1. On transaction release, if there is no transaction timestamp, then it is set automatically by the date of the transaction and/or by the current date and time.

 2. When the automatic set of the timestamp in the transaction release does not set the correct date and time in accordance with to the business process, a transaction timestamp is defined in the store orders (or another document generating transactions, such as Reconciliations). Thus, another module which controls and executes the orders is available to set a specific <i>transaction timestamp</i> defined by its business logic.

Users can change the <i>transaction timestamp</i> in one of two ways:

 1. By editing the store orders (their <i>transaction timestamps</i> will be copied to the executing transactions). 
 
 2. By editing the transactions directly (before their release or afterwards by [adjustment documents](https://docs.erp.net/tech/concepts/documents/adjustments.html?q=adjustment%20documents)).

No matter how the timestamp is set, it has to comply with the following restrictions: 

if the quantity in the transaction row is different from 0, then the Document Date should match the date of the <b>transaction timestamp</b>.

More detailed description of the logic behind the automatic set of the <i>transaction timestamp</i> may be found in the following articles:

- **[More specific cases of setting the transaction timestamp](https://docs.erp.net/tech/modules/logistics/concepts/setting-transaction-timestamp/more-specific-cases-of-setting-the-transaction-timestamp.html?q=More%20Specific%20Cases%20Of%20Setting%20The%20Transaction%20Timestamp)**

- **[Setting transaction timestamp by store orders](https://docs.erp.net/tech/modules/logistics/concepts/setting-transaction-timestamp/setting-transaction-timestamp-by-store-orders.html?q=Setting%20Transaction%20Timestamp%20by%20Store%20Orders)**

- **[Setting transaction timestamp in reconciliations](https://docs.erp.net/tech/modules/logistics/concepts/setting-transaction-timestamp/setting-transaction-timestamp-in-reconciliations.html?q=Setting%20Transaction%20Timestamp%20In%20Reconciliations)**

- **[Setting transaction timestamp on transaction release](https://docs.erp.net/tech/modules/logistics/concepts/setting-transaction-timestamp/setting-transaction-timestamp-on-transaction-release.html?q=Setting%20Transaction%20Timestamp%20On%20Transaction%20Release)**
