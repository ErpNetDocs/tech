# STATECHANGING
#### EVENT SUMMARY
|Name| STATECHANGING
|:----|:----
|**Layer**| Back-End
|**Description**| Occurs during the document state change. The state is specified in the 'Parameter' field. Possible parameter values are 'PLANNING', 'FIRMPLANNING', 'RELEASING', 'COMPLETING' and 'CLOSING'.**
|**Version**| Introduced: 2017.1 <br> Updated: -

The "Change of state" event means that it happens during the change (before). If there is, for example, a FAIL action set on Change of state event, if the rule is activated, the state of the document would not be successfully changed. It would remain in its previous state.

It is very important to set the event correctly. The event happens in the data which is set in the repository of the business rule. So if we set the "Change of state" event in user business rule with repository "General.Products.Products" this rule would never be activated because the products do not support the "Change of state" event. Also, if a rule has a repository with document lines, for example "Crm.Invoicing.InvoiceLines" this event would not be appropriate and would not activate the rule ever. This is because the document lines do not support the change of state event, this event is supported by documents (their headers).

The event always goes with an event parameter. Possible values of the event parameter are:
- PLANNING
- FIRMPLANNING
- RELEASING
- COMPLETING
- CLOSING
