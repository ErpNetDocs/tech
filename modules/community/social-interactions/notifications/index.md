---
uid: notifications
---

# Notifications

Notification is a single notification of one user for one event. The event can contain multiple references to objects, definitions, etc.

- Although **notification** is an entity in the @social-interactions module, a notification can be raised by any module in the system.

- Notifications **CAN** specify a data object.

If they do, the notification is related to the data object. However, this attribute is not required and can be null.

- Notifications contain URLs.

If a user clicks on the notification, the specified URL will be opened.

- Each notification has a class which specifies the type of the notification:

  - NT_SOC_REPLY - there was a reply to my post or comment
  - NT_SOC_MENTION - I was mentioned in a post or comment
  - NT_SOC_NEW_POST - new post in a group, in which I am member
  - NT_SOC_REACTION - there was a reaction to my post or comment
  - NT_WM_QTY_BELOW_MIN - in @wms, when the qty in a tracked bin falls below the minimum
  
 - When a notification is displayed to a user, it is marked as **read**. This does not guarantee that the user has read or understood it.
 
> [!NOTE] 
> The UI in some apps might require the user to actually click on the notification in order to mark it as read.
