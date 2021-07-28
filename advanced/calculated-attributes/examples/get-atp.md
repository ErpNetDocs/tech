
---
items: CalculatedAttributeExamples
---

# Get Available To Promise (ATP) Quantity

This example shows how you can create a calculated attribute which gets the avaible to promise (ATP) quantity on a particular date using the [AvailableToPromise View](xref:Logistics.Inventory.DemandManagement.AvailableToPromise View).
In the example we get the ATP quantity in a Shipment order line on its Required Delivery Date.


```
10	GETOBJVALUE	EXP:20	ATTRIB:ATPBaseValue		
20	FIRST	EXP:30				
30	SORT	EXP:40	ATTRIB:FromDate	CONST:DESC
40	SELECT	REPO:Logistics.Inventory.DemandManagement.AvailableToPromise	EX:50		
50	WHERE	EXP:0	EXP:60		
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

- 10: 
