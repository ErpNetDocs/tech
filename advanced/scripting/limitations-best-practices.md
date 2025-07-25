# Limitations and best practices

This page describes key limitations to consider when writing scripts, along with recommended best practices to ensure reliability, security, and maintainability in @@name.

## Limitations

- **Sandboxed Environment:**  
  Scripts run in a restricted sandbox. Access to system resources (files, network, OS) is limited to what is explicitly provided (such as the [Domain Model](./domain-model/index.md) and [Action object](./global-action-object/index.md)).
  
- **No Control Over Transactions:**  
  Scripts do not control transaction boundaries. Changes take effect only if the outer logic commits the transaction.
  
- **Timeouts and Resource Usage:**  
  Scripts have execution timeouts and limits on memory or CPU usage, as defined by system configuration.
  - Memory allocations limit: 50 MB per script.
  - Execution timeout: 5 seconds per script.
  - Maximum statements: 500,000 JavaScript statements.
  
- **Limited Language Support:**  
  Official support is for JavaScript only. C# scripting is legacy, not recommended, and will be removed in future versions.
  
- **Module/Context Availability:**  
  Not all parts of the system support scripting. The available context and objects depend on where the script is triggered.
  
## Best Practices

- **Always check for nulls:**  
  The `subject` variable and other context objects may be null. Check before using them.
  
- **Use logging wisely:**  
  Log important actions and errors for traceability, but avoid excessive logging that could clutter the system.
  
- **Limit data volume:**  
  Use `fetch` and filters to limit the amount of data processed in queries. Avoid large result sets in scripts.
  
- **Handle errors gracefully:**  
  Use `Action.error()` and `Action.cancel()` to manage errors and control script flow.
  
- **Write clear, maintainable code:**  
  Use comments, meaningful variable names, and consistent formatting for easier maintenance and debugging.
  
## See Also

- [Action Object](./global-action-object/index.md)
- [Entity Operations](./domain-model/entity-operations.md)
- [Advanced Examples](./domain-model/advanced-examples.md  )