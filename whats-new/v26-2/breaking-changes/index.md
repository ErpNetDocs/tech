# Breaking changes

## **Follow Levels and Notifications Behavior**

Notifications now depend on the Follow Level of objects. All existing follows have been migrated to TAGGED.<br>
TAGGED objects deliver chat/comment events only.

➡️ To continue receiving update or implicit notifications, mark important objects as Follow or Favorite.
[Details](follows-and-notifications.md)

## **JavaScript Enum Handling in User Business Rules**

Enum values are now handled as **strings instead of numbers** in JavaScript user business rules.  
Numeric enum comparisons may no longer work as expected.  

➡️ [Details](../user-business-rules/index.md)
