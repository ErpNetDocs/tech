# Scripting in user business rules

You can embed custom scripts directly in user business rules to automate logic, perform complex validations, or interact with @@name Domain Model.

Scripting dramatically simplifies solutions that previously required complex configuration or workarounds-- such as creating additional Calculated Attributes just to enable a validation or automation. 

Now, many of these scenarios can be handled more directly and elegantly with just a few lines of script.

## How it works

- **Script language:**
Choose the scripting language for your rule (JavaScript is recommended and officially supported).

- **Script text:**
Write your script directly in the business rule's `ScriptText` attribute. This script is executed whenever the rule is triggered (e.g., on a COMMIT event).

The script runs in a sandboxed environment with access to:
- The entity that triggered the rule (via the `subject` variable)
- The entire @@name Domain Model
- The global `Action` object for logging, notifications, and more

## Example: Whole quantity validation

This example builds on an [existing user business rule for whole quantity validation](../examples/whole-quantity-validation.md) that previously required the creation of a dedicated Calculated Attribute to flag decimal quantities.

With scripting, the same business requirement can be enforced much more simply and directly. Instead of configuring additional calculated attributes and logic, you can now achieve the validation with a single line of script:

- **Repository:** Crm.Sales.SalesOrderLines
- **Event:** COMMIT
- **Script Language:** JavaScript
- **Script Text:**
```js
if (subject.Quantity != null && subject.Quantity.Value % 1 !== 0) {
    Action.cancel("You have entered a decimal number as a quantity. Please, check the data entered in the sales order lines and try again!");
}
```

Whenever a sales order line is saved, this script checks if the quantity is not a whole number and cancels the operation with your custom error message.

This approach eliminates the need for extra calculated attributes and keeps your business logic concise and easy to maintain.

-------------

For more details and advanced scripting scenarios, see the [Scripting documentation](../../scripting/index.md).