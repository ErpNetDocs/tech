# Global Action object

The maintained guide to `Action` logging, cancellation, current-user/session data, HTTP requests, notifications, and files is in the [Developer Documentation](https://docs.erp.net/dev/scripting/action/index.html).

Some actions depend on execution context; for example, `Action.notify.user` needs an entity context and is not available to transaction-context managed scripts. See the [Action API reference](https://docs.erp.net/dev/scripting/action/api-reference.html).
