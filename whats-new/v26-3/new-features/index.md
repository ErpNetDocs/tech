## Breaking Change

⚠️ **Desktop reports: Maximum row limit reduced to 200,000**

The maximum number of rows that can be requested in Desktop reports has been reduced from 1,000,000 to 200,000 to prevent excessive load on the server, network, and Desktop client.

If a higher value is entered in Filter field "Max row count", it is automatically reset to 200,000 and a notification is displayed. The same limit is also applied when opening saved views that contain a higher row limit.

<img width="325" height="96" alt="image" src="https://github.com/user-attachments/assets/57d710b2-9c62-4059-945e-9dae844ea4b3" />

## Other features

### 1. Update records directly from the navigator

A new ["Update records" function](https://docs.erp.net/webclient/navigators/guide/update-records.html) is now available in supported navigators, allowing you to update existing records or create new ones directly from the navigator with a single command. In Desktop client this is function "Merge".

The function compares the prepared rows with existing records using the entity's **primary key**. Matching records are updated with the new values, while rows with no matching record are created as new records.

This is especially useful when copying or importing predefined data into a navigator, enabling you to apply mass changes quickly and consistently without editing records one by one.

![picture](../pictures/update-success.png)
