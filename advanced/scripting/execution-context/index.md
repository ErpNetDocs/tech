# Execution context

The execution context defines what data, objects, and services are available to a script at runtime.

Understanding the execution context is essential for writing effective scripts, as it determines which entities and helpers you can access and manipulate.

## What is the execution context?

When a script is triggered- such as by a business rule or other system event - it runs within a specific context.

This context typically includes:

- The entity that triggered the script:
Available as the `subject` variable, representing the entity being processed.

- Global objects:
Helpers such as the **[Action object](../global-action-object/index.md)**, providing utility methods for notifications, logging, and other actions.

## Example

Suppose a script is triggered by a user business rule attached to the Customers repository. In this context:

- The subject variable will reference the specific customer entity involved.
- You have access to the global `Action` and can interact with the Domain Model as needed.

```js
// Example: Log a message about the current customer.
Action.log("Processing customer: " + subject.Number);
```

## Context can vary

The execution context depends on where and how the script is triggered.
E.g., the type of the `subject` variable will change based on the business rule's entry point and the repository to which it is attached. If a rule is attached to the Customers repository, subject will be a Customer entity; if attached to another repository, `subject` will represent an instance of that entity type.

Always refer to the documentation for your specific script entry point to understand exactly which context variables and objects will be available during execution.