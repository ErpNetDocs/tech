---
uid: brat-WARNING
items: ActionTypes
---

# WARNING

Usually used to show a non-blocking message, that helps  users in certain situation. It may be useful when we just want to show a reminder, instead of stopping the transaction with an error using a **[FAIL](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-business-rules/action-types/fail.md)** business rule. The WARNING syntax is simple - the message that is  going to be shown is set as a first parameter of the WARNING action. 

**Example:**

ActionNo: **1**; Action Type: **WARNING;** Parameter1 Type: **Constant**; Parameter1 Value: **'warning message text'**.
