# Planned Reconciliation 

In **ERP.net**, **Planned Reconciliation** optimizes inventory management by allowing users to efficiently organize and filter inventories based on their status (Planned, Firm Planned), store location, and recent dates. 

This feature enhances visibility and control, providing comprehensive details such as **Default Product Group**, **Document Number**, and **Document Date** directly within the inventory list.

**Planned Reconciliation** is ideal for comprehensive, scheduled inventories, such as annual counts or planned audits based on product groups. 

In contrast, **Quick Reconciliation** is designed for fast, on-the-spot counts or when discrepancies are observed. 

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

![picture](pictures/Planned_Reconciliation_Reconciliation_09_07.png) 

###### Reconciliation Type

There are two options for **Reconciliation Type**: **Full** and **Partial**. 

![picture](pictures/Planned_Reconciliation_Type_09_07.png) 

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

[!]Note:
For more information about how to scan a product, go to our article on the [subject]( https://docs.erp.net/tech/modules/logistics/wms/wms-worker/orders/scanning.html?q=scan)

![picture](pictures/Planned_Reconciliation_Scan_08_07.png) 

The info panel logs all scans, showing the time of each scan. 

![picture](pictures/Planned_Reconciliation_Time_08_07.png) 

You can also delete scans from this log if necessary.

![picture](pictures/Planned_Reconciliation_Delete_logs_08_07.png) 

[!]Note:
You can see the scanned products in **Counted**.

![picture](pictures/Planned_Reconciliation_Counted_08_07.png) 

[!]Note:
The platform retains information about ongoing **Planned Reconciliations** persistently, even if you navigate away from the page or close the platform entirely.

# Calculate reconciliation based on the counts

The "Calculate reconciliation based on the counts" function consolidates product quantities from the Counts panel of a reconciliation order into summarized lines in the Lines panel.

It ensures that products counted in the same store and product group are either summed up or represented with a zero quantity, depending on the reconciliation type (Partial or Full).

For more information, you can read our [article](https://docs.erp.net/tech/modules/logistics/inventory/how-to/reconciliation-based-counts.html) on the subject.

> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.
