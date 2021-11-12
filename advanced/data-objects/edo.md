---
uid: extensible-data-objects
---

# EDO

The Extensible data objects (EDO) is a system in @@name, which allows attaching additional data to all entities in the system.

The following can be attached:

- files
- **[Track changes](https://docs.erp.net/tech/advanced/data-objects/track-changes.html)** tracking data

## How it works?

Extensible data objects are stored in the **Sys_Objects** entity. The system works in the following way:

1. An object in an entity requires attaching additional data => A new record is created in Sys_Objects. 
2. Additional data is created in sub-tables which have referential integrity to Sys_Objects. 

The record in Sys_Objects has only untyped soft reference (not referential integrity) to the original record. <br> It contains the **Entity_Type** and **Entity_Item_Id** fields, which uniquely identify the original record. 

All additional data is related to Sys_Objects through **typed** referential integrity. 

Therefore, the only untyped soft reference is the original reference in Sys_Objects. <br> Most data is solidly related through typed referential integrity.

> [!NOTE] 
> 
> The **[Custom attributes](https://docs.erp.net/tech/advanced/custom-attributes/index.html)** system was implemented prior to the EDO system, so it also uses untyped soft reference. <br>
> If it was implemented now, it would be in the form of 'additional data' to the EDO system.

## Future plans

The EDO system is very useful for creating additional data which can be attached to multiple entities. 

It's **not** required for the type of data to be attachable to ALL entities.

The data model allows attaching data to any entity, but **[system business rules](https://docs.erp.net/model/templates/template-description-system-business-rules.html)** or **[business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** can be used to limit the entities which 'accept' the data.

Possible (planned) future uses:

- Comments/Replies - many objects in the system can be augmented by allowing users to comment and reply to them.
- All kinds of attachments - links, pictures, other system objects, etc.
- Tags/Labels for back-link navigation.
- Future simplified implementation of custom properties.
- Reactions - Facebook-inspired reactions.
- Reviews - Marketplace-inspired reviews.

#### See also:

**[@Systems.Core.ExtensibleDataObjects](https://docs.erp.net/model/entities/Systems.Core.ExtensibleDataObjects.html)**
