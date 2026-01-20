# Breaking changes

## **1. Follow Levels and Notifications Behavior**

Notifications now depend on the Follow Level of objects. All existing follows have been migrated to TAGGED.<br>
TAGGED objects deliver chat/comment events only.

➡️ To continue receiving update or implicit notifications, mark important objects as Follow or Favorite.
[Details](follows-and-notifications.md)

## **2. JavaScript Enum Handling in User Business Rules**

Enum values are now handled as **strings instead of numbers** in JavaScript user business rules.  
Numeric enum comparisons may no longer work as expected.  

➡️ [Details](../user-business-rules/index.md)

## **3. ToDo application shows all Tasks now**

The default behavior of the ToDo application has changed.

Linked ToDo tasks are now **visible by default**, whereas previously they were hidden until explicitly enabled by the user. Users who prefer the previous behavior can disable it using the [**/ToDo/ShowLinked** configuration key](https://docs.erp.net/tech/reference/config-options-reference.html#73-todoshowlinked).

➡️ [Details](../my-apps/index.md)
