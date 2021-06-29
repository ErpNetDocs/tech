---
uid: brat-WARNING
items: ActionTypes
---

# WARNING

Usually used to show a non-blocking message, that helps  users in certain situation. It may be useful when we just want to show a reminder, instead of stopping the transaction with an error using a [FAIL](https://olddocs.erp.net/tech/fail-41146659.html) business rule. The WARNING syntax is simple - the message that is  going to be shown is set as a first parameter of the WARNING action. 



***Example:\***

ActionNo: **1**; Action Type: **WARNING;** Parameter1 Type: **Constant**; Parameter1 Value: **'warning message text'**.
