# Setting transaction timestamp in reconciliations

In Reconciliations, <i>transaction timestamps</i> which are about to be generated in the store transactions rows are calculated the same way as on Release. In the Reconciliation document form, when the current availability of the products is calculated and stored in the rows, <i>transaction timestamps</i> are filled in as follows:

- If the Reconciliation has a present or future Document Date, then the <i>transaction timestamp</i> in the row has the current date and time.

- if the Reconciliation has a past Document Date, then the <i>transaction timestamp</i> is XX.XX.XXXX 23:59:00, where XX.XX.XXXX is the document date.

The same principle is used for Reconciliation release, in case there are rows with empty <i>transaction timestamps</i>.

When the Reconciliation creates transactions for discrepancies, the dates and times already set in the Reconciliation are copied to the newly created store transactions. Thus, the <i>transaction timestamps</i> in the transactions are defined by the current creation time or Reconciliation release and not by the current release time (of the store transaction).


