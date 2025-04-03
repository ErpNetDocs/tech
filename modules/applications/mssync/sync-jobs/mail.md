---
erp.type: syncjob
erp.topic: mssync
---

# Mail

The Mail Sync Job enables the synchronization of emails between Microsoft 365 and your @@name instance. This ensures that emails sent or received in Microsoft 365 are automatically reflected in @@name, keeping your communication records aligned across both platforms.

## System requirements

1. **MSSync service user must be an admin**

Because the service user must obtain mail messages from all users using MSSync, it should have administrative privileges.

## Per user requirements

1. **Default local mailbox in @@name**

Each user must have a local mailbox marked as the default.

2. **Default local mailbox email**

The default local mailbox must have an email address that matches the principal name (i.e., the user's email address).

3. **No mailbox encryption**

The default local mailbox must not use encryption.
Synchronizing with a mailbox that has encryption enabled in @@name is not supported.

## Initial sync (first-time synchronization)

1. Only remote messages (from Microsoft 365) older than 7 days and up to the present will be synchronized.

2. Only local messages (from @@name) older than 7 days and up to the present will be synchronized.

## Considerations and specific scenarios

- @@name mailbox encryption is not supported.
- Message attachments are currently not fully supported. When present, they are represented properly as attachments, but their content is specified as a URI.

## Resources

- https://docs.erp.net/model/entities/Applications.Mail.Boxes.html
- https://docs.erp.net/model/entities/Applications.Mail.BoxFolders.html
- https://docs.erp.net/model/entities/Applications.Mail.Messages.html
- https://learn.microsoft.com/en-us/graph/api/resources/message?view=graph-rest-1.0