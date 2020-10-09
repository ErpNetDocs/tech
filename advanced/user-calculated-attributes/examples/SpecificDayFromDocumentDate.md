---
items: CalculatedAttributeExamples
---

# Specific Day From Document Date

A Calculated Attribute is added with the following parameters:

```
Repository Name: Crm.Sales.SalesOrders
Name: TenDaysFromDocumentDay
```

And the Calculated Attribute expressions are as follows:

```
10: ADDDAYS ATTRIB:DocumentDate CONST:10
```

> Explanation:
>
> 10: Add 10 days to the date in DocumentDate

If showed in the Sales Order form, this attribute calculates and displays 10 days added to the DocumentDate.