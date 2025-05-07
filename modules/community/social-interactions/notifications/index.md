---
uid: notifications
---

# Notifications

Notification is a single [notification](https://docs.erp.net/model/entities/Communities.Notifications.html) of one user for one event. 
The event can contain multiple references to objects, definitions, etc.

- Although **notification** is an entity in the @social-interactions module, a notification can be raised by any module in the system.
- A notification is most often "transmitted" by a [real-time event](../../../../advanced/concepts/real-time-events.md).
- Each notification is persistent. It lives in the database (i.e. it has a corresponding record).
- Notifications **MAY** specify a data object.

> [!NOTE]
> If a notification specifies a data object, this means that it's related to this data object. However, this attribute is not required and can be null.

## Notification interaction

Often, the user can interact with a notification. 
The most common example when the notification appears as a toast- the user can click on it. 
In this scenario, if the notification is bound to a data object, it will be opened.

A simple example:
- You're following a specific document. E.g., an offer.
- Someone writes a comment in its corresponding chatter control.
- If you're online, you'll receive a notification as a toast.
- If you click on the notification- you'll be navigated to the document (i.e. the offer).

> [!NOTE]
> When a notification is displayed to a user, it is marked as **read**. This does not guarantee that the user has read or understood it.
 
> [!NOTE] 
> The UI in some apps might require the user to actually click on the notification in order to mark it as read.

## Notification classes

Each notification has a class which specifies the type of the notification. Additionally, all notification classes are grouped for better classification.

Also, most of the notifications are created automatically via business rules when the corresponding event occurs (e.g. when someone writes a comment).

| Notification class | Group | Business rule | Description |
| ---- | ---- | ----------- |
| NT_DOC_STATE_IMPLICIT | Document | **[R33718](https://docs.erp.net/model/business-rules/R33718.html) Document**- Notify All Implicit Followers | If a document changes its state and you're following an entity, related to this document (e.g. its customer, its document type, etc) you'll receive a notification. |
| NT_SOC_REPLY | Social | **[R33428](https://docs.erp.net/model/business-rules/R33428.html) SocialComment**- Notify User Comment Replied | There was a reply to your post or comment. |
| NT_SOC_NEW_POST | Social | -  | New post in a group, in which you're a member. |
| NT_SOC_MENTION | Social | **[R32943](https://docs.erp.net/model/business-rules/R32943.html) SocialComment**- Notify The Mentioned User | You're mentioned in a post or comment. |
| NT_SOC_REACTION | Social | **[R33427](https://docs.erp.net/model/business-rules/R33427.html) SocialReaction**- Notify User Comment Reaction | There was a reaction to your post or comment. |
| NT_NEW_COMMUNITY_USER | Social | **[R33153](https://docs.erp.net/model/business-rules/R33153.html) Security Users**- Notify Admins On Community User Creation | New external (community) user '{Login}' is created.|
| NT_SOC_GROUP_MEMBER_ADDED | Social | **[R37141](https://docs.erp.net/model/business-rules/R37141.html) Social Group**- Notify Group Members Changed | You were added to the group '{Group.Name}'.|
| NT_SOC_GROUP_MEMBER_REMOVED | Social | **[R37141](https://docs.erp.net/model/business-rules/R37141.html) Social Group**- Notify Group Members Changed | You were removed from the group '{Group.Name}'.|
| NT_SOC_GROUP_MEMBERSHIP_ADDED | Social | **[R37141](https://docs.erp.net/model/business-rules/R37141.html) Social Group**- Create comment in the chat upon adding a member to a group | You were added to the group '{Group.Name}'.|
| NT_SOC_GROUP_MEMBERSHIP_REMOVED | Social |**[R37141](https://docs.erp.net/model/business-rules/R37141.html) Social Group**- Create comment in the chat upon removing a member from a group | You were removed from the group '{Group.Name}'.|
| NT_WM_QTY_BELOW_MIN | WMS | - | In @wms, when the qty in a tracked bin falls below the minimum. |
| NT_SOC_NEW_COMMENT | Social | **[R33417](https://docs.erp.net/model/business-rules/R33417.html) SocialComment**- Notify All Object Followers | New comment to an object you are following. |
| NT_ALL_UPDATE | All Entities | **[R34361](https://docs.erp.net/model/business-rules/R34361.html) All Entities** - Notify All Object Followers Upon Update | Create notification for all followers of each updated object. |
| NT_ACT_REMINDER | Activity Reminders | - | Activity reminder, within the next 15 minutes at the latest. |
| NT_TODO_REMINDER | Todo Reminders | - | Todo task reminder, within the next 15 minutes at the latest. |
| NT_DOC_ASSIGNMENT | Document | **[R35922](https://docs.erp.net/model/business-rules/R35922.html) Document** - Notify Assigned To User Upon Assignment | Notify user when a document has been assigned to them.
| NT_DOC_STATE_ASSIGN | Document | **[R35927](https://docs.erp.net/model/business-rules/R35927.html) Document** - Notify Assigned To User For State Change | Notify the assigned user when the document state is changed.
| NT_DOC_UPDATE_ASSIGN | Document | **[R35940](https://docs.erp.net/model/business-rules/R35940.html) Document** - Notify Assigned To User For Update | Notify the assigned user when the document is edited.
| NT_TODO_ASSIGNMENT | To Do | **[R35962](https://docs.erp.net/model/business-rules/R35962.html) Task** - Notify Assigned To User Upon Assignment | Notify the assigned user when the To Do has been assigned to them.
| NT_TODO_UPDATE_ASSIGN | To Do | **[R35951](https://docs.erp.net/model/business-rules/R35951.html) Task** - Notify Assigned To User For Update | Notify the assigned user when the To Do is edited.
| NT_LEAD_ASSIGNMENT | Lead | **[R35980](https://docs.erp.net/model/business-rules/R35980.html) Lead** - Notify Assigned To Sales Person Upon Assignment | Notify the assigned sales person's user when the Lead has been assigned to them.
| NT_LEAD_UPDATE_ASSIGN | Lead | **[R35958](https://docs.erp.net/model/business-rules/R35958.html) Lead** - Notify Assigned To Sales Person For Update | Notify the assigned sales person's user when the Lead is edited.
| NT_CASE_ASSIGNMENT | Case | **[R38379](https://docs.erp.net/model/business-rules/R38379.html) Case** - Notify Assigned To User On Assignment | Notify the assigned user when the Case has been assigned to them.
| NT_CASE_UPDATE_ASSIGN | Case | **[R38389](https://docs.erp.net/model/business-rules/R38389.html) Case** - Notify Assigned To User For Update | Notify the assigned user when the Case is edited.
| NT_ACTPARTICIPANTS_ASSIGN | Activity | **[R36471](https://docs.erp.net/model/business-rules/R36471.html) Activity** - Notify Activity Participants Upon Assignment | Notify users when they are assigned as participants in the Activity.
| NT_COMPILATION_COMPLETION | Compilation | **[R36563](https://docs.erp.net/model/business-rules/R36563.html) Compilation** - Notify On Completion | Notify the user who initiated the compilation when the compilation is finished.

## I don't care about notifications

You can always mute the notification classes you're not interested in. Or you can mute all of them. 
This way you won't be notified of anything you don't want. 
For more information see our separate topic [Notification settings](./settings.md)

## Create notifications programmatically

It's possible to create notifications programmatically via Domain API. For more information, check the dev topic
https://docs.erp.net/dev/domain-api/common-tasks/create-notification.html
