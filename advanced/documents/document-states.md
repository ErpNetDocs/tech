# Document States

## Description

The documents in the system have a current STATE. This state determines the effect on the system and whether the document can be updated. The allowed states of the document are:

- **New** - the document is entered and saved in the system but does not affect (on planning, availability, etc.)
- **Planned** - the document is planned automatically by the system to occur at some point in the future
- **Firm Planned** - the document is planned to occur at some point in the future by a user. Firm Planned status is automatically set by the system if a user edits a Planned document.
- **Released** - the document is released for execution. The responsible party starts to execute it.
- **Completed** - the activities of the document are finished. Sometimes this state is also referred to as "Finished".
- **Closed** - the document is verified and no more changes are expected in it.

## Document Editing Rules

Whether a document can be edited by a user depends on its state:

- **New** - the document can be edited freely.
- **Planned** - the document can be edited, but if you save the changes, the state will automatically change to Firm Planned (see below).
- **Firm Planned** - the document can be edited.
- **Released** - the document can no longer be edited, but an Adjustment Document can be created and applied (see heading below).
- **Completed** - the document cannot be changed, but its state can be returned to Released.
- **Closed** - the document cannot be changed, but its state can be returned to Completed.

Planned documents reflect a plan, created automatically by the system. On the next planning run, planned documents are usually erased or voided (actually the system tries to erase them, but if they use sequence generators, they can only be voided, not erased). The Firm Planned state helps avoid the voiding. When a user makes changes to Planned document, the system changes the state automatically to Firm Planned in order to protect the user changes before the next planning run.

> [!Note]
> Planned sub-documents are also erased or voided when a parent document state changes. This behavior is system defined and cannot be changed. Planned documents can only be protected from voiding by making them Firm Planned.

## Rules for Changing Document State

Changing the document state usually goes straight, from New to Closed. However, sometimes it might be needed to revert back to the previous state. The following table shows when this is allowed:

| Old State    | New State    | Allowed     |
| :----------- | :----------- | :---------- |
| Planned      | New          | Allowed     |
| Firm Planned | Planned      | Allowed     |
| Released     | Firm Planned | Not Allowed |
| Completed    | Released     | Allowed     |
| Closed       | Completed    | Allowed     |

There is a borderline at the Released state - once reached, the state cannot be reverted. The document can only be voided.

## Parent Document Relationship Type

When a document has a Parent Document, there are constraints, which determine which states are allowed. The applicable states depend on the relation between the parent document and the child document.

The relationship is contained in the Parent Document Relationship Type attribute. Its possible values are:

- **Sub-Task** - the child document is a sub-task that must be completed to complete the parent document
- **Next Task** - the child document is not related to the next task and the parent document can be completed without waiting for the child document to be completed.

For example, the *Sales Order* to *Store Order* relationship is usually of Sub-Task type, because to complete the *Sales Order*, the *Store Order* must be completed first.

In contrast, the *Offer* to *Sales Order* relationship is usually of the Next Task type because the work on the Offer can be completed once the Sales Order is created. There is no need to complete the *Sales Order* first, to complete the *Offer.*.

The allowed child document states depends on the relationship type and the parent document state. The following table summarizes the allowed states:

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

## Adjustment Documents

[Adjustment Documents](adjustment-documents.md) are documents, which adjust other documents. Adjustments can be made only on documents, which are in the Released or Completed states.

Adjustment documents can change only primary measurement values. They are usually used to increase or decrease quantities and/or amounts of released documents. Adjustment Documents are separate documents, but when applied to a main document, they change its internal values. If an adjusted document is opened on the screen, it will look like it always has been adjusted. The previous versions of the document are securely stored and can be revealed by the document history.

The adjustment documents come in effect (e.g. change the main document) when their state is changed to the special "Adjustment state". As these documents are only used to adjust other documents, they cannot have parent and/or child documents.

## Planning Only

Some documents are created specifically only for planning purposes. They are not intended to be ever released. There is a special flag, which signals this intention to the system, called "Planning Only". When this flag is set, the system would allow only New and Planned states for the document. No upper states would be allowed by the system. Usually, the document is later voided by its creator (when the plan changes or actual execution is about to begin).

## User-Defined Document Statuses

Each Document Type can contain user-defined sub-statuses to the system states.

For example, one can define the following user statuses for a document type, called "Direct Production Order":

| Document Type(user defined) | Document State(system defined) | User Status(user defined) | Exit Status(Yes/No) |
| :-------------------------- | :----------------------------- | :------------------------ | :------------------ |
| Document Type(user defined) | Document State(system defined) | User Status(user defined) | Exit Status(Yes/No) |
| Direct Production Order     | New                            |                           |                     |
| Direct Production Order     | Planned                        |                           |                     |
| Direct Production Order     | Firm Planned                   | For Processing            |                     |
| Direct Production Order     | Firm Planned                   | Needs Check               |                     |
| Direct Production Order     | Firm Planned                   | Needs Approval            |                     |
| Direct Production Order     | Firm Planned                   | Approved                  | Yes                 |
| Direct Production Order     | Released                       | Started                   |                     |
| Direct Production Order     | Released                       | Tested                    | Yes                 |
| Direct Production Order     | Completed                      |                           |                     |
| Direct Production Order     | Closed                         |                           |                     |

Each system state can have as many user statuses, as needed. As shown in the table above, one of the user statuses within each system state can be defined as Exit Status. The Exit Status is required to be reached to move to the next system state.

In the example above, in order to release a Direct Production Order, the Firm Planned/Approved state must first be set. This creates a control point for moving ahead of the state.

> [!Note]
> The exit User Status-es are usually secured, so that only the authorized users can set them.
