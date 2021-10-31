# Zone based routing

## The basic idea

With zone based routing, the rules for processing the goods are determined based on the zone, in which the goods are stored for each step.
The zones are sequentially numbered, relative to their "closeness" to final shipping. For example:

> 1 IN -> 2 INSP -> 3 BULK -> 4 PICK -> 5 KIT -> 6 PACK -> 7 OUT
>
> RECEIVE ------------> --OPTIMIZE--> ----------------> DISPATCH

The main processes in the warehouse - receive, optimize and dispatch, are ordered consecutively through the zone sequence.
The receive process starts at the inbound docks and runs until goods are placed in bulk.
The optimization process usually deals with replenishment of the picking zones, but can also be used for pre-kitting.
The planning of the dispatch process works backwards - from the final step (the dispatch from the outbound docks) to the first step (usually picking).
This is similar to how MRP/DRP works, but applied for WMS.

Zone based routing and sequencing provides great flexibility in the route formation process, while keeping things simple and understandable for the process designers.
It allows the process designers to focus separately on each zone, leaving the complex full routing formation to the system.
Zone based routing allows programming of very complicated routes, while still keeping things simple and maintainable.

## How it works?

For each zone, there are rules, which define how the goods will be processed, when they pass the zone.
The rules for a zone are defined separately for each of the WMS processes - receive, dispatch and replenishment.
The full route is the concatenation of all route steps for each consecutive zone.

## Hierarchical rules

Since zones are hierarchical, for any given zone there might be multiple rules, coming from different levels of the hierarchy.
All rules in the hierarchy are combined when creating the routing.
Combining the rules is performed separately for each STEP NO within each zone.
To determine the "winning" rule for each step, the RULE PRIORITY is used within all rules, which satisfy the RULE CONDITIONS.

## Start and finish of the process

The receive process starts at the inbound dock and is planned through the zones, until there are no more steps.
Usually, it finishes at the BULK zone.
The dispatch process works in the opposite way - it first determines the quantities needed at the outbound docks, and than determines what previous steps could supply these quantities.
The optimization process is a middle ground - it just runs for all zones, for which there is a definition for the optimization process.

## Movement between the zones

When a rule has a MOVE task, it orders movement of the goods to another zone.
The algorithm for determining the routing steps is then restarted for this new zone and so on until the goods reach their final destination and state.

## Rule and task conditions

*Rule conditions* are evaluated when the routing is determined.
They can be used to alter the routes based on conditions, which are known by the time the route is created.
Rule conditions include such things as product group, zone characteristics, etc.

*Task conditions* are evaluated later in the process and hence allow processing based on what is know in real time during the execution of the order.
They are first copied to the warehouse order.
Then, upon actual execution of the order, they are evaluated in real time.
Task conditions can be based on runtime characteristics like quality inspection status, lot characteristics, etc.
