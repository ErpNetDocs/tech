---
uid: brat-WEBHOOK
items: ActionTypes
---
 
# WEBHOOK

| Name             | WEBHOOK                                                      |
| ---------------- | ------------------------------------------------------------ |
| Description      |  Used for executing a [webhook](https://en.wikipedia.org/wiki/Webhook) using business rules. <br/><br/> The webhook to be executed must be an existing webhook template, part of the [Web Hooks](https://docs.erp.net/model/entities/Systems.Core.WebHooks.html) entity. **Parameter 1** specifies its code. <br/><br/> The WEBHOOK action type is executed asynchronously by the server with the limitations, listed in the section below [Key points and specific limitations](#key-points-and-specific-limitations). |
| Parameter 1      | **[WEBHOOK CODE]** - the code of the webhook to be executed. |
| Parameter 1 type | Constant (string)                                            |
| Parameter 2      | Not used                                                     |
| Parameter 3      | Not used                                                     |
| Examples         | See the [Example](#example) section below                    |
| Version          | Introduced in: 2022                                          |

## Compatible events chart

WEBHOOK is compatible with all events.

| Event type                                                     | Compatibility with WEBHOOK                                   |
| -------------------------------------------------------------- | ------------------------------------------------------------ |
| Client commit (e.g. [CLIENTCOMMIT](../events/client-commit.md), [AGGREGATECLIENTCOMMIT](../events/aggregate-client-commit.md)) | compatible |
| Client committed (e.g. [CLIENTCOMMITTED](../events/client-committed.md), [AGGREGATECLIENTCOMMITTED](../events/aggregate-client-committed.md)) | compatible |
| Document events - (e.g. [STATECHANGING](../events/statechanging.md), [STATECHANGED](../events/statechanged.md), [VOIDING](../events/voiding.md))| compatible |
| Commit (e.g. [COMMIT](../events/commit.md))                    | compatible                                                   |
| Committed (e.g. [COMMITTED](../events/committed.md))                    | compatible                                                   |
| Front-end (e.g. [CREATENEW](../events/create-new.md), ATTRIBUTECHANGING, ATTRIBUTECHANGED) | compatible |

### Example:

А **[business rule](../index.md)** executes a webhook when a service activity is created or updated.

| Repository                             |                 |                    |                  |
| -------------------------------------- | --------------- | ------------------ | ---------------- |
| Applications.Service.ServiceActivities |                 |                    |                  |
| **Events**                             |                 |                    |                  |
| Event type                             | Event parameter | Execution priority |                  |
| AGGREGATECLIENTCOMMIT                  |                 | Normal             |                  |
| **Actions**                            |                 |                    |                  |
| Action No                              | Action type     | Parameter1 type    | Parameter1 value |
| 1                                      | WEBHOOK         | Constant           | wh_01            |

The value of the WEBHOOK's Parameter1 is simply the code of the corresponding [Web Hook](https://docs.erp.net/model/entities/Systems.Core.WebHooks.html) entity.

| Name             | Value                                                      |
| ---------------- | ---------------------------------------------------------- |
| Code             | wh_01                                                      |
| Name             | Webhook 01                                                 |
| Repository name  | Applications.Service.ServiceActivities                     |
| URL              | http://my-external-system:12345/{EntityName}               |
| Body             | <pre>{{<br/>    "Id": "{Id}",<br/>    "Number": "{DocumentNo}",<br/>    "Date": "{DocumentDate}",<br/>    "Subject": "{Subject}",<br/>    "State": "{State}"<br/>}}</pre> |
| Headers          | <pre>User-Agent: @@name<br/>X-Auth-Token: my_security_token</pre>                                                      |
| Retry logic      | Retry up to 3 times                                        |
| Notes            | Sends a HTTP POST request to the target url, identifying the updated service activity. |

The table above shows the webhook template "behind" the code "wh_01". Note that the values for the URL and body properties are using string interpolation. And because a webhook is by definition just a HTTP POST request, you can see below what the HTTP message would look like, according to the examples above.

```
POST /Srv_Service_Activities HTTP/1.1
Host: my-external-system:12345
User-Agent: ERP.net
X-Auth-Token: my_security_token
Content-Length: 153

{
    "Id": "9b68c23b-e3bc-4aa3-a906-cfa83fe1cdfc",
    "Number": "00001",
    "Date": "12.01.2022",
    "Subject": "Test activity",
    "State": "New"
}
```

## Key points and specific limitations
* Each webhook is executed asynchronously by the server, by putting it in a queue (FIFO).
* Each ERP instance has its own queue, processed independently.
* There's an intentional pause of 1 second after the execution of each webhook before proceeding to the next one.
* A queue is capped of 1000 webhooks. Any webhook that would exceed it will be discarded.
* Only the first webhook discard event will be logged for a calendar day as a warning.
* Each webhook has a timeout of 10 seconds to get a response from the external system. 
* All HTTP response codes that are **not** in the range [200-299] (as well as the timeouts) are treated as errors and logged as such.
* There's a quota allowing logging up to 100 errors per calendar day.

> [!WARNING]
> 
> When a webhook action is triggered by events other than \*COMMITTED, the webhook is dispatched. However, at this point, the @@name **transaction is still in progress**.
>
> This means that the upcoming changes **haven't yet taken place**.
>
> Consequently, if your external application performs a READ operation, there's a chance that you're reading an outdated record— i.e., one that has not yet been physically committed.
>
> **The same applies when you CREATE and CHANGE the state of a document simultaneously, i.e., at once, especially when utilizing a [document generation procedure](../../document-flow/generation.md)**.
>
> A common approach is for your external application to implement an initial delay upon receiving the webhook, ensuring sufficient time for the entire process (i.e. the @@name transaction) to complete before proceeding with its subsequent actions.

-------------
## See more

- **[Webhook wiki](https://en.wikipedia.org/wiki/Webhook)**
- **[WebHooks entity](https://docs.erp.net/model/entities/Systems.Core.WebHooks.html)**
- **[String interpolation](../../string-interpolation/index.md)**
