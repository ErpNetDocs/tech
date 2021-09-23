
# AGGREGATE CLIENT COMMIT

#### EVENT SUMMARY

|Name|AGGREGATECLIENTCOMMIT
|:----|:-----
|**Layer**| Back-End
|**Description**| Occurs for the aggregate root when saving a change of an aggregate object, but only when the change is made by a client application. If the change is made by the server, the event will not be triggered.
|**Version**| Introduced: 2019.1, Updated:-


The Aggregate Client Commit event is introduced in version 2019.1 and is a variation of the **[Client Commit](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-business-rules/events/client-commit.md)** event. It allows triggering User Business Rules for objects which are an aggregate root, not only when there is a change for the object itself, but also when some of its referent objects are edited . 

For more information about the Aggregate's root, see **Aggregates**.

Let's take a look at the following structure which is one single aggregate in @@name :
- a Sales Order (which is the aggregate's root)
- the Sales Order Lines of this Sales Order
- the Distributed Amounts for each of these Sales Order Lines
- the Document Amounts of this Sales Order
- the Payment Plan of this Sales Order

In the example above, the **[Client Commit](https://github.com/ErpNetDocs/tech/blob/master/advanced/user-business-rules/events/client-commit.md)** event would occur for the **Sales Order** only if the Sales Order object itself has changed. While the **Aggregate Client Commit** will occur for the **Sales Order** if any of the objects in the aggregate has changed. For example, changing just a single Sales Order Line (without changing the Sales Order itself) would still trigger the Sales Order 
Aggregate event.


**In summary, a User Business Rule with an Aggregate Client Commit event will be triggered when:**

- the saving is performed by a client application;
- as the repository of the User Business Rule is an entity which is an aggregate root;
- there is a change for the aggregate root or for some of its constituent objects.
