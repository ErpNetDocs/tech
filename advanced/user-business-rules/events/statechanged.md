# STATECHANGED
 
 
#### EVENT SUMMARY
|Name|STATECHANGED
|:-----|:-----
|**Layer**| Back-End
|**Description**| Occurs when the document state is changed. The <br> state is specified in the 'Parameter' field. Possible <br>parameter values are 'PLANNED', 'FIRMPLANNED', <br> 'RELEASED', 'COMPLETED' and 'CLOSED'.
|**Version**| Introduced: 2017.1 <br> Updated: -
 
This event will occur **AFTER** the change of the Document state but **BEFORE** that change has actually been saved. 

If there is, for example, a [FAIL](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-business-rules/action-types/fail.md) action set on STATECHANGED event, the rule will be triggered after all rules and validation registered on **[STATECHANGING](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-business-rules/events/statechanging.md)** are performed but before the document is saved into the database.  In this case, when the conditions are met and the rule fails - the state of the document will not be successfully changed and it will remain in its previous state.

Another example of a use case for this event is when we want to check if the availability of the product would be over 100 PCS when we receive a batch of goods. We would want to use the STATECHANGED event so the quantities of the current store transaction are included in the calculation.

The event always goes with an event parameter. Possible values are:

- **PLANNED**
- **FIRMPLANNED**
- **RELEASED**
- **COMPLETED**
- **CLOSED**
