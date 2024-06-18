# Use system variables for managing user status in documents

There are system variables for managing the user status in a document, making them part of the “STATECHANGED” and “STATECHANGING” document events. 

This allows them to be used across any other **[business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)**.

- **$FromUserStatusId** – relates to the initial user status.
- **$ToUserStatusId** – relates to the targeted user status.
	
You can select these variables from the list of attributes of the **Condition** of the user business rule, specifying the ID of the user status in the **Value** field.

### Step-by-step example

In this example, we will call the STATECHANGING event for documents of type *BGVATDeclarations*. 

1. Create at least two new user statuses.

	![picture](pictures/step_one.png)

2. Add a new business rule.
 
	![picture](pictures/step_two.png)

3. Create one offer and start changing its statuses. As part of the rule conditions, change the target **attribute** and its **value**. 

4. Every time a condition is met, you should get a "Yes" warning. 
