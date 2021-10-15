---
uid: track-changes
---

# Track changes

Track changes is a system in @@name, which can be used to track the changes in any data table.


## Tracking levels

The tracking levels specify the detail level of the tracking, as per the following table:


| Track changes level | Name | Description |
| -- | ------------------------------- | ---------------------------------------------|
| 0 | Do not track changes | Do not track any changes for this entity. |
| 1 | Track last change | Store information only for the latest modification of the tracked object. |
| 2 | Track object changes| All the data of Level 1 <br> + <br> General tracking information about each update of the object. <br> Do not store information about the changes in the attributes. |
| 3 | Track object & attribute changes |  All the data of Level 2 <br> + <br> Information about the changes in the attributes, excluding the BLOB attributes. <br> The BLOB (Binary Large Objects) attributes are large size attributes like images, files, etc.|
| 4 | Track object, attribute & BLOB changes | All the data of Level 3 <br> + <br> Changes in the values of BLOB attributes.                |


## Effects and storage

The system stores information based on the tracking level. The following topics summarizes the stored data and other considerations and remarks:

### Level 0 - do not track changes. 

No information is stored.

### Level 1 - track last change

Store information only for the latest modification.
This is the lightest tracking mode with the least storage requirements.
The information is stored in the @Systems.Core.ExtensibleDataObjects

> [!NOTE] 
> [Extensible Data Objects](https://docs.erp.net/tech/advanced/data-objects/extensible-data-objects.html) object is created and maintained ONLY for the root object of the object [Aggregates](https://docs.erp.net/tech/advanced/concepts/aggregates.html). 
> Upon first update of the tracked object, a new EDO record is created, if there isn't already one. 
> For each successive update of any object in the aggregate, the data in the EDO is updated.

The tracking data includes:

- **Version number** - incremented on each update
- **Creation user** - the user who initially created the tracked object (if *Track Changes* was enabled by that time).
- **Creation time (UTC)** - the time of initial creation in Universal Coordinated Time (UTC) timezone.
- **Last update user** - the user who performed the last update OR deleted the object.
- **Last update time (UTC)** - the time of the last update.
- **Is deleted** - specifies whether the tracked object is deleted. After the tracked object is deleted, the [Extensible Data Objects](https://docs.erp.net/tech/advanced/data-objects/extensible-data-objects.html) information stays in the DB for some time, but can be purged by cleanup processes. Please note, that when the tracked object is deleted, the deletion user & time are stored in the *Last update user / Time*.

### Level 2 - track object changes

With this level, the [Extensible Data Objects](https://docs.erp.net/tech/advanced/data-objects/extensible-data-objects.html) is still updated, but also, for each modification, a new record is created in two tables:

#### @Systems.Core.ObjectChangesets contains data about change-sets.

A change-set is one modification request, sent to the server. One request can contain modifications (creates/updates/deletes) of multiple objects. Each change-set stores the following data:

- **User** - the user, who initiated the server request.
- **Time** (UTC) - server time in UTC, when the request was executed.
- **Application** - the name of the client application, which executed the request.
- **Server version** - the version of the server by the time when the request was executed.

#### Object changes stores one row for each modified object. 

One change-set can contain data about multiple object changes. The following data is stored:

- **Repository name** - the name of the object repository, containing the object.
- **Entity item id** - the Id of the tracked object.
- **Change type** - the type of modification: C, U or D for Create/Update/Delete.
- **Root object id** - the Id of the [Extensible Data Objects](https://docs.erp.net/tech/advanced/data-objects/extensible-data-objects.html) for the root object of the [Aggregates](https://docs.erp.net/tech/advanced/concepts/aggregates.html).

### Level 3 - track object & attribute changes

When this level is selected, all the data for Level 2 is still stored and maintained. But now, also data about each attribute (field) change is also stored.

> [!NOTE] 
> This tracking level can consume A LOT of disk space. Use it only when absolutely necessary. Also, make sure to setup some cleanup process (integrated or external).

 **Attribute changes**- stores the following data about each attribute change:
 
- **Attribute name** - the name of the changed attribute
- **New value** - the string representation (culture insensitive) of the new value

Some attribute changes might not be 'sensed' correctly by the system. Since the track changes system works at the application level, changes made by direct SQL statements will not be recorded. When a next update occurs, the system will record the changes to the attribute like it is being made by the next update. This behavior is by design.

The most frequent effect of this behavior is that the *Document No* attribute (which is set by SQL statements and not by the
application layer) is recorded as being changed by the 2nd modification of the document. 

Only the new values are stored (not the old values). This design was chosen for the following reasons:

- We do not store both old values AND new values to save space.
- If only the old (and not the new) values are stored, the track changes algorithm can save some space (initial object creation do not need to store values), but performance suffers. This was the initial implementation of the track changes system, but it was abandoned. The track changes process needed to synchronously read the previous database value before each update. This slowed down the actual database transactions and it was decided that the 'new values only' approach would better fit the performance requirements.
- The storage of the new values can be performed asynchronously AFTER the actual database transaction has completed. In this way, the track changes system has very minor effect on the speed of the every-day OLTP transactions.
- One drawback of the asynchronous saving is that, upon server crash, the track changes data about the attribute changes might be lost. In this case, the Object Change will still be recorded, because it is recorded synchronously (as part of the transaction).

### Level 4 - track Object, attribute & BLOB changes

Same as Level 3, but the values of BLOB attributes are also saved. This can severely affect the storage requirements and should be used only for small tables and as last resort measure.

## Configuring track changes

The track changes functionality is activated through the @Systems.Core.EntitySettings table.
<br> Steps:

1. Create a record in *Entity Types*, specifying the desired entity.
2. In the *Track Changes Level* field, fill the desired tracking level.
3. Save and close.
4. The tracking will shortly start.

For document entities is provided an opportunity for mass activation of the *Track Changes* system using the **DocumentVersioningSystem** registry key. For more information see the description key number 42 in the [Config options reference](https://docs.erp.net/tech/reference/config-options-reference.html) topic.

> [!NOTE] 
> If you try to configure a level lower than the default tracking levels, the option will be ignored.

## Default tracking levels

[Default tracking levels](https://docs.erp.net/tech/advanced/data-objects/default-tracking-levels.html)

