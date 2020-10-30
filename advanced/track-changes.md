---
uid: track-changes
---

# Track Changes

Track Changes is a system in EnterpriseOne, which can be used to track the changes in any data table.

## Configuring Track Changes

The Track Changes functionality is activated through the Entity Types table.

Steps:

- Create a record in Entity Types, specifying the desired entity.
- In the Track Changes Level field, fill the desired tracking level.
- Save and close.

The tracking will shortly start.

For document entities is provided an opportunity for mass activation of the Track Changes system using the DocumentVersioningSystem registry key. For more information see the description key number 42 in the @(Config Options Reference) topic.

## Tracking Levels

The tracking levels specify the detail level of the tracking, as per the following table:


| Track Changes Level | Name | Description |
| -- | ------------------------------- | ---------------------------------------------|
| 4 | Track Object, Attribute & BLOB Changes | All the data of Level 3 <br> + <br> Changes in the values of BLOB attributes.                |
| 3 | Track Object & Attribute Changes |  All the data of Level 2 <br> + <br> Information about the changes in the attributes, excluding the BLOB attributes. <br> The BLOB (Binary Large Objects) attributes are large size attributes like images, files, etc.|
| 2 | Track Object Changes| All the data of Level 1 <br> + <br> General tracking information about each update of the object. <br> Do not store information about the changes in the attributes. |
| 1 | Track Last Change | Store information only for the latest modification of the tracked object. |
| 0 | Do Not Track Changes | Do not track any changes for this entity. |


## Effects And Storage

The system stores information based on the tracking level. The following table summarizes the stored data and other considerations and remarks:

#### Level 0 - Do Not Track Changes. 

No information is stored.

#### Level 1 - Track Last Change

Store information only for the latest modification.

This is the lightest tracking mode with the least storage requirements.

The information is stored in the @(Extensible Data Objects (EDO)) entity (stored in the Sys_Objects table).

> [!NOTE] 
> EDO object is created and maintained ONLY for the root object of the @(object aggregate). 
> Upon first update of the tracked object, a new EDO record is created, if there isn't already one. 
> For each successive update of any object in the aggregate, the data in the EDO is updated.

The tracking data includes:

- Version Number - incremented on each update
- Creation User - the user who initially created the tracked object (if Track Changes was enabled by that time).
- Creation Time (UTC) - the time of initial creation in Universal Coordinated Time (UTC) timezone.
- Last Update User - the user who performed the last update OR deleted the object.
- Last Update Time (UTC) - the time of the last update.
- Is Deleted - specifies whether the tracked object is deleted. After the tracked object is deleted, the EDO information stays in the DB for some time, but can be purged by cleanup processes.Please note, that when the tracked object is deleted, the deletion user & time are stored in the Last Update User / Time.



