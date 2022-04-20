# Warehouse policies

Warehouse policies is a hierarchical system for applying policies to warehouse operations. 


# Policy kind
Warehouse policies have diferent kinds/types which specify what the actual action of the policy is. The list of the policy kinds is system predifined.  


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
