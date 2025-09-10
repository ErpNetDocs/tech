---
items: CalculatedAttributeExamples
---

# Get available to promise (ATP) quantity

This example shows how you can create a calculated attribute that gets the **[avaible to promise (ATP)](https://docs.erp.net/tech/modules/logistics/planning/available-to-promise/index.html)** quantity on a particular date using the **AvailableToPromise** view.

In the example, you'll learn how to get the ATP quantity in a shipment order line on its required delivery date.

> [!NOTE]
> 
> The repository of the attributes is *Logistics.Shipment.ShipmentOrderLines*

```

10  GETOBJVALUE   EXP:20                                                      ATTRIB:A TPBaseValue
20  FIRST         EXP:30
30  SELECT        REPO:Logistics.Inventory.DemandManagement.AvailableToPromise  EXP:40
40  TOP           CONST:1                                                    EXP:50
50  ORDERBY       ATTRIB:FromDate   CONST:DESC                               EXP:60
60  WHERE         EXP:90    EXP:70
70  AND           EXP:120   EXP:80
80  AND           EXP:150   EXP:180
90  EQUAL         ATTRIB:ProductId                                            EXP:100
100 GETOBJVALUE   INPUT:10                                                   EXP:110
110 GETOBJVALUE   REF:ParentSalesOrderLine   ATTRIB:ProductId
120 EQUAL         ATTRIB:StoreId                                               EXP:130
130 GETOBJVALUE   INPUT:10                                                   EXP:140
140 GETOBJVALUE   REF:ParentSalesOrderLine   ATTRIB:LineStoreId
150 EQUAL         ATTRIB:EnterpriseCompanyId                                   EXP:160
160 GETOBJVALUE   INPUT:10                                                   EXP:170
170 GETOBJVALUE   REF:ShipmentOrder          ATTRIB:EnterpriseCompanyId
180 LTE           ATTRIB:FromDate                                              EXP:190
190 GETOBJVALUE   INPUT:10                                                   EXP:200
200 GETOBJVALUE   REF:ShipmentOrder          ATTRIB:RequiredDeliveryDate


```

**Explanation:**
- **10**: Gets the `ATPBaseValue` of the record returned by **EXP:20**.  
- **20**: Takes the first element from the list returned by **EXP:30**.  
- **30**: Selects the `AvailableToPromise` records from the repository.  
- **40**: Limits the result set to **1** record from **EXP:50**.  
- **50**: Orders the records by `FromDate` in descending order (most recent first).  
- **60**: Filters the records for which both **EXP:90** and **EXP:70** are `True`.  
- **70**: Returns `True` only if both **EXP:120** and **EXP:80** are `True`.  
- **80**: Returns `True` only if both **EXP:150** and **EXP:180** are `True`.  
- **90**: Returns `True` if the `ProductId` of the `AvailableToPromise` record is equal to **EXP:100**.  
- **100**: Gets **EXP:110** from the repository of **INPUT:10** (i.e., from the current shipment order line).  
- **110**: Gets the `ProductId` of the `ParentSalesOrderLine`.  
- **120**: Returns `True` if the `StoreId` of the `AvailableToPromise` record is equal to **EXP:130**.  
- **130**: Gets **EXP:140** from the repository of **INPUT:10**.  
- **140**: Gets the `LineStoreId` of the `ParentSalesOrderLine`.  
- **150**: Returns `True` if the `EnterpriseCompanyId` of the `AvailableToPromise` record is equal to **EXP:160**.  
- **160**: Gets **EXP:170** from the repository of **INPUT:10**.  
- **170**: Gets the `EnterpriseCompanyId` of the `ShipmentOrder`.  
- **180**: Returns `True` if the `FromDate` of the `AvailableToPromise` record is less than or equal to **EXP:190**.  
- **190**: Gets **EXP:200** from the repository of **INPUT:10**.  
- **200**: Gets the `RequiredDeliveryDate` of the `ShipmentOrder`. 
