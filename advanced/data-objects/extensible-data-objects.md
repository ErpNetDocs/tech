---
uid: extensible-data-objects
---

# Extensible Data Objects EDO

## Description and usage

The Extensible Data Objects (EDO) is a system in @@name, which allows attaching additional data to all entities in the system.

Types of additional data, which can currently be attached:

- file attachments.
- [Track changes](https://docs.erp.net/tech/advanced/data-objects/track-changes.html) change tracking data.

## How it works?

EDO objects are stored in the **Sys_Objects** entity. The system works in the following way:

- An object in any entity requires attaching additional data.
- A new record is created in Sys_Objects.
- The additional data is created in sub-tables, which have referential integrity to Sys_Objects.

The record in **Sys_Objects** has only untyped soft reference (not referential integrity) to the original record. It contains **Entity_Type** and **Entity_Item_Id** fields, which uniquely identify the original record.

All additional data is related to **Sys_Objects** through typed referential integrity. In this way, the only untyped soft reference is the original reference in **Sys_Objects**, but most data is solidly related through typed referential integrity.

> [!NOTE] 
> The [Custom attributes](https://docs.erp.net/tech/advanced/custom-attributes/index.html) system was implemented prior to the Extensible Data Objects system, so it also uses untyped soft reference.
> If we would have to design the Custom Properties system now, it would be implemented as 'additional data' to the EDO system.

## Future plans

The EDO system is very useful for creating additional data, which can be attached to multiple entities. It is not required that the type of data should be attachable to ALL entities.

The data model allows attaching data to any entity, but system business rules or [Business rules](https://docs.erp.net/tech/advanced/business-rules/index.md) can be used to limit the entities, which actually 'accept' the data.

Possible (planned) future uses:

- Comments/Replies - many objects in the system can be augmented by allowing the users to comment and reply to them.
- All kinds of attachments - links, pictures, other system objects, etc.
- Tags/Labels for back-link navigation.
- Future simplified implementation of custom properties.
- Reactions - Facebook style reactions.
- Reviews - marketplace style reviews.

#### See also: @Systems.Core.ExtensibleDataObjects
