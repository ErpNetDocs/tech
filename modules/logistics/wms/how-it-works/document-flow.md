## Document flow in WMS

The link between other modules/processes in the system and the WMS is performed through the Inventory module. And more precisely, the document that communicates with the WMS Module is the Inventory Store order. 

The Store Order creates both:
-	the Warehouse Requisition that inform the WMS Module what is requested by the other modules/processes;
-	and the Store Transaction, which contains the information how these requests are actually fulfilled by WMS module.

## How it works?
Here is the scheme of the document and execution flow:

![Flow](pictures/flow_detailed.png)

(1) **The Store Order (SO)** generates a **Warehouse Requisition (WR)** using the [LOG0205](https://docs.erp.net/model/generations/LOG0205.html) generation procedure. 

The Warehouse Requisition is the document that informas the WMS Module what is requested by the other modules/processes. Usually the Warehouse Requisition is almost an exact copy of the Store Order. 

The document fulfillment between the SO and WR is calculated using the [Fulfillment table method](~/advanced/document-flow/fulfillment.md#fulfillment-documents). "Planned Document Fulfillment records which
