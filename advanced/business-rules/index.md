
# User Business Rules

User Business Rules are business rules which the user defines on his  own. They may be used to provide some kind of validation which is not  available in the system business rules or to create working logic which  is not currently available in the software. They may be registered on  different layers - BackEnd and/or FrontEnd. The BackEnd means that the  user business rule is processed on the server. A FrontEnd user business  rule is processed in the client application.

The user business  rule consist of the following information: "where?" "when?" and on "what conditions?" something ("what?") should happen.

The user business rules have the following information:

- Code - unique code of the rule;
- Name - the name of the user business rule;
- Repository Name - the name of the repository for which the business rule is  defined. For example - Invoices or Invoice Lines. Its value may be  selected from a dropdown list and the value contains the path to the  selected value, dot separated. For example: if the user needs to create  user business rule so he can use it in the Invoices forms or in the  Invoices navigators, the Repository should be "Crm.Invoicing.Invoices".  If the rule is created to be used in the invoice lines, then the  Repository should be "Crm.Invoicing.InvoiceLines";
- Notes - notes, comments, short information on the user business rules usage, purpose and more;
- IsActive - the user business rule may be activated and deactivated;
- *Layer* - currently this is unavailable. All user business rules are registered in the BackEnd layer.

The events which has to happen so the user business rule to be activated  are described in the User Business Rules - Events panel. It is consisted of the following information:

- Event Type - the event for which to register the user business rule;
- Event Parameter - registration parameter. The meaning of this parameter is  determined by the type of the event. For more information on event  parameters see [Business rules - Events](user-business-rules-events/index.md);
- Execution Priority - execution priority. Lowes values indicate earlier  priorities. Possible values are: 30-Early, 50-Normal; 70-Late;
- *Layer -* currently this is unavailable. All events are events of the BackEnd layer.

The conditions which have to be met when the event happen so the rule to be processed are entered as follows:

- Condition No - consecutive number of the condition, unique within the user business rule.
- Attribute Name - the name of the attribute which will be validated in the condition.
- Comparison Type - what is the comparison type. The available options are: =, !=, >=, <=, Like, IsNull,
- Value - the constant value to which the value of attribute (specified in the Attribute Name) is compared to.

So the condition is met when the value of the specified attribute and the  specified value compose a true statement with the selected comparison  type. For example, IsActive = True or Quantity < 100.0 and more. 

 

> [!NOTE] 
>
> If there are more than one conditions, the rule would be applied when all conditions are true.

The actions which may be executed by the rule contain the following information:

- Action No - consecutive number of the action, unique within the user business rule;
- Action Type - specifies the type of action to be performed by the rule.  Possible values are: SETVALUE and FAIL. For more information on the  action types see [Business rules Actions - Action types](action-types/index.md);
- Parameter1 Type, Parameter2 Type, Parameter3 Type - the type of the parameter specifies how to obtain the parameter value; 
- Parameter1 Value, Parameter2 Value, Parameter3 Value - the actual value of the parameter.
