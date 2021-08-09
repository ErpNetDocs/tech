# Scheduled Document Events
Scheduled Document Events are postponed events, which will be executed later.
 
Usually, these are numerous recalculation events, resulting from other events. For example, releasing a cost correction creates scheduled events for all affected documents. 
 
The Scheduled Document Events have to be executed to be applied. In the case of a scheduled event created by a cost correction, the execution causes a resetting of the document state of the store transactions which was included in the cost correction. The resetting triggers the Accounting Voucher generation procedures and causes the re-accounting of documents, including the adjusted cost.
 
The execution can be performed manually through the "Execute Scheduled Evens" navigator or automatically using the job [J30724 - Run scheduled event](https://github.com/ErpNetDocs/tech/blob/410296041dd31e2572dff39474157c429c83c8b8/advanced/jobs/J30724.md).

