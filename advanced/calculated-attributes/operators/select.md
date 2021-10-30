---
uid: cao-SELECT
items: Operators
---

# SELECT 

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the objects matching the clauses.           |
| Parameter 1 Name      | Repository                                                         |
| Parameter 1 Type      | repository                                    |
| Parameter 2 Name      | Clauses (optional, but highly advisable) // For more information, see the section below)           |
| Parameter 2 Type      | operators ([WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html), [TOP](https://docs.erp.net/tech/advanced/calculated-attributes/operators/top.html))                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return value          | Returns a list of objects from Repository matching Clauses.                                                        |

> [!NOTE]
> 
> **SELECT** returns limited number of records - 20 000. This limit is only for the returned records count, so as setting much filters as possible are highly recommended (filters in the [WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html) clause).

***Example***

The [WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html) clause of the **SELECT** statement supports the following operators:

- **[AND](https://docs.erp.net/tech/advanced/calculated-attributes/operators/and.html)**
- **[TOP](https://docs.erp.net/tech/advanced/calculated-attributes/operators/top.html)**
- **[EQUAL](https://docs.erp.net/tech/advanced/calculated-attributes/operators/equal.html)**
- **[GT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/gt.html)**
- **[GTE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/gte.html)**
- **[LT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/lt.html)**
- **[LTE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/lte.html)**

The operators which are not supported by the **SELECT** operator but may be used by the [FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html) operator are:

- **[NOT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/not.html)**
- **[OR](https://docs.erp.net/tech/advanced/calculated-attributes/operators/or.html)**
- **[LIKE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/like.html)**


### FILTER AND WHERE filtering of a SELECT

Having this in mind, it is really important when extracting lists from the database. When using **SELECT**, we send a request to the database and it is preferred to set as much [WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html) filters as possible. But if there is a filter not supported by the @@name server, then the list that is returned by the select may be filtered additionally with the [FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html) operator.

The disadvantages are that the **SELECT** statement makes a direct request to the database, which may reflect on the productivity and may slow down the calculation of the attribute. When using **SELECT**, the user has to apply as much [WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html) filters as possible, because this would limit the amount of data which would be extracted from the database into the client. And then, if the select statement does not provide enough filters, the result from the select may be filtered by the [FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html) operator which operates on the already loaded data in the client.

### Here are some examples to picture the information so far:

If there is a need of a list of documents which DocumentTypeId is equal to 'bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e' or '89ca5ca4-ad57-44c7-9b33-2ff44e054bff'. The documents are work orders. So the following calculated attribute would be incorrect:

```
10: SELECT REPO:Production.ShopFloor.WorkOrders EXP:20
20: WHERE EXP:30
30: OR EXP:40 EXP:50
40: EQUAL CONST:bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e
45: ATTRIB:DocumentTypeId CONST:System.Guid
50: EQUAL EXP:45 CONST:89ca5ca4-ad57-44c7-9b33-2ff44e054bff
```

This calculated attribute is incorrect and would return errors when used. So, we can set calculated attribute which selects the work orders and then to filter the list, which the **SELECT** operator returned and apply the [FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html) operator for more precision. So the correct calculated attribute is as follows:

```
10: FILTER EXP:20 EXP:30
20: SELECT REPO:Production.ShopFloor.WorkOrders 
30: OR EXP:40 EXP:50
40: EQUAL EXP:45 CONST:bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e
45: CAST ATTRIB:DocumentTypeId CONST:System.Guid
50: EQUAL ATTRIB:DocumentTypeId CONST:89ca5ca4-ad57-44c7-9b33-2ff44e054bff
```
