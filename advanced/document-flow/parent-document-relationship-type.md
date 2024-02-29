# Parent document relationship type

When a document has a parent document, there are constraints that determine which states are allowed. <br> The applicable states depend on the relationship between a parent document and a child document.

The relationship is contained in the 'parent-document relationship type' attribute. Its possible values are:

- **Sub-task** - the child document is a sub-task that must be done to complete the parent document
- **Next task** - the child document is NOT related to the next task and the parent document can be completed **without** requiring the child document to be completed.
- **Independent task** - the child document is an independent task, and there are no restrictions regarding the states of the parent and the child document.

For example, **the sales order-store order** relationship tends to be of 'sub-task' type since the store order must be completed before the sales order. The **offer-sales order** relationship is of 'next task' type, as the work on the offer can be completed once the sales order is created. 
There's no need to complete the sales order first.

The allowed child document states depend on the relationship type and the parent document state. 

The following table summarizes the allowed states:

| Relationship type | Parent state | Allowed child states                                    |
| :---------------- | :----------- | :------------------------------------------------------ |
| Sub-task          | New          | New                                                     |
| Sub-task          | Planned      | New, Planned                                            |
| Sub-task          | Firm Planned | New, Planned, Firm Planned                              |
| Sub-task          | Released     | New, Planned, Firm Planned, Released, Completed, Closed |
| Sub-task          | Completed    | Completed, Closed                                       |
| Sub-task          | Closed       | Closed                                                  |
| Next task         | New          | New                                                     |
| Next task         | Planned      | New, Planned                                            |
| Next task         | Firm Planned | New, Planned, Firm Planned                              |
| Next task         | Released     | New, Planned, Firm Planned, Released, Completed, Closed |
| Next task         | Completed    | New, Planned, Firm Planned, Released, Completed, Closed |
| Next task         | Closed       | New, Planned, Firm Planned, Released, Completed, Closed |
| Independent task  | Each possible state | Each possible state                              |


