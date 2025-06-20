---
items: CalculatedAttributeExamples
---

# RequisitionType of the Requisition linked to a Warehouse Order

This attribute extracts the direction (type) of the requisition document associated with a warehouse order. It resolves the requisition type by navigating through a line in the order and following its reference back to the parent requisition document.

The value returned corresponds to the **RequisitionType** field of the requisition (e.g. `Inbound`, `Outbound`, etc.).

> [!NOTE]  
> The repository of the attribute is *Logistics.Wms.WarehouseOrders*

### Expression
```
10: GETOBJVALUE EXP:20 EXP:30  
20: FIRST CHILD:Lines  
30: GETOBJVALUE REF:ParentDocument EXP:40  
40: GETVALUE ATTRIB:RequisitionType
```
### Explanation

- 20: Retrieves the first line from the warehouse order.
- 30: Follows the reference from the line to its parent document (assumed to be a requisition).
- 40: Extracts the value of the RequisitionType attribute from the requisition.
- 10: Returns the requisition type as the final value.

This attribute is useful when you need to display or filter warehouse orders based on the requisition’s direction (e.g. in dashboards or grids).
