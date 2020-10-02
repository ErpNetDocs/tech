# Get Current Availabilities of a Product

This example shows how  to create a calculated attribute which returns the sum of the currently  available Quantity Base of a particular product. In the example below  are applied filters by Product, Store, Store Bin, Lot and Serial Number, because of the specification of the repository of the calculation  attribute. Other filters, such as Product Variant and Enterprise Company could be also added if needed. The example is created for Consumption  Order Lines, but such attribute could be created for other documents o  definitions as well. 



```
Repository Name: Production.ShopFloor.ConsumptionOrderLines
```


```
10:   SUM EXP: 20  ATTRIB: QuantityBaseValue 
20:   FILTER EXP: 30  EXP: 70 
30:   SELECT REPO: Logistics.Inventory.CurrentBalances  EXP: 40 
40:   WHERE EXP: 50 
50:   EQUAL ATTRIB: ProductId  EXP: 60 
60:   GETOBJVALUE INPUT: 10  ATTRIB: ProductId 
70:   AND EXP: 100  EXP: 80 
80:   AND EXP: 130  EXP: 90 
90:   AND EXP: 150  EXP: 170 
100: EQUAL ATTRIB: StoreId  EXP: 110 
110: CAST EXP: 120  CONST: System.Guid 
120: GETOBJVALUE INPUT: 10  ATTRIB: StoreId 
130: EQUAL ATTRIB: StoreBinId  EXP: 140 
140: GETOBJVALUE INPUT: 10  ATTRIB: StoreBinId 
150: EQUAL ATTRIB: LotId  EXP: 160 
160: GETOBJVALUE INPUT: 10  ATTRIB: LotId 
170: EQUAL ATTRIB: SerialNumberId  EXP: 180 
180: GETOBJVALUE INPUT: 10  ATTRIB: SerialNumberId 
```

>
> Explanation:
>
> 10:   Sum Quantity Base from the filtered list returned by EXP:20
>
> 20:   Filter the list from EXP: 30 by the clauses of EXP: 70 
>
> 30:   Select repository "Logistics.Inventory.CurrentBalances" and filter by the clauses in EXP: 40 
>
> 40:   Filter the list above by the records WHERE/in which the clauses in EXP: 50 are True
>
> 50:   Check whether ATTRIB: ProductId is equal to EXP: 60 
>
> 60:   Get ATTRIB:ProductId from the repository of EXP:10
>
> 70:   EXP: 100 and EXP: 80 
>
> 80:   EXP: 130 and EXP: 90 
>
> 90:   EXP: 150 and EXP: 170 
>
> 100: Check whether ATTRIB:StoreId is EQUAL to EXP: 110 
>
> 110: CAST EXP: 120  to System.Guid 
>
> 120: Get ATTRIB:StoreId from the repository of EXP:10
>
> 130: Check whether ATTRIB: StoreBinId is EQUAL to EXP: 140
>
> 140: Get ATTRIB: StoreBinId from the repository of EXP:10
>
> 150: Check whether ATTRIB: LotId is EQUAL to EXP: 160 
>
> 160: Get ATTRIB: LotId from the repository of EXP:10
>
> 170: Check whether ATTRIB: SerialNumberId is EQUAL to EXP: 180 
>
> 180: Get ATTRIB: SerialNumberId from the repository of EXP:10
