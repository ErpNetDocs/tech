---
uid: brat-NOTIFYUSER
items: ActionTypes
---

# NOTIFYUSER

| Name             | NOTIFYUSER                                                   |
| ---------------- | ------------------------------------------------------------ |
| Description      | Used for creating notifications with a specific text for the object for  which the business rule has been triggered, which are later going to be  sent to the users that were indicated in the rule by the [Notifications](https://docs.erp.net/tech/modules/community/social-interactions/notifications/index.html) system. <br/><br/> More specifically, the action creates a record in the *Notifications* table for each of the users specified in Parameter1 (if there are more than  one), whereUserId = the Id of the user in Parameter1 ValueSubject = Parameter2 ValueNotificationClass = Parameter3 Value, if emty - set a default value which is 'BR' + '_' + 'UserBusinessRule.Code' e.g. 'BR_0005'.DataObject = the extensible data object of the aggregate root of the entity for which the rule has been triggered. For more info, see [Aggregates](https://docs.erp.net/tech/advanced/concepts/aggregates.html) and [Extensible Data Objects](https://docs.erp.net/tech/advanced/data-objects/extensible-data-objects.html). If there are not explicitly created [Notification Settings](https://docs.erp.net/tech/modules/community/social-interactions/notifications/settings.html) for the class specified in Parameter3, the notification will only be sent as an in-app notification.<br/><br/>**IMPORTANT:** The NOTIFYUSER action is not compatible with all [events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html). For more info, see the *Compatible Events Chart* below. |
| Parameter 1      | **<User> -** The user/users for which the notification is going to be created. We can set either the UserId or the User's login. If there are more than one recipients they can be entered in a  comma-separated list, but the list must contain  only UserIds (Id1,Id2,...IdN) or only user's logins  (Login1,Login2,...LoginN). |
| Parameter 1 Type | Guid, String, List                                           |
| Parameter 2      | **<Text>** - The text which is going to be displayed in the notification. |
| Parameter 2 Type | String // usually used in combination with the [formatted string ](https://docs.erp.net/tech/advanced/user-business-rules/parameter-types/formattedstring.html) parameter type. |
| Parameter 3      | **<Class>** (optional) - The class which will be set for the notification.  If the parameter is not explicitly set will be used a default value.  The default value is 'BR' + '_' + 'UserBusinessRule.Code' e.g.  'BR_0005'.For more information about *Classes*, see [Notifications](https://docs.erp.net/tech/modules/community/social-interactions/notifications/index.html). |
| Parameter 3 Type | String                                                       |
| Example          | see the Example section below                                |
| Version          | Introduced in: 2020.1                                        |

## Compatible Events Chart

The NOTIFYUSER action is not compatible with all [events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html). For more info, look into the following chart.

| Event Type                                                   | Compatibility with NOTIFYUSER                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Client Commit (e.g. CLIENTCOMMIT, AGGREGATECLIENTCOMMIT)     | compatible                                                   |
| Document Events - (e.g. STATECHANGING, STATECHANGED, VOIDING) | compatible                                                   |
| Commit (e.g. COMMIT)                                         | not compatible// NOTIFYUSER will create a notification but it will not be displayed to the user in  real time. The notification will be displayed at the next login into the program. |
| Front-End (e.g ATTRIBUTECHANGING, ATTRIBUTECHANGED)          | not compatible// NOTIFYUSER will not create a notification.  |

## Example

А [business rule](https://docs.erp.net/tech/advanced/user-business-rules/business-rules/index.html) that creates a notification for the sales person, when one of their sales orders has been released.



| Repository            |                 |                    |                  |                                                              |                                             |                 |                         |
| --------------------- | --------------- | ------------------ | ---------------- | ------------------------------------------------------------ | ------------------------------------------- | --------------- | ----------------------- |
| Crm.Sales.SalesOrders |                 |                    |                  |                                                              |                                             |                 |                         |
| **Events**            |                 |                    |                  |                                                              |                                             |                 |                         |
| Event Type            | Event Parameter | Execution Priority |                  |                                                              |                                             |                 |                         |
| Change of State       | RELEASED        | Normal             |                  |                                                              |                                             |                 |                         |
| **Actions**           |                 |                    |                  |                                                              |                                             |                 |                         |
| Action No             | Action Type     | Parameter1 Type    | Parameter1 Value | Parameter2 Type                                              | Parameter2 Value                            | Parameter3 Type | Parameter3 Value        |
| 1                     | NOTIFYUSER      | Attribute          | SalesPersonId    | [Formatted String ](https://docs.erp.net/tech/advanced/user-business-rules/parameter-types/formattedstring.html) | sales order {DocumentNo} has been released. | Constant        | Sales_Person_SOReleased |
