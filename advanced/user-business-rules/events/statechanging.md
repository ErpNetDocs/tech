---
uid: statechanging
items: events
---

# STATECHANGING

<br>

|Name| STATECHANGING
|:----|:----
|**Layer**| Back-end
|**Description**| Occurs during a **[document state](https://docs.erp.net/tech/concepts/documents/states.html)** change, specified in the _Parameter_ field.
|**Version**| Introduced: 2017.1 <br> Updated: -

This event happens **during** a change. <br><br>

**Example 1**

There's a **[FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html)** action set on a STATECHANGING event. If the rule is activated, the state of the document **won't** be changed and it'll remain in its previous state.

It's crucial to set the event correctly, as it happens in the data of the repository of the **[business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)**. 

**Example 2**

When you set а STATECHANGING event in a business rule with repository 'General.Products.Products', this rule would **never** be activated because the products don't support the event. 

**Example 3**

If a rule has a repository with document lines 'Crm.Invoicing.InvoiceLines', the event wouldn't activate the rule as the document lines **don't** support it. However, the event is supported by documents (their headers). <br><br>

STATECHANGING always goes with an event parameter. Possible values are:

- **PLANNING**
- **FIRMPLANNING**
- **RELEASING**
- **COMPLETING**
- **CLOSING**
