# Warehouse zones and locations

Warehouse zones are used to organize the different storage areas of the warehouse.

## Zone hierarchy

The zones are organized in a hierarchy, where each zone can have sub-zones, which can have its own sub-zones and so on.
For example:

- Picking
  - Aisle P1
    - Rack P1.1
      - Shelf P1.1.1
      - Shelf P1.1.2
      - Shelf P1.1.3
  - Aisle P2
- Refrigeration
  - Aisle R1
    - Rack R1.1
  - Aisle R2
- Carts
  - Cart C1
- Bulk
  - Rack B1
  - Rack B2

## Primary and sub-zones

In the above example, Picking, Refrigeration, Carts and Bulk are *primary zones*. Aisle M1, Rack M1.1, etc. are called *sub-zones*.

The primary zones have no parent zone. Sub-zones always have a parent zone.

## Locations

The warehouse locations (sometimes called bins) are used for the actual storage of the goods.
They are the leafs in the hierarchy and are structured under the warehouse zones.
For example:

Zone "Shelf P1.1.3" can contain 3 locations:

- P1.1.3-A
- P1.1.3-B
- P1.1.3-C
