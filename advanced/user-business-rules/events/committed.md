---
uid: committed
items: events
---

# COMMITTED

<br />

|Name|COMMITTED
|:----|:----
|**Layer**|Back-end
|**Description**|Occurs after an object change is saved.
|**Version**|Introduced: 2023 <br/> Updated: -

This event occurs after data is actually **saved** into a database. It's used for all kinds of data types - definitions, documents and more. After an object change is saved, the rule is activated, as long as it meets the conditions.

**COMMITTED** can be used for scenarios where you want to notify that an object has been created or modified. E.g. to send an [email](../action-types/sendmail.md), [notification](../action-types/notifyuser.md) or a [webhook](../action-types/webhook.md).

> [!NOTE]
> 
> The main difference with the "COMMIT" event is that COMMITTED occurs **after** the actual commit. I.e. if COMMITTED triggers, there's a guarantee that the entity **is** already saved and exists in the database.