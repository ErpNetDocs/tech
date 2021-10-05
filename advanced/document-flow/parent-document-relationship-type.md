# Parent document relationship type

When a document has a parent document, there are constraints, which determine which states are allowed. The applicable states depend on the relation between the parent document and the child document.

The relationship is contained in the Parent document relationship type attribute. Its possible values are:

- **Sub-Task** - the child document is a sub-task that must be completed to complete the parent document
- **Next Task** - the child document is not related to the next task and the parent document can be completed without waiting for the child document to be completed.

For example, the *Sales Order to Store Order* relationship is usually of Sub task type because to complete the sales order, the store order must be completed first.

In contrast, the *Offer to Sales Order* relationship is usually of Next task type because the work on the offer can be completed once the sales order is created. There is no need to complete the sales order first.

The allowed child document states depends on the relationship type and the parent document state. 

The following table summarizes the allowed states:

| Relationship Type | Parent State | Allowed Child States                                    |
| :---------------- | :----------- | :------------------------------------------------------ |
| Sub-Task          | New          | New                                                     |
| Sub-Task          | Planned      | New, Planned                                            |
| Sub-Task          | Firm Planned | New, Planned, Firm Planned                              |
| Sub-Task          | Released     | New, Planned, Firm Planned, Released, Completed, Closed |
| Sub-Task          | Completed    | Completed, Closed                                       |
| Sub-Task          | Closed       | Closed                                                  |
| Next Task         | New          | New                                                     |
| Next Task         | Planned      | New, Planned                                            |
| Next Task         | Firm Planned | New, Planned, Firm Planned                              |
| Next Task         | Released     | New, Planned, Firm Planned, Released, Completed, Closed |
| Next Task         | Completed    | New, Planned, Firm Planned, Released, Completed, Closed |
| Next Task         | Closed       | New, Planned, Firm Planned, Released, Completed, Closed |

