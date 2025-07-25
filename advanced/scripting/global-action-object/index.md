# Global action object

The Action object is a powerful, always-available global helper in the scripting environment.

It allows your scripts to log information, handle errors, communicate with users, access contextual data, and even interact with external systems.

The `Action` object is provided automatically to every script.

It exposes system helpers for:
- Logging messages and errors.
- Canceling execution with an error.
- Sending notifications to users.
- Getting current user/session information.
- Making HTTP requests

You do **not** need to import or instantiate anything - just use `Action` directly.

## Logging and messaging

### Logging information

You can log informational messages from your scripts using `Action.log()`.

Each call to `Action.log()` creates a new [Information Message](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html) with its [InformationMessageType](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html#informationmessagetype) set to `Information`.

```js
Action.log("Order " + subject.DocumentNo + " processed successfully.");
```

> [!NOTE]
>
> Logging with `Action.log()` is a best practice for tracking script execution, troubleshooting issues, or leaving operational notes in the system history.

### Logging errors

You can log error messages from your scripts using `Action.error()`.

This is useful for recording issues, failed validations, or other problems that occur during script execution.

```js
Action.error("Failed to validate order details.");
```

Each call to `Action.log()` creates a new [Information Message](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html) with its [InformationMessageType](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html#informationmessagetype) set to `Error`.

> [!NOTE]
>
> Logging errors is important for troubleshooting, audit trails, and understanding how and why business rules are enforced in scripts.

## Script cancellation

You can immediately stop the execution of a script using `Action.cancel()`.

This method throws a script-level exception, halting all further script processing and optionally providing a human-readable reason.

```js
Action.cancel("This operation is not allowed for this customer.");
```
The reason argument is optional. If you omit it, a generic cancellation message will be used:

```js
Action.cancel(); // The operation was canceled.
```

Canceling script execution is typically used to enforce business rules, prevent invalid operations, or stop processing when certain conditions are not met.

## Sending notifications

You can send notifications directly to specific users from your scripts using the `Action.notify.user()` method.

This is useful for alerting users about important events or tasks.

```js
// Send an immediate notification to a user by their ID
Action.notify.user("6dc7e681-8b65-4095-beb1-b3bc0c948b7c", "Your task requires attention.");
```

- The first argument is the user's unique identifier.
- The second argument is the message text that will be delivered to the user.

When you use `Action.notify.user()`, the system internally creates a new [Notification entity](https://docs.erp.net/model/entities/Systems.Core.Notifications.html) and delivers it immediately to the target user.

> [!NOTE]
>
> Make sure you use a valid user ID for the recipient. If the user doesn't exist or the ID is incorrect, an error will be raised and the notification will not be sent.

## User and session Info

The `Action` object provides easy access to information about the user executing the script and the current session context.

You can use this data for auditing, logging, personalization, or implementing advanced business rules.

### Current user

You can access details about the current user with the `Action.user` property:

```js
const userId = Action.user.id;         // The user's unique identifier
const name = Action.user.name;         // The user's display name
const roles = Action.user.roles;       // Comma-separated list of role names
const locale = Action.user.locale;     // The user's default language code
const email = Action.user.email;       // The user's email address (if available)
```

### Current session

Information about the current session is available via the `Action.session` property:

```js
var sessionId = Action.session.id;         // Unique session identifier
var startedAt = Action.session.startedAt;  // ISO 8601 UTC session start time (string)
```

> [!NOTE]
>
> These properties are read-only and reflect the user and session associated with the script execution context. If a property is unavailable, it will be returned as null.

## HTTP actions

The `Action.http` property lets your scripts interact with external web services by sending HTTP requests.

You can use it to call REST APIs, fetch data, or integrate with other systems.

### Sending HTTP GET requests

Use `Action.http.get()` to send an HTTP GET request to a specified URL and retrieve the response as a string.

```js
var response = Action.http.get("https://api.example.com/status");
```

Optionally, you can provide custom headers as a string (e.g., "Authorization: Bearer ..."):

```js
var response = Action.http.get("https://api.example.com/status", "Authorization: Bearer TOKEN");
```

### Sending HTTP POST requests

Use `Action.http.post()` to send an HTTP POST request with a specified request body.

```js
var response = Action.http.post(
    "https://api.example.com/data",
    "{ 'value': 42 }"
);
```

You can also include custom headers:

```js
var response = Action.http.post(
    "https://api.example.com/data",
    "{ 'value': 42 }",
    "Content-Type: application/json\nAuthorization: Bearer TOKEN"
);
```
This will send a POST request with both Content-Type and Authorization headers included.

> [!NOTE]
>
> Always format multiple headers as separate lines within the same string.

[!include[API Reference](api-reference.md)]