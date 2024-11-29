---
uid: client-commit
items: events
---

# CLIENT COMMIT

<br>

|Name| CLIENTCOMMIT
|:------|:------
|**Layer**|Back-end
| **Description**|Occurs when saving a change of an object, made by a client application. If the change is made by the server, the event won't be triggered.
| **Version**|Introduced: 2019.1  <br>Updated: -

This event is a variation of **[COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/commit.html)**. Both occur for a particular object from the repository of a **[user business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** when an object change is saved. 

However, CLIENT COMMIT is triggered **only** when the saving is initiated by a client application, such as @@name Windows Client. If an object is modified by the @@name server, the event **won't** be triggered. 

This could be used if, for example, you want the business rule to be executed when you're manually saving a document, but the system is currently saving the document after its creation with a **[generation procedure](https://docs.erp.net/tech/advanced/document-flow/generation-procedures.html)**.
