# STATECHANGING
## Event summary
|Name| STATECHANGING
|:----|:----
|**Layer**| Back-End
|**Description**| Occurs during the document state change. The state is specified in the 'Parameter' field. Possible parameter values are 'PLANNING', 'FIRMPLANNING', 'RELEASING', 'COMPLETING' and 'CLOSING'.**
|**Version**| Introduced: 2017.1 <br> Updated: -

This event happens during the change (before). If there is, for example, a [FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html) action set on the STATECHANGING event, if the rule is activated, the state of the document would not be successfully changed. It would remain in its previous state.

It is very important to set the event correctly. The event happens in the data which is set in the repository of the business rule. 

When we set the STATECHANGING event in a [user business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html) with repository 'General.Products.Products', this rule would never be activated because the products do not support the event. 

If a rule has a repository with document lines, for example 'Crm.Invoicing.InvoiceLines', this event would not be appropriate and would not activate the rule either. This is because the document lines do not support the change of state event; this event is supported by documents (their headers).

The event always goes with an event parameter. Possible values are:

- **PLANNING**
- **FIRMPLANNING**
- **RELEASING**
- **COMPLETING**
- **CLOSING**
