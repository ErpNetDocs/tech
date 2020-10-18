---
uid: cao-GETOBJVALUE
items: Operators
---

# GETOBJVALUE - Calculated Attribute Operator

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

The following example returns the value of the field 'Default Delivery Term Days' set in the definition of the Customer set the current Sales Order:
```
10: GETOBJVALUE REF:Customer ATTRIB:DefaultDeliveryTermDays
```
OUTPUT: If 'DefaultDeliveryTermDays = 5', the output will be '5'.

> [!NOTE]
> The repository of the attribute is *Crm.Sales.SalesOrders*

#### More Examples
[Check If a Value of a Field Is Changed in the Adjustment Document](../examples/CheckIfAValueOfAFieldIsChangedInTheAdjustmentDocument.md)
<br/>[Get Value And Description Of Referent Object](../examples/GetValueAndDescriptionOfReferentObject.md)
