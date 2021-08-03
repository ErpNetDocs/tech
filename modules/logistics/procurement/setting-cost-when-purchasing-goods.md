# Setting Cost When Purchasing Goods

In @@name goods are purchased in two stages:
 
1. Stage One: recording the quantities. In this stage, only quantities are entered into the system - those which are actually received. This stage changes only the stock holds. In this stage also the user defines the lots.
2. Stage Two: recording the costs. This is done by separating store documents from the documents from stage One. This is because the cost is defined by the purchase invoices for the goods which do not always arrive along with the actual goods.

The current article describes stage Two. The documents that are part of both stages of the purchasing process are as follows:
 
- **Receiving Orders** - These documents represent what we expect to receive and not what is actually received.
- **Purchase Invoices** - created from or by **Receiving Orders** and contain the cost of the goods. This is the document sent by the supplier and the user enters it the way it is received;
- **Store Receipt Orders** - created from the **Receiving Order** and record the quantity that has to be entered in the store;
- **Quantity Transactions** - created from or by the **Store Orders**. They contain the stocks that are entered into the store (they may be entered directly by a barcode scanner). These documents do not record the goods cost yet;
- **Cost Transactions** - created from the **Receiving Orders** and record the cost, which is copied from the **Purchase Invoice**. They should get the exact lots and Transaction Timestamp from the **Quantity Transactions**.

Stage One is represented by **Receiving Order** => **Store Receipt Orders** => **Quantity Transactions** while the second stage is represented by **Receiving Order** => **Cost Transactions** and only after the **Purchase Invoice** is entered in the system.
 
The cost is set only for the products which are received by the **Quantity Transaction**. I.e. if there is a **Receiving Order** with no **Quantity Transaction** then no **Cost Transaction** will be created. The cost is calculated when the quantities from the **Quantity Transaction** are multiplied by the unit cost, defined by the **Purchase Invoice**. So if there is no **Purchase Invoice** no **Cost Transaction** will be created. 
 
The *Unit Cost* for one row in the **Receiving Order** is defined as follows:
 
1. All rows of released, non-voided **Purchase Invoices** for the current row from the **Receiving Order** are summed up. If there are no such rows, then the unit cost is **0**. 
2. For each row from p.1,an end cost is defined: 

**[End Cost]** = **[Line Amount]** + **[sum of the distributed amounts for the current row]**. 

**Note**: Only [Additional Amounts](https://github.com/ErpNetDocs/tech/blob/900817b9f1540003d08297f43c8c3a2aa6827ce0/advanced/documents/additional-amounts.md) that are marked with Add To Line as True. Also, the additional amount may be entered by other **Purchase Invoices** (for example - transport purchase invoice).

3. At the end the **[End Cost]** for all rows from p.1 are summed up, the quantities for those rows are summed up and the end cost is divided by those quantities. If the quantities are **0** then the unit cost is also **0**. 
Not: When summing up all end costs have to be converted to the currency of the **Receiving Order**, and all quantities have to be converted to the measurement unit of the **Receiving Order** row.

Then, when creating **Cost Transaction** for a **Receiving Order**, for each row of the current **Receiving Order** the following calculations are made:
 
1. All rows of released, non-voided **Cost Transactions** for the current row of the **Receiving Order**, are summed up;
2. For each row from p.1, a new row in the **Transaction Cost** is created in which the quantity and the unit cost are **0**, the lot and the *Transaction Timestamp* are copied from p.1. and the cost is equal to the quantity of the row multiplied by the unit cost for the row in the **Receiving Order**.
 
***Example 1***:
 
There is a **Receiving Order #1** with two rows:
 
- row #10, Product A, **10 PCS**;
- row #20, Product B, **12 PCS**;

The following Quantity Transactions are created:
 
- Transaction **#1** for **Receiving Order #1 row #10**, Product A,Lot **12B**, **4 PCS**, Transaction Timestamp = 15/10/2020 12:59;
- Transaction **#1** for **Receiving Order #1 row #20**, Product B,Lot **9A, 10 PCS**, Transaction Timestamp = 15/10/2020 12:59;
- Transaction **#2** for **Receiving Order #1 row #10**, Product A,Lot **17B, 3 PCS**, Transaction Timestamp = 17/10/2020 14:15;
- Transaction **#2** for **Receiving Order #1 row #20**, Product B,Lot **13A, 1 PCS**, Transaction Timestamp = 17/10/2020 14:15.

Also, there are two **Purchase Invoices** for **Receiving Order #1** and one **Purchase Invoice** for transport, which distributes an additional amount on the first two **Purchase Invoices**:
 
- **Purchase Invoice #1**, for **Receiving Order #1 row #10, 8 PCS, 64 EUR**;
- **Purchase Invoice #1**, for **Receiving Order #1 row #20, 13 PCS, 39 EUR**;
- **Purchase Invoice #2**, for **Receiving Order #1 row #10, 1 PCS, 10 EUR**;
- **Purchase Invoice #3** with no rows and an additional amount of **44 EUR** for transport which is distributed by the quantities. So the added amounts are **16 EUR, 26 EUR** and **2 EUR**;

In this case, the **Cost Transactions** on this delivery should be as follows:
 
- Product A, lot 12B, **0 PCS**, Transaction Timestamp = **15/10/2020 12:59**, Line Cost = 4 PCS * ((64 EUR + 16 EUR + 10 EUR + 2 EUR) / (8 PCS + 1 PCS)) ~ **40.89 EUR**;
- Product B, lot 9A, **0 PCS**, Transaction Timestamp = **15/10/2020 12:59**, Line Cost = 10 PCS * ((39 EUR + 26 EUR) / 13 PCS) = **50 EUR**;
- Product A, lot 17B, **0 PCS**, Transaction Timestamp = **17/10/2020 14:15**, Line Cost = 4 PCS * ((64 EUR + 16 EUR + 10 EUR + 2 EUR) / (8 PCS + 1 PCS)) ~ **30.67 EUR**;
- Product B, lot 13A, **0 PCS**, Transaction Timestamp = **17/10/2020 14:15**, Line Cost = 4 PCS * ((39 EUR + 26 EUR) / (16 PCS) = **5 EUR**;

