---
uid: aggregates
---

# Aggregates

## What are Aggregates?

"Aggregate is a pattern in Domain-Driven Design. A DDD aggregate is a cluster of domain objects that can be treated as a single unit. An example may be an order and its line-items, these will be separate objects, but it's useful to treat the order (together with its line items) as a single aggregate."

https://martinfowler.com/bliki/DDD_Aggregate.html

## Examples

For example, in @@name, this is one single aggregate:

- a SalesOrder
- the Sales Order Lines of this Sales Order
- the Distributed Amounts for each of these Sales Order Lines
- the Document Amounts of this Sales Order
- the Payment Plan of this Sales Order

## Parent And Root Objects

Each object in an aggregate can have a parent object.The parent is the logical "owner" of the child object(s).

For example:

- The parent of **Sales Order Line** is **Sales Order**.
- The parent of **Distributed Amount** is the **Sales Order Line**.

The ultimate object, which has no parent in the aggregate is the Aggregate Root. In this example, this is the **Sales Order**.


## Aggregate Events

The **Commit** and **ClientCommit** events are now available in two different variations:

1. Object Commit / Client-Commit
1. Aggregate Commit / Client-Commit

What is the difference?

When an object commit event occurs, it means that the object itself was changed. The aggregate event occurs for the object when there is a change in **ANY** of its constituent objects, but only if the objects is an aggregate root.

Lets take a look at the following structure which in EnterpriseOne is one single aggregate:

- a SalesOrder (which is the aggregate's root)
- the Sales Order Lines of this Sales Order
- the Distributed Amounts for each of these Sales Order Lines
- the Document Amounts of this Sales Order
- the Payment Plan of this Sales Order

In the example above, the **Commit** event would occur for the **Sales Order** if and only if the Sales Order object itself has changed. While the **Aggregate Commit** will occur for the Sales Order if any of the objects in the aggregate has changed. For example, changing just a single Sales Order Line (without changing the Sales Order itself) would still trigger the Sales Order Aggregate event.

> [!NOTE] 
> Commit and Client-Commit still have the same meaning. E.g., Commit is the low-level event, which is triggered for everything committed to the database (be it from client request or as a result of some server processing). While Client-Commit is triggered only based on client requests and is considered the more light-weight approach.

> [!NOTE] 
>Initially, only the Aggregate Client Commit event would be available for user-defined business rules [Business Rules](https://github.com/ErpNetDocs/tech/advanced/business-rules/overview.md). The Aggregate Commit will be used only internally, for system-defined business rules todo:(System Business Rules) 

The reason is to have a more light tread approach. If there is serious need, we can consider adding the Aggregate Commit event in the future for [Business Rules](https://github.com/ErpNetDocs/tech/advanced/business-rules/overview.md).

#### See also: @Systems.Core.ExtensibleDataObjects

