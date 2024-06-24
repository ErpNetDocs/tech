# Manage the user status of a document

You can use system variables for **[business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** with the "STATECHANGED" and "STATECHANGING" events to trigger specific actions when changing the user status of a document.

- **$FromUserStatusId** – the rule is tied to the initial user status
- **$ToUserStatusId** – the rule is tied to the user status the initial one will be changed to

## Set up a business rule

In this example, we will create a business rule for documents of type *Offer*. 

In the end, we should trigger a warning message when changing an offer's document status.

### Step-by-step example

1. If not present, create at least two user statuses for the _FIRMPLANNING_ document state of the _Offer_ document type.
2. Define a _STATECHANGING_ event with a _FIRMPLANNING_ parameter.
3. In the **Conditions** panel, select _$ToUserStatusId_ from the **Attribute name** field.

   Within the **Value** field, input the ID of the user status corresponding with the _FIRMLANNING_ state of the Offer document type.

	![picture](pictures/conditions_set.png)

4. Define a **warning** action with a **formatted string** parameter (e.g. "yes") and save the business rule.

Now, if you change the user status of an offer in Firm planned state to the one specified in the condition of the business rule, you will trigger a warning.

![picture](pictures/statechangeds.png)

