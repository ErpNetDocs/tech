---
items: CalculatedAttributesQA
---

# How to check if a list has values?

When working with lists, you can check if they contain any values (or records). 

For example, there is an attribute which calculates the quantity in the sales order lines in specified measurement unit. You could enter a product which has no dimensions for the required measurement unit. 

In such cases, an instrument to check the lists records count is needed. 

The described case is solved by the following expression:

```
SUM(List, 1)
```

This expression returns integer value containing the number of records in the entered list.

Here is a sample expression and its description. This example is defined in the sales order header and checks if the lines contain one specific product. 

The repository of the calculated attribute is **Crm.Sales.SalesOrders** and its expressions are:

```
10: SUM EXP:20 CONST:1
20: FILTER CHILD:Lines EXP:30
30: EQUAL ATTRIB:ProductId CONST:d3d83bf0-d1fc-e611-9c53-00155d001f52
```

**Explanation:**

- 10: check the records count in list in expression 20
- 20: filter the list of lines (detailed objects of the sales order object) by the filter in expression 30
- 30: check if the **ProductId** in the line is equal to **Guid d3d83bf0-d1fc-e611-9c53-00155d001f52**

This calculated attribute returns zero or greater value, depending on the count of records in the sales order line with product with ID **d3d83bf0-d1fc-e611-9c53-00155d001f52**.
