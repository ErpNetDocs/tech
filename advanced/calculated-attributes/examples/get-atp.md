---
items: CalculatedAttributeExamples
---

# Get available to promise (ATP) quantity

This example demonstrates how to use a **Calculated Attribute** to retrieve an **[Available To Promise (ATP)](https://docs.erp.net/tech/modules/logistics/planning/available-to-promise/index.html)** quantity for a product **on a specific date**.  

Being able to compute ATP through a Calculated Attribute allows business logic, validation rules, automations, and UI fields to dynamically reflect the product’s availability without requiring custom extensions or any external code. 

In this example, the calculation determines the ATP quantity *as of the Required Delivery Date* of a shipment order line. The same pattern, however, can be easily adapted with minimal adjustments to calculate ATP for any other date your business logic requires.


## Overview

The ATP Calculated Attribute queries the **[Available To Promise view](https://docs.erp.net/model/entities/Logistics.Inventory.DemandManagement.AvailableToPromise.html)**, finds the ATP record that is valid as of the requested date, and returns its ATP Base Value.

This example shows how it works:

1. **Reads the repository of the **[Available To Promise view](https://docs.erp.net/model/entities/Logistics.Inventory.DemandManagement.AvailableToPromise.html)**** for the given product.  
2. **Filters** by Product, Store, and Enterprise Company.  
3. **Sorts** the results by `FromDate`, newest first.  
4. **Applies a delivery deadline** (`FromDate ≤ RequiredDeliveryDate`).  
5. **Returns only the first valid record** using `TOP 1`.  
6. **Outputs the `ATPBaseValue`**, representing the promised availability.

This section provides the conceptual overview; the next one shows the exact implementation.

> [!NOTE]
> 
> The repository of the attributes is *Logistics.Shipment.ShipmentOrderLines*
> 
> The `ORDERBY` operator for `FromDate` in this report is supported starting from **version 26**.  
> In earlier versions of ERP.net, `ORDERBY` was not available, so the same behavior had to be achieved by combining a `FILTER` with a `SORT`.

```txt
10   GETOBJVALUE     EXP:20                           ATTRIB:ATPBaseValue 
20   FIRST           EXP:30
30   SELECT          REPO::Logistics.Inventory.DemandManagement.AvailableToPromise   EXP:40
40   TOP             CONST:1                          EXP: 50
50   ORDERBY         ATTRIB:FromDate                  CONST:DESC                     EXP:60
60   WHERE           EXP:70                           EXP:80
70   AND             EXP:90                           EXP:120
80   AND             EXP:150                          EXP:180
90   EQUAL           ATTRIB:ProductId                 EXP:100
100  GETOBJVALUE     INPUT:10                         EXP:110
110  GETOBJVALUE     REF::ParentSalesOrderLine        ATTRIB:ProductId
120  EQUAL           ATTRIB:StoreId                   EXP:130
130  GETOBJVALUE     INPUT:10                         EXP:140
140  GETOBJVALUE     REF::ParentSalesOrderLine        ATTRIB:LineStoreId
150  EQUAL           ATTRIB:EnterpriseCompanyId       EXP:160
160  GETOBJVALUE     INPUT:10                         EXP:170
170  GETOBJVALUE     REF::ShipmentOrder               ATTRIB:EnterpriseCompanyId
180  LTE             ATTRIB:FromDate                  EXP:190
190  GETOBJVALUE     INPUT:10                         EXP:200                                                 
200  GETOBJVALUE     REF::ShipmentOrder               ATTRIB:RequiredDeliveryDate     
```

**Detailed еxplanation:**
- **10**: Gets the `ATPBaseValue` of the record returned by **EXP:20**.  
- **20**: Takes the first element from the list returned by **EXP:30**.  
- **30**: Selects the `AvailableToPromise` records from the repository.  
- **40**: Limits the result set to **1** record from **EXP:50**.  
- **50**: Orders the records by `FromDate` in descending order (most recent first).  
- **60**: Filters the records for which both **EXP:70** and **EXP:80** are `True`.  
- **70**: Returns `True` only if both **EXP:90** and **EXP:120** are `True`.  
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
