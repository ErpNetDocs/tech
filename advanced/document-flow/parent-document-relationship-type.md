# Parent document relationship type

When a document has a parent document, there are constraints, which determine which states are allowed. The applicable states depend on the relation between the parent document and the child document.

The relationship is contained in the parent document relationship type attribute. Its possible values are:

- **Sub-task** - the child document is a sub-task that must be completed to complete the parent document
- **Next task** - the child document is not related to the next task and the parent document can be completed without waiting for the child document to be completed.

For example, the *sales order-store order* relationship is usually of **Sub** task type because the store order must be completed before the sales order can.

In contrast, the *offer-sales order* relationship is usually of **Next** task type because the work on the offer can be completed once the sales order is created. There is no need to complete the sales order first.

The allowed child document states depends on the relationship type and the parent document state. 

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

