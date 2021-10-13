---
uid: aggregates
---

# Aggregates

## What are аggregates?

'Aggregate is a pattern in domain-driven design. A DDD aggregate is a cluster of domain objects that can be treated as a single unit. An example may be an order and its line-items, these will be separate objects, but it's useful to treat the order (together with its line items) as a single aggregate."

https://martinfowler.com/bliki/DDD_Aggregate.html

## Examples

For example, in @@name, this is one single aggregate:

- a SalesOrder
- the sales order lines of this sales order
- the distributed amounts for each of these sales order lines
- the document amounts of this sales order
- the payment plan of this sales order

## Parent and root objects

Each object in an aggregate can have a parent object.The parent is the logical "owner" of the child object(s).

For example:

- The parent of **sales order line** is **sales order**.
- The parent of **distributed amount** is the **sales order line**.

The ultimate object, which has no parent in the aggregate is the aggregate root. In this example, this is the **sales order**.


## Aggregate events

The **Commit** and **ClientCommit** events are now available in two different variations:

1. object commit / client-commit
1. aggregate commit / alient-commit

What is the difference?

When an object commit event occurs, it means that the object itself was changed. The aggregate event occurs for the object when there is a change in **ANY** of its constituent objects, but only if the objects is an aggregate root.

Lets take a look at the following structure which in @@name is one single aggregate:

- a SalesOrder (which is the aggregate's root)
- the Sales order lines of this sales order
- the distributed amounts for each of these sales order lines
- the document amounts of this sales order
- the payment plan of this sales order

In the example above, the **Commit** event would occur for the **sales order** if and only if the sales order object itself has changed. While the **aggregate commit** will occur for the sales order if any of the objects in the aggregate has changed. For example, changing just a single sales order line (without changing the sales order itself) would still trigger the Sales order aggregate event.

> [!NOTE] 
> Commit and client-commit still have the same meaning. E.g., commit is the low-level event, which is triggered for everything committed to the database (be it from client request or as a result of some server processing). While client-commit is triggered only based on client requests and is considered the more light-weight approach.

> [!NOTE] 
>Initially, only the agregate client commit event would be available for user-defined business rules [business rules](~/advanced/business-rules/index.md). The aggregate commit will be used only internally, for system-defined business rules [System Business Rules](xref:system-business-rules) 

The reason is to have a more light tread approach. If there is serious need, we can consider adding the aggregate commit event in the future for [business rules](~/advanced/business-rules/index.md).

#### See also: @Systems.Core.ExtensibleDataObjects

