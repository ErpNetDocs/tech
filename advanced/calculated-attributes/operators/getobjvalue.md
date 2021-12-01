---
uid: cao-GETOBJVALUE
items: Operators
---

# GETOBJVALUE 

| Specification| Value|
| ---- | ----- |
| Description| Gets a value from a specified object. Used when you want to retrieve a value from an object different from the current one. That object is listed in the _Repository Name_ field of the current row.|
| Parameter 1 Name| obj |
| Parameter 1 Type| object |
| Parameter 2 Name| value |
| Parameter 2 Type| attribute value |
| Parameter 3 Name| - |
| Parameter 3 Type| - |
| Return value| Returns value from obj. |


**Example:**

Let's return the value of _Default Delivery Term Days_ set in the definition of a customer in a sales order:
```
10: GETOBJVALUE REF:Customer ATTRIB:DefaultDeliveryTermDays
```
OUTPUT: <br> If 'DefaultDeliveryTermDays = 5', the output will be '5'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrders*

#### More examples:

- **[Check if a value of a field is changed in the adjustment document](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-field-is-changed-in-adjustment.html)**
- **[Get value and description of referent object](https://docs.erp.net/tech/advanced/calculated-attributes/examples/get-value-and-description-of-referent-object.html)**
