# CLIENT COMMIT
#### EVENT SUMMARY
|Name| CLIENTCOMMIT
|:------|:------
|**Layer**|**Back-End**
| **Description**|**Occurs when saving a change of the object, when the <br> change is made by a client application. If the change <br> is made by the server, the event will not be triggered.**
| **Version**|**Introduced: 2019.1  <br>Updated: -**

Thе event is a variation of the **COMMIT** and similar to it - it occurs for the particular object of the repository of the **User business rule** when an object change is saved. 

The difference is that it is triggered only when the saving is initiated by a client application, such as the @@name Windows Client. If the object is modified by the @@name server, then this event is not triggered. This could be used if, for example, we want the business rule to be executed when a user is manually saving a document, but the system is currently saving the document after its creation with a generation procedure.
 

