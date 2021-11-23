---
uid: aggregates
---

# Aggregates

Aggregates are patterns in domain-driven design. A DDD aggregate is a cluster of domain objects that can be treated as a single unit. 

For an order and its line-items, aggregates will be separate objects, but it's useful to treat them as a single aggregate. Learn more **[here](https://martinfowler.com/bliki/DDD_Aggregate.html)**.

#### In @@name, these are single aggregates:

- a SalesOrder
- the sales order lines of this sales order
- the distributed amounts for each of these sales order lines
- the document amounts of this sales order
- the payment plan of this sales order

### Parent and root objects

Each object in an aggregate can have a parent object. The parent is the logical "owner" of the child object(s).

For example:

- The parent of a sales order line is sales order.
- The parent of a distributed amount is the sales order line.

The ultimate object, which has no parent in the aggregate, is the **aggregate root**. Here, this is the sales order.


### Aggregate events

The **Commit** and **ClientCommit** events are now available in two different variations:

- object commit / client-commit
- aggregate commit / alient-commit

#### What's the difference?

When an object commit event occurs, it means the object itself was changed. The aggregate event occurs for the object when there's a change in **ANY** of its constituent objects, but only if the object is an aggregate root.

Let's take a look at the following structure, which is a single aggregate in @@name:

- a SalesOrder (which is the aggregate's root)
- the sales order lines of this sales order
- the distributed amounts for each of these sales order lines
- the document amounts of this sales order
- the payment plan of this sales order

The **Commit** event would occur for the sales order **only** if the sales order object itself has changed. 

The **aggregate commit** will occur for the sales order if **any** of the objects in the aggregate has changed. Changing just a single sales order line without changing the order itself would **still** trigger the sales order aggregate event.

> [!NOTE] 
> 
> Commit and client-commit have the same meaning. Commit is the low-level event, which is triggered for everything committed to the database. Client-commit is triggered only based on client requests and is considered the more light-weight approach.<br>
> Currently, only the agregate client commit event is available for **[user-defined business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)**. <br> The aggregate commit will be used only internally, for **[system-defined business rules](xref:system-business-rules)**

The end goal is to have a more light approach. 

#### See also: 

@Systems.Core.ExtensibleDataObjects

