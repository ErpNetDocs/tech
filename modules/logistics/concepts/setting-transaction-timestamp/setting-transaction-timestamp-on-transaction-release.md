# Setting transaction timestamp on transaction release

On first release of the document, the <i>transaction timestamp</i> is set automatically in each transaction row that has no value. If the transaction has inherited some specific dates and times from the store orders or the user has entered them manually, these values will remain unchanged and the new dates and times will be set only in the rows with no values for <i>transaction timestamp</i>.

When releasing the transaction, the values in the rows with no <i>transaction timestamps</i> are set according the following business rules:

- If the transaction's Document Date is today's date or a future date, the <i>transaction timestamp</i> for all rows is the current date and time.

- If the transaction's Document Date is in the past, then the transaction timestamp is XX.XX.XXXX 23:59:00, where XX.XX.XXXX is the Document Date.

When a transaction is released with a past date, the time is set to 23:59:00 because it is unknown when exactly the transaction happened. It is assumed that it happened after all the other transactions which were released in time. In other words, late transactions are listed at the end of the selected date. If they are too late or cannot be ordered correctly among the other transactions from the same day, then the user may change the time manually - by **[adjustment documents](https://docs.erp.net/tech/concepts/documents/adjustments.html?q=Adjustment%20Documents)**. 

The time "23:00:00" follows the same principles because it helps the user manage late transactions from a given date more easily. For example, if it is necessary for a transaction to come after another one, the user should adjust it in the remaining minute of the current day. If the selected time was "23:59:59:999", that would not be possible.


