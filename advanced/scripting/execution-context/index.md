# Execution context

Detailed scripting execution-context guidance is in the [Developer Documentation](https://docs.erp.net/dev/scripting/concepts/execution-context-and-results.html).

For user business rules, `subject` is the entity that triggered the rule. Managed scripts instead receive declared inputs through `args` and have no current-entity `subject`. Use the developer guide to choose the correct contract for each entry point.
