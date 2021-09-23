# How to Use Business Rules to Set a Value into a Custom Property?
We can use Business rules to set values into different fields, including custom properties (**[User Business Rules Actions - Action Types](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/action-types/index.md)**). Currently, if we want to set a value into a custom property, we can either copy/ get that value from another custom property or use an attribute/ field/ constant whose data type is String.
 
### Example 1 - The value is copied from another Custom Property's value:
If we want to copy a value from a specific Custom Property and set it as a value for another Custom Property in a Sales Order Document, for example, then we can create a **[User Business Rule](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/index.md)**  with the following data:

Repository
|:----
Crm.Sales.SalesOrders

Events
|:----

Event Type|Event Parameter|Execution Priority
|:----|:----|:----
Change of State|RELEASING|Normal

Actions
|:----

Action No|Action Type|Parameter1 Type|Parameter1 Value|Parameter2 Type|Parameter2 Value
|:----|:----|:----|:----|:----|:----
1|SETVALUE|Attribute|@Property1|Attribute|@Property2

> [!Note]
> Both Custom Property's Value and Custom Property's Description are copied.
 
> [!Note]
> In this case, there are no limitations if the Custom Properties in which we set the value to inherit its allowed values from another Entity or Custom Property. The only condition is the setting in both Custom Properties to be compatible according to the principles described in the topic **Inheriting and Copying Custom Properties**.
 
### Example 2 -  Set a specific value that is not copied from another Custom Property's value:

If we want to set a specific value (that is not copied from another Custom Property's value) for a Custom Property in a Sales Order Document, then we can create a **[User Business Rule](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/index.md)** with the following data:

Repository
|:----
Crm.Sales.SalesOrders

Events
|:----

Event Type|Event Parameter|Execution Priority
|:----|:----|:----
Change of State|RELEASING|Normal

Actions
|:----

Action No|Action Type|Parameter1 Type|Parameter1 Value|Parameter2 Type|Parameter2 Value
|:----|:----|:----|:----|:----|:----
1|SETVALUE|Attribute|@PropertyCode|Constant|'StringValue01

> [!Note]
> Using this method, we can only set the Custom Property's Value and not its Description. An exception is made when we are setting a value that is defined as a Property Allowed value. For more info, see the 'But what if the custom property has allowed values and we want to set one of them?' section below.

> [!Note]
> Parameter2 Type is not limited to a Constant. We could use the Attribute type as well and load the value from another system Attribute or a **[Calculated Attribute](https://github.com/ErpNetDocs/tech/blob/master/advanced/calculated-attributes/index.md)**. Note, however, that the value must be from a String type. If it is not, you can cast or convert the value to a String using a **[Calculated Attribute](https://github.com/ErpNetDocs/tech/blob/master/advanced/calculated-attributes/index.md)** and use that **[Calculated Attribute](https://github.com/ErpNetDocs/tech/blob/master/advanced/calculated-attributes/index.md)** in the  **[User Business Rule](https://github.com/ErpNetDocs/tech/blob/master/advanced/business-rules/index.md)**.

#### But what if the custom property has allowed values, and we want to set one of them?

This functionality is supported even when the custom property has allowed values, and we want to set one of them as a value of the particular property, but **only if the property does not inherit its** allowed values from another entity. 

When custom properties inherit their values from another custom property or their values are manually defined in the “Property Allowed Values” panel - if one of these values is set by a Business rule it will be recognized as an allowed value for this property. In this case, the Allowed Value's Description will be inherited as well.
