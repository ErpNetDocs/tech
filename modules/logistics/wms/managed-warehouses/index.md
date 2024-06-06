# Managed Warehouses 

Managed warehouses are visual representations of complex storage facilities that necessitate efficient inventory management. 

In ERP.net, they are organized into various locations and zones, each enforcing its own policies and consisting of one or more workers. 

This structured approach allows for precise tracking, better organization and streamlined logistics within the managed warehouse.

### Navigation 

To access your managed warehouses, navigate to the **Managed Warehouses** panel of the **WMS** section. 

![pictures](pictures/Managed_Warehouses_navigation_03_06.png)

Clicking the panel's title will take you to a table listing all of your existing managed warehouses as well as the ability to create new ones.

![pictures](pictures/Managed_Warehouses_view_04_06.png)

## Warehouse components 

The building blocks of a managed warehouse are established during its creation. 

They can be subsequently modified if the warehouse experiences any changes.

### Warehouse 

This panel contains the **name** of the warehouse and some optional **notes** about it. 

![pictures](pictures/Managed_Warehouses_warehouse_04_06.png)

### Workers 

This panel contains a list of workers assigned to the managed warehouse.

![pictures](pictures/Managed_Warehouses_workers_04_06.png)

You can find the following information about every worker:

- **Name** - This the worker's full name.

- **Person** - Specifies the person representing the worker. If a **User** is not set for the worker, this column will be NULL as well, which means that the person's identity may be unknown or the worker might be a non-person entity.

> [!NOTE]
> The **Person** column is read-only.

- **Notes** - Additional information or special instructions related to the worker's role and responsibilities.

- **Is Active** - Specifies whether the worker is active and capable of executing tasks. 

- **Active From** - The date the worker's record became active in the warehouse. This helps in tracking the duration of the worker's service.

- **Active To** - The termination date of the worker's activity in the warehouse. This can be NULL for workers who are still active and have not been terminated previously.

- **User** - Refers to the user name associated with the worker. This includes only internal and virtual users.

> [!NOTE]
> Updating the User will also update the Person.

### Policies 

In the **Policies** panel, you can find details about the policies of the current managed warehouse. 

![pictures](pictures/Managed_Warehouses_policies_04_06.png)

Each policy is associated with a particular zone, denoted by its code. 

Additional information includes the type of policy, its corresponding value, and any associated product group codes.

### Locations

In the **Locations** panel, you can find details about the locations of the current managed warehouse. 

![pictures](pictures/Managed_Warehouses_locations_04_06.png)

Each location is identified by its unique address within the warehouse zone. 

The table also provides additional notes relevant for each location.

### Zones 

In the **Zones** panel, you can find details about the zones of the managed warehouse. 

![pictures](pictures/Managed_Warehouses_zones_04_06.png)

Each zone is identified by its name and may include additional notes for clarification. 

The table also indicates the parent zone, if applicable, and assigns a unique code to each zone for identification purposes.
