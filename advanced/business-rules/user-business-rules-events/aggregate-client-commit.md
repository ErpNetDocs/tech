
# AGGREGATE CLIENT COMMIT

#### EVENT SUMMARY

|Name|AGGREGATECLIENTCOMMIT
|:----|:-----
|**Layer**| Back-End
|**Description**| Occurs for the aggregate root when saving a change of an aggregate object, but only when the change is made by a client application. If the change is made by the server, the event will not be triggered.
|**Version**| Introduced: 2019.1, Updated:-


The Aggregate client commit event is introduced in version 2019.1 and is a variation of the **[Client commit](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/user-business-rules-events/client-commit.md)** event. It allows triggering User business rules for objects which are an aggregate root, not only when there is a change for the object itself, but also when some of its referent objects are edited . 

For more information about the Aggregate's root, see **Aggregates**.

Let's take a look at the following structure which is one single aggregate in @@name :
- a Sales order (which is the aggregate's root)
- the Sales order lines of this Sales order
- the Distributed amounts for each of these Sales order lines
- the Document amounts of this Sales order
- the Payment plan of this Sales order

In the example above, the **[Client commit](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/user-business-rules-events/client-commit.md)** event would occur for the **Sales order** only if the Sales order object itself has changed. While the **Aggregate client commit** will occur for the **Sales order** if any of the objects in the aggregate has changed. For example, changing just a single Sales order line (without changing the Sales order itself) would still trigger the Sales order 

Aggregate event.


**In summary, a User business rule with an Aggregate client commit event will be triggered when:**

- the saving is performed by a client application;
- as the repository of the User business rule is an entity which is an aggregate root;
- there is a change for the aggregate root or for some of its constituent objects.
