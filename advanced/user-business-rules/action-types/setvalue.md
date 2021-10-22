---
uid: brat-SETVALUE
items: ActionTypes
---

# SETVALUE

The SETVALUE action is used to update information or data in the  system implicitly. When all conditions of the business rules are met and the specified event has happened, then the SETVALUE action updates the  value of the specified attribute available for the repository (including the custom properties for the particular entity).

The SETVALUE action requires the following parameters:

1. Parameter 1 - the value which is updated (set). Currently, the available  parameter type is Attribute. So, in Parameter 1 value the user enters  the name of the attribute, which value has to be modified.
2. Parameter 2 - the value which is set in Parameter 1. Currently, the available  parameter types are AAttribute and Constant. If the parameter type is Attribute, in parameter value the name of the attribute is selected.  The selected attribute value would be used to be set as value of  parameter 1. If the parameter type is Constant, then in parameter  value a constant value has to be entered and every time the user  business rule is execute, the parameter 1 attribute would be set to the  constant value. The format of the different type of constants is  described here: [Parameter Type CONST](https://docs.erp.net/tech/advanced/calculated-attributes/parameter-types/const.html).



Example:

| Repository            |                 |                    |                  |                 |                  |
| --------------------- | --------------- | ------------------ | ---------------- | --------------- | ---------------- |
| Crm.Sales.SalesOrders |                 |                    |                  |                 |                  |
| **Events**            |                 |                    |                  |                 |                  |
| Event Type            | Event Parameter | Execution Priority |                  |                 |                  |
| Change of State       | RELEASING       | Normal             |                  |                 |                  |
| **Actions**           |                 |                    |                  |                 |                  |
| Action No             | Action Type     | Parameter1 Type    | Parameter1 Value | Parameter2 Type | Parameter2 Value |
| 1                     | SETVALUE        | Attribute          | Notes            | Constant        | 'Approved'       |
