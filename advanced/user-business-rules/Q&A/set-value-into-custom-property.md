# How to use business rules to set a value into a custom property?
We can use business rules to set values into different fields, including custom properties [action types](https://docs.erp.net/tech/advanced/user-business-rules/action-types/index.html). Currently, if we want to set a value into a custom property, we can either copy/get that value from another custom property or use an attribute/field/ constant whose data type is String.
 
### Example 1 - The value is copied from another Custom Property's value:
If we want to copy a value from a specific Custom Property and set it as a value for another Custom Property in a sales order document, for example, then we can create a [user business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)  with the following data:

Repository
|:----
Crm.Sales.SalesOrders

Events
|:----

Event type|Event parameter|Execution priority
|:----|:----|:----
Change of State|RELEASING|Normal

Actions
|:----

Action No|Action type|Parameter1 type|Parameter1 value|Parameter2 type|Parameter2 value
|:----|:----|:----|:----|:----|:----
1|SETVALUE|Attribute|@Property1|Attribute|@Property2

> [!Note]
> Both Custom Property's **Value** and Custom Property's **Description** are copied.
 
> [!Note]
> In this case, there are no limitations if the Custom Properties in which we set the value to inherit its allowed values from another Entity or Custom Property. The only condition is the setting in both Custom Properties to be compatible according to the principles described in the topic **Inheriting and copying custom properties**.
 
### Example 2 -  Set a specific value that is not copied from another Custom Property's value:

If we want to set a specific value (that is not copied from another Custom Property's value) for a Custom Property in a sales order document, then we can create a [user business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html) with the following data:

Repository
|:----
Crm.Sales.SalesOrders

Events
|:----

Event type|Event parameter|Execution priority
|:----|:----|:----
Change of State|RELEASING|Normal

Actions
|:----

Action No|Action type|Parameter1 type|Parameter1 value|Parameter2 type|Parameter2 value
|:----|:----|:----|:----|:----|:----
1|SETVALUE|Attribute|@PropertyCode|Constant|'StringValue01

> [!Note]
> Using this method, we can **only** set the Custom Property's Value and **not** its description. An exception is made when we are setting a value that is defined as a Property Allowed value. For more info, see the section below.

> [!Note]
> Parameter2 Type is not limited to a Constant. We could use the attribute type as well and load the value from another system attribute or a [calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html). Note, however, that the value must be from a string type. If it is not, you can cast or convert it using a calculated attribute for the user business rule.

#### But what if the custom property has allowed values, and we want to set one of them?

This functionality is supported even when the custom property has allowed values, and we want to set one of them as a value of the particular property, but only if the property **does not** inherit its allowed values from another entity. 

When custom properties inherit their values from another custom property or their values are manually defined in the 'Property Allowed Values' panel - if one of these values is set by a [business rule](https://docs.erp.net/tech/advanced/user-business-rules/business-rules/index.html), it will be recognized as an allowed value for this property. In this case, the Allowed Value's description will be inherited as well.
