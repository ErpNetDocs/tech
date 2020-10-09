---
items: CalculatedAttributesQ&A
---

# How to create an optimally fast calculated attribute?

When creating a calculated attribute there are some things that are good too keep in mind in order to create an optimally fast syntax. Here we are going to describe some advices that should be followed during the design of the attribute.

Generally, those advices can be summarized to:

1.  Use REF instead of SELECT
2.  If you have to use a SELECT – Use WHERE clauses instead of FILTER clauses
3.  Filter the FILTER - Filter the list returned to the FILTER as much as you can



But let's get into the details. 

Using a REF means that we are using the collection of elements that have  already been loaded in the memory. The REF connection leads only to the  records that refer to by the current entity.

Using a  SELECT means that for each calculation of attribute the system will  create a request to the server and will look through the whole table  that we have selected. A single table could contain millions of records  (or even more). 

More records inevitably means slower calculation. Like any other design when creating a calculated attribute there usually is more than one way that we can use to calculate the  value especially when the calculation is a bit more complicated.  Sometimes using SELECT looks like the simplest option (the fist that  comes in mind) to reach the value we need, but first, we should always  try to think if there is a reference connection that we can use instead  in order to achieve a faster calculation.



*Example:*

Let's imagine that we need to show a field with Total Line Amount value in  the Sales Order Line. Therefore we will need to calculate the Sum of the Line Amount of all Sales Order lines of the particular Sales Order.  Such attribute can be created at least two ways (the repository is  Crm.Sales.SalesOrderLines):

- Using a SELECT (using all records in the Crm.Sales.SalesOrderLines table)

```
10     SUM  EXP: 20  ATTRIB: LineAmountValue                            

20     SELECT REPO: Crm.Sales.SalesOrderLines  EXP: 30             

30     WHERE EXP: 40                                      

40     EQUAL ATTRIB: SalesOrderId   EXP:50                

50     GETOBJVALUE  INPUT: 10      ATTRIB: SalesOrderId          
```



- Using a REF (using only the lines of the current SalesOrder)

```
10     SUM   EXP: 20 ATTRIB: LineAmountValue                    

20     GETOBJVALUE  REF: SalesOrder CHILD: Lines           


```

Of course, there are some scenarios in which we want to reach the data of a table to which we simply can use a reference connection. But when using a SELECT the are some tricks that we can use to fast the calculation. 

When we SELECT a table we can filter its records with WHERE or FILTER clauses. The most important thing that we must know about them is that when using:

- WHERE clauses – the conditions are applied together with the SELECT to the  whole list and directly on the server. Much faster performance in  comparison with FILTER, especially for a list with lots of records.
-  FILTER clauses - filters are applied locally (on the client side) to the list that has been returned from the SELECT. 



Knowing this there are two basic conclusions that we can come to.

First, if we should always choose WHERE clauses instead FILTER clauses if  possible. Most of the other operators are supported in both cases, but  we must say that WHERE clauses have certain limitation. For example,  they can not be used along with [NOT](../operators/not.md), [OR](../operators/or.md) and [LIKE](../operators/like.md) operators (for more information, see [SELECT](../operators/select.md)). If we have no other choice but to use FILTER we proceed to the next paragraph (advice).

And second, when we use FILTER clauses we should always try to narrow down  the list that we are returning. How to do so? Just apply as much WHERE  clauses as possible to the SELECT. This way we are filtering the list  before it is returned to the FILTER and therefore it will contain fewer  records, which will lead to a faster calculation.



As a conclusion, we don’t claim that using a SELECT is a bad thing it is a very powerful tool that just has to be used wisely.