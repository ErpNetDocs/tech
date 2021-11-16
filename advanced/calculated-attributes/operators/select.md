---
uid: cao-SELECT
items: Operators
---

# SELECT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets objects that match clauses.           |
| Parameter 1 Name      | Repository                                                         |
| Parameter 1 Type      | repository                                    |
| Parameter 2 Name      | Clauses (optional, but highly recommended) // <br> For more information, see the section below)           |
| Parameter 2 Type      | operators (**[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)**, **[TOP](https://docs.erp.net/tech/advanced/calculated-attributes/operators/top.html)**)                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | Returns a list of objects from Repository that matches Clauses.                                                        |

> [!NOTE]
> 
> **SELECT** returns a limited number of records - 20 000. This limit is only for the returned records count. <br> It's recommended to set as many filters as possible. (in the **WHERE** clause).

**Example:**

The **[WHERE]** clause of the **SELECT** statement supports the following operators:

- **[AND](https://docs.erp.net/tech/advanced/calculated-attributes/operators/and.html)**
- **[TOP](https://docs.erp.net/tech/advanced/calculated-attributes/operators/top.html)**
- **[EQUAL](https://docs.erp.net/tech/advanced/calculated-attributes/operators/equal.html)**
- **[GT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/gt.html)**
- **[GTE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/gte.html)**
- **[LT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/lt.html)**
- **[LTE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/lte.html)**

Operators not supported by **SELECT**  but used by the **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** operator are:

- **[NOT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/not.html)**
- **[OR](https://docs.erp.net/tech/advanced/calculated-attributes/operators/or.html)**
- **[LIKE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/like.html)**

### FILTER AND WHERE filtering of a SELECT

Having this in mind, it's really important to extract lists from the database. 

When using **SELECT**, you send a request to the database with as many **[WHERE]** filters as possible. 

If there's an unsupported filter, then the list returned by **SELECT** may be filtered additionally by **[FILTER]**.

The disadvantages are that a **SELECT** statement makes a direct request to the database, which may influence productivity and slow down the calculation of the attribute. When using **SELECT**, the user has to apply as many **[WHERE]** filters as possible, because this would limit the amount of data which would be extracted from the database into the client. 

If **SELECT** doesn't provide enough filters, the result may be filtered by **[FILTER]**, which operates on data already loaded in the client.

#### Examples:

Let's say you need a list of documents whose **DocumentTypeId** is equal to 'bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e' or '89ca5ca4-ad57-44c7-9b33-2ff44e054bff'. The documents are work orders. 

The following calculated attribute would be **incorrect** and return errors when used:

```
10: SELECT REPO:Production.ShopFloor.WorkOrders EXP:20
20: WHERE EXP:30
30: OR EXP:40 EXP:50
40: EQUAL CONST:bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e
45: ATTRIB:DocumentTypeId CONST:System.Guid
50: EQUAL EXP:45 CONST:89ca5ca4-ad57-44c7-9b33-2ff44e054bff
```

You can set an attribute which selects the work orders. 

Then, to filter the list which the **SELECT** operator returned, apply the **[FILTER]** operator for more precision. 

The correct calculated attribute is as follows:

```
10: FILTER EXP:20 EXP:30
20: SELECT REPO:Production.ShopFloor.WorkOrders 
30: OR EXP:40 EXP:50
40: EQUAL EXP:45 CONST:bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e
45: CAST ATTRIB:DocumentTypeId CONST:System.Guid
50: EQUAL ATTRIB:DocumentTypeId CONST:89ca5ca4-ad57-44c7-9b33-2ff44e054bff
```
