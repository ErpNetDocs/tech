# Receipt and issue balance validation in store transfers

The current article describes the validation if the **receipt** does not exceed the **issue** in the product transfer. In this case a transfer may be any of the following actions:
 
- moving a product from one store to another store by a store transfer;
- products production (that it is considered that the materials are issued and transferred as a new product into another store);
- returning products by a customer (this is considered a transfer - the products are issued from one store and given to the customer and then they return\transfer them to the same or other store);
- returning a rented asset which has been delivered to the customer (here the situation is similar to the returning of sold products except that the returning may happen or not, but after we delivered assets to the renters, we expect their return is mandatory when the rental contract expires).

This validation is important so unrealistic situations can be avoided (for example - transactions with incorrect chronology) which may lead to incorrect goods cost.
 
For more information on cost calculation, see [Calculating cost for transferred products](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/calculating-cost-for-transferred-products.html?q=Calculating%20Cost%20For%20Transferred%20Products), [Calculating cost for returned products](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/calculating-cost-for-returned-products.html?q=Calculating%20Cost%20For%20Returned%20Products), [Calculating cost for produced products](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/calculating-cost-for-produced-products.html?q=Calculating%20cost%20for%20produced%20products) and [Calculating cost when returning rented assets](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/calculating-cost-when-returning-rented-assets.html?q=Calculating%20cost%20when%20returning%20rented%20assets).
 
## Validation in transfer of one product

Usually in store transfers one product is issued from one store and the same product is entered into the target store (the same record in the products nomenclature). The current article describes the validation in this usual type of transfer. Other transfers (such as production, where one product (or more) are issued from the first store and other products (or products) are entered into the target store) is not covered in the current article.
 
The validation is applied on every issue and receipt transaction release (from the respective store). And the validation applies on every transfer row. All issue transactions and all receipt transactions, resulting from the current row, are summed up.
 
At first, these operations are ordered. For every two store transactions - **[transaction 1]** and **[transaction 2]**, their chronological order has to be defined. This is executed as follows:
 
- If the *transaction timestamps* of **[transaction 1]** and **[transaction 2]** are different - the transaction with a smaller timestamp is before the other
- If the *transaction timestamps* are equal, but the movement type is not the same (issue or receipt) - then the issue transaction is before the receipt transaction.
- If the *transaction timestamps* are equal and both transactions are **issued** - then the transaction with a bigger quantity is placed before the other.
- If the *transaction timestamps* are equal and both transactions are **receipts** - then the transaction with *less* quantity is placed before the other.

After the transactions are ordered chronologically, the costs are set to zero:

**[issue quantity total]** = 0 and **[receipt quantity total]** = 0.
 
Then, for every element of the ordered list with transactions, depending on its direction - issue or receipt - its base quantity is added to the respective total. Then, the system checks if **[issue quantity total]** < **[receipt quantity total]** is true. If it is true, the current operation (transaction release) is aborted and an error message appears. If it is false, then the system moves to the next element of the ordered list of transactions.
 
If the *Transaction Timestamps* are equal in **receipt** transactions, the transactions are in quantity ascending order because the following case is possible: the first transaction is an issue transaction of **10 PCS** at **12:42**, the next operation is a **receipt** transaction of **10 PCS** at **13:17** and there are two more **receipt** transactions with equal *Transaction Timestamps* of **13:31** - one transaction for **3 PCS** and one transaction for **-3 PCS**. The last two transactions may appear after correction of the **receipt** document of 10 PCS. So if the transactions are not in ascending order, it is possible to add the quantity of the transaction with quantity of **3 PCS** first and in this moment the **[issue quantity total] = 10** and **[receipt quantity total] = 13**, which may mislead us for imbalance between **issue** and **receipt** transactions, no matter that the next transaction immediately fixes it.
 
Under the same considerations, the **issue** transactions with equal *Transaction Timestamps* are in quantity descending order. It is possible to correct the first operation with **-3 PCS** and this correction will have the same *Transaction Timestamp* as the original transaction. Then if the **-3 PCS** transaction is first, there will be redundant/non-existing imbalance - **[issue quantity total]** = **-3** and **[receipt quantity total] = 0**.
 
## Validation in transfer of different products (production)

In production there is a change in the algorithm above. As the products that are received in the target store (manufactured goods) are usually different from the ones that we issue from the first store, it is not appropriate to check directly if **[issue quantity total] > [receipt quantity total]**. Also, it is not appropriate to sum quantities of different materials/products in one total **[issue quantity total]**. This is the reason for the different calculation of the **[issue quantity total]**.
 
Instead of summing the **issue** transactions in one **[issue quantity total]** , each material/product has its own total and the result is several totals. These totals and the quantities that are defined by the manufactured good recipes are used to calculate if enough materials are issued by the current moment. This quantity is added to the **[issue quantity total]**.

