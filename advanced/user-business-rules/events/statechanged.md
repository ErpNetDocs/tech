---
uid: statechanged
items: events
---

# STATECHANGED

|Name|STATECHANGED
|:-----|:-----
|**Layer**|Back-end
|**Description**|Occurs when a **[document state](https://docs.erp.net/tech/concepts/documents/states.html)** specified in the _Parameter_ field is changed.
|**Version**|Introduced: 2017.1 <br> Updated: -

This event occurs **AFTER** the change of the document state but **BEFORE** that change is saved. <br><br>

**Example 1**

There's a **[FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html)** action set on a STATECHANGED event.

The rule will be triggered once all rules and validations registered on **[STATECHANGING](https://docs.erp.net/tech/advanced/user-business-rules/events/statechanging.html)** are performed. However, this happens **before** the document is saved into the database. When conditions are met and the rule fails, the state of the document **won't** be changed and it'll remain in its previous state.

**Example 2**

When you receive a batch of goods, you want to check if the availability of a product would be over 100 PCS. <br> It's best to use STATECHANGED so the quantities of the current store transaction are included in the calculation. <br><br>

STATECHANGED always goes with an event parameter. Possible values are:

- **PLANNED**
- **FIRMPLANNED**
- **RELEASED**
- **COMPLETED**
- **CLOSED**
