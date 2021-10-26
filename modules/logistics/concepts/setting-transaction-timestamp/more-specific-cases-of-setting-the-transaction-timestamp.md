# More specific cases of setting the transaction timestamp

When generating cost transactions from receiving orders, there is a specific way of getting the <i>transaction timestamps</i>. It is wrong because of the irregular generation procedure: direct transaction creation from another module is not supposed to happen, as the other modules are not supposed to work with internal module operations.

In this transaction generation, only the cost is filled in (all quantities are 0). It is the cost coming from the purchase invoices, for the quantities which are already entered in the store by the receiving order. To have correct time and date for the cost, the generated transaction should have a specific <b>transaction timestamp</b> equal to the <b>transaction timestamp</b> with which the quantities enter the store. If the cost is entered later, the products will turn out with zero cost.

For examples and more detailed information about goods cost when purchasing, see <b>[Setting cost when purchasing goods](https://docs.erp.net/tech/modules/logistics/procurement/setting-cost-when-purchasing-goods.html?q=Setting%20cost%20when%20purchasing%20goods)</b>.


