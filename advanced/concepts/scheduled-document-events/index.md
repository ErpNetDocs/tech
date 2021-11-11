# Scheduled document events

Scheduled document events are postponed events which will be executed **later**.
 
They typically appear in the form of numerous recalculations resulting from other events. 

For example, releasing a cost correction creates scheduled events for all affected documents. 
 
A scheduled document event needs to be executed **before** it's applied. If it's created by a cost correction, the execution causes a resetting of the document state of the store transactions, which was included in the cost correction. The reset triggers the accounting voucher generation procedures and causes re-accounting of documents, including the adjusted cost.
 
An execution can be performed:

- **manually** through the ''Execute Scheduled Events'' navigator 

- **automatically**, using the job **[J30724 - Run scheduled events](https://docs.erp.net/tech/advanced/jobs/J30724.html)**.

