# Warehouse setup

To start working with Warehouse Management Module (WMS), you need to complete the setup of the general warehouse definitions – warehouse, locations, workers, and policies.

## Create warehouse definition/s

Setting up a warehouse, naturally starts with the creation of the definitions of the warehouse themselves. 

A single warehouse definition represents a complete physical warehouse. It may a contain several individual buildings that together form a complete warehouse complex, which is treated as a single entity by the other processes. 

Typically, warehouses largely follow the structure of stores in the from the Inventory Module, but it is not mandatory. 

## Link the warehouse definitions to the stores they will be serving
We have created warehouse definitions, the next step is to link these warehouses to the existing stores of the Inventory Module.
This way, when we have a warehouse requisition coming from the Inventory Module, we will know which warehouse from the WMS module corresponds to it and therefore has to fulfill the requisition.

The link is made trough the **Managed Warehouse** field in the store’s definition.

Usually, the link is one to one - one warehouse is linked to only one store. We can still we can still link a single warehouse to two or more stores. We must bear in mind, however, that if a warehouse is linked to more than one stores - the reverse operations, such as warehouse reconciliation may require manual post-processing.

## What to do next?
You can continue setting up your warehouse by creating zones, locations, workers and policies. 

More information can be found in the following topics:
-	[Zones and locations](zones-and-locations.md)
-	[Warehouse workers](warehouse-workers.md)
-	[Warehouse policies](warehouse-policies.md)

> **_NOTE:_**  Note that in order to work with or test the module or the @wms-worker app, you need to create at least one warehouse, zone, location and worker.
