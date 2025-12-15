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


2. **Each user has a default enterprise company and location**

This is required when creating new activities in @@name. Since an activity is essentially a document, each document requires the [EnterpriseCompany](https://docs.erp.net/model/entities/General.Activities.Activities.html#enterprisecompany) and [EnterpriseCompanyLocation](https://docs.erp.net/model/entities/General.Activities.Activities.html#enterprisecompanylocation) properties to be filled.

3. **Each user must enable their own synchronization**

Each user is responsible for enabling their own synchronization settings.  

> **Important:** Synchronization is only executed for activities created by users who have synchronization enabled.

For example:  
- User1 creates an activity and includes User2 as a participant.
- The activity will appear in Outlook **only if User1** (the creator) has synchronization enabled.
- If **User2** has synchronization enabled but **User1** does not, the activity will **not** appear in Outlook.
- The same rule applies in reverse: when User2 creates an activity, it will only synchronize if **User2** has synchronization enabled.


## Considerations and specific scenarios

- Only remote events from Microsoft 365 that fall within a rolling one-month window will be synchronized.
MSSync retrieves Microsoft 365 events starting from the synchronization date and up to one month ahead, and creates corresponding @@name activities.

Example: *If synchronization starts on January 25, MSSync will synchronize all Microsoft 365 events occurring between January 25 and February 25. An activity with a start date of February 10 will be synchronized, while an activity with a start date of March 1 will not.*
- @@name activities older than 1 day will not be synchronized.
- When an @@name activity is in read-only state (`Released`, `Closed`), all updates triggered from Microsoft 365 will fail. This will result in a synchronization conflict, and the Microsoft 365 activity will be marked accordingly.
- Recurring events are not supported.
- When an event is deleted in Microsoft 365, the corresponding @@name activity will be voided.

## Resources

- https://docs.erp.net/model/entities/General.Activities.Activities.html
- https://learn.microsoft.com/en-us/graph/api/resources/event?view=graph-rest-1.0
