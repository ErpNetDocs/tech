# Scheduled document events

Scheduled document events are postponed events which will be executed **later**.
 
They typically appear in the form of numerous recalculations resulting from other events. 

For example, releasing a cost correction creates scheduled events for all affected documents. 
 
A scheduled document event needs to be executed **before** it's applied. If it's created by a cost correction, the execution causes a reset of the **[document state](https://docs.erp.net/tech/concepts/documents/states.html)** of the store transactions, included in the cost correction. A reset triggers the accounting voucher generation procedures and causes re-accounting of documents, including adjusted cost.
 
An execution can be performed:

- **manually** through the ''Execute Scheduled Events'' navigator 

- **automatically**, using the job **[J30724 - Run scheduled events](https://docs.erp.net/tech/advanced/jobs/J30724.html)**.

