# Warehouse Management



Warehouse Management Module follows the concepts of the Warehouse Management Systems ([WMS](https://en.wikipedia.org/wiki/Warehouse_management_system)). The main objective for implementing a WMS is to optimize the efficiency of the warehouse operations in the **Managed Warehouses**.

**Managed Warehouses** are physical warehouses. which have managed operation. They exist outside of existing Store definitions. The Stores concept is used for management of inventory levels and general ledger (accounting) entries. Managed Warehouses are sub-level, which is used to manage all warehouse activities, including:

- Picking
- Put-Away
- Counting
- Packing/Unpacking
- Inspection
- Robot interactions
- etc.

One Managed Warehouse can encapsulate the storage and operations of multiple legal entities (Enterprise Companies). While the existing "Store" concept is strictly bound to enterprise company, the warehouse can accommodate goods of multiple entities. It can even be used to store goods from external companies.

The most important part for achieving operational effectiveness is to properly organize the layout of the warehouses. Layout optimization is outside the scope of this document.

Managed Warehouses are organized using **Zones** and **Locations**. Zones are sub-division of a warehouse.

Zones are used to accommodate different storage needs, such as different temperature requirements or turnover rate of the products.

The zones are further divided in **Locations**. Locations have name (like #1-8-20), which is used to uniquely identify them.

Use Warehouse Management to increase efficiency by automating warehouse routing and identifying storage locations for your products.

The two most basic documents of WMS are:

- **Warehouse Requisitions (W.R.) 
  **They contain outside request for warehouse operation (usually inbound/outbound).

  

- **Warehouse Orders (W.O.)**
  They are the internal plan for execution of W.R. They contain routes, locations, workers, etc.

The basic operation flow of WMS is the following:

The steps, noted in (parens) in the diagram are as follows:

1. The outside module/department creates W.R. based on its needs.
2. Inside the WMS, the team devises a plan for execution and stores it as a W.O. In the best case scenario, the creation of WO is totally automated.
3. The workers use their handheld devices to execute the order. Each step is recorded as both Warehouse Transaction and Warehouse Order Execution.
4. After the WO is fully executed, the Warehouse Requisition Execution is updated.
5. After the WR is fully executed, the external module/department updates its execution state.

Typically, managed warehouse operations are executed using some sort of handheld devices, which are used to scan bar-codes, NFC tags, etc.

