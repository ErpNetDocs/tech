---
erp.type: syncjob
erp.topic: mssync
---

# Calendar

The Calendar Sync Job enables the synchronization of calendar events between Microsoft 365 and your @@name instance. This feature ensures that all calendar events created or updated in Microsoft 365 are automatically reflected in @@name as corresponding activities and vice-versa.

## System requirements

1. **Document Type _Meeting_ for Activity Entity**
   
A document type with the code **_Meeting_** must exist for the [Activity entity](https://docs.erp.net/model/entities/General.Activities.Activities.html) within @@name.
   
If this document type does not exist, the MSSync service user must have permissions to create it. This is required when syncing Microsoft 365 calendar events that result in the creation of new activities in @@name.
   
2. **MSSync service user must be an admin**

When the default activity document type is secured with `CanUpdate` and/or `CanVoid` permissions, the service user must be able to grant these permissions to itself.

## Per user requirements

1. **Valid and enabled mailbox on Microsoft 365 side**
   
The calendar events are managed by the mailbox, so each user must have a valid and enabled mailbox in Microsoft 365. Only users with an active mailbox can have calendar events synchronized.


2. **Each user has default enterprise company and location**

This is required when creating new activities in @@name. Since an activity is essentially a document, each document requires the [EnterpriseCompany](https://docs.erp.net/model/entities/General.Activities.Activities.html#enterprisecompany) and [EnterpriseCompanyLocation](https://docs.erp.net/model/entities/General.Activities.Activities.html#enterprisecompanylocation) properties to be filled.

## Initial sync (first-time synchronization)

1. Only remote events (from Microsoft 365) occurring from today until one month later will be synchronized.

In other words, MSSync will pull all Microsoft 365 events from today until the next month and create corresponding @@name activities.

## Considerations and specific scenarios

- @@name activities older than 1 day will not be synchronized.
- When an @@name activity is in read-only state (`Released`, `Closed`), all updates triggered from Microsoft 365 will fail. This will result in a synchronization conflict, and the Microsoft 365 activity will be marked accordingly.
- Recurring events are not supported.
- When an event is deleted in Microsoft 365, the corresponding @@name activity will be voided.

## Resources

- https://docs.erp.net/model/entities/General.Activities.Activities.html
- https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0