---
uid: brat-NOTIFYUSER
items: ActionTypes
---

# NOTIFYUSER

| Name             | NOTIFYUSER                                                   |
| ---------------- | ------------------------------------------------------------ |
| Description      | Used for creating notifications with a specific text for the object that triggered the business rule. These notifications will later be sent to users indicated in the rule by the **[Notifications](https://docs.erp.net/tech/modules/community/social-interactions/notifications/index.html)** system. <br/><br/> The action creates a record in the **Notifications** table for each user specified in _Parameter1_: <br><br> **UserId** = the Id of the user in Parameter1 <br> **ValueSubject** = Parameter2 <br> **ValueNotificationClass** = Parameter3 <br> **DataObject** = the EDO of the aggregate root of the entity for which the rule has been triggered. <br> if **empty** - set a default value 'BR' + '_ ' + 'UserBusinessRule.Code', e.g. 'BR_0005'<br><br>For more info, see **[Aggregates](https://docs.erp.net/tech/advanced/concepts/aggregates.html)** and **[EDO](https://docs.erp.net/tech/advanced/data-objects/extensible-data-objects.html)**. <br><br> If there aren't explicitly created **[notification settings](https://docs.erp.net/tech/modules/community/social-interactions/notifications/settings.html)** for the class specified in _Parameter3_, the notification will only be sent as an in-app notification.<br/><br/>**IMPORTANT:** NOTIFYUSER is not compatible with all **[events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html)**. <br> For more info, see the **Compatible events chart** section below. |
| Parameter 1      | The user(s) for which a notification will be created. You can set either the **UserId** or the user's **login**. If there's more than one recipient, they can be entered in a comma-separated list which must contain only **UserIds** (Id1,Id2,...IdN) or **logins** (Login1,Login2,...LoginN). |
| Parameter 1 type | Guid, String, List                                           |
| Parameter 2      | The text displayed in the notification. |
| Parameter 2 type | String // usually used in combination with **[formatted string](https://docs.erp.net/tech/advanced/user-business-rules/parameter-types/formattedstring.html)**  |
| Parameter 3      | (Optional) The class which will be set for the notification. It must meet the format specified in [R35312 Notifications - Validate Notification Class](/github.com/ErpNetDocs/model/business-rules/R35312.md) <br> If the parameter isn't explicitly set, a default value will be used instead: 'USR' + '\_' + 'BR' + '\_'  + 'UserBusinessRule.Code', e.g. 'USR_BR_0005'. <br><br> For more information about classes, see **[Notifications](https://docs.erp.net/tech/modules/community/social-interactions/notifications/index.html)**. |
| Parameter 3 type | String                                                       |
| Examples         | see the **Example** section below                            |
| Version          | Introduced in: 2020.1                                        |

## Compatible events chart

NOTIFYUSER is **not** compatible with all events.

| Event type                                                   | Compatibility with NOTIFYUSER                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Client commit (e.g. [CLIENTCOMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/client-commit.html), [AGGREGATECLIENTCOMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/aggregate-client-commit.html))     | compatible                                                   |
| Document events - (e.g. [STATECHANGING](https://docs.erp.net/tech/advanced/user-business-rules/events/statechanging.html), [STATECHANGED](https://docs.erp.net/tech/advanced/user-business-rules/events/statechanged.html), [VOIDING](https://docs.erp.net/tech/advanced/user-business-rules/events/voiding.html))| compatible                                                   |
| Commit (e.g. [COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/commit.html))                                         | incompatible// <br> NOTIFYUSER will create a notification which will be displayed on the **next** login into the program. |
| Front-end (e.g ATTRIBUTECHANGING, ATTRIBUTECHANGED)          | incompatible// <br> NOTIFYUSER **won't** create a notification.  |

### Example:

А **[business rule](https://docs.erp.net/tech/advanced/user-business-rules/business-rules/index.html)** creates a notification for а sales person when one of their sales orders has been released.



| Repository            |                 |                    |                  |                                                              |                                             |                 |                         |
| --------------------- | --------------- | ------------------ | ---------------- | ------------------------------------------------------------ | ------------------------------------------- | --------------- | ----------------------- |
| Crm.Sales.SalesOrders |                 |                    |                  |                                                              |                                             |                 |                         |
| **Events**            |                 |                    |                  |                                                              |                                             |                 |                         |
| Event type            | Event parameter | Execution priority |                  |                                                              |                                             |                 |                         |
| Change of state       | RELEASED        | Normal             |                  |                                                              |                                             |                 |                         |
| **Actions**           |                 |                    |                  |                                                              |                                             |                 |                         |
| Action No             | Action type     | Parameter1 type    | Parameter1 value | Parameter2 type                                              | Parameter2 value                            | Parameter3 type | Parameter3 value        |
| 1                     | NOTIFYUSER      | Attribute          | SalesPersonId    | Formatted string | sales order {DocumentNo} has been released. | Constant        | USR_SALESPERSON_SORELEASED |
