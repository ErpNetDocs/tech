---
uid: cao-LIST
---

# LIST - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Returns a list with the string values of the specified attribute of the list of objects.The values in the created list are separated by a separator. If there is no indicated separator, then the list is separated with ", " (comma + space) by default.           |
| Parameter 1 Name      | list                                                         |
| Parameter 1 Type      | list of objects                                    |
| Parameter 2 Name      | attribute                                                           |
| Parameter 2 Type      | attribute of the object // An attribute of a referent object could be used as well. For more information, see the example below.                                                         |
| Parameter 3 Name      | separator (optional) // If Parameter3 is not specified, then the default separator is ", " (comma + space)                                                           |
| Parameter 3 Type      | string                                                           |
| Return Value          | (attributeValue1, attributeValue2, ...)                                                         |
| Introduced In Version | 2019.1                                                       |


## Example

Repository: Crm.Sales.SalesOrders 
```
10: LIST CHILD:Lines EXP:20 CONST:'; '
20: GETOBJVALUE REF:Product ATTRIB:Name
```
Returned Value: 'ProductsName1; ProductName2 ...'
