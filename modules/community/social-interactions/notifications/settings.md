---
uid: notification-settings
---

# Notifications settings

These settings allow users to specify which notifications they want to receive. They can also specify whether the notifications should be sent in-app, by mail or by sms.

- A setting is for a single user, for a single notification class.

- Only whole notification classes can be set up. Currently, there is no support for muting specific notification types.

- A setting determines whether the user should receive:

   - Notification - these are the in-app @notifications.
   - Email - the user should receive email on their primary email.
   - Sms - the user should receive SMS on their primary phone number.
   
- For more information about notification types and classes, see @notifications.

## Follow Levels and Notifications Behavior

Release 26.2 introduces Follow-Level-aware notifications and updates the default behavior for existing follows. With this release, a new logic is introduced where **notifications depend on the Follow Level** of objects in the system.

_What’s changing?_
<br>All existing Favorite records are migrated to **Follow Level = TAGGED**. After the update, **no objects will be marked as Favorite by default**.

_What this means for users?_
<br>Users may temporarily stop receiving notifications they previously received.

When an object is at **Follow Level = TAGGED**:
- Only **chat / comment events** are delivered  
- **Record update notifications are NOT sent**  
- **Implicit notifications** (e.g. new related content) **are NOT sent**

_To continue receiving notifications_
<br>Users must **explicitly mark objects as Follow or Favorite** to receive update or implicit notifications.

_What does NOT change?_

- Chat events and direct mentions are still delivered, regardless of Follow Level  
- Object access and group membership are not affected

_Technical note (for internal teams)_
<br>Follow Level logic applies **only** to Record Update and Implicit notifications.  Other business processes are not affected unless explicitly stated.
