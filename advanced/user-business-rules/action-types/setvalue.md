---
uid: brat-SETVALUE
items: ActionTypes
---

# SETVALUE

This action type is used to implicitly update information or data in the system. When all conditions of a business rules are met and a specified event happens, **SETVALUE** updates the value of the specified attribute available for the repository, including custom properties of the particular entity.

The action requires the following parameters:

- **Parameter 1** - the updated (or set) value. Currently, the available parameter type is 'Attribute'. 

You should enter the name of the attribute whose value needs to be modified. 

- **Parameter 2** - the value set in Parameter 1. The available parameter types are 'Attribute' and 'Constant'. 

    * If the parameter type is 'Attribute', select the name of the attribute in the parameter value. <br>This value will be used to as a value for **Parameter 1**. 
    * If the parameter type is 'Constant', enter a constant in the parameter value. <br> Every time the user business rule is executed, **Parameter 1** will be set to a constant value. 
        
The format of the different types of constants is described **[here](https://docs.erp.net/tech/advanced/calculated-attributes/parameter-types/const.html)**.
**Example:**

| Repository            |                 |                    |                  |                 |                  |
| --------------------- | --------------- | ------------------ | ---------------- | --------------- | ---------------- |
| Crm.Sales.SalesOrders |                 |                    |                  |                 |                  |
| **Events**            |                 |                    |                  |                 |                  |
| Event type            | Event parameter | Execution priority |                  |                 |                  |
| Change of state       | RELEASING       | Normal             |                  |                 |                  |
| **Actions**           |                 |                    |                  |                 |                  |
| Action No             | Action type     | Parameter1 type    | Parameter1 value | Parameter2 type | Parameter2 value |
| 1                     | SETVALUE        | Attribute          | Notes            | Constant        | 'Approved'       |
