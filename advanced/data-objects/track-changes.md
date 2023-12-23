uid: track-changes
---

# Track Changes

Track Changes is a system in @@name which can be used to track changes in а data table.


## Tracking levels

**[Тracking levels](https://docs.erp.net/tech/advanced/data-objects/default-tracking-levels.html)** specify the detail level of the tracking, as per the following table:

| Level | Name | Description |
| -- | ------------------------------- | ---------------------------------------------|
| 0 | Do not track changes | Do not track any changes for this entity. |
| 1 | Track last change | Stores information for latest modification of the tracked object. |
| 2 | Track object changes| All the data of Level 1 <br> + <br> General tracking information about each update of the object. <br> Does not store information about the changes in the attributes. |
| 3 | Track object & attribute changes |  All the data of Level 2 <br> + <br> Information about the changes in the attributes, excluding BLOB attributes. These are large-size attributes like images, files, etc.|
| 4 | Track object, attribute & BLOB changes | All the data of Level 3 <br> + <br> Changes in the values of BLOB attributes.                |


## Effects and storage

The system stores information based on tracking level. 

The following topics summarize the stored data as well as other considerations and remarks:

### Level 0 - do not track changes. 

No information is stored.

### Level 1 - track last change

This is the lightest tracking mode with least storage requirements. Information is stored only for the latest modification, in **@Systems.Core.ExtensibleDataObjects**.

> [!NOTE] 
> 
> An **[extensible data object](https://docs.erp.net/tech/advanced/data-objects/edo.html)** is created and maintained ONLY for the root object of the **[aggregates](https://docs.erp.net/tech/advanced/concepts/aggregates.html)**. <br>
> Upon first update of the tracked object, a new EDO record is created, if there isn't already one. <br>
> For each successive update of an object in the aggregate, the data in the EDO is updated.

The tracking data includes:

- **Version number** - incremented on each update
- **Creation user** - the user who initially created the tracked object (if the Track Changes system was enabled by that time).
- **Creation time (UTC)** - the time of initial creation in Universal Coordinated Time (UTC) timezone.
- **Last update user** - the user who performed the last update OR deleted the object.
- **Last update time (UTC)** - the time of the last update.
- **Is deleted** - specifies whether the tracked object is deleted. 

After the tracked object is deleted, the **EDO** information stays in the database for some time, but can be purged by cleanup processes. The deletion user & time are stored in **Last update user** / **Time**.

### Level 2 - track object changes

Here, the extensible data object is still updated, but for each modification, a new record is created in two tables:

1. **@Systems.Core.ObjectChangesets** contains data about change-sets.

A change-set is a modification request sent to the server. 

One request can contain modifications (creates/updates/deletes) of multiple objects. 

Each change-set stores the following data:

- **User** - the user who initiated the server request.
- **Time** (UTC) - server time in UTC showing when the request was executed.
- **Application** - the name of the client application which executed the request.
- **Server version** - the version of the server by the time the request was executed.

2. **Object changes** stores one row for each modified object. 

One change-set can contain data about multiple object changes. 

The following data is stored:

- **Repository name** - the name of the repository containing the object.
- **Entity item id** - the Id of the tracked object.
- **Change type** - the type of modification: C, U or D for Create/Update/Delete.
- **Root object id** - the Id of the EDO for the root object of the aggregates.

### Level 3 - track object & attribute changes

When this level is selected, all data from Level 2 is still stored and maintained. 

But now, data about each attribute (field) change is also kept.

> [!NOTE] 
> 
> This level can consume A LOT of disk space. Use it only when absolutely necessary. <br> Also, make sure to setup some cleanup process (integrated or external).

**Attribute changes** stores the following data about each attribute change:
 
- **Attribute name** - the name of the changed attribute.
- **New value** - the string representation (culture insensitive) of the new value.

Some attribute changes might not be reflected properly by the system. Since it works at application level, changes made by direct SQL statements will **not** be recorded. When a future update occurs, the system will record the changes to the attribute as if they're being made by the next update. This behavior is part of its core design.

The *Document No* attribute (set by SQL statements) is often recorded as changed by the **2nd** modification of the document. Therefore, only the **new** values are stored. 

This design was chosen for the following reasons:

- Both old values AND new values are **not** stored to save space.

- If only old values are stored, the track-changes algorithm can save some space, but performance **will** suffer. Initial object creation doesn't need to store values. 
 
This was the initial and **abandoned** implementation of the track changes system. 

The process needed to synchronously read the previous database value before each update. This slowed down database transactions - the **'new values only'** approach was better fit to meet performance requirements.

- The storage of new values can be performed asynchronously **AFTER** the actual database transaction has completed. In this way, the TC system has minor effect on the speed of every-day OLTP transactions.

- One drawback of asynchronous saving: upon server crash, track-changes data about the attribute changes might be **lost**. The object change will still be recorded **synchronously** (as part of the transaction).

### Level 4 - track object, attribute & BLOB changes

Same as Level 3, but the values of BLOB attributes are also saved. 

It can severely affect storage requirements and should be used only for small tables and as last-resort measure.

## Configuring track changes

The track-changes functionality is activated through the **Entities navigator** (Systems.Core.EntitySettings table).

**Steps:**
 
1. Create a record in *Entity Types*, specifying the desired entity.
2. In the *Track Changes Level* field, fill the desired tracking level.
3. Save and close.
4. Tracking will soon start.

For document entities, mass activation of the *Track Changes* system using the **DocumentVersioningSystem** registry key is possible. To learn more, see the description key number 42 in **[Config options reference](https://docs.erp.net/tech/reference/config-options-reference.html)**.

> [!NOTE] 
> 
> If you try to configure a level lower than the default tracking levels, the option will be ignored.

### Enable or disable attributes change tracking

You can configure one of three **rules** which determine how field changes are tracked in a certain document type.

For instance, if you create a sales order, any subsequent changes to its fields may be collected in a dedicated **Change History** panel, allowing you to see technical details about each modification as well as which user made them.

This may be useful for contracts and other field-sensitive documents but may result in unnecessary accummulation of data if not needed. 

#### Track Attribute Changes rules

Within the **Track Attribute Changes** field of a document type configuration, it is possible to enforce one of the following rules:
 
- **Default** - Allows all changes within the particular document type to be tracked. **Does not** apply if the document is transitional.
- **Force Enable** - Allows all changes to be tracked **regardless** of whether the document is transitional or not.
- **Force Disable** - Prevents the ability for changes to be tracked.

> [!NOTE]
> If you create an **adjustment document** for the purpose of correcting a field in an existing document, changes **will not** be tracked regardless of the **Track Attribute Changes** field configuration.
