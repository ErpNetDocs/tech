---
uid: aggregate-client-committed
---

# AGGREGATE CLIENT COMMITTED

<br />

|Name|AGGREGATECLIENTCOMMITTED
|:----|:-----
|**Layer**| Back-end
|**Description**| Occurs for the aggregate root after a change is made to an **[aggregate](../../concepts/aggregates.md)** object, but only when the change is made by a client application. If it's made by the server, the event won't be triggered.
|**Version**| Introduced: 2023 <br /> Updated:-

This event is a variation of the **[CLIENT COMMITTED](./client-committed.md)** event. It allows triggering **[user business rules](../index.md)** for objects which are an aggregate root. This can happen when there's a change for the object itself and/or when some of its referenced objects are edited. 

**Let's take a look at the following structure - a single aggregate in @@name:**

- sales order (which is the aggregate's root)
- sales order lines of this sales order
- distributed amounts for each of these sales order lines
- document amounts of this sales order
- payment plan of this sales order

In the example above, a CLIENT COMMITTED event would occur for the sales order **only** if its object has changed. The AGGREGATE CLIENT COMMITTED will occur if **any** of the objects in the aggregate have changed. Changing just a single sales order line without changing the order itself **still** triggers the aggregate event.

**In summary, a user business rule with an aggregate client committed event will be triggered when:**

- the saving was performed by a client application;

- the repository of the user business rule is an aggregate root entity;

- there's a change for the aggregate root or for some of its objects, part of the aggregate tree.

> [!NOTE]
> 
> The main difference with the "AGGREGATECLIENTCOMMIT" event is that AGGREGATECLIENTCOMMITTED occurs **after** the actual commit. I.e. if AGGREGATECLIENTCOMMITTED triggers, there's a guarantee that the entity **is** already saved and exists in the database.