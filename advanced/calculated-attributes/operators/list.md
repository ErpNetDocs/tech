---
uid: cao-LIST
items: Operators
---

# LIST 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Returns a list with string values of a specified attribute from a list of objects. <br> The values in the list are separated. <br> If there's no indicated separator, the list is separated with ", " (comma + space) by default.           |
| Parameter 1 Name      | list                                                         |
| Parameter 1 Type      | list of objects                                    |
| Parameter 2 Name      | attribute                                                           |
| Parameter 2 Type      | attribute of the object <br/>// An attribute of a referent object could be used as well. See the example below.                                                         |
| Parameter 3 Name      | separator (optional) <br/>// If Parameter3 is not specified, then the default separator is ", " (comma + space)                                                           |
| Parameter 3 Type      | string                                                           |
| Return value          | (attributeValue1, attributeValue2, ...)                                                         |
| Introduced in version | 2019.1                                                       |


**Example:**
 
```
10: LIST CHILD:Lines EXP:20 CONST:'; '
20: GETOBJVALUE REF:Product ATTRIB:Name
```
OUTPUT: <br> 'ProductsName1; ProductName2 ...'

> [!NOTE] 
> 
> The repository of the attribute is Crm.Sales.SalesOrders
