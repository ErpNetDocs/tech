---
uid: cao-GETOBJVALUE
---

# GETOBJVALUE - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the specified value from the specified object. This operator is used when the user wants the retrieve a value from object different than the current one. The current object is listed in the 'Repository Name' field in the current row.          |
| Parameter 1 Name      | obj                                                        |
| Parameter 1 Type      | object                                    |
| Parameter 2 Name      | value                                                            |
| Parameter 2 Type      | attribute value                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Returns value from obj.                                                       |


## Example
The Repository in this example is Crm.Sales.SalesOrders.
```
10: GETOBJVALUE REF:Customer ATTRIB:DefaultPaymentAccountId 
```
This line returns the Id of the Default Payment Account set in the Customer's definition of the current Sales Order.

This value could be used to set the Payment Account in Sales Order through a User Business Rules, for example.
