# Store order rows execution algorithm

This algorithm is applied when there are many unfulfilled store orders or products going in and out of the store. The purpose is to create transactions, fulfilling the orders as correctly as possible. The idea behind the algorithm is that the system automatically defines which store orders should be fulfilled and what part of them - automatically, without user interference. This allows faster processing of the issue and receipt transactions, especially when the data (orders and products) volume is large.

The starting data for the algorithm is two lists:

 - list of unfulfilled store order rows - **[ORD]**. This list is usually a partial sample of all unfulfilled store orders in the database, e.g the orders from a certain customer/supplier or certain order. In **[ORD]** there are only the quantities which are unfulfilled, because if for a given store order row for **10 PCS** there are released transactions with **7 PCS**, then in **[ORD]** the quantity for this row would be **3 PCS**. The rows completely fulfilled by transactions are not part of **[ORD]**;
- List of store transactions - **[FUL]**, which contain data about products currently being moved in or out of the store. The data consist of **Product, Lot, Serial Number** and **Quantity**.  Afterwards, data is saved in the newly created Transactions. The list **[FUL]** is usually the result of a control system (such as barcode scanner) which is placed at the entrance/exit of the store.

Both lists must consist of the same type of operations - meaning **[ORD]** is a list of receipt store order rows and **[FUL]** is a list of receipt store order rows or if **[ORD]** contains only issue store order rows and **[FUL]** is a list of issue store order rows. If **[ORD]** and **[FUL]** contain both issue and receipt transactions, then the lists must be separated into two uniform parts and the algorithm will be applied on each part separately. 

## Store orders execution algorithm

The purpose of the algorithm is the distribution of all operations/quantities from **[FUL]**  to the rows of **[ORD]**. It is possible that some operations are defined as fulfilment of one row from **[ORD]**. Besides, the quantities from one operation can be separated amongst more than one row.

At first, the two lists are sorted. **[FUL]** is sorted according to the entering order of the operations. **[ORD]** is sorted by *Document Date, Document Number* and *Line Number* (this is standard sorting, but other types of sorting using data from CRM or SCM modules which has initialized 
the orders are also possible). These sortings set a kind of initial priority, which should be used for orders fulfilment. Then, the algorithm continues to 4 stages and at each operations/quantities from **[FUL]** are compared to **[ORD]** rows by defined criteria.

At each stage the system goes through **[FUL]** (after it is sorted) and for each operation with quantity no equal to zero (the quantity may be 0 at a previous stage) the following actions are executed:

1. Search for a row in **[ORD]** that matches the operation according to the current stage criteria.
2. If there is no such row, the algorithm goes to step 7. If there is such a row, the algorithm continues to the next step.
3. The part of the operation quantity this row fulfills is defined. At stage I, II and III the quantity is defined by comparison of the row quantities and the operations quantities. The smaller value is defined as quantity. Exception is stage IV where the algorithm takes the quantity in the operation.
4. A new transaction row is created with the **Product, Lot** and **Serial Number** from the operation and the quantity defined in step 3. As a *transaction timestamp* in the transaction row, the current date and time is set. Also, the row from **[ORD]**, which is found in step 1, is marked in the transaction row.
5. The row from step 1 and the operation are edited and their quantity is decreased by the quantity from step 3 (i.e. the algorithm updates what is left for fulfilment).
6. If the remaining quantity in the operation is different than 0, all steps by now are repeated. Otherwise, the algorithm goes to the next step.
7. The processing of the current operation is over and the algorithm goes to the next one. 

So for each operation the algorithm finds a store order row, fulfilling it, according to the current criteria, and this is repeated until the quantity in the operation is 0 or there are no store orders found (that match the operation).

The criteria by which the store order row is found for a given operation is a comparison between the row and the operation by their values of **Product, Lot** and **Serial number**. Three types of comparison exist:

- *Exact match* means that the row and the operation have the same value. For example, *exact lot match* means that either the row and the operation have the same lot or both have no lot specified.
- *Weakened match* means that either the value is the same in both (row, operation) or one of them may be null. For example, *weakened lot match* returns match even if the operation has a lot and in the row there is no lot.
- *Free match* means that the algorithm does not take into account the values and always returns a match.

At the different stages there are the following criteria for store order rows fulfilment:

- Stage I: Searching for a match by **Product** and by **Lot** and by **Serial number**. Also, it is required that  the quantity in the row should be different than 0 (in this stage this should be true for each row in **[ORD]**).
- Stage II: Searching for a match by **Product** and *weakened match* by **Lot** and by **Serial number**. Again, it is required that the quantities in the order rows are different  than 0 (here, it is possible that zero quantity rows are found because of the update in stage I).
- Stage III: Searching for a match by **Product**, *free match* by **Lot** and by **Serial number** and non-zero quantities in the order rows.
- Stage IV: Searching for a match by **Product** and *free match* by **Lot** and by **Serial number**. The difference from stage III is that here the quantities in the rows can be zero.

It becomes clear that in the first stage the algorithm tries to strictly comply with the product, lot and serial number, and during the next stages the algorithm weakens the criteria allowing violation of the lots and serial numbers from the store orders. At stage III over execution is still not allowed (because of the non-zero quantities criteria). The purpose of the last stage is to be used in cases when the user issues/receives more than what was ordered. So in the last stage the user is able to fulfill orders with zero quantities, combined with the way of defining the quantities of stage III - the over execution is allowed. If the quantities from **[FUL]** are not more than the quantities in **[ORD]**, then stage IV will not be reached at all.

Also, in each stage the algorithm requires *exact match* by **Product**. This means that if in **[FUL]** there are products that are not listed in **[ORD]**, then they will remain even after stage IV. Those cases (by now) are not covered by the system and have to be managed by the user. Otherwise, after stage IV in all operations from **[FUL]** there would only be zero quantities. By this we reach the purpose that all quantities in **[FUL]** should be distributed to a row from **[ORD]**.

***Example 1:***

There are the following rows in **[ORD]** (serial numbers are null everywhere):

**row 10, Product #1, 4 PCS, Lot #ab17**

**row 20, Product #1, 3 PCS, Lot #ss54**


**row 30, Product #1, 2 PCS**

**row 40, Product #1, 7 PCS, Lot #ts23**


In **[FUL]** there is only one operation for **Product #1, Lot#ab17**, with no serial number and quantity of **14 PCS**.

So in stage I the algorithm will cover **row 10** by **4 PCS** from the operation, at stage II the algorithm will cover **row 30** and at stage III the algorithm will cover part of **row 40**.

This is how the lists **[ORD]** and **[FUL]** will look like at each stage:

After stage I:
|**[ORD]**|**[FUL]**|
|:----|:----|
**row 10, Product #1, 0 PCS, lot #ab17**|**Product #1, lot #ab17, 10 PCS**
**row 20, Product #1, 3 PCS, lot #ss54**|
**row 30, Product #1, 2 PCS**|
**row 40, Product #1, 7 PCS, lot #ts23**|

After stage II:
|**[ORD]**|**[FUL]**|
|:----|:----|
**row 10, Product #1, 0 PCS, lot #ab17**|**Product #1, lot #ab17, 8 PCS**|
**row 20, Product #1, 3 PCS, lot #ss54**|
**row 30, Product #1, 0 PCS**|
**row 40, Product #1, 7 PCS, lot #ts23**

After stage III:
|**[ORD]**|**[FUL]**|
|:----|:----|
**row 10, Product #1, 0 PCS, lot #ab17**|**Product #1, lot #ab17, 0 PCS**|
**row 20, Product #1, 0 PCS, lot #ss54**|
**row 30, Product #1, 0 PCS**|
**row 40, Product #1, 2 PCS, lot #ts23**|

***Example 2:***

If there are the same **[ORD]** and **[FUL]** except for the fact that the quantity in **[FUL]** is **18 PCS** (i.e. **2** more than the orders).

Then in stages I and II the fulfilments will be the same. At stage III **row 40** will be fulfilled completely and at stage IV the remaining **2 PCS** from **[FUL]** will cover **row 10** and it will be over executed.
