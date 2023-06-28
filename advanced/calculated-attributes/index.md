---
uid: ca
---

# User calculated attributes

User calculated attributes are user-defined objects which extend the system entities.

They're defined like formulas.

When the value of a calculated attribute is requested, it's calculated "on the fly", in **real-time**.

> [!NOTE]
> 
> Calculated attribute formulas are compiled to native executable format.<br>
> Their calculation speed is very similar to the speed of the system-defined calculated attributes.

**Example 1 - Get default payment term days**

Suppose that in a sales order, you want to display the customers default payment term (in days).

You can define the following calculated attribute:

| No | Operation | Param1 | Param2 | Param3 |
|----|-----------|--------|--------|--------|
| 10 | GETOBJVALUE | REF:Customer | ATTRIB:DefaultPaymentTermDays ||

**Explanation:**

- **GETOBJVALUE ** - gets information from a related entity. The related entity is specified in **Param1**. <br> The desired information is specified in **Param2**.
- Line number 10 is the only line in the calculated attribute
- The return value is the value of the attribute **DefaultPaymentTermDays** in the customer entity.

**Example 2 - Complex filter and summation**

The following calculated attribute sums all sales order lines, the product of which:

- has a user data attribute called 'CustPropPrj', equal to '500'
- has a name containing the word 'Tool'

| No | Operation | Param1 | Param2 | Param3 |
|----|-----------|--------|--------|--------|
| 10 | SUM | EXP:20 | ATTRIB:LineAmount |
| 20 | FILTER | CHILD:Lines | EXP:30 |
| 30 | IN | ATTRIB:Product | EXP:40 |
| 40 | FILTER | QUERY:Gen_Products | EXP:50 |
| 50 | AND | EXP:60 | EXP:70 |
| 60 | EQUALS | ATTRIB:CustPropPrj | CONST:500 |
| 70 | LIKE | ATTRIB:Name | CONST:'Tool' |

**Explanation:**

- Line 10: Iterates through the data set on Line 20 (EXP:20); SUMs the attribute **LineAmount**.
- Line 20: Filters the lines subset with the filter specified in Line 30 (EXP:30).
- Line 30: Creates a filter which is satisfied only by products in the query on Line 40 (EXP:40).
- Line 40: Creates a query, which filters the products with the condition specified on Line 50.
- Line 50: Specifies that the condition is comprised of two conditions linked with **AND**.
- Line 60: Specifies that the first condition is the value of an attribute called 'CustPropPrj' should be '500'.
- Line 70: Specifies that the second condition is that the name of the product should contain 'Tool'. <br><br>

Attributes can calculate complicated formulas, query the database and get related values. 

--------
### See more

- **[Operators](https://docs.erp.net/tech/advanced/calculated-attributes/operators/index.html)**
- **[Examples](https://docs.erp.net/tech/advanced/calculated-attributes/examples/index.html)**
- **[Parameter types](https://docs.erp.net/tech/advanced/calculated-attributes/parameter-types/index.html)**
- **[Q&A](https://docs.erp.net/tech/advanced/calculated-attributes/QA/index.html)**
