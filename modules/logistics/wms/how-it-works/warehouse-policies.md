# Warehouse policies

Warehouse policies is a hierarchical system for applying policies to warehouse operations. 


# Policy kind
Warehouse policies have diferent kinds/types which specify what the actual action of the policy is. 

The list of the policy kinds is system predifined.  

| Type | Description |
| :------ | :----------------- |
| AllowProductChange   |  Allows execution with а different product than the ordered. <br /> If _ApplicablePolicy = null_ or _ApplicablePolicy.Value_ _== false_ and _WarehouseOrderLine.Product != null_, <br /> then when executing in _Orders_, it’s not possible to define _Product != WarehouseOrderLine.Product_. <br /> If another value is defined, an error sound will play, along with the appearance of a popup message: <br /> <br /> _“Product change is not allowed. Please select the suggested product.”_  <br /><br /> • Stored as 'APC'. <br /> • Database Value: 'APC' <br /> • Model Value: 0 <br /> • Domain API Value: 'AllowProductChange'     |
| AllowLotChange   | Allows execution with a different lot than the ordered. <br /> If _Value == false_ and _WarehouseOrderLine.Lot != null_, then when executing in _Orders_, it’s not possible to define product _Lot !=WarehouseOrderLine.Lot_. <If another value is defined, an error sound is played, along with the appearance of a popup message: <br /><br /> _“Lot change is not allowed. Please select the suggested lot.”_ <br /><br /> • Stored as 'ATC'. <br /> • Database Value: 'ATC' <br /> • Model Value: 1 <br /> • Domain API Value: 'AllowLotChange'         |
| AllowLocationChange   | Allows execution from a different location than the ordered. <br /> If _Value == false_ and _WarehouseOrderLine.Location != null_, then when executing in _Orders_, it’s not possible to define product _Location != WarehouseOrderLine.Location_. If another value is defined, an error sound is played, along with the appearance of a popup message: <br /><br /> _"Location change is not allowed. Please select the suggested location."_  <br /><br /> • Stored as 'ALC'. <br /> • Database Value: 'ALC' <br /> • Model Value: 2 <br /> • Domain API Value: 'AllowLocationChange'|
| AllowUnitChange   | Allows execution of a quantity in a different measurement unit than the ordered. <br /> If _Value == false_ and _WarehouseOrderLine.QuantityUnit != null_, then when executing in _Orders_, it’s not possible to define product _QuantityUnit != WarehouseOrderLine.QuantityUnit_. If another value is defined, <br /> an error sound is played, along with the appearance of a popup message: <br /> <br />  _"Quantity Unit change is not allowed. Please select the suggested quantity unit."_ <br /><br /> • Stored as 'AUC'. <br /> • Database Value: 'AUC' <br /> • Model Value: 3 <br /> • Domain API Value: 'AllowUnitChange' |
| RequireSourceScan   | Requires scanning of the source location when moving or dispatching. <br /> If _Value == true_, then when executing in _Orders_, the **USE** button in the Location screen will be hidden, while the Availability table will be inaccessible.  <br /><br /> • Stored as 'RSS'. <br /> • Database Value: 'RSS' <br /> • Model Value: 4 <br /> • Domain API Value: 'RequireSourceScan' |
| RequireDestinationScan   | Requires scanning of the destination location when moving or receiving. <br /> If _Value == true_, then when executing in _Orders_, the **USE** button in the Destination screen will be hidden. <br /><br /> • Stored as 'RDS'. <br /> • Database Value: 'RDS' <br /> • Model Value: 5 <br /> • Domain API Value: 'RequireDestinationScan' |
| AllowLineSkip   | Allows skipping of an order line when executing (allow quantity = 0). Not planned for release at the moment. <br /><br /> • Stored as 'ALS'. <br /> • Database Value: 'ALS' <br /> • Model Value: 6 <br /> • Domain API Value: 'AllowLineSkip' |
| ZoneType   | Specifies the type of zone for receiving, shipping, packing, etc. <br /> It can have the following values: **picking**, **packing**, **receiving**, **shipping**, and **storage**. According to the _Zone Policies_ rule, the policy has a "Zone" and there are no “Product”, “Product group” or “Product type” fields.  <br /><br /> • Stored as 'ZTY'. <br /> • Database Value: 'ZTY' <br /> • Model Value: 7 <br /> • Domain API Value: 'ZoneType'



# Applicability

You set up each warehouse policy by defining the conditions where it applies, to which products and for how long. 
Each warehouse policy can apply to:

* Warehouse

* Zone and its sub-zones

* Product group and its sub-groups

* Product type

* Specific product

* From date

* To date

NOTE: Some policies can be applied only at the warehouse or zone level.

 

# Importance

Policies have importance. When evaluating a policy, the setting with the highest importance is applied.

For example, if a policy is applied to a root zone and to a sub-zone, the importance of the sub-zone setting determines which setting will be applied:

* If the sub-zone setting has higher priority, it will be applied.

This can be used for hierarchical application of policies for zones.

* If the root zone setting has higher priority, it will be applied. 

This can be used for root zone (or even warehouse level) setting, which overrides the setting for specific zones.


Importance is an integer value, allowing even negative numbers (for very low importance).
