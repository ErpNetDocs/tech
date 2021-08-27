# More Specific Cases of Setting the Transaction Timestamp

When generating Cost Transactions from Receiving Orders, there is a specific way of getting the <i>Transaction Timestamps</i>. It is wrong because of the irregular generation procedure: direct Transaction creation from another module is not supposed to happen, as the other modules are not supposed to work with internal module operations.

In this transaction generation, only the cost is filled in (all quantities are 0). It is the cost coming from the Purchase Invoices, for the quantities which are already entered in the store by the Receiving Order. To have correct time and date for the cost, the generated Transaction should have a specific <b>Transaction Timestamp</b> equal to the <b>Transaction Timestamp</b> with which the quantities enter the store. If the cost is entered later, the products will turn out with zero cost.

For examples and more detailed information about goods cost when purchasing, see <b>Setting Cost When Purchasing Goods</b>.


