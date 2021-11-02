
# User business rules

These are business rules which a user defines on his own. They may be used to provide some kind of validation which is not available in the system business rules or to create working logic which is not currently available in the software. They may be registered on different layers - BackEnd and/or FrontEnd. The BackEnd means that the user business rule is processed on the server. A FrontEnd user business rule is processed in the client application.

The user business rules consist of the following information: 'where?', 'when', and on 'what conditions?' something ('what?') should happen.

They have the following information:

- Code - unique code of the rule;
- Name - the name of the user business rule;
- Repository Name - the name of the repository for which the business rule is  defined. For example - invoices or invoice lines. Its value may be  selected from a dropdown list and the value contains the path to the  selected value, dot separated. For example: if the user needs to create  user business rule so he can use it in the invoices forms or in the  invoices navigators, the repository should be 'Crm.Invoicing.Invoices'.  If the rule is created to be used in the invoice lines, then the repository should be 'Crm.Invoicing.InvoiceLines';
- Notes - notes, comments, short information on the user business rules usage, purpose and more;
- IsActive - the user business rule may be activated and deactivated;
- *Layer* - currently this is unavailable. All user business rules are registered in the BackEnd layer.

The events which need to happen for the user business rule to be activated are described in the [User business rules - Events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html) panel. It consists of the following information:

- Event type - the event for which to register the user business rule;
- Event parameter - registration parameter. The meaning of this parameter is  determined by the type of the event;
- Execution priority - execution priority. Lowes values indicate earlier  priorities. Possible values are: 30-Early, 50-Normal; 70-Late;
- Layer - currently this is unavailable. All events are events of the BackEnd layer.

The conditions which have to be met when the event happen so the rule to be processed are entered as follows:

- Condition No - consecutive number of the condition, unique within the user business rule.
- Attribute name - the name of the attribute which will be validated in the condition.
- Comparison type - what is the comparison type. The available options are: =, !=, >=, <=, Like, IsNull,
- Value - the constant value to which the value of attribute (specified in the Attribute name) is compared to.

So the condition is met when the value of the specified attribute and the  specified value compose a true statement with the selected comparison  type. For example, IsActive = True or Quantity < 100.0 and more. 

> [!Note] 
> If there is more than one condition, the rule will be applied when **all** conditions are true.

The [actions](https://docs.erp.net/tech/advanced/user-business-rules/action-types/index.html) which may be executed by the rule contain the following information:

- Action No - consecutive number of the action, unique within the user business rule;
- Action type - specifies the [type of action](https://docs.erp.net/tech/advanced/user-business-rules/action-types/index.html) to be performed by the rule. Possible values are: [SETVALUE](https://docs.erp.net/tech/advanced/user-business-rules/action-types/setvalue.html) and [FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html). 
- Parameter1 type, Parameter2 type, Parameter3 type - the type of the parameter specifies how to obtain the parameter value; 
- Parameter1 value, Parameter2 value, Parameter3 value - the actual value of the parameter.

### Temporary

[!list depth=1 style="bullet" limit=100]
