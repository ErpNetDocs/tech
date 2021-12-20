---
uid: cao-ORDERBY
items: Operators
---

# ORDERBY 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Specifies a column or expression on which the query result set is sorted. <br> Used as a clause of **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)**.           |
| Parameter 1 Name      | attribute                                                         |
| Parameter 1 Type      | any type                                 |
| Parameter 2 Name      | order (optional) <br> // if not set, the default is ASC                                                            |
| Parameter 2 Type      | const - ASC or DESC                                                            |
| Parameter 3 Name      | inner clauses (optional)                                                            |
| Parameter 3 Type      | expression                                                           |
| Return value          | Ordered result set of a query by the specified column or expression.                                                          |
| Introduced in version | 2020 |


> [!NOTE]
> Not all attributes support sorting by ORDERBY. You can check if the attribute supports ORDERBY in the "Supports Order By: True/False" property of the attribute. The information is available in the Attribute Details section in the model documentation of the entity. E.g. https://docs.erp.net/model/entities/Crm.Sales.SalesOrders.html#documentdate


**Example:**
_Select the last 5 Sales Order Lines sorted by Sales Order's document date	._
```
10: SELECT REPO:Crm.Sales.SalesOrderLines EXP:20
20: TOP CONST:5 EXP:30
30: ORDERBY EXP:40 CONST:DESC EXP:50
40: GETOBJVALUE	REF:SalesOrder	ATTRIB:DocumentDate		
50: WHERE ...
```
