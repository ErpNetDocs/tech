# Setting cost when purchasing goods

In @@name goods are purchased in two stages:
 
1. Stage one: recording the quantities. In this stage, only quantities are entered into the system - those which are actually received. This stage changes only the stock holds. In this stage also the user defines the lots.
2. Stage two: recording the costs. This is done by separating store documents from the documents from stage one. This is because the cost is defined by the purchase invoices for the goods which do not always arrive along with the actual goods.

The current article describes stage two. The documents that are part of both stages of the purchasing process are as follows:
 
- **Receiving orders** - These documents represent what we expect to receive and not what is actually received.
- **Purchase invoices** - created from or by **receiving orders** and contain the cost of the goods. This is the document sent by the supplier and the user enters it the way it is received;
- **Store receipt orders** - created from the **receiving order** and record the quantity that has to be entered in the store;
- **Quantity transactions** - created from or by the **store orders**. They contain the stocks that are entered into the store (they may be entered directly by a barcode scanner). These documents do not record the goods cost yet;
- **Cost transactions** - created from the **receiving orders** and record the cost, which is copied from the **purchase invoice**. They should get the exact lots and Transaction Timestamp from the **quantity transactions**.

Stage one is represented by **receiving order** => **store receipt orders** => **quantity transactions** while the second stage is represented by **receiving order** => **cost transactions** and only after the **purchase invoice** is entered in the system.
 
The cost is set only for the products which are received by the **quantity transaction**. I.e. if there is a **receiving order** with no **quantity transaction** then no **cost transaction** will be created. The cost is calculated when the quantities from the **quantity transaction** are multiplied by the unit cost, defined by the **purchase invoice**. So if there is no **purchase invoice** no **cost transaction** will be created. 
 
The *unit cost* for one row in the **receiving order** is defined as follows:
 
1. All rows of released, non-voided **purchase invoices** for the current row from the **receiving order** are summed up. If there are no such rows, then the unit cost is **0**. 
2. For each row from p.1,an end cost is defined: 

**[End Cost]** = **[Line Amount]** + **[sum of the distributed amounts for the current row]**. 

> [!NOTE]
> Only [additional amounts](https://docs.erp.net/tech/advanced/document-amounts/index.html) that are marked with Add To Line as True. Also, the additional amount may be entered by other **purchase invoices** (for example - transport purchase invoice).

3. At the end the **[End Cost]** for all rows from p.1 are summed up, the quantities for those rows are summed up and the end cost is divided by those quantities. If the quantities are **0** then the unit cost is also **0**. 
Not: When summing up all end costs have to be converted to the currency of the **receiving order**, and all quantities have to be converted to the measurement unit of the **receiving order** row.

Then, when creating **cost transaction** for a **receiving order**, for each row of the current **receiving order** the following calculations are made:
 
1. All rows of released, non-voided **cost transactions** for the current row of the **receiving order**, are summed up;
2. For each row from p.1, a new row in the **transaction cost** is created in which the quantity and the unit cost are **0**, the lot and the *transaction timestamp* are copied from p.1. and the cost is equal to the quantity of the row multiplied by the unit cost for the row in the **receiving order**.
 
***Example 1***:
 
There is a **Receiving Order #1** with two rows:
 
- row #10, Product A, **10 PCS**;
- row #20, Product B, **12 PCS**;

The following quantity transactions are created:
 
- Transaction **#1** for **Receiving Order #1 row #10**, Product A,Lot **12B**, **4 PCS**, Transaction Timestamp = 15/10/2020 12:59;
- Transaction **#1** for **Receiving Order #1 row #20**, Product B,Lot **9A, 10 PCS**, Transaction Timestamp = 15/10/2020 12:59;
- Transaction **#2** for **Receiving Order #1 row #10**, Product A,Lot **17B, 3 PCS**, Transaction Timestamp = 17/10/2020 14:15;
- Transaction **#2** for **Receiving Order #1 row #20**, Product B,Lot **13A, 1 PCS**, Transaction Timestamp = 17/10/2020 14:15.

Also, there are two **purchase invoices** for **Receiving order #1** and one **purchase invoice** for transport, which distributes an additional amount on the first two **purchase invoices**:
 
- **Purchase Invoice #1**, for **Receiving Order #1 row #10, 8 PCS, 64 EUR**;
- **Purchase Invoice #1**, for **Receiving Order #1 row #20, 13 PCS, 39 EUR**;
- **Purchase Invoice #2**, for **Receiving Order #1 row #10, 1 PCS, 10 EUR**;
- **Purchase Invoice #3** with no rows and an additional amount of **44 EUR** for transport which is distributed by the quantities. So the added amounts are **16 EUR, 26 EUR** and **2 EUR**;

In this case, the **cost transactions** on this delivery should be as follows:
 
- Product A, lot 12B, **0 PCS**, Transaction Timestamp = **15/10/2020 12:59**, Line Cost = 4 PCS * ((64 EUR + 16 EUR + 10 EUR + 2 EUR) / (8 PCS + 1 PCS)) ~ **40.89 EUR**;
- Product B, lot 9A, **0 PCS**, Transaction Timestamp = **15/10/2020 12:59**, Line Cost = 10 PCS * ((39 EUR + 26 EUR) / 13 PCS) = **50 EUR**;
- Product A, lot 17B, **0 PCS**, Transaction Timestamp = **17/10/2020 14:15**, Line Cost = 4 PCS * ((64 EUR + 16 EUR + 10 EUR + 2 EUR) / (8 PCS + 1 PCS)) ~ **30.67 EUR**;
- Product B, lot 13A, **0 PCS**, Transaction Timestamp = **17/10/2020 14:15**, Line Cost = 4 PCS * ((39 EUR + 26 EUR) / (16 PCS) = **5 EUR**;
