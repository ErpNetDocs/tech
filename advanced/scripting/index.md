# Scripting

The scripting feature in @@name provides users with a powerful tool to customize and extend core business functionality.

By enabling the creation and execution of scripts within your instance, this feature makes it possible to automate business processes, implement custom business rules, and adapt workflows to unique organizational requirements.

Scripting enhances the flexibility of @@name, allowing businesses to efficiently tailor their operations to specific needs.

## Abstract

This documentation describes the @@name scripting feature, including how to create, execute, and manage scripts within your instance.

It covers supported scripting languages, integration with the domain model, available APIs, example use cases, and important security considerations.

## Supported scripting languages

@@name supports the following scripting languages:

- **JavaScript**: JavaScript is the officially supported scripting language. All new scripts should be written using standard JavaScript syntax.

- **C#**: It's available as a **legacy** feature. Support for C# scripts **will be removed** in future releases and its use is **not recommended** for new development.

## Scripting availability

Scripting is currently available only within [User Business Rules](../user-business-rules/index.md).

Support for additional modules, where scripting will be available, is planned for future releases.

## Script access scope

What a script can access depends on where it is executed within the system. In most cases, scripts have access to the **[Domain Model](./domain-model/index.md)**, allowing you to read, create, and update entities.

Additionally, scripts always have access to the **[Global action object](./global-action-object/index.md)**- helper that provides quick access to commonly used actions.

The available objects and data may vary depending on the specific context in which the script runs.

Always refer to the documentation for your script's entry point to see exactly what is accessible in that environment.

[!include[Getting started](features.md)]

[!include[Getting started](getting-started.md)]

## Next steps

- **[Execution context](./execution-context/index.md)**
- **[Accessing Domain Model](./domain-model/index.md)**
- **[Global action object](./global-action-object/index.md)**
- **[Limitations and best practices](./limitations-best-practices.md)**
- **[JavaScript examples](https://github.com/erpnet/JavaScriptExamples)**