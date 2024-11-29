---
uid: create-new
items: events
---

# CREATENEW

|Name| CREATENEW
|:----|:----
|**Layer**| Front-end
|**Description**| Occurs immediately after creating a new object.
|**Version**| Introduced: 2022 <br> Updated: -

This event occurs immediately after the following core events:
- The object creation
- Initialization of its system attributes

This is the earliest possible point in the object's life cycle.

A typical use case is when you need to initialize one or more object attributes with user-defined values.

> [!NOTE]
> The object has not yet been saved and has never been. I.e., its first commit is coming up.

-------------
## See more

- **[Set an initial attribute for a new sales order](../examples/sales-order-init-attribute.md)**