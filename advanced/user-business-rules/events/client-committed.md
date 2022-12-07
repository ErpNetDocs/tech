---
uid: client-committed
---

# CLIENT COMMITTED

<br />

|Name| CLIENTCOMMITTED
|:------|:------
|**Layer**|Back-end
| **Description**|Occurs after saving a change to an object, made by a client application. If the change is made by the server, this event won't be triggered.
| **Version**|Introduced: 2023 <br/> Updated: -

This event is a variation of **[COMMITTED](./committed.md)**. Both occur for a particular object from the repository of a **[user business rule](../index.md)** after an object change is saved. 

However, CLIENT COMMITTED is triggered **only** if the saving was initiated by a client application, such as @@name Windows Client or @@name Web Client. If an object is modified by the @@name server, the event **won't** be triggered. 

This is especially useful for data-sync scenarios when the external application have to be notified (e.g. via a [webhook](../action-types/webhook.md)) when an entity changes (or is created).