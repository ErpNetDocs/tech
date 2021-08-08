# Enterprise Asset Management

## Description
From Wikipedia:

Enterprise Asset Management (EAM) involves the maintenance management of an organization’s physical assets throughout each asset's lifecycle. EAM is used to plan, optimize, execute, and track the needed maintenance activities with the associated priorities, skills, materials, tools, and information. This covers the design, construction, commissioning, operations, maintenance and decommissioning or replacement of plant, equipment and facilities.

You can learn more at:

[Enterprise set management](https://en.wikipedia.org/wiki/Enterprise_asset_management)
 
In @@name, the Enterprise Asset Management application deals with the maintenance and locations of the company assets.

In the following sections, we will describe the different entity types, comprising the EAM data model.

## Maintenance Types

When planning the required maintenance for an asset, there are different types of maintenance that can be required.

For example, if we have a car, we can plan:

- Insurance renewal - once per year
- Oil change - each 20,000 km
- Gearbox check - every 5 years OR 100,000 km

Each of the above maintenances represents a different ***Maintenance Type***.

In an Enterprise, there might be many different types of assets. Each type of asset requires different maintenance types. Some maintenance types might be applicable for multiple asset types and others -  unique for specific asset types.

There might be many maintenance types and they need to be organized. That is why, there is the hierarchical organization, called ***Maintenance Type Groups***.

## Asset Types

In an enterprise, there might be many assets, which need to be managed. However, the different types of assets need different kinds of management. For this reason, we can define different ***Asset Types***.

Example asset types:

- Car
- Heavy Truck
- Aircraft
- Building
- Street Lamp
- Computer

## Asset Type - Tracked Parameters
For each asset type, we can track different parameters. For example:

- Car
  - Mileage (in km)
- Heavy truck
  - Mileage (in km)
  - Cycles
- Airplane
  - Flight hours
  - Cycles

The tracked parameters are used to track the usage and wearing out of the asset and hence plan the desired maintenance.

## Asset Type - Maintenance Types

For each asset type, we define what kind of maintenance is needed for the assets of that type. Also, we can define a default schedule. 

For example:

- Car
  - Insurance - Every 12 months
  - Oil - Every 15,000 km
  - Gearbox
- Heavy truck
  - Insurance - Every 12 months
  - Oil - Every 30,000 km
  - Gearbox
  - Refrigerating compartment check etc.
- Aircraft
  - A-Check - Every 200 cycles
  - B-Check - Every 6 months
  - C-Check - Every 20 months
  - D-Check - Every 80 months

>[!NOTE]
You can see here that although both cars and heavy trucks need oil change, the required mileage is different. In practice, every car and truck might have even different mileage requirements.

## Service Centers

When planning the maintenance of the assets, the different maintenances are executed by different ***Service Centers***. Then, each maintenance schedule for an asset is assigned to a different service center.

The service center might be an authorized service center for the asset. But it might also be an employee(s), executing the desired maintenance.

## Managed Assets

Finally, we can define every asset, the maintenance of which will be managed by the application. The asset can be defined in other parts of the ERP - as fixed asset, as vehicle (in Fleet management), etc. Defining the asset in the EAM application as ***Managed Asset***, allows its maintenance to be managed.

Example managed assets:

- Car Peugeot 508, Y2016, Reg.No. CC0303PM
- Car Jeep Grand Cherokee, Y2017, Reg.No.YY0202PS
- Mobile Station 5011, Address:...etc.

Because there might be many managed assets, they are organized in a hierarchy of ***Managed Asset Groups***.

## Managed Assets - Maintenance Schedules

When an asset is defined as specific ***Asset Type***, it inherits some default maintenance schedules. However, each asset might be of different age and wear and might have unique maintenance needs. Hence, the specific maintenance schedules of each specific managed asset are defined in 

***Managed Asset Maintenance Schedules***.

For example:

- Car Peugeot 508, Y2016, Reg.No. CC0303PM
  - Insurance - Every 12 months
  - Oil - Every 18,000 km
- Car Jeep Grand Cherokee, Y2017, Reg.No.YY0202PS
  - Insurance - Every 12 months
  - Oil - Every 20,000 km

## Managed Assets - Scheduled Maintenances

The maintenance schedules define the general plan for maintenance. However, we have to schedule each specific maintenance as well. The scheduling might be for different reasons:

- The time limit after the last maintenance was reached (by date).
- The mileage for the next maintenance was reached (by tracked parameter).
- The asset was purchased second hand and one initial maintenance should be scheduled after up to 20 days (manually planned).

Each of the above represents a ***Managed Asset Scheduled Maintenance***. They can be both manually entered or automatically planned.

Emergency repair is not planned hence it is not scheduled maintenance. Emergency repairs are directly processed through Maintenance orders (which will be shortly presented).

## Managed Assets - Locations

The EAM module allows the tracking of asset assignments to different company locations and responsible persons. Assets can also be re-assigned multiple times (even within a month).

Asset assignment can be used to determine the cost centers to which the depreciation will be distributed.
 
Asset locations contains data about each assignment:

- Date of assignment
- Company location
- Responsible person
- Notes - for more precise location or other notes.

## Maintenance Orders

The ***Maintenance Order***  document is the final data piece in the EAM data model. It represents one concrete appointment for a specific type of maintenance(s) for one (or many) specific asset(s).
It is created by the maintenance planner to denote the actual appointment with the service center.
The statuses of the maintenance order correspond to the progress of the maintenance:

- Firm planned - the maintenance is appointed with the service center for specific time and date.
- Released - the maintenance has started (used mostly for maintenances which are performed in-house)
- Completed - the maintenance was performed.

Maintenance orders can create other sub-documents to represent the actual work (like Service orders) or the materials requested and used (Store order / Store transaction), etc.

## Maintenance Order - Lines

One maintenance order can appoint at once the maintenance of many managed assets. Each maintenance type for each asset is represented with one ***Maintenance Order Line***.
 

