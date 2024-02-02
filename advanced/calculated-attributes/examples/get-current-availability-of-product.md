---
items: CalculatedAttributeExamples
---

# Get current availability of a product

This example shows how to create a calculated attribute which returns the sum of the available quantity base of a particular product. Filters are applied by enterprise company, store, product, lot, store bin and serial number, because of the unique nature of the repository of the calculation attribute. Additional filter by Product variant could also be added. 

We recommend always filtering by EnterpriseCompanyId, StoreId, and ProductId inside the Select clauses when searching for product availability. If EnterpriseCompanyId or StoreId is missed, the calculation will happen much slower.

This is the order of filtering for the CurrentBalances. We can exclude filters from bottom to top but we cannot remove filters from above until we have removed all from below.

**EnterpriseCompanyId,** <BR>
**StoreId,** <BR>
**ProductId,** <BR>
**LotId,** <BR>
**StoreBinId,** <BR>
**SerialNumberId,** <BR>
**ProductVariantId**<BR>

The example is suited for consumption order lines, but such an attribute could be used with other documents or definitions as well. 

```
Repository Name: Production.ShopFloor.ConsumptionOrderLines
```


```
10: SUM	EXP:20 ATTRIB:QuantityBaseValue			
20: SELECT REPO:Logistics.Inventory.CurrentBalances EXP:30	
30: WHERE EXP:50 EXP:80			
50: EQUAL ATTRIB:EnterpriseCompanyId EXP:60			
60: GETOBJVALUE INPUT:10 EXP:70			
70: GETOBJVALUE	REF:Document ATTRIB:EnterpriseCompanyId		
80: AND	EXP:120	EXP:90			
90: AND	EXP:140	EXP:100			
100: AND EXP:160 EXP:110			
110: AND EXP:180 EXP:200			
120: EQUAL ATTRIB:StoreId EXP:130			
130: GETOBJVALUE INPUT:10 ATTRIB:StoreId			
140: EQUAL ATTRIB:ProductId EXP:150			
150: GETOBJVALUE INPUT:10 ATTRIB:ProductId			
160: EQUAL ATTRIB:LotId EXP:170			
170: GETOBJVALUE INPUT:10 ATTRIB:LotId			
180: EQUAL ATTRIB:StoreBinId EXP:190			                  
190: GETOBJVALUE INPUT:10 ATTRIB:StoreBinId			
200: EQUAL ATTRIB:SerialNumberId EXP:210			
210: GETOBJVALUE INPUT:10 ATTRIB:SerialNumberId		
```

**Explanation:**

- 10: Sum _Quantity Base_ from the filtered list returned by EXP:20
- 20: Select repository **Logistics.Inventory.CurrentBalances** and filter by the clauses in EXP:30 
- 30: Filter the list above by the records WHERE, in which the clauses in EXP:50 and EXP:80 are True
- 50: Check whether **ATTRIB:EnterpriseCompanyId** is equal to EXP:60 
- 60: Get value from the repository of EXP:10 and reference EXP:70
- 70: Get **ATTRIB:EnterpriseCompanyId**  from the referenced document
- 80: EXP:120 EXP:90
- 90: EXP:140 EXP:100
- 100: EXP:160 EXP:110
- 110: EXP:180 EXP:200
- 120: Check whether **ATTRIB:StoreId** is EQUAL to EXP:130 
- 130: Get **ATTRIB:StoreId** from the repository of EXP:10
- 140: Check whether **ATTRIB:ProductId** is EQUAL to EXP:150 
- 150: Get **ATTRIB:ProductId** from the repository of EXP:10
- 160: Check whether **ATTRIB:LotId** is EQUAL to EXP:170
- 170: Get **ATTRIB:LotId** from the repository of EXP:10
- 180: Check whether **ATTRIB:StoreBinId** is EQUAL to EXP:190 
- 190: Get **ATTRIB:StoreBinId** from the repository of EXP:10
- 200: Check whether **ATTRIB:SerialNumberId** is EQUAL to EXP:210 
- 210: Get **ATTRIB:SerialNumberId** from the repository of EXP:10

