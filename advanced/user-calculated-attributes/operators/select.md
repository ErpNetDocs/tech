---
uid: cao-SELECT
---

# SELECT - Calculated Attribute Operator

| Specification         | Value                                                        |
| --------------------- | ------------------------------------------------------------ |
| Description           | Gets the objects matching the clauses.           |
| Parameter 1 Name      | Repository                                                         |
| Parameter 1 Type      | repository                                    |
| Parameter 2 Name      | Clauses (optional, but highly advisable) // For more information see the 'FILTER AND WHERE filtering of a SELECT' section below)           |
| Parameter 2 Type      | operators (@WHERE, @TOP)                                                           |
| Parameter 3 Name      | -                                                            |
| Parameter 3 Type      | -                                                            |
| Return Value          | Returns a list of objects from Repository matching Clauses.                                                        |

> [!NOTE]
> The SELECT operator returns limited number of records - 20 000. This limit is only for the returned records count, so as setting much filters as possible are highly recommended (filters in the [WHERE](where.md) clause).

## Example

The WHERE clause of the SELECT statement supports the following operators:

[AND](and.md)

[TOP](top.md)

[EQUAL](equal.md)

[GT](gt.md)

[GTE](gte.md)

[LT](lt.md)

[LTE](lte.md)

The operators which are not supported by the SELECT operator but may be used by the FILTER operator are:

[NOT](not.md)

[OR](or.md)

[LIKE](like.md)


FILTER AND WHERE filtering of a SELECT

Having this in mind is really important when extracting lists from the database. When using SELECT operator we send a request to the database and it is preferred to set as much WHERE filters as possible. But if there is a filter, which is not supported by the EnterpriseOne Server, then the list that is returned by the select may be filtered additionally with the FILTER operator.

The disadvantages are that the SELECT statement make a direct request to the database, which may reflect on the productivity and may slow down the calculation of the attribute. When using the SELECT operator the user has to apply as much WHERE filters as possible, because this would limit the amount of data which would be extracted from the database into the client. And then, if the select statement does not provide enough filters, the result from the select may be filtered by the FILTER operator which operates on the already loaded data in the client.

Here are some examples to picture the information by far:

If there is a need of a list of documents which DocumentTypeId is equal to 'bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e' or '89ca5ca4-ad57-44c7-9b33-2ff44e054bff'. The documents are Work Orders. So the following calculated attribute would be incorrect:

```
10: SELECT REPO: Production.ShopFloor.WorkOrders EXP: 20
20: WHERE EXP: 30
30: OR EXP: 40 EXP: 50
40: EQUAL CONST: bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e
45: ATTRIB: DocumentTypeId CONST: System.Guid
50: EQUAL EXP:45 CONST: 89ca5ca4-ad57-44c7-9b33-2ff44e054bff
```

This calculated attribute is incorrect and would return errors when used. So, we can set calculated attribute which selects the work orders and then to filter the list, which the SELECT operator returned and apply the FILTER operator for more precision. So the correct calculated attribute is as follows:

```
10: FILTER EXP:20 EXP: 30
20: SELECT REPO: Production.ShopFloor.WorkOrders 
30: OR EXP: 40 EXP: 50
40: EQUAL EXP:45 CONST: bbd8e7ae-c0e0-4c1b-8730-7d68fa52971e
45: CAST ATTRIB: DocumentTypeId CONST: System.Guid
50: EQUAL ATTRIB: DocumentTypeId CONST: 89ca5ca4-ad57-44c7-9b33-2ff44e054bff
```
