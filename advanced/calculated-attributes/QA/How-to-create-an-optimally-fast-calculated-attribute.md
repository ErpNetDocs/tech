---
items: CalculatedAttributesQA
---

# How to create an optimally fast calculated attribute?

When creating a calculated attribute, there are some things to keep in mind in order to create an optimally fast syntax. 

Let's see some steps that should be followed during the design of the attribute:

1.  Use **REF** instead of **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)**
2.  If you're using **[SELECT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/select.html)**, use **[WHERE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/where.html)** clauses instead of **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** clauses
3.  Filter the filter - Filter the list returned to the **[FILTER](https://docs.erp.net/tech/advanced/calculated-attributes/operators/filter.html)** as much as you can

Using a **REF** means that you're using the collection of elements that have already been loaded in the memory. The **REF** connection leads only to the records that refer to the current entity.

Using a **[SELECT]** means that for each attribute calculation, the system will create a request to the server and will look through the whole table that you have selected. A single table could contain millions of records (or even more). 

More records means slower calculation. Like any design, when creating a calculated attribute, there is usually more than one way to calculate the value. Sometimes **[SELECT]** is the simplest option to use to reach the value, but you should always try to find a link instead, in order to achieve faster calculation.

**Example:**

Suppose you need to show a field with *_Total Line Amount_* value in the sales order line. You will need to calculate the sum of the line amount of all sales order lines of the particular sales order. 

Such attribute can be created in at least two ways (the repository being **Crm.Sales.SalesOrderLines**):

#### Using a [SELECT] (with all records in the Crm.Sales.SalesOrderLines table)

```
10     SUM  EXP:20  ATTRIB:LineAmountValue                            
20     SELECT REPO:Crm.Sales.SalesOrderLines  EXP:30             
30     WHERE EXP:40                                      
40     EQUAL ATTRIB:SalesOrderId   EXP:50                
50     GETOBJVALUE  INPUT:10      ATTRIB:SalesOrderId          
```
#### Using a REF (with only the lines of the current SalesOrder)

```
10     SUM EXP:20 ATTRIB:LineAmountValue                    
20     GETOBJVALUE REF:SalesOrder CHILD:Lines           
```

There are some cases where you want to reach the data of a table, to which you could simply use a reference connection. But with **[SELECT]**, there are some tricks that you can master to speed up the calculation. 

When you **[SELECT]** a table, you can filter its records with **[WHERE]** or **[FILTER]** clauses. 

Keep in mind that when using:

- **WHERE** clauses, the conditions are applied together with **[SELECT]** to the whole list and directly on the server. Much faster performance in comparison with **[FILTER]**, especially for a list with lots of records.

-  **FILTER** clauses, filters are applied locally (on the client side) to the list that has been returned from the **[SELECT]**. 

Knowing this, you can reach two basic conclusions:

First, you should choose **[WHERE]** clauses instead **[FILTER]** clauses, if possible. Most of the other operators are supported in both cases, though **[WHERE]** clauses do have certain limitation. For example, they cannot be used along with **[NOT](https://docs.erp.net/tech/advanced/calculated-attributes/operators/not.html)**, **[OR](https://docs.erp.net/tech/advanced/calculated-attributes/operators/or.html)** and **[LIKE](https://docs.erp.net/tech/advanced/calculated-attributes/operators/like.html)** operators. 

Second, when you have no choice but to use **[FILTER]** clauses, you should always try to narrow down the list that you are returning. Just apply as much **[WHERE]** clauses as possible to the **[SELECT]**. This way, you are filtering the list before it is returned to the **[FILTER]** and therefore, it will contain fewer records, which will lead to a faster calculation.

OVerall, **[SELECT]** is a very powerful tool that needs to be used wisely.
