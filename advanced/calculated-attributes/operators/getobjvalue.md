---
uid: cao-GETOBJVALUE
items: Operators
---

# GETOBJVALUE 

| Specification| Value|
| ---- | ----- |
| Description| Gets the specified value from the specified object. This operator is used when the user wants the retrieve a value from object different than the current one. The current object is listed in the 'Repository Name' field in the current row.|
| Parameter 1 Name| obj |
| Parameter 1 Type| object |
| Parameter 2 Name| value |
| Parameter 2 Type| attribute value |
| Parameter 3 Name| - |
| Parameter 3 Type| - |
| Return Value| Returns value from obj. |


## Example

The following example returns the value of the field 'Default Delivery Term Days' set in the definition of the customer set the current sales order:
```
10: GETOBJVALUE REF:Customer ATTRIB:DefaultDeliveryTermDays
```
OUTPUT: If 'DefaultDeliveryTermDays = 5', the output will be '5'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrders*

#### More examples:
- **[Check if a value of a field is changed in the adjustment document](https://docs.erp.net/tech/advanced/calculated-attributes/examples/check-if-field-is-changed-in-adjustment.html)
- **[Get value and description of referent object](https://docs.erp.net/tech/advanced/calculated-attributes/examples/get-value-and-description-of-referent-object.html)**
