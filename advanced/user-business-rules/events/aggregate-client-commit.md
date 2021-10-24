
# Aggregate client commit

## Event summary 

|Name|AGGREGATECLIENTCOMMIT
|:----|:-----
|**Layer**| Back-End
|**Description**| Occurs for the aggregate root when saving a change of an aggregate object, but only when the change is made by a client application. If the change is made by the server, the event will not be triggered.
|**Version**| Introduced: 2019.1, Updated:-


The Aggregate Client Commit event is introduced in version 2019.1 and is a variation of the [Client commit](https://docs.erp.net/tech/advanced/user-business-rules/events/client-commit.html) event. It allows triggering user business rules for objects which are an aggregate root, not only when there is a change for the object itself, but also when some of its referent objects are edited . 

For more information about the aggregate's root, see [Aggregates](https://docs.erp.net/tech/advanced/concepts/aggregates.html).

Let's take a look at the following structure which is one single aggregate in @@name :
- a sales order (which is the aggregate's root)
- the Sales Order lines of this sales order
- the distributed amounts for each of these Sales Order lines
- the document amounts of this sales order
- the payment plan of this sales order

In the example above, the [Client commit](https://docs.erp.net/tech/advanced/user-business-rules/events/client-commit.html)** event would occur for the sales order only if the sales order object itself has changed. While the aggregate client commit will occur for the sales order if any of the objects in the aggregate has changed. For example, changing just a single sales order line (without changing the sales order itself) would still trigger the Sales Order 
Aggregate event.


**In summary, a user business rule with an Aggregate Client Commit event will be triggered when:**

- the saving is performed by a client application;
- as the repository of the user business rule is an entity which is an aggregate root;
- there is a change for the aggregate root or for some of its constituent objects.
