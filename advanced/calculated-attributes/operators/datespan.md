---
uid: cao-DATESPAN
items: Operators
---

# DATESPAN

| Specification    | Value                                                        |
| ---------------- | ------------------------------------------------------------ |
| Description      | Returns the difference between dates as a duration in the specified interval type. The interval is fulfilled when the same date and time is reached in the next interval. |
| Parameter 1 Name | StartDate                                                    |
| Parameter 1 Type | Date, DateTime                                               |
| Parameter 2 Name | EndDate                                                      |
| Parameter 2 Type | Date, DateTime                                               |
| Parameter 3 Name | Interval                                                     |
| Parameter 3 Type | String (Days, Months, Years). Defaults to Days if not specified. |
| Return value     | If Interval = 'Days' then Days(EndDate - StartDate)<br />If Interval = 'Months' then Months(EndDate - StartDate)<br />If Interval = 'Years' then Years(EndDate - StartDate) |

> [!NOTE]
> 
> Parameter 3 (Interval) accepts input in the form of a string, allowing you to specify the interval type as either 'Days' (alias 'D'), 'Months' (alias 'M'), or 'Years' (alias 'Y'). If you don't explicitly specify an interval type, it will default to 'Days'.

**Examples:**

```
10:  DATEDIFF ATTRIB:DocumentDate ATTRIB:RequiredDeliveryDate CONST:Days             
```
OUTPUT:
<br/> If 'DocumentDate = 2020-01-01 23:59' and 'RequiredDeliveryDate = 2020-01-02 00:01'  , the output will be '0'.
<br/> If 'DocumentDate = 2020-01-01 23:58' and 'RequiredDeliveryDate = 2020-01-02 23:59'  , the output will be '1'.
<br/> If 'DocumentDate = 2023-09-20' and  'RequiredDeliveryDate = 2023-10-05', the output will be '15'.
<br/> If 'DocumentDate = 2023-09-20' and 'RequiredDeliveryDate = 2023-09-10', the output will be '-10'.

\*\*

```
10: 10:  DATEDIFF ATTRIB:DocumentDate ATTRIB:RequiredDeliveryDate CONST:Months
```

OUTPUT:
<br/> If 'DocumentDate = 2023-09-20' and 'RequiredDeliveryDate = 2023-10-05' , the output will be '0'.
<br/> If 'DocumentDate = 2023-09-20' and 'RequiredDeliveryDate = 2023-10-20' , the output will be '1'.

\*\*

```
10:  DATEDIFF ATTRIB:DocumentDate ATTRIB:RequiredDeliveryDate CONST:Years
```

OUTPUT:
<br/> If 'DocumentDate = 2023-10-05' and 'RequiredDeliveryDate = 2024-01-20' , the output will be '0'.
<br/> If 'DocumentDate = 2023-10-05' and 'RequiredDeliveryDate = 2024-10-05' , the output will be '1'.

\*\*

> [!NOTE]
> 
> The repository of the attribute is *Crm.Sales.SalesOrder*

------------
### See more

- **[DATEDIFF operator](datediff.md)**
- **[Difference between DATESPAN and DATEDIFF](../QA/what-is-the-difference-between-datespan-and-datediff.md)**