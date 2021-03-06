---
uid: track-changes
---

# Track Changes

Track Changes is a system in @@name, which can be used to track the changes in any data table.


## Tracking Levels

The tracking levels specify the detail level of the tracking, as per the following table:


| Track Changes Level | Name | Description |
| -- | ------------------------------- | ---------------------------------------------|
| 0 | Do Not Track Changes | Do not track any changes for this entity. |
| 1 | Track Last Change | Store information only for the latest modification of the tracked object. |
| 2 | Track Object Changes| All the data of Level 1 <br> + <br> General tracking information about each update of the object. <br> Do not store information about the changes in the attributes. |
| 3 | Track Object & Attribute Changes |  All the data of Level 2 <br> + <br> Information about the changes in the attributes, excluding the BLOB attributes. <br> The BLOB (Binary Large Objects) attributes are large size attributes like images, files, etc.|
| 4 | Track Object, Attribute & BLOB Changes | All the data of Level 3 <br> + <br> Changes in the values of BLOB attributes.                |


## Effects And Storage

The system stores information based on the tracking level. The following topics summarizes the stored data and other considerations and remarks:

### Level 0 - Do Not Track Changes. 

No information is stored.

### Level 1 - Track Last Change

Store information only for the latest modification.
This is the lightest tracking mode with the least storage requirements.
The information is stored in the @Systems.Core.ExtensibleDataObjects

> [!NOTE] 
> [Extensible Data Objects](extensible-data-objects.md) object is created and maintained ONLY for the root object of the object [Aggregates](~/advanced/concepts/aggregates.md)). 
> Upon first update of the tracked object, a new EDO record is created, if there isn't already one. 
> For each successive update of any object in the aggregate, the data in the EDO is updated.

The tracking data includes:

- **Version Number** - incremented on each update
- **Creation User** - the user who initially created the tracked object (if Track Changes was enabled by that time).
- **Creation Time (UTC)** - the time of initial creation in Universal Coordinated Time (UTC) timezone.
- **Last Update User** - the user who performed the last update OR deleted the object.
- **Last Update Time (UTC)** - the time of the last update.
- **Is Deleted** - specifies whether the tracked object is deleted. After the tracked object is deleted, the [Extensible Data Objects](extensible-data-objects.md) information stays in the DB for some time, but can be purged by cleanup processes. Please note, that when the tracked object is deleted, the deletion user & time are stored in the Last Update User / Time.

### Level 2 - Track Object Changes

With this level, the [Extensible Data Objects](extensible-data-objects.md) is still updated, but also, for each modification, a new record is created in two tables:

#### @Systems.Core.ObjectChangesets contains data about change-sets.

A change-set is one modification request, sent to the server. One request can contain modifications (creates/updates/deletes) of multiple objects. Each change-set stores the following data:

- **User** - the user, who initiated the server request.
- **Time** (UTC) - server time in UTC, when the request was executed.
- **Application** - the name of the client application, which executed the request.
- **Server Version** - the version of the server by the time when the request was executed.

#### Object Changes stores one row for each modified object. 

One change-set can contain data about multiple object changes. The following data is stored:

- **Repository Name** - the name of the object repository, containing the object.
- **Entity Item Id** - the Id of the tracked object.
- **Change Type** - the type of modification: C, U or D for Create/Update/Delete.
- **Root Object Id** - the Id of the [Extensible Data Objects](extensible-data-objects.md) for the root object of the [Aggregates](~/advanced/concepts/aggregates.md).

### Level 3 - Track Object & Attribute Changes

When this level is selected, all the data for Level 2 is still stored and maintained. But now, also data about each attribute (field) change is also stored.

> [!NOTE] 
> This tracking level can consume A LOT of disk space. Use it only when absolutely necessary. Also, make sure to setup some cleanup process (integrated or external).

**Attribute Changes** stores the following data about each attribute change:

- **Attribute Name** - the name of the changed attribute
- **New Value** - the string representation (culture insensitive) of the new value

Some attribute changes might not be "sensed" correctly by the system. Since the Track Changes system works at the application level, changes made by direct SQL statements will not be recorded. When a next update occurs, the system will record the changes to the attribute like it is being made by the next update. This behavior is by design.

The most frequent effect of this behavior is that the Document No attribute (which is set by SQL statements and not by the
application layer) is recorded as being changed by the 2nd modification of the document. 

Only the new values are stored (not the old values). This design was chosen for the following reasons:

- We do not store both old values AND new values to save space.
- If only the old (and not the new) values are stored, the track changes algorithm can save some space (initial object creation do not need to store values), but performance suffers. This was the initial implementation of the track changes system, but it was abandoned. The track changes process needed to synchronously read the previous database value before each update. This slowed down the actual database transactions and it was decided that the "new values only" approach would better fit the performance requirements.
- The storage of the new values can be performed asynchronously AFTER the actual database transaction has completed. In this way, the track changes system has very minor effect on the speed of the every-day OLTP transactions.
- One drawback of the asynchronous saving is that, upon server crash, the track changes data about the attribute changes might be lost. In this case, the Object Change will still be recorded, because it is recorded synchronously (as part of the transaction).

### Level 4 - Track Object, Attribute & Blob Changes

Same as Level 3, but the values of BLOB attributes are also saved. This can severely affect the storage requirements and should be used only for small tables and as last resort measure.

## Configuring Track Changes

The Track Changes functionality is activated through the @Systems.Core.EntitySettings table.
<br> Steps:

1. Create a record in Entity Types, specifying the desired entity.
1. In the Track Changes Level field, fill the desired tracking level.
1. Save and close.
1. The tracking will shortly start.

For document entities is provided an opportunity for mass activation of the Track Changes system using the **DocumentVersioningSystem** registry key. For more information see the description key number 42 in the [Config Options Reference](~/reference/config-options-reference.md) topic.

> [!NOTE] 
> If you try to configure a level lower than the default tracking levels, the option will be ignored.

## Default Tracking Levels

Some entities are configured by default to track their changes. The default tracking level is system configured and cannot be lowered. However, the users can specify higher tracking levels.

The following table contains the default system specified tracking levels.

| Entity | Default Tracking Level | Activated in version |
| -- | ------------------------------- | ---------------------------------------------|
| Entities | 3 | 2019.1 |
| Config | 3 | 2019.1 |
| Products | 2 | 2019.1 |
| Parties | 4 | 2019.1 |
| Companies | 3 | 2019.1 |
| Company Locations | 3 | 2019.1 |
| Persons | 3 | 2019.1 |
| Enterprise Companies | 3 | 2019.1 |
| Payment Types | 2 | 2019.1 |
| Payment Accounts | 2 | 2019.1 |
| POS Locations | 3 | 2019.1 |
| POS Terminals | 2 | 2019.1 |
| POS Operators | 3 | 2019.1 |
| POS Roles | 3 | 2019.1 |
| POS Sequences | 2 | 2019.1 |
| Users | 3 | 2019.1 |
| Groups | 3 | 2019.1 |
| User Groups | 3 | 2019.1 |
| Group Access Keys | 3 | 2019.1 |
| Document Types | 4 | 2019.1 |
| Printout Layouts | 4 | 2019.1 |
| Calculated Attributes | 3 | 2019.1 |
| User Business Rules | 3 | 2019.1 |


