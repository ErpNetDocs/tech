# Setting Transaction Timestamp In Reconciliations

In Reconciliations, <i>Transaction Timestamps</i> which are about to be generated in the Store Transactions rows are calculated the same way as on Release. In the Reconciliation document form, when the current availability of the products is calculated and stored in the rows, <i>Transaction Timestamps</i> are filled in as follows:

- If the Reconciliation has a present or future Document Date, then the <i>Transaction Timestamp</i> in the row has the current date and time.

- if the Reconciliation has a past Document Date, then the <i>Transaction Timestamp</i> is XX.XX.XXXX 23:59:00, where XX.XX.XXXX is the document date.

The same principle is used for Reconciliation release, in case there are rows with empty <i>Transaction Timestamps</i>.

When the Reconciliation creates Transactions for discrepancies, the dates and times already set in the Reconciliation are copied to the newly created Store Transactions. Thus, the <i>Transaction Timestamps</i> in the Transactions are defined by the current creation time or Reconciliation release and not by the current release time (of the Store Transaction).


