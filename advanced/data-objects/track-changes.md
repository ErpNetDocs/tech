---
uid: track-changes
---

# Track Changes

Track Changes is a system in @@name which can be used to track changes in а data table.


## Tracking levels

**[Тracking levels](https://docs.erp.net/tech/advanced/data-objects/default-tracking-levels.html)** specify the detail level of the tracking, as per the following table:

| Level | Name | Description |
| -- | ------------------------------- | ---------------------------------------------|
| 0 | Do not track changes | Do not track any changes for this entity. |
| 1 | Track last change | Stores information for the latest modification of the tracked object. |
| 2 | Track object changes| All the data of Level 1 <br> + <br> General tracking information about each update of the object. <br> Does not store information about the changes in the attributes. |
| 3 | Track object & attribute changes |  All the data of Level 2 <br> + <br> Information about the changes in the attributes, excluding BLOB attributes. These are large-size attributes like images, files, etc.|
| 4 | Track object, attribute & BLOB changes | All the data of Level 3 <br> + <br> Changes in the values of BLOB attributes.                |


## Effects and storage

The system stores information based on tracking level. 

The following topics summarize the stored data as well as other considerations and remarks:

### Level 0 - do not track changes. 

No information is stored.

### Level 1 - track last change

This is the lightest tracking mode with the least storage requirements. Information is stored only for the latest modification, in **@Systems.Core.ExtensibleDataObjects**.

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
- **Application** - the name of the client application that executed the request.
- **Server version** - the version of the server by the time the request was executed.

2. **Object changes** stores one row for each modified object. 

One change-set can contain data about multiple object changes. 

The following data is stored:

- **Repository name** - the name of the repository containing the object.
- **Entity item id** - the ID of the tracked object.
- **Change type** - the type of modification: C, U, or D for Create/Update/Delete.
- **Root object id** - the ID of the EDO for the root object of the aggregates.

### Level 3 - track object & attribute changes

When this level is selected, all data from Level 2 is still stored and maintained. But now, data about each attribute (field) change is also kept. 

When activated, stores the following data about each attribute change within the entity:
 
- **Attribute name** -The name of the attribute that was changed.
- **New value** - A culture-insensitive string representation of the updated value.

**Example:** `[Default Customer Credit Limit Base] set to BGN 20000.00`

Attribute changes for the record can be viewed through the **Changes History mode** in the @@name web client. The option is accessible from the Form Menu for each entity record definition.

> [!NOTE] 
> 
> This level can consume an increased amount of disk space. Use it only when necessary. <br> Additionally, ensure to set up some cleanup process (integrated or external).

Some attribute changes might not be reflected properly by the system. Since it works at the application level, changes made by direct SQL statements will **not** be recorded. When a future update occurs, the system will record the changes to the attribute as if they're being made by the next update. This behavior is part of its core design.  
Such an example is the *Document No* attribute (set by SQL statements) is often recorded as changed by the **2nd** modification of the document. 

Additionally, certain attributes have tracking disabled at the system level. This means that even if attribute tracking is enabled for a table, changes to specific attributes or fields will still not be recorded.  
Such an example is the *Last Interaction Time UTC* field in Social Groups. This field is designed to capture frequent updates from system processes. Enabling tracking for it would generate excessive load, potentially impacting system performance and stability.  

**Attribute changes storage and processing**

**Before v24:**  
- Each attribute change was stored as a separate entry in the `Sys_Attribute_Changes` table, leading to increased storage usage and performance overhead.  
- Record creation and updates were processed **synchronously**, which could slow down operations.

**As of v24:**  
- Attribute changes are now stored in the `Old_Values_Json` field within the `Sys_Object_Changes` table. To optimize storage, JSON data exceeding 50 characters is compressed.  
- Instead of logging changes synchronously, tracking operations are now processed **asynchronously** in the background, reducing performance impact on user operations.  

This resulted in major optimizations: attribute tracking time was reduced by approximately 64%, while storage usage saw a significant drop, with Sys_Attribute_Changes now taking up zero additional space-cutting storage needs by over 50%


### Level 4 - track object, attribute & BLOB changes

Same as Level 3, but the values of BLOB attributes are also saved. 

It can severely affect storage requirements and should be used only for small tables and as a last-resort measure.

## Configuring track changes

The track-changes functionality is activated through the **Entities navigator** (Systems.Core.EntitySettings table).

**Steps:**
 
1. Create a record in *Entity Types*, specifying the desired entity.
2. In the *Track Changes Level* field, fill in the desired tracking level.
3. Save and close.
4. Tracking will soon start.

For document entities, mass activation of the *Track Changes* system using the **DocumentVersioningSystem** registry key is possible. To learn more, see the description key number 42 in **[Config options reference](https://docs.erp.net/tech/reference/config-options-reference.html)**.

> [!NOTE] 
> 
> If you try to configure a level lower than the default tracking levels, the option will be ignored.

### Enable or disable attribute changes tracking for document entities

Tracking attributes changing history may be useful for invoices and other field-sensitive documents, but may result in unnecessary accumulation of data if not needed. Therefore, a specific configuration can be applied to each document type.

You can define how attribute (field) changes to be tracked for documents of a certain type through the **Track Attribute Changes** field in the document type definition.

Within the **Track Attribute Changes** field, it is possible to enforce one of the following **rules**:

•	**Default** - Allows attribute changes for the documents of the particular document type to be tracked. Does not apply if the document is transitional.

•	**Force Disable** - Prevents the ability for changes to be tracked.

•	**Force Enable** - Allows attribute changes to be tracked regardless of whether the document is transitional or not.


> [!NOTE]
> Regardless of the **Track Attribute Changes** field configuration:
> - attribute changes will not be tracked for adjustment documents
> - Level 1 and Level 2 tracking levels will continue to apply, so the data collected by them will be stored and available for review.
