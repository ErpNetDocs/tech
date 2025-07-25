## Getting started

The scripting feature in @@name is accessible from specific modules and workflows, such as **user-defined business rules** within your instance.

It allows you to embed custom logic directly where business decisions or specific custom processes are required.

### How to create a script

> [!NOTE]
> 
> The examples below are tailored for scripting within [User Business Rules](https://docs.erp.net/model/entities/Systems.Bpm.UserBusinessRules.html).

1. Navigate to a module where scripting is supported (e.g., [User Business Rules](https://docs.erp.net/model/entities/Systems.Bpm.UserBusinessRules.html)).

2. Create a new rule or edit an existing one.

3. In the [Script Language](https://docs.erp.net/model/entities/Systems.Bpm.UserBusinessRules.html#scriptlanguage) attribute, select the desired scripting language/platform, and enter your script in the [Script Text](https://docs.erp.net/model/entities/Systems.Bpm.UserBusinessRules.html#scripttext) field.

> [!NOTE]
> 
> JavaScript is the recommended and officially supported scripting language.

4. Complete the remaining required fields for the user business rule- such as when it should be triggered, the context repository, etc.

5. Save.

Done.

The script will execute every time the rule is activated.

### Your first script

A classic way to get started with scripting is to log a simple message. The following example demonstrates how to write "hello world" to the system log whenever the rule is triggered:

```js
Action.log("hello world");
```

Once the rule containing this script is activated, you'll see "hello world" appear as a new [information message](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html).

This serves as a simple test to confirm that your scripting environment is working correctly.

> [!NOTE]
>
> The `Action` variable is a reference to the **global action object**. You can find more information and usage details [here](./global-action-object/index.md).