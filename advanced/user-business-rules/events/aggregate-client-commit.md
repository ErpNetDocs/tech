---
uid: aggregate-client-commit
items: events
---

# AGGREGATE CLIENT COMMIT

<br>

|Name|AGGREGATECLIENTCOMMIT
|:----|:-----
|**Layer**| Back-end
|**Description**| Occurs for the aggregate root when saving a change of an **[aggregate](https://docs.erp.net/tech/advanced/concepts/aggregates.html)** object, but only when the change is made by a client application. If it's made by the server, the event won't be triggered.
|**Version**| Introduced: 2019.1, Updated:-

This event is a variation of the **[CLIENT COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/client-commit.html)** event. It allows triggering **[user business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** for objects which are an aggregate root. This can happen when there's a change for the object itself and/or when some of its referent objects are edited. 

**Let's take a look at the following structure - a single aggregate in @@name:**

- sales order (which is the aggregate's root)
- sales order lines of this sales order
- distributed amounts for each of these sales order lines
- document amounts of this sales order
- payment plan of this sales order

In the example above, a CLIENT COMMIT event would occur for the sales order **only** if its object has changed. The AGGREGATE CLIENT COMMIT will occur if **any** of the objects in the aggregate have changed. Changing just a single sales order line without changing the order itself **still** triggers the aggregate event.

**In summary, a user business rule with an aggregate client commit event will be triggered when:**

- the saving is performed by a client application;

- the repository of the user business rule is an aggregate root entity;

- there's a change for the aggregate root or for some of its constituent objects.
