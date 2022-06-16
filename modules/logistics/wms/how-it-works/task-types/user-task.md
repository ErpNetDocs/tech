# User task - task type

A user task is a task (work) that needs to be done by a human actor (the worker). 

When the process arrives at such task, the process execution stops and the application displays a text that guides the user of what needs to be done for this task. 
The text to be displayed must be indicated in advance in the Notes field of the particular Warehouse Order Line.

Once the user (worker) has completed the execution of this task, he has to manually confirm that the job is completed.

When the task is confirmed as completed, the process continues to the next task that needs to be done (if any).

## Result
When executed, the warehouse order lines with a 'User task' task type create a Document Fulfillment as follows:

DocumentFulfillment.Document = WarehouseOrder
DocumentFulfillment.DocumentLineId = WarehouseOrderLineId
DocumentFulfillment.LineNo = WarehouseOrderLine.LineNo
DocumentFulfillment.FulfillmentType = Completed
DocumentFulfillment.IsFinal = false
DocumentFulfillment.LineType = Line
DocumentFulfillment.QuantityBase = 0.00
DocumentFulfillment.StandardQuantity = 0.00
DocumentFulfillment.Product = null
DocumentFulfillment.Lot = null
DocumentFulfillment.SerialNumber = null
DocumentFulfillment.ProductVariant = null
DocumentFulfillment.DestinationEntityName = ???
