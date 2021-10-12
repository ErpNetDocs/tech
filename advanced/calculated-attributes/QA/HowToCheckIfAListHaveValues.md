---
items: CalculatedAttributesQA
---

# How to check if a list has values?

When working with lists, often there is a need to check if  this list actually contains any values (records). For example, there is a calculated attribute which calculates the quantity in the Sales Order Lines panel in specified measurement unit. There is always the possibility that the user enter a product which has no dimensions for the required measurement unit. In such cases, an instrument to check the lists records count is needed. 

The described case is solved by the following expression:

```
SUM(List, 1)
```

This expression returns integer value containing the number of records in the entered list.

Here is an example expression and its description. This example is defined in the sales order header and checks if the lines contain one specific product. So the repository of the calculated attribute is Crm.Sales.SalesOrders and its expressions are:

```
10: SUM EXP:20 CONST:1
20: FILTER CHILD:Lines EXP:30
30: EQUAL ATTRIB:ProductId CONST:d3d83bf0-d1fc-e611-9c53-00155d001f52
```

Explanation:

- 10: check the records count in list in expression 20
- 20: filter the list of lines (detailed objects of the sales order object) by the filter in expression 30
- 30: check if the ProductId in the line is equal to Guid d3d83bf0-d1fc-e611-9c53-00155d001f52

This calculated attribute returns zero or greater value, depending on the count of the records in the Sales Order Lines with product with id of d3d83bf0-d1fc-e611-9c53-00155d001f52.
