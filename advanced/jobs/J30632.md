---
uid: jobs-J30632
---

# J30632 Notifications - Deletе Old Notifications

| Code                  | J30632                                                       |
| :-------------------- | ------------------------------------------------------------ |
| Entity                | Notifications                                                |
| Job Type Name         | Deletе Old Notifications                                     |
| Parameters            | -                                                            |
| Description           | The system job deletes all old Notifications, whose CreationTimeUtc is older than 32 days:(CreationTimeUtc - Now()) > 32 days |
| First to Process      | Notification.CreationTimeUtc (ASC)                           |
| Records per Iteration | 10 000                                                       |
| Version               | Introduced: 2020.1                                           |

**For more information about the Jobs Documentation Template and a short explanation of each column, see topic** [Jobs Template](~/templates/template-description-jobs.md).
