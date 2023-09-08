---
uid: cao-DATEDIFF
items: Operators
---

# DATEDIFF

| Specification    | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | Returns the difference between dates as the date difference for the specified interval type |
| Parameter 1 Name | StartDate                                                    |
| Parameter 1 Type | Date, DateTime                                               |
| Parameter 2 Name | EndDate                                                      |
| Parameter 2 Type | Date, DateTime                                               |
| Parameter 3 Name | Interval                                                     |
| Parameter 3 Type | String (Days, Months, Years) If empty then value is Days     |
| Return value     | If Interval = 'Days' then Day(EndDate) - Day(StartDate)<br />If Interval = 'Months' then Month(EndDate) - Month(StartDate)<br />If Interval = 'Years' then Year(EndDate) - Year(StartDate) |



**Example:**

```
10:  DATEDIFF ATTRIB:DocumentDate ATTRIB:RequiredDeliveryDate ATTRIB:Days            
```
OUTPUT: If 'DocumentDate = 2020-01-01 23:59' and 'RequiredDeliveryDate = 2020-01-02 00:01'  , the output will be '1'.

OUTPUT: If 'DocumentDate = 2020-01-01 23:58' and 'RequiredDeliveryDate = 2020-01-02 23:59'  , the output will be '1'.

OUTPUT: If 'DocumentDate = 2023-09-20' and  'RequiredDeliveryDate = 2023-10-05', the output will be '15'.

OUTPUT: If 'DocumentDate = 2023-09-20' and 'RequiredDeliveryDate = 2023-09-10', the output will be '-10'.

**



```
10:  DATEDIFF ATTRIB:DocumentDate ATTRIB:RequiredDeliveryDate ATTRIB:Months            
```

OUTPUT: If 'DocumentDate = 2023-09-20' and 'RequiredDeliveryDate = 2023-10-05' , the output will be '1'.

OUTPUT: If 'DocumentDate = 2023-09-20' and 'RequiredDeliveryDate = 2023-10-20' , the output will be '1'.

**



```
10:  DATEDIFF ATTRIB:DocumentDate ATTRIB:RequiredDeliveryDate ATTRIB:Years            
```

OUTPUT: If 'DocumentDate = 2023-10-05' and 'RequiredDeliveryDate = 2024-01-20' , the output will be '1'.

OUTPUT: If 'DocumentDate = 2023-10-05' and 'RequiredDeliveryDate = 2024-10-05' , the output will be '1'.

**



> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrder*


#### 

