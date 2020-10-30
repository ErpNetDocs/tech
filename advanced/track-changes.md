---
uid: track-changes
---

# Track Changes

Track Changes is a system in EnterpriseOne, which can be used to track the changes in any data table.

## Configuring Track Changes

The Track Changes functionality is activated through the Entity Types table.

Steps:

- 1. Create a record in Entity Types, specifying the desired entity.
- 2. In the Track Changes Level field, fill the desired tracking level.
- Save and close.

The tracking will shortly start.

For document entities is provided an opportunity for mass activation of the Track Changes system using the DocumentVersioningSystem registry key. For more information see the description key number 42 in the @(Config Options Reference) topic.

## Tracking Levels

The tracking levels specify the detail level of the tracking, as per the following table:


| Track Changes Level | Name | Description |
| -- | --- | -------------------------------------- |
| 4 |Track Object, Attribute & BLOB Changes | All the data of Level 3 
+ 
Changes in the values of BLOB attributes.|
|   |                                       | +                                         |
|   |                                       | Changes in the values of BLOB attributes. |
| -- | --- | -------------------------------------- |
| 3 | Track Object & Attribute Changes |  All the data of Level 2 + Information about the changes in the attributes, excluding the BLOB attributes. The BLOB (Binary Large Objects) attributes are large size attributes like images, files, etc.|
| 2 | Track Object Changes| All the data of Level 1 + General tracking information about each update of the object. Do not store information about the changes in the attributes. |
| 1 | Track Last Change | Store information only for the latest modification of the tracked object. |
| 0 | Do Not Track Changes | Do not track any changes for this entity. |


## Effects And Storage

The system stores information based on the tracking level. The following table summarizes the stored data and other considerations and remarks:


