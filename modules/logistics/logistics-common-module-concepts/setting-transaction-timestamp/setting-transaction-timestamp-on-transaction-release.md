# Setting Transaction Timestamp On Transaction Release

On first release of the document, the <i>Transaction Timestamp</i> is set automatically in each Transaction row that has no value. If the Transaction has inherited some specific dates and times from the Store Orders or the user has entered them manually, these values will remain unchanged and the new dates and times will be set only in the rows with no values for <i>Transaction Timestamp</i>.

When releasing the Transaction, the values in the rows with no <i>Transaction Timestamps</i> are set according the following business rules:

- If the Transaction's Document Date is today's date or a future date, the <i>Transaction Timestamp</i> for all rows is the current date and time.

- If the Transaction's Document Date is in the past, then the Transaction Timestamp is XX.XX.XXXX 23:59:00, where XX.XX.XXXX is the Document Date.

When a Transaction is released with a past date, the time is set to 23:59:00 because it is unknown when exactly the transaction happened. It is assumed that it happened after all the other transactions which were released in time. In other words, late transactions are listed at the end of the selected date. If they are too late or cannot be ordered correctly among the other transactions from the same day, then the user may change the time manually - by <b>Adjustment Documents</b>. 

The time "23:00:00" follows the same principles because it helps the user manage late transactions from a given date more easily. For example, if it is necessary for a transaction to come after another one, the user should adjust it in the remaining minute of the current day. If the selected time was "23:59:59:999", that would not be possible.


