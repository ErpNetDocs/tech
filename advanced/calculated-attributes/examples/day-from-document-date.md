---
items: CalculatedAttributeExamples
---

# Specific day from document date

This attribute calculates and displays a certain number of days added to a document date.

**Example:**

A calculated attribute is added with the following parameters:

```
Repository Name:Crm.Sales.SalesOrders
Name:TenDaysFromDocumentDay
```

The calculated attribute expressions are as follows:

```
10: ADDDAYS ATTRIB:DocumentDate CONST:10
```

**Explanation:**

- 10: Add 10 days to the date in **DocumentDate**

If showed in the sales order form, this attribute calculates and displays 10 days added to the **DocumentDate**.
