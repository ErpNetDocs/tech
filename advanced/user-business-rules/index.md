# User business rules

These are business rules which you define on your own. 

They may be used:

- to provide some kind of validation **unavailable** in the system business rules 
- to create working logic which is **unavailable** in the software. 

User business rules can be registered on different layers - **BackEnd** and/or **FrontEnd**. 

- BackEnd means that the rule is processed on the **server**. 
- FrontEnd implies that the rule is processed in the **client application**.

User business rules are based around questions: 

'where?', 'when', and on 'what conditions?' something ('what?') should happen.

They contain the following information:

- **Code** - unique code of the rule.

- **Name** - the name of the user business rule.

- **Repository Name** - the name of the repository for which the business rule is  defined. 
 
For example, 'Invoices' or 'Invoice lines'. 

The value of a repository name can be selected from a dropdown list. It contains the path to the selected value, dot-separated. If you need to create a user business rule which you can use in invoice forms or in invoice navigators, the repository should be 'Crm.Invoicing.Invoices'. If the rule is created for usage in invoice lines, the repository name becomes 'Crm.Invoicing.InvoiceLines'.

- **Notes** - notes, comments or short information about the user business rules' usage, purpose and more.

- **IsActive** - a user business rule may be activated or deactivated.

- **Layer** - currently, this is unavailable. All user business rules are registered in the **BackEnd** layer.

### Events

Some events need to happen for a user business rule to become active.

The **[Events](https://docs.erp.net/tech/advanced/user-business-rules/events/index.html)** panel consists of the following fields:

- **Event type** - the event the user business rule can be registered for.

- **Event parameter** - registration parameter, determined by the type of the event.

- **Execution priority** - lower values indicate earlier priorities. Possible values: 30-Early, 50-Normal; 70-Late.

- **Layer** - currently, this is unavailable. All events belong to the **BackEnd** layer.

### Conditions

There are several conditions that must be met for an event to happen:

- **Condition No** - consecutive number of the condition, unique within the user business rule.

- **Attribute name** - the name of the attribute that will be validated in the condition.

- **Comparison type** - the type of comparison. Available options are: '=', '!=', '>=', '<=', 'Like', 'IsNull',

- **Value** - the constant value to which the value specified in _Attribute name_ is compared.

A condition is met when the value of the specified attribute and the specified value compose a **TRUE** statement with the selected comparison type. For example, `IsActive = True`, `Quantity < 100.0` and more. 

> [!NOTE] 
> 
> If there's more than one condition, the rule will be applied when **all** conditions are true.

### Actions

**[Actions](https://docs.erp.net/tech/advanced/user-business-rules/action-types/index.html)** executable by rules contain the following information:

- **Action No** - consecutive number of the action, unique within the user business rule.

- **Action type** - specifies the type of action that will be performed by the rule. <br> Possible values are: **[SETVALUE](https://docs.erp.net/tech/advanced/user-business-rules/action-types/setvalue.html)** and **[FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html)**. 

- **Parameter1 type**, **Parameter2 type**, **Parameter3 type** - the type of parameter specifies how to obtain the parameter value.

- **Parameter1 value**, **Parameter2 value**, **Parameter3 value** - the actual value of the parameter.
