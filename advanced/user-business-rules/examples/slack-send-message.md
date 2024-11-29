---
items: UserBusinessRuleExamples
---

# How to send a message in a channel in Slack when voiding a sales order?

The following is required to send a message in Slack when а sales order is voiding:
* [Webhook template](https://docs.erp.net/model/entities/Systems.Core.WebHooks.html) set up according to the endpoint in Slack REST API.
* [User business rule](../index.md) configured to execute when a sales order is voiding.
* The user business rule must define an [action of type WEBHOOK](../action-types/webhook.md), pointing to the code of the webhook template.

## Webhook template

Below is an example of what the webhook template should contain.

| Attribute name  | Attribute value                                             |
| --------------- | ----------------------------------------------------------- |
| Code            | slack_void_01                                               |
| Name            | Slack - voiding a sales order                               |
| Repository name | Crm.Sales.SalesOrders                                       |
| URL             | <span>https://</span>slack.com/api/chat.postMessage?channel=\<channel\>&text=\<{DisplayText}\> |
| Headers         | Authorization: Bearer \<accessToken\>                       |
| Notes           | Sends a message in a Slack channel when a sales order is voiding. |

Where,

* **\<channel\>** - the Slack channel where the message will be sent.
* **{DisplayText}** - the message contents. It is also an interpolated string. It will be evaluated by @@name and will contain the display text of the sales order (e.g., *Sales Order 00108*). 
* **\<accessToken\>** - the access token provided from Slack.

> [!NOTE]
> 
> **Body** attribute is missing intentionally. It's not required.

## User business rule

А business rule that triggers when a sales order is voiding.

|Repository|
|:----|
|Crm.Sales.SalesOrders|

|Events|
|:----|

|Event type|Event parameter|Execution priority|
|:----|:----|:----|
|VOIDING||Normal|

|Actions|
|:----|

|Action No|Action type|Parameter1 type|Parameter1 value|
|:----|:----|:----|:----|
|1|WEBHOOK|Constant|slack_void_01|

-------------
## See more

- **[User business rules](../index.md)**
- **[String interpolation](../../string-interpolation/index.md)**
- **[Display format](../../data-objects/display-format.md)**
- **[Slack API Reference](https://api.slack.com/methods)**
- **[Slack access tokens](https://api.slack.com/authentication/token-types)**