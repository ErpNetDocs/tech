---
uid: brat-NOTIFYUSER
items: ActionTypes
---

# NOTIFYUSER

| Name             | NOTIFYUSER                                                   |
| ---------------- | ------------------------------------------------------------ |
| Description      | Used for creating notifications with a specific text for the object for  which the business rule has been triggered, which are later going to be  sent to the users that were indicated in the rule by the [Notifications](https://olddocs.erp.net/tech/notifications-805540872.html) system.More specifically, the action creates a record in the Notifications table  for each of the Users specified in Parameter1 (if there are more than  one), whereUserId = the Id of the user in Parameter1 ValueSubject = Parameter2 ValueNotificationClass = Parameter3 Value, if emty - set a default value which is"BR" + "_" + "UserBusinessRule.Code" e.g. "BR_0005".DataObject = the Extensible Data Object of the Aggregate Root of the Entity for which the rule has been triggered. For more info, see [Aggregates](https://olddocs.erp.net/tech/aggregates-796819535.html) and [Extensible Data Objects](https://olddocs.erp.net/tech/extensible-data-objects-796819770.html).If there are not explicitly created [Notification Settings](https://olddocs.erp.net/tech/notification-settings-805540876.html) for the Class specified in Parameter3, the notification will only be sent as an in-app notification.**IMPORTANT:** The NOTIFYUSER action is not compatible with all [User Business Rules - Events](https://olddocs.erp.net/tech/user-business-rules-events-41146209.html). For more info, see the *C**ompatible Events Chart* below. |
| Parameter 1      | **<User> -** The user/users for which the notification is going to be created. We can set either the UserId or the User's login. If there are more than one recipients they can be entered in a  comma-separated list, but the list must contain  only UserIds (Id1,Id2,...IdN) or only User's logins  (Login1,Login2,...LoginN). |
| Parameter 1 Type | Guid, String, List                                           |
| Parameter 2      | **<Text>** - The text which is going to be displayed in the notification. |
| Parameter 2 Type | String // usually used in combination with the [Formatted String ](https://olddocs.erp.net/tech/formattedstring-808550544.html)parameter type. |
| Parameter 3      | **<Class>** (optional) - The Class which will be set for the notification.  If the Parameter is not explicitly set will be used a default value.  The default value is "BR" + "_" + "UserBusinessRule.Code" e.g.  "BR_0005".For more information about Classes, see [Notifications](https://olddocs.erp.net/tech/notifications-805540872.html). |
| Parameter 3 Type | String                                                       |
| Example          | see the Example section below                                |
| Version          | Introduced in: 2020.1                                        |

## Compatible Events Chart

The NOTIFYUSER action is not compatible with all [User Business Rules - Events](https://olddocs.erp.net/tech/user-business-rules-events-41146209.html). For more info look into the following chart.

| Event Type                                                   | Compatibility with NOTIFYUSER                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Client Commit (e.g. CLIENTCOMMIT, AGGREGATECLIENTCOMMIT)     | compatible                                                   |
| Document Events - (e.g. STATECHANGING, STATECHANGED, VOIDING) | compatible                                                   |
| Commit (e.g. COMMIT)                                         | not compatible// NOTIFYUSER will create a notification but it will not be displayed to the user in  real time. The notification will be displayed at the next login into the program. |
| Front-End (e.g ATTRIBUTECHANGING, ATTRIBUTECHANGED)          | not compatible// NOTIFYUSER will not create a notification.  |

## Example

А [User Business Rules](https://olddocs.erp.net/tech/user-business-rules-35586099.html) that creates a notification for the Sales Person, when one of his Sales Orders has been released.



| Repository            |                 |                    |                  |                                                              |                                             |                 |                         |
| --------------------- | --------------- | ------------------ | ---------------- | ------------------------------------------------------------ | ------------------------------------------- | --------------- | ----------------------- |
| Crm.Sales.SalesOrders |                 |                    |                  |                                                              |                                             |                 |                         |
| **Events**            |                 |                    |                  |                                                              |                                             |                 |                         |
| Event Type            | Event Parameter | Execution Priority |                  |                                                              |                                             |                 |                         |
| Change of State       | RELEASED        | Normal             |                  |                                                              |                                             |                 |                         |
| **Actions**           |                 |                    |                  |                                                              |                                             |                 |                         |
| Action No             | Action Type     | Parameter1 Type    | Parameter1 Value | Parameter2 Type                                              | Parameter2 Value                            | Parameter3 Type | Parameter3 Value        |
| 1                     | NOTIFYUSER      | Attribute          | SalesPersonId    | [Formatted String ](https://olddocs.erp.net/tech/formattedstring-808550544.html) | Sales Order {DocumentNo} has been released. | Constant        | Sales_Person_SOReleased |