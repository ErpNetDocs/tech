## API Reference

### Methods

#### `Action.log(message: string): void`

Logs an informational message.

* **Creates:** [Information Message](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html) (type: `Information`)

```js
Action.log("Order completed.");
```

---

#### `Action.error(message: string): void`

Logs an error message.

* **Creates:** [Information Message](https://docs.erp.net/model/entities/Systems.Monitoring.InformationMessages.html) (type: `Error`)

```js
Action.error("Order validation failed.");
```

---

#### `Action.cancel(message?: string): void`

Cancels script execution and throws an exception.

* **Parameter:** `message` (optional) – Reason for cancellation
* **Effect:** Halts execution immediately

```js
Action.cancel("This operation is not permitted.");
Action.cancel(); // Uses a generic message
```

---

### Properties

#### `Action.notify`

Notification helpers.

##### `Action.notify.user(userId: string, message: string): void`

Sends a notification to a specific user.

```js
Action.notify.user("6dc7e681-8b65-4095-beb1-b3bc0c948b7c", "Please review this document.");
```

---

#### `Action.user`

Read-only object with information about the current user.

| Property | Type   | Description                |
| :------- | :----- | :------------------------- |
| `id`     | string | User ID                    |
| `name`   | string | Display name               |
| `roles`  | string | Comma-separated role names |
| `locale` | string | Default language code      |
| `email`  | string | Email address              |

```js
var userId = Action.user.id;
var roles = Action.user.roles;
```

---

#### `Action.session`

Read-only object with information about the current session.

| Property    | Type   | Description                     |
| :---------- | :----- | :------------------------------ |
| `id`        | string | Session ID                      |
| `startedAt` | string | ISO 8601 UTC session start time |

```js
var sessionId = Action.session.id;
var start = Action.session.startedAt;
```

---

#### `Action.http`

HTTP request helpers.

##### `Action.http.get(url: string, headers?: string): string`

Sends an HTTP GET request.

```js
var response = Action.http.get("https://api.example.com/status");
var response2 = Action.http.get(
  "https://api.example.com/status",
  "Authorization: Bearer TOKEN"
);
```

##### `Action.http.post(url: string, body: string, headers?: string): string`

Sends an HTTP POST request with a request body and optional headers.

```js
var response = Action.http.post(
  "https://api.example.com/data",
  '{ "value": 42 }',
  "Content-Type: application/json\nAuthorization: Bearer TOKEN"
);
```

---

### Summary Table

| Property/Method                          | Description                              |
| ---------------------------------------- | ---------------------------------------- |
| `Action.log(message)`                    | Log informational message                |
| `Action.error(message)`                  | Log error message                        |
| `Action.cancel([message])`               | Cancel script execution                  |
| `Action.notify.user(userId, message)`    | Send notification to user                |
| `Action.user`                            | Current user information                 |
| `Action.session`                         | Current session information              |
| `Action.http.get(url, [headers])`        | Send HTTP GET request                    |
| `Action.http.post(url, body, [headers])` | Send HTTP POST request with body/headers |