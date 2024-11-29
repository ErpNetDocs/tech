---
items: UserBusinessRuleExamples
---

# How to send a message to Azure Service Bus when an entity is created or updated?

To be able to send a message to Azure Service Bus you need to have a:
* [Webhook template](https://docs.erp.net/model/entities/Systems.Core.WebHooks.html) set up according to the service bus endpoint.
* [User business rule](../index.md) configured to trigger when an entity object of specific type is created or updated.
* The user business rule must define an [action of type WEBHOOK](../action-types/webhook.md), pointing to the code of the webhook template.

> [!NOTE]
> 
> For the purposes of the example, the [ServiceActivities](https://docs.erp.net/model/entities/Applications.Service.ServiceActivities.html) entity is used, but you can do it with any entity of your needs.

## Webhook template

Below is an example of what the webhook template should contain.

| Attribute name  | Attribute value                                             |
| --------------- | ----------------------------------------------------------- |
| Code            | sb_service_activity_01                                      |
| Name            | Azure Service Bus - service activity updates                |
| Repository name | Applications.Service.ServiceActivities                      |
| URL             | https://\<serviceNamespace\>.servicebus.windows.net\<queuePath \| topicPath\>/messages |
| Body            | <pre>{{<br/>    "Id": "{Id}",<br/>    "Number": "{DocumentNo}",<br/>    "Date": "{DocumentDate}",<br/>    "Subject": "{Subject}",<br/>    "State": "{State}"<br/>}}</pre> |
| Headers         | Authorization: \<authorizationToken\> |
| Notes           | Sends a message to Azure Service Bus queue when a service activity is created or updated. |

Where, 

* **\<serviceNamespace\>**, **\<queuePath\>** OR **\<topicPath\>** are specific to your service bus endpoint's configuration.

* **\<authorizationToken\>** as the name suggests, is an authorization token that can be:
	* **Azure AD JWT token** - in case registration of an application.<br/>
	`Authorization: Bearer <Azure AD JWT token>`

	* **SAS token** - in case of a shared access key.<br/>
	`Authorization: SharedAccessSignature sr=<NAMESPACE NAME>.servicebus.windows.net&sig=<SIGNATURE>&se=<TOKEN EXPIRY INSTANT>&skn=<SHARED KEY NAME>`,<br/><br/>
	where the **\<SIGNATURE\>** is to be calculated as follows (pseudocode):<br/><br/>
	`urlencode(base64(hmacsha256(urlencode('https://<NAMESPACE NAME>.servicebus.windows.net/') + "\n" + '<TOKEN EXPIRY INSTANT>', '<SHARED ACCESS KEY>')))`<br/><br/>
	For how you can generate a SAS token in different programming languages, visit the following link: [Generate SAS token](https://docs.microsoft.com/en-us/rest/api/eventhub/generate-sas-token)

* The **Body** is an interpolated string, formed in JSON format. When evaluated, it will contain the data for the entity in the context of which the business rule is executed.

## User business rule

The webhook template can't be used as a standalone thing. This is simply a template that in this particular case must be evaulated in the context of a service activity when the latter is created or updated. Therefore, a user business rule needs to be defined.

|Repository|
|:----|
|Applications.Service.ServiceActivities|

|Events|
|:----|

|Event type|Event parameter|Execution priority|
|:----|:----|:----|
AGGREGATECLIENTCOMMIT| |Normal|

|Actions|
|:----|

|Action No|Action type|Parameter1 type|Parameter1 value|
|:----|:----|:----|:----|
|1|WEBHOOK|Constant|sb_service_activity_01|

This seems pretty straightforward. A business rule that will trigger on **AGGREGATECLIENTCOMMIT** event and will execute a **WEBHOOK** action with code *sb_service_activity_01*.

-------------
## See more

- **[User business rules](../index.md)**
- **[String interpolation](../../string-interpolation/index.md)**
- **[Service Bus service REST / Send messages to queue](https://docs.microsoft.com/en-us/rest/api/servicebus/send-message-to-queue)**
- **[Authentication with Shared Access Signatures](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-sas#generate-a-shared-access-signature-token)**
- **[Generate SAS token](https://docs.microsoft.com/en-us/rest/api/eventhub/generate-sas-token)**
- **[Authenticate from an application](https://docs.microsoft.com/en-us/rest/api/servicebus/get-azure-active-directory-token)**