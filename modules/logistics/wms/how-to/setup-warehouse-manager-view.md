# Setup Warehouse Manager View

# Warehouse Manager View – Technical Overview

## Access and Purpose

The **Warehouse Manager View** is a **Saved View** in the ERP.net **Desktop Client**, accessed via the `WarehouseOrders Navigator`. It is designed to provide warehouse supervisors with a consolidated operational interface that enables:

- Quick access to order states and statuses
- Visual status feedback via conditional formatting
- Multi-level document inspection and control
- Mass-assignment and execution of warehouse orders

## Interface Composition

The view is structured in **two parts**:

### 1. Main Navigator (Left Pane)

Displays a list of `Warehouse Orders` with enhanced color-coded status visualization.

#### Conditional Appearance (CA) Rules

The navigator includes multiple **Conditional Appearances (CAs)**:
- **By Progress**:
  - **Green** – Completed
  - **Yellow** – Released
  - **Red** – Completed with shortages
  - **Gray** – Not Started
- **By Direction**:
  - Additional icon or formatting indicating the logistical flow direction

### 2. Web Panels (Right Pane)

There are **four Web View panels**, configured to load documents in `Single Record` form via dynamic URLs.

## Web Panel 1: Warehouse Order Details

Displays the selected `Warehouse Order` form, including:

- **Lines** – With custom indicators:
  - Fulfilled Quantity
  - Remaining Quantity
  - Fulfillment Status
- **Transactions** – Bound to order lines

### Setup

Use the following in **Change View → Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Wms_WarehouseOrders({Id})
```

Replace `<instance>` with the actual tenant or instance name (e.g., `internal-nbeta`).

### Functional Highlights

- Lines display execution progress via embedded CA rules
- Users can mark the order as **Completed** directly from this panel

## Web Panel 2: Requisition (Parent Document)

Displays the `Warehouse Requisition` associated with the selected order.

### Setup

```
https://<instance>.my.erp.net/cl/forms/Logistics_Wms_WarehouseRequisitions({Parent.Id})
```

### Functional Highlights

- Users can mark the requisition as **Completed**
- This triggers automatic **Store Order Posting**
- A corresponding **Store Transaction** is generated
- Related links to execution logic and trigger flow will be added here

## Web Panel 3: Store Order (Grandparent Document)

Displays the **parent of the requisition**, which is the `Store Order`.

### Setup

```
https://<instance>.my.erp.net/cl/forms/Logistics_Inventory_StoreOrders({Parent.Parent.Id})
```

### Functional Highlights

- Enables creation of **Follow-Up Store Orders** (e.g., for unfulfilled lines)
- A link to the partial fulfillment logic or UI command will be provided

## Web Panel 4: Warehouse Orders Navigator

Embeds the navigator **again**, enabling **mass operations** such as:

- Multi-select assignment of orders to a specific performer
- Execution of bulk UI actions (via toolbar)

## Notes

- The instance name in the Web Panel URLs should reflect the current ERP tenant (e.g., `internal-nbeta`).
- Use the `Change View` mode to customize or replicate this layout for other operational views.
- Conditional Appearances (CA) referenced in this view are defined in a separate documentation section.
