**Breaking Change: Follow Levels and Notification Behavior**

This release introduces Follow-Level-aware notifications and updates the default behavior for existing follows. With this release, a new logic is introduced where **notifications depend on the Follow Level** of objects in the system.

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
