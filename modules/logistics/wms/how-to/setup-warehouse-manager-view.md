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

You can see how By Progress attributes are created here: [Execution status for warehouse orders](../../../../advanced/calculated-attributes/examples/execution-status-for-warehouse-orders.md)
You can see how By Direction attribute is created here: [Execution status for warehouse orders](../../../../advanced/calculated-attributes/examples/requisition-type.md)



### 2. Web Panels (Right Pane)

There are four Web View panels, configured to load documents in Single Record form via dynamic URLs. 
The content in these panels is automatically synchronized with the selection in the navigator on the left. 
When a Warehouse Order is selected, each panel displays information relevant to that specific order.

## Web Panel 1: Warehouse Order Details

This panel displays the Single Record Form of the Warehouse Order selected in the navigator on the left.

It provides a complete operational view of the order — allowing warehouse managers to track what has been ordered, how much has been fulfilled, and how execution is progressing.  
The **Lines** section includes all key information about the ordered items, such as product, quantity, unit of measure, and other essential system fields.

In addition to the standard data, the following calculated attributes are shown to highlight execution progress:

- Fulfilled Quantity  
- Remaining Quantity  
- Fulfillment Status  

You can see how **Fulfilled Quantity** and **Remaining Quantity** are created here: [Fulfilled and remaining quantity attributes](#)  
You can see how **Fulfillment Status** is created here: [Fulfillment status attribute](#)

The **Transactions** section shows:

- User who executed the operation  
- Timestamp of execution  
- Line-level details (product, quantity, location, lot, serial numbers, etc.)

### Setup

In Change View mode, enter the following in the field **Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Wms_WarehouseOrders({Id})
```
You can also customize the panel’s name using the **Panel title** field.

#### Functional Highlights

- The order is marked as Completed automatically when the warehouse worker finishes it through the handheld device.  
- The warehouse manager can then see the updated status here and proceed to the next steps using the following panels.

## Web Panel 2: Requisition (Parent Document)

This panel displays the Single Record Form of the Warehouse Requisition that is the parent document of the selected Warehouse Order.  
When the requisition is marked as Completed, the corresponding Store Transaction is automatically created through the document event [Completed Warehouse Requisition](#).

### Setup

In Change View mode, enter the following in the field **Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Wms_WarehouseRequisitions({Parent.Id})
```
You can also customize the panel’s name using the **Panel title** field.

#### Functional Highlights

- Depending on whether the order was fulfilled in full or requires further execution, the manager can choose to proceed to the next panel either to initiate a follow-up or to verify that everything is complete.


## Web Panel 3: Store Order (Grandparent Document)

This panel displays the Single Record Form of the Store Order, which is the grandparent document of the selected Warehouse Order.  
It is used to review the source document that generated the requisition.  
If some lines remain unfulfilled, the manager can create a follow-up Store Order from here.  
This action starts a new execution cycle by generating a new requisition and Warehouse Order, which will then appear in Panel 1 and Panel 4 for further processing.

### Setup

In Change View mode, enter the following in the field **Source URL (with placeholders)**:
```
https://<instance>.my.erp.net/cl/forms/Logistics_Inventory_StoreOrders({Parent.Parent.Id})
```
You can also customize the panel’s name using the **Panel title** field.

#### Functional Highlights

- Create a follow-up Store Order using the UI function [Create Follow-Up Store Order](#).


## Web Panel 4: Warehouse Orders Navigator

This panel embeds the Warehouse Orders navigator again, making it possible to perform bulk actions on multiple orders directly from the view.

#### Functional Highlights

- Assign selected orders to a specific performer using the UI function [Assign to performer](#)  
- Change the performer of already assigned orders via [Change performer](#)

### Setup

In Change View mode, you can configure this panel to display the Warehouse Orders navigator again by setting a saved view.  
The panel’s name can be adjusted using the **Panel title** field.

![Notes] 
- Use the Change View mode to customize or replicate this layout for other operational views  
- The instance name in the Web Panel URLs must match the name of your specific ERP tenant instance  

