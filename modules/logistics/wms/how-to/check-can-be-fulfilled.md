## Check if a dispatch order can be fulfilled

Planning a dispatch Warehouse Order usually leads to the question “Can this order be fulfilled?” i.e. is there enough availability to dispatch all lines of this order?
To answer this question we have created a set of three calculated attributes:

* **"Can Be Fulfilled" attribute in the Warehouse Order Header**

It returns “true” if there is enough availability for all lines of the current Warehouse Order. The attribute can be shown in the Warehouse Orders navigator to help guide the planners on which Warehouse Orders require their attention.

* **"Line Can Be Fulfilled" attribute in the Warehouse Order Lines**

It returns “true” if there is enough availability for all lines. If it returns “false” it means that there is not enough availability to execute this line and the planner needs to review it and probbaly make some decisions and adjustments before releasing the order – e.g. to select a different lot, to cancel the order, to execute as much as is available and request the rest, etc.

* **"Available Quantity Base" attribute in the Warehouse Order Lines**

It returns the sum of the Available Quantity Base for this line. It takes into account whether there is a particular Warehouse Location, Lot, Serial Number, Variant, or Logistic Unit that is specified in the line and shows the availability according to these criteria. 

### Calculated attributes expression
Here is a list with the calculated attribute expressions. Of course, еach attribute can be modified by the implementatior according to the organization's needs.

> **_NOTE:_** You can easily create these attributes in your database by copy-pasting their expression into your database.

* **"Can Be Fulfilled" attribute**

Repository: Logistics.Wms.WarehouseOrders

| Exp No | Operator | Parameter1 | P1 Value | Parameter2 | P2 Value | Parameter3 | P3 Value |
| ------ | -------- |----------- |--------- |----------- |--------- |----------- |--------- |
| 	10	 | 	IIF	 | 	EXP	 | 	20	 | 	CONST	 | 	FALSE	 | 	CONST	 | 	TRUE	 |
| 	20	 | 	GTE	 | 	EXP	 | 	30	 | 	CONST	 | 	1	 |				
| 	30	 | 	COUNT	 | 	EXP	 | 	40	 | 		 | 		 |				
| 	40	 | 	FILTER	 | 	CHILD	 | 	Lines	 | 	EXP	 | 	50	 |				
| 	50	 | 	EQUAL	 | 	ATTRIB	 | 	#LineCanBeFulfilled	 | 	CONST	 | 	FALSE	 |				

* **"Line Can Be Fulfilled" attribute**

Repository: Logistics.Wms.WarehouseOrderLines

| Exp No | Operator | Parameter1 | P1 Value | Parameter2 | P2 Value | Parameter3 | P3 Value |
| ------ | -------- |----------- |--------- |----------- |--------- |----------- |--------- |
| 	10	 | 	IIF	 | 	EXP	 | 	20	 | 	CONST	 | 	TRUE	 | 	CONST	 | 	FALSE	 |
| 	20	 | 	GTE	 | 	ATTRIB	 | 	#AvailableQuantityBase	 | 	ATTRIB	 | 	QuantityBaseValue	 |				

* **"Available Quantity Base" attribute**

Repository: Logistics.Wms.WarehouseOrderLines

| Exp No | Operator | Parameter1 | P1 Value | Parameter2 | P2 Value | Parameter3 | P3 Value |
| ------ | -------- |----------- |--------- |----------- |--------- |----------- |--------- |
| 	100	 | 	SUM	 | 	EXP	 | 	200	 | 	ATTRIB	 | 	QuantityBaseAvailable	 |				
| 	200	 | 	IIF	 | 	EXP	 | 	210	 | 	EXP	 | 	300	 | 	EXP	 | 	230	 |
| 	210	 | 	EQUAL	 | 	EXP	 | 	220	 | 	CONST	 | 	NULL	 |				
| 	220	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	WarehouseLocationId	 |				
| 	230	 | 	FILTER	 | 	EXP	 | 	300	 | 	EXP	 | 	240	 |				
| 	240	 | 	EQUAL	 | 	ATTRIB	 | 	WarehouseLocationId	 | 	EXP	 | 	250	 |				
| 	250	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	WarehouseLocationId	 |				
| 	300	 | 	IIF	 | 	EXP	 | 	310	 | 	EXP	 | 	400	 | 	EXP	 | 	330	 |
| 	310	 | 	EQUAL	 | 	EXP	 | 	320	 | 	CONST	 | 	NULL	 |				
| 	320	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	LotId	 |				
| 	330	 | 	FILTER	 | 	EXP	 | 	400	 | 	EXP	 | 	340	 |				
| 	340	 | 	EQUAL	 | 	ATTRIB	 | 	LotId	 | 	EXP	 | 	350	 |				
| 	350	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	LotId	 |				
| 	400	 | 	IIF	 | 	EXP	 | 	410	 | 	EXP	 | 	500	 | 	EXP	 | 	430	 |
| 	410	 | 	EQUAL	 | 	EXP	 | 	420	 | 	CONST	 | 	NULL	 |				
| 	420	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	SerialNumberId	 |				
| 	430	 | 	FILTER	 | 	EXP	 | 	500	 | 	EXP	 | 	440	 |				
| 	440	 | 	EQUAL	 | 	ATTRIB	 | 	SerialNumberId	 | 	EXP	 | 	450	 |				
| 	450	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	SerialNumberId	 |				
| 	500	 | 	IIF	 | 	EXP	 | 	510	 | 	EXP	 | 	600	 | 	EXP	 | 	530	 |
| 	510	 | 	EQUAL	 | 	EXP	 | 	520	 | 	CONST	 | 	NULL	 |				
| 	520	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	ProductVariantId	 |				
| 	530	 | 	FILTER	 | 	EXP	 | 	600	 | 	EXP	 | 	540	 |				
| 	540	 | 	EQUAL	 | 	ATTRIB	 | 	ProductVariantId	 | 	EXP	 | 	550	 |				
| 	550	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	ProductVariantId	 |				
| 	600	 | 	IIF	 | 	EXP	 | 	610	 | 	EXP	 | 	1000	 | 	EXP	 | 	630	 |
| 	610	 | 	EQUAL	 | 	EXP	 | 	620	 | 	CONST	 | 	NULL	 |				
| 	620	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	LogisticUnitId	 |				
| 	630	 | 	FILTER	 | 	EXP	 | 	2000	 | 	EXP	 | 	640	 |				
| 	640	 | 	EQUAL	 | 	ATTRIB	 | 	LogisticUnitId	 | 	EXP	 | 	650	 |				
| 	650	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	LogisticUnitId	 |				
| 	1000	 | 	FILTER	 | 	EXP	 | 	2000	 | 	EXP	 | 	1100	 |				
| 	1100	 | 	EQUAL	 | 	ATTRIB	 | 	ProductId	 | 	EXP	 | 	1200	 |				
| 	1200	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	ProductId	 |				
| 	2000	 | 	SELECT	 | 	REPO	 | 	Logistics.Wms.WarehouseAvailabilityView	 | 	EXP	 | 	2100	 |				
| 	2100	 | 	WHERE	 | 	EXP	 | 	2200	 | 	EXP	 | 	2400	 |				
| 	2200	 | 	EQUAL	 | 	ATTRIB	 | 	ProductId	 | 	EXP	 | 	2300	 |				
| 	2300	 | 	GETOBJVALUE	 | 	INPUT	 | 	100	 | 	ATTRIB	 | 	ProductId	 |				
| 	2400	 | 	GT	 | 	ATTRIB	 | 	StandardQuantityAvailable	 | 	CONST	 | 	0	 |				
