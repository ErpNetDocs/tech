---
uid: warehouse-policies
---

# Warehouse policies

Warehouse policies are a hierarchical system for applying policies when working with the WMS module.

The most important properties that any policy has are policy kind and value. Policy kinds are predifined system types, which specify the usage of the policy. 
Different policy kinds have different effect on the system. Some kinds manage certain restrictions during the operations execution of operations, others affect the WMS Worker app's interface, while others store important values that are used by the calculation algorithms.

Warehouse policies can be set up for different warehouses, zones or even product groups, depening on the meaning of the kind of the particular policy. We can also specify if one policy is more important than another policy of the same kind, which compliments the hierarchical structure of the policies and allows flexibility.


# Available policy kinds
Policy kinds specify what the actual action of the policy is. 

The list of the policy kinds is system predifined.  

| Kind | Details |
| :------ | :----------------- |
| AllowProductChange   | **Description:** Allows execution with a different product than the ordered. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/> If there is an applicable policy to the line and its value is „false“, then the Product which was initially specified in the Warehouse Order Line cannot be changed during the line execution. <br/><br/> If the user tries to enter a different product, the app will make a negative sound and will display a pop message: _“Product change is not allowed. Please select the suggested product.”_ <br/><br/> Otherwise, the Product can be changed during the execution.  |
| AllowLotChange   | **Description:** Allows execution with a different lot than the ordered. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/>  If there is an applicable policy to the line and its value is „false“, then the Lot (if any) which was initially specified in the Warehouse Order Line cannot be changed during the line execution. <br/><br/>  If the user tries to enter a different lot, the app will make a negative sound and will display a pop message: _“Lot change is not allowed. Please select the suggested lot.”_ <br/><br/> Otherwise, the Lot can be changed during the execution.  |
| AllowLocationChange   |**Description:** Allows execution from a different location than the ordered. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/> If there is an applicable policy to the line and its value is „false“, then the Warehouse Location (if any) which was initially specified in the Warehouse Order Line cannot be changed during the line execution. <br/><br/> If the user tries to enter a different location, the app will make a negative sound and will display a pop message: _"Location change is not allowed. Please select the suggested location."_ <br/><br/> Otherwise, the Location can be changed during the execution. |
| AllowUnitChange   | **Description:**_ Allows execution of a quantity in a different measurement unit than the ordered. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/> If there is an applicable policy to the line and its value is „false“, then the Quantity Unit which was initially specified in the Warehouse Order Line cannot be changed during the line execution. <br/><br/> If the user tries to enter a different quantity unit, the app will make a negative sound and will display a pop message: _"Quantity Unit change is not allowed. Please select the suggested quantity unit."_ <br/><br/> Otherwise, the Unit can be changed during the execution.  |
| RequireSourceScan   | **Description:** Requires scanning of the source location when receiving, moving or dispatching. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/> If there is an applicable policy to the line and its value is „true“, then the interface of the Location screen won‘t allow easy selection of the Warehouse Location. <br/><br/> The USE button will be hidden and the selection through the availability table will be inactive. |
| RequireDestinationScan   | **Description:** Requires scanning of the destination location when moving. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/> If there is an applicable policy to the line and its value is „true“, then the interface of the Destination screen won‘t allow easy selection of the Warehouse Location. <br/><br/> The USE button will be hidden and the selection through the availability table will be inactive. |
| RequireProductScan   | **Description:** Requires scanning of the product. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders execution in the WMS Worker app. <br/><br/> If there is an applicable policy to the line and its value is „true“, then the interface of the Product screen won‘t allow easy selection of the Product. <br/><br/> The USE button will be hidden and the selection through the availability table will be inactive. |
| AllowLineSkip   | **Description:** Allows skipping of an order line when executing (allow quantity = 0). <br/><br/> Not planned for release at the moment.  |
| ZoneType   | **Description:** Specifies the type of zone for receiving, shipping, packing, etc. <br/> Can be saved only if the Warehouse and Zone fields are filled in. <br/> The policy is hierarchical, this means that if it set for a particular zone it will applies to all of its subzones. <br/><br/> **Possible values:** picking, packing, receiving, shipping, and storage. <br/><br/> **Action:** Currenty only the picking value is taken into account of the algorithms. It is used by the [Suggest warehouse locations funtion](xref:suggest-warehouse-locations).|
| KittingControllingLevel | **Description:** Used when working with composite products. Specifies the level of control during the kitting of the composite product’s components. <br/><br/> **Possible values:** 10, 20, 30, 40, 50 <br/><br/> **Action:** Depends on the specified level. For more information, see @levels .|
| DekittingControllingLevel | **Description:** Used when working with composite products. Specifies the level of control during the dekitting of the composite product. <br/><br/> **Possible values:** 10, 20, 30, 40, 50 <br/><br/> **Action:** Depends on the specified level. For more information, see @levels .|
| GS1SSCCCompanyPrefix | **Description:** Used when working with logistic units and GS1 SSCC barcodes. Specifies the GS1 company prefix issued by the national SG1 organization. <br/><br/> **Possible values:** а digit number <br/><br/> **Action:** Used by alghorithm that generates SSCC codes of the logistic units.|
| GS1SSCCNextSerial | **Description:** Used when working with logistic units and GS1 SSCC barcodes. Specifies the next reference serial number used when generating SSCC codes. А digit number acting as a counter: e.g. 0000001, 0000002… Must be set up after the GS1SSCCCompanyPrefix policy, because its allowed lenght depends on the GS1SSCCCompanyPrefix value's lenght.<br/><br/> **Possible values:** а digit number, with lenght that is equal to "16 - GS1CompanyPrefix value's lenght".<br/><br/> **Action:** Used by alghorithm that generates SSCC codes of the logistic units.|
|CustomRouting|**Description:** Specifies a custom routing, based on a user-defined attribute of the locations. The policy specifies the code of the user-defined attribute, whose values contain the sequence of the route. The custom routing is employed by the Suggest Routing function and can be defined only at warehouse level.<br/><br/> **Possible values:** all values are possible, but only a value of a Custom Property Code, which has values in the Warehouse Locations table will affect the Suggest Routing Function <br/><br/> **Action:** The Suggest Routing function in the Warehouse Order Execution will use the Custom Property Values in the Warehouse Locations panel. The Suggest Routings function will suggest Locations in the order described in the Custom Property Values. The values are taken as a string, so you have to write the values in this format 001,002,003...010..100.|
| UnassignedOrdersSectionVisibility | **Description:** Depending on your warehouse's organization, you can prevent warehouse workers from seeing and taking Unassigned orders. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders list in the WMS Worker app. <br/><br/>If there is an applicable policy to the Warehouse and its value is „false“, then the Unassigned section will be hidden from the Workers' orders list in this Warehouse. <br/><br/> If there is an applicable policy to the Warehouse and its value is „true“ or there is no defined policy, then the Unassigned section will be visible in the Workers' orders list in this Warehouse. |
| StartedByOthersSectionVisibility | **Description:** Depending on your warehouse's organization, you can prevent warehouse workers from seeing and joining Started by others orders. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders list in the WMS Worker app. <br/><br/>If there is an applicable policy to the Warehouse and its value is „false“, then the Stared by Others section will be hidden from the Workers' orders list in this Warehouse. <br/><br/> If there is an applicable policy to the Warehouse and its value is „true“ or there is no defined policy, then the Started by Others section will be visible in the Workers' orders list in this Warehouse. |
| AssignedToOthersSectionVisibility | **Description:** Depending on your warehouse's organization, you can prevent warehouse workers from seeing and taking Assigned to Others orders. <br/><br/> **Possible values:** true, false <br/><br/> **Action:** Used in the Orders list in the WMS Worker app. <br/><br/>If there is an applicable policy to the Warehouse and its value is „false“, then the Assigned to Others section will be hidden from the Workers' orders list in this Warehouse. <br/><br/> If there is an applicable policy to the Warehouse and its value is „true“ or there is no defined policy, then the Assigned to Others section will be visible in the Workers' orders list in this Warehouse. |



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
