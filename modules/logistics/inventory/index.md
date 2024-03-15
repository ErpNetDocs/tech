# Inventory 

Inventory is designed to assist you in the process of inventory control and warehouse management.

It includes the ability to **create** various invoices, reconciliation documents and transfer orders, add **definitions** and utilize different **views**.

![picture](pictures/Inventory_view_21_02.png)

## Documents

#### Transactions 

In **Transaction** you can find the receipts for  your (warehouse’s existing) stores. **Store-Receipts** reflect incoming goods, while **Store-Issues** denote outgoing goods. 

Outgoing goods in Store-Issues are recorded with negative quantity values. Based on a **Purchase Order**, a receipt is generated. 

![picture](pictures/Inventory_Transactions_14_03.png)
 
#### Transfer Orders 

The **Transfer Orders** section facilitates seamless stock transfers between stores, offering detailed specifications and customizable workflows. 

It integrates with other panels for inventory management and provides real-time monitoring capabilities for proactive intervention when needed.

![picture](pictures/Inventory_Transactions_Orders_14_03.png)
 
#### Reconciliations

In the **Reconciliations** section, you can efficiently manage your stock availability. 

It generates receipt store transactions (+) and issue store transactions (-) based on variations between recorded stock levels and actual availability, reflecting the differences between stock levels and availability.

![picture](pictures/Inventory_Reconiciliations_14_03.png)
 
## Definitions 

#### Stores 

**Stores** represent the physical warehouses within your inventory management system. To utilize the inventory, you must define one or more stores to house your inventory.

![picture](pictures/Inventory_Stores_14_03.png)
 
#### Lots

Warehouse lots consist of individual entries for each distinct product, detailing its status, production batch, and specific warehouse conditions. 

The status of each lot can restrict certain operations within the warehouse.

![picture](pictures/Inventory_Lots_14_03.png)
 
#### Serial Numbers 

**Serial numbers** are assigned to items and tracked within documents. 

Each serial number generates a unique entry upon its initial occurrence in a document. 

These entries can be removed once the last occurrence of the serial number is deleted from the document.

![picture](pictures/Inventory_Serial_Numbers_14_03.png)
 
#### Requisition Plan

You have the option to assign the current requisition (MRP) plan, which is designed to maintain optimal inventory levels to meet demand while minimizing excess stock and associated costs. 

This plan involves resetting and regenerating data during each planning cycle.

 ![picture](pictures/Inventory_Requisition_plan_14_03.png)

## Views 

#### Available To Promise and Available To Promise By Lots

**The Availability to Promise** feature provides quantities available for various date periods, including current and projected availability, while the **Availability to Promise by Lot** feature specifically tracks 
quantities available for different date periods, considering both current and projected availability, with a focus on individual lot quantities and those without lot specifications.

![picture](pictures/Inventory_views_21_02.png)

Learn more about Inventory in the following articles:
 
- **[Execute store orders function](https://docs.erp.net/tech/modules/logistics/inventory/execute-store-orders-function/index.html?q=Execute%20store%20orders%20function)**

- **[Lots](https://docs.erp.net/tech/modules/logistics/inventory/lots/index.html?q=Lots)**

- **[Store orders](https://docs.erp.net/tech/modules/logistics/inventory/store-orders/index.html?q=Store%20orders)**

- **[Available to promise](https://docs.erp.net/tech/modules/logistics/inventory/available-to-promise/index.html)**

- **[Projected availability report](https://docs.erp.net/tech/modules/logistics/inventory/projected-availability-report.html?q=Projected%20availability%20report)**

- **[Receipt and issue balance validation in store transfers](https://docs.erp.net/tech/modules/logistics/inventory/receipt-and-issue-balance-validation-in-store-transfers.html?q=Receipt%20and%20issue%20balance%20validation%20in%20store%20transfers)**

- **[Inventory Control](inventory-control/index.md)**


> [!NOTE]
> 
> The screenshots taken for this article are from v24 of the platform.
