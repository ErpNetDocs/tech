---
items: CalculatedAttributesQA
---

# How to create an optimally fast calculated attribute?

When creating a calculated attribute there are some things that are good too keep in mind in order to create an optimally fast syntax. Here we are going to describe some advices that should be followed during the design of the attribute.

Generally, those advices can be summarized to:

1.  Use **REF** instead of **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)**
2.  If you have to use a **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** – Use **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)** clauses instead of **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** clauses
3.  Filter the **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** - Filter the list returned to the **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** as much as you can


But let's get into the details. 

Using a **REF** means that we are using the collection of elements that have  already been loaded in the memory. The **REF** connection leads only to the records that refer to by the current entity.

Using a **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** means that for each calculation of attribute the system will create a request to the server and will look through the whole table that we have selected. A single table could contain millions of records  (or even more). 

More records inevitably means slower calculation. Like any other design when creating a calculated attribute there usually is more than one way that we can use to calculate the  value especially when the calculation is a bit more complicated. Sometimes using **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** looks like the simplest option (the fist that comes in mind) to reach the value we need, but first, we should always try to think if there is a reference connection that we can use instead in order to achieve a faster calculation.

*Example:*

Let's imagine that we need to show a field with **Total Line Amount** value in the sales order line. Therefore we will need to calculate the sum of the line amount of all sales order lines of the particular sales order. Such attribute can be created at least two ways (the repository is Crm.Sales.SalesOrderLines):

#### Using a SELECT

Using a **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** (using all records in the Crm.Sales.SalesOrderLines table)

```
10     SUM  EXP:20  ATTRIB:LineAmountValue                            
20     SELECT REPO:Crm.Sales.SalesOrderLines  EXP:30             
30     WHERE EXP:40                                      
40     EQUAL ATTRIB:SalesOrderId   EXP:50                
50     GETOBJVALUE  INPUT:10      ATTRIB:SalesOrderId          
```

#### Using a REF

Using a **REF** (using only the lines of the current SalesOrder)

```
10     SUM EXP:20 ATTRIB:LineAmountValue                    
20     GETOBJVALUE REF:SalesOrder CHILD:Lines           
```

Of course, there are some scenarios in which we want to reach the data of a table to which we simply can use a reference connection. But when using a **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** the are some tricks that we can use to fast the calculation. 

When we **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** a table we can filter its records with **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)** or **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** clauses. The most important thing that we must know about them is that when using:

- WHERE clauses – the conditions are applied together with the **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** to the  whole list and directly on the server. Much faster performance in  comparison with **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)**, especially for a list with lots of records.

-  FILTER clauses - filters are applied locally (on the client side) to the list that has been returned from the SELECT. 


Knowing this there are two basic conclusions that we can come to.

First, if we should choose **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)** clauses instead **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** clauses, if possible. Most of the other operators are supported in both cases, but we must say that **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)** clauses have certain limitation. For example, they cannot be used along with **[NOT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/not.html)**, **[OR](https://docs.erp.net/tech/advanced/calculated-attributes/operators/or.html)** and **[LIKE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/like.html)** operators. If we have no choice but to use **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** we proceed to the next paragraph (advice).

And second, when we use **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** clauses we should always try to narrow down the list that we are returning. How to do so? Just apply as much **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)** clauses as possible to the **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)**. This way we are filtering the list before it is returned to the **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** and therefore it will contain fewer records, which will lead to a faster calculation.

As a conclusion, we don’t claim that using a **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)** is a bad thing it is a very powerful tool that just has to be used wisely.
