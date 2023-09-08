---
uid: cao-DATEDIFF
items: Operators
---

# DATEDIFF

| Specification    | Value                                           |
| ---------------- | ----------------------------------------------- |
| Description      | Return the number of days between the two dates |
| Parameter 1 Name | StartDate                                       |
| Parameter 1 Type | Date                                            |
| Parameter 2 Name | EndDate                                         |
| Parameter 2 Type | Date                                            |
| Parameter 3 Name | -                                               |
| Parameter 3 Type | -                                               |
| Return value     | EndDate minus StartDate in days                 |



**Example:**

```
10:  DATEDIFF ATTRIB:RequiredDeliveryDate ATTRIB:DocumentDate               
```
OUTPUT: If 'RequiredDeliveryDate = 2023-10-05' and 'DocumentDate = 2023-09-20' , the output will be '15'.

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrder*


#### 

