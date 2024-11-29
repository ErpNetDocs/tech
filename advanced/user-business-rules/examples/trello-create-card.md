---
items: UserBusinessRuleExamples
---

# How to create a card in Trello when a sales order has been released?

To successfully create a Trello card, you need the following:
* [Webhook template](https://docs.erp.net/model/entities/Systems.Core.WebHooks.html) set up according to the endpoint in Trello REST API.
* [User business rule](../index.md) configured to trigger when a sales order is released.
* The user business rule must define an [action of type WEBHOOK](../action-types/webhook.md), pointing to the code of the webhook template.

## Webhook template

Below is an example of what the webhook template should contain.

| Attribute name  | Attribute value                                             |
| --------------- | ----------------------------------------------------------- |
| Code            | trello_release_so_01                                        |
| Name            | Trello - released sales order                               |
| Repository name | Crm.Sales.SalesOrders                                       |
| URL             | <span>https://</span>api.trello.com/1/cards?idList=\<id_list\>&name={DisplayText}&key=\<yourKey\>&token=\<yourToken\> |
| Notes           | Creates a card in Trello when a sales order is released.    |

Where, 

* **\<yourKey\>** and **\<yourToken\>** - the API keys, provided from Trello.
* **\<id_list\>** - the Id of the list where the new card should be created.
* **{DisplayText}** - the name of the card. It is also an interpolated string. It will be evaluated by @@name and will contain the display text of the sales order (e.g., *Sales Order 00108*). 

> [!NOTE]
> 
> **Body** and **Headers** attributes are missing intentionally. They are not required.

## User business rule

А business rule that triggers when a sales order has been released.

|Repository|
|:----|
|Crm.Sales.SalesOrders|

|Events|
|:----|

|Event type|Event parameter|Execution priority|
|:----|:----|:----|
|STATECHANGED|RELEASED|Normal|

|Actions|
|:----|

|Action No|Action type|Parameter1 type|Parameter1 value|
|:----|:----|:----|:----|
|1|WEBHOOK|Constant|trello_release_so_01|


-------------
## See more

- **[User business rules](../index.md)**
- **[String interpolation](../../string-interpolation/index.md)**
- **[Display format](../../data-objects/display-format.md)**
- **[Trello API Introduction](https://developer.atlassian.com/cloud/trello/guides/rest-api/api-introduction/)**
- **[Trello REST API Reference](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)**