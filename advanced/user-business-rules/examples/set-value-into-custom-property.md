---
items: UserBusinessRuleExamples
---

# How to use business rules to set a value into a custom property?

You can use **[business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** to set values into different fields, including custom properties **[action types](https://docs.erp.net/tech/advanced/user-business-rules/action-types/index.html)**. 

To set a value into a custom property, you'll either copy or get that value from another custom property. Alternatively, you can use an attribute/field/constant with data type 'String'.

**Example 1** 

Let's say you have a sales order document.

If you want to copy a value from a specific custom property and set it as a value in another custom property, you can create a user business rule with the following data:

Repository|
|:----|
Crm.Sales.SalesOrders|

Events|
|:----|

Event type|Event parameter|Execution priority
|:----|:----|:----|
Change of State|RELEASING|Normal

Actions|
|:----|

Action No|Action type|Parameter1 type|Parameter1 value|Parameter2 type|Parameter2 value
|:----|:----|:----|:----|:----|:----|
1|SETVALUE|Attribute|@Property1|Attribute|@Property2|

> [!NOTE] 
> 
> Both the custom property's **value** and **description** are copied.

> [!NOTE] 
> 
> In this case, there are **NO** limitations for custom properties in which you set the value to inherit its allowed values from another entity or custom property. The only condition is the setting in both custom properties to follow the principles described in **Inheriting and copying custom properties**.

**Example 2** 

Let's say you have a sales order document.

If you want to set a specific value for a custom property that's not copied from another custom property's value, you can create a **user business rule** with the following data:

Repository| 
|:----| 
Crm.Sales.SalesOrders| 

Events| 
|:----| 

Event type|Event parameter|Execution priority
|:----|:----|:----
Change of State|RELEASING|Normal

Actions| 
|:----| 

Action No|Action type|Parameter1 type|Parameter1 value|Parameter2 type|Parameter2 value
|:----|:----|:----|:----|:----|:----
1|SETVALUE|Attribute|@PropertyCode|Constant|'StringValue01

> [!NOTE] 
> 
> Using this method, you can only set the custom property's **value** - not its description. An exception is when you're setting a value defined as a _Property Allowed_ value.

> [!NOTE] 
> 
> _Parameter2 Type_ is not limited to a constant. You could use the attribute type as well and load the value from another system attribute or a **[calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)**. However, the value **must** be from a 'String' type. Otherwise, you can **[CAST](https://docs.erp.net/tech/advanced/calculated-attributes/operators/cast.html)** or **[CONVERT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/convert.html)** it.

If a custom property has allowed values, you may want to set one of them as a value of the particular property. This is possible only when the property **doesn't** inherit its allowed values from another entity. 

Custom properties can inherit their values from another custom property or have them manually defined in the **Property Allowed Values** panel. If one value is set by a business rule, it'll be recognized as an allowed value for this property. The value's description will then be inherited as well.
