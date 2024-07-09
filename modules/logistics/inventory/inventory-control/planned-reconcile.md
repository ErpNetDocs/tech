# Planned Reconcile

This section allows you to count and update the available product quantities of your inventory based on an existing reconciliation order.

It optimizes the inventory management process by allowing you to filter products by their product groups and a store. 

It further makes the process flexible by offering one of two reconciliation types.

**Planned reconciliation** is ideal for larger inventories where annual counts or planned audits are performed for individual stores and product groups. 

In contrast, **[Quick reconciliation](quick-reconcile.md)** is designed for fast, on-the-spot counts or even when minor discrepancies are observed. 

![pictures](pictures/planned_reconc.png)

### Prerequisites

Make sure you've set the correct document type for this operation within the **[Settings](settings.md)**.

You need to create a reconciliation order in order to use this module.

## Overview

Planned Reconcile is composed of three tabs:

* **Availability**
* **Counted**
* **Info**

### Availability

This is where all of your reconciliation order products are listed, together with their current quantities and lots, if present.

### Counted

Here, you can find how many quantities of the products have been **counted** as opposed to being **available** in total.

For example, out of 150pcs, only 131 may be present. This will be reflected in the reconciliation document.

### Info

If you tap on a product from the **Availability** tab, you'll be shown further information about it here. 

This includes revealing its part number and additional codes, if present, as well as counted quantities.

If more lots are present, the **available-counted** ratio will be distributed based on the FEFO principle.

## Scanning

In order to count the currently available quantities of your products, you need to use the **Scan** field.

It lets you quickly insert the instances of a product you want to **count** either manually or through **barcode commands**.

For a list of available barcode templates, check out the **[Command list](command-list.md)**.

If you're unfamiliar with the process of scanning a product and require assistance, refer to our **[overview](index.md)**.

### Higher count

The currently available pcs of a product may be **more** than what is set as available in the system.

You can update the number by providing the higher counted value, which will be reflected in the final reconciliation document.

### New count

If a product previously absent from the system is now available, you can **add** it by scanning it.

Its pcs will be reflected immediately, and once a reconciliation document is released, the **Available** bar will be updated with the new quantity.

### Zero count

You can enter a Zero quantity for the products that are missing from the store. 

Each zero count is interpreted as the product or lot having "0 pcs" in the final reconciliation document.

## Navigation 

To use **Planned Reconciliation**, go to **Logistics -> Inventory Control -> Planned Reconciliation**. 

![picture](pictures/Planned_Reconciliation_Navigation_09_07.png)

## Planned Reconciliation usage

Here are the steps required to perform a **Planned Reconciliation**.

### Create a Reconciliation document 

The reconciliation is for store reconciliations (physical counting), useful for real-world inventories, and establishing an opening balance.

#### Navigation 

Go to **Logistics -> Inventory -> Reconciliations -> Create Reconciliation**.

![picture](pictures/Planned_Reconciliation_Navigation_Reconciliations_09_07.png)

#### New Reconciliation 

To perform a reconciliation, you must fill in certain fields: **Default Store**, **Default Product Group**, and **Reconciliation Type**.

![picture](pictures/Planned_Reconciliation_Reconciliations_09_07.png) 

###### Reconciliation Type

There are two options for **Reconciliation Type**: **Full** and **Partial**. 

![picture](pictures/Planned_Reconciliation_Types_09_07.png) 

To proceed with a **Planned Reconciliation**, you must first select a product group. 

During the audit of this group, uncounted products will have their quantities set to zero in **Full Reconciliation**, while in **Partial Reconciliation**, their previous quantities will be retained.

[!]Note:
For a **Reconciliation** to appear in **Planned Reconciliations**, its status needs to be set to **planned**.
 
![picture](pictures/Planned_Reconciliation_Planned_08_07.png) 

### View Planned Reconciliations

When you navigate to **Planned Reconciliations** in **Inventory Control**, you will see a list of all upcoming reconciliations and those from the past week with the status set to **Planned**.

![picture](pictures/Planned_Reconciliation_Inventory_control_view_08_07.png) 

[!]Note: 
If a reconciliation has a product group, it will be named accordingly. If not, it will be named “-”.

![picture](pictures/Planned_Reconciliation_Name_08_07.png) 

### Planned Reconciliation Execution

Clicking on a reconciliation in the list will open the **Availability** tab. 

Here, you will find all products from the assigned product group in the storage. 

![picture](pictures/Planned_Reconciliation_Availability_08_07.png) 

If no product group is assigned, the entire storage availability will be shown.

![picture](pictures/Planned_Reconciliation_Availability_no_group_08_07.png) 

### Scan Products

To scan products, click on them and then click the arrow button.

> [!Note]
> For more information about how to scan a product, go to our article on the [subject]( https://docs.erp.net/tech/modules/logistics/wms/wms-worker/orders/scanning.html?q=scan)

![picture](pictures/Planned_Reconciliation_Scan_08_07.png) 

The info panel logs all scans, showing the time of each scan. 

![picture](pictures/Planned_Reconciliation_Time_08_07.png) 

You can also delete scans from this log if necessary.

![picture](pictures/Planned_Reconciliation_Delete_logs_08_07.png) 

> [!Note]
> You can see the scanned products in **Counted**.

![picture](pictures/Planned_Reconciliation_Counted_08_07.png) 

> [!Note]
> The platform retains information about ongoing **Planned Reconciliations** persistently, even if you navigate away from the page or close the platform entirely.

## Calculate reconciliation based on counts

The Calculate reconciliation based on the counts function consolidates product quantities from the Counts panel of a reconciliation order into summarized lines in the Lines panel.

It ensures that products counted in the same store and product group are either summed up or represented with a zero quantity, depending on the reconciliation type (Partial or Full).

For more information, please refer to this **[article](https://docs.erp.net/tech/modules/logistics/inventory/how-to/reconciliation-based-counts.html)**.

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.
