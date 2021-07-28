
---
items: CalculatedAttributeExamples
---

# Get Available To Promise (ATP) Quantity

This example shows how you can create a calculated attribute which gets the avaible to promise (ATP) quantity on a particular date using the [AvailableToPromise View](xref:Logistics.Inventory.DemandManagement.AvailableToPromise View).
In the example we get the ATP quantity in a Shipment order line on its Required Delivery Date.

> [!NOTE]
> The repository of the attributes is *Logistics.Shipment.ShipmentOrderLines*

```
10	GETOBJVALUE	EXP:20	ATTRIB:ATPBaseValue		
20	FIRST	EXP:30				
30	SORT	EXP:40	ATTRIB:FromDate	CONST:DESC
40	SELECT	REPO:Logistics.Inventory.DemandManagement.AvailableToPromise	EXP:50		
50	WHERE	EXP:80	EXP:60		
60	AND	EXP:110	EXP:70		
70	AND	EXP:140	EXP:170		
80	EQUAL	ATTRIB:ProductId	EXP:90		
90	GETOBJVALUE	INPUT:10	EXP:100		
100	GETOBJVALUE	REF:ParentSalesOrderLine	ATTRIB:ProductId		
110	EQUAL	ATTRIB:StoreId	EXP:120		
120	GETOBJVALUE	INPUT:10	EXP:130		
130	GETOBJVALUE	REF:ParentSalesOrderLine	ATTRIB:LineStoreId		
140	EQUAL	ATTRIB:EnterpriseCompanyId	EXP:150		
150	GETOBJVALUE	INPUT:10	EXP:160		
160	GETOBJVALUE	REF:ShipmentOrder	ATTRIB:EnterpriseCompanyId		
170	LTE	ATTRIB:FromDate	EXP:180		
180	GETOBJVALUE	INPUT:10	EXP:190		
190	GETOBJVALUE	REF:ShipmentOrder	ATTRIB:RequiredDeliveryDate		
```


Explanation:
 
- 10: Get the atrribute "ATPBaseValue" of the AvailableToPromise record returned by EXP:20
- 20: Get the first record of the list of AvailableToPromise records returned by EXP:30
- 30: Sort the list of AvailableToPromise records returned by EXP:40 - descending by the value of the "FromDate" attribute
- 40: Select the AvailableToPromise records which are mathin the clauses of EXP:50
- 50: Filter the list above by the records WHERE/in which the clauses in EXP:80 and EXP:60 are True
- 60: Filter the list above by the records WHERE/in which the clauses in EXP:110 and EXP:70 are True
- 70: Filter the list above by the records WHERE/in which the clauses in EXP:140 and EXP:170 are True
- 80: Returns True if the ProductId of the AvailableToPromise record is equal to EXP:90
- 90: Gets EXP:100 from the repository of EXP:10 i.e. of the current Shipment Order Line
- 100: Gets the ProductId specified in the ParentSalesOrderLine 
- 110: Returns True if the StoreId of the AvailableToPromise record is equal to EXP:120
- 120: Gets EXP:130 from the repository of EXP:10 i.e. of the current Shipment Order Line
- 130: Gets the LineStoreId specified in the ParentSalesOrderLine 
- 140: Returns True if the EnterpriseCompanyId of the AvailableToPromise record is equal to EXP:150
- 150: Gets EXP:160 from the repository of EXP:10 i.e. of the current Shipment Order Line
- 160: Gets the EnterpriseCompanyId of the ShipmentOrder 
- 170: Returns True if the FromDate of the AvailableToPromise record lower or equal to EXP:180
- 180: Gets EXP:160 from the repository of EXP:10 i.e. of the current Shipment Order Line
- 160: Gets the RequiredDeliveryDate of the ShipmentOrder 
