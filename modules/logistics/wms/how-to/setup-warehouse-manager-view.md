# Setup Warehouse Manager View

## Access and Purpose

The **Warehouse Manager View** is a Saved View in the ERP.net Desktop Client, accessed via the WarehouseOrders Navigator. It is designed to provide warehouse supervisors with a consolidated operational interface that enables:

- Quick access to order states and statuses
- Visual status feedback via conditional formatting
- Multi-level document inspection and control
- Mass-assignment and execution of warehouse orders

## Interface Composition

The view is structured in two parts:

### 1. Main Navigator (Left Panel)

Displays a list of Warehouse Orders with enhanced color-coded status visualization.

#### Calculated Attributes

The navigator includes several example calculated attributes configured to demonstrate typical scenarios:

- By Progress:
  - Green – Completed
  - Yellow – Released
  - Red – Completed with shortages
  - Gray – Not Started
- By Direction:
  - Indicates the logistical flow direction with specific formatting

These are just examples provided for convenience. Users can define and apply their own calculated attributes according to their operational needs.

You can see how By Progress attributes are created here [Execution status for warehouse orders](tech/advanced/calculated-attributes/examples/execution-status-for-warehouse-orders.md)
You can see how By Progress attributes are created here [Execution status for warehouse orders](tech/advanced/calculated-attributes/examples/execution-status-for-warehouse-orders.md)



### 2. Web Panels (Right Pane)

There are four Web View panels, configured to load documents in Single Record form via dynamic URLs. 
The content in these panels is automatically synchronized with the selection in the navigator on the left. 
When a Warehouse Order is selected, each panel displays information relevant to that specific order.

## Web Panel 1: Warehouse Order Details

Displays the selected Warehouse Order form, including:

- **Lines** – Show:
  - Fulfilled Quantity
  - Remaining Quantity
  - Fulfillment Status

- **Transactions** – Show:
  - User who executed the operation
  - Timestamp of execution
  - Line-level details (product, quantity, location, batch/serial numbers, etc.)

### Setup

In Change View mode, enter the following in the field **Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Wms_WarehouseOrders({Id})
```
You can also customize the panel’s name using the **Panel title** field.

### Functional Highlights

- Lines display execution progress via embedded CA rules
- Users can mark the order as Completed directly from this panel

## Web Panel 2: Requisition (Parent Document)

Displays the Warehouse Requisition associated with the selected order.

### Setup

In Change View mode, enter the following in the field **Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Wms_WarehouseRequisitions({Parent.Id})
```
You can also customize the panel’s name using the **Panel title** field.

### Functional Highlights

- Users can mark the requisition as Completed
- This triggers automatic Store Order Posting
- A corresponding Store Transaction is generated

## Web Panel 3: Store Order (Grandparent Document)

Displays the parent of the requisition, which is the Store Order.

### Setup

In Change View mode, enter the following in the field **Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Inventory_StoreOrders({Parent.Parent.Id})
```
You can also customize the panel’s name using the **Panel title** field.

### Functional Highlights

- Enables creation of Follow-Up Store Orders (e.g., for unfulfilled lines)

## Web Panel 4: Warehouse Orders Navigator

Embeds the navigator again, enabling mass operations such as:

- Multi-select assignment of orders to a specific performer
- Execution of bulk UI actions (via toolbar)

### Setup

In Change View mode, you can configure this panel to display the Warehouse Orders navigator again by setting a saved view.  
The panel’s name can be adjusted using the **Panel title** field.

## Notes

- The instance name in the Web Panel URLs should reflect the current ERP tenant (e.g., `internal-nbeta`)
- Use the Change View mode to customize or replicate this layout for other operational views
- Conditional Appearances (CA
