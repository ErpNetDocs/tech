# Specific Procedures of Cost Corrections

Apart from the standard method of <b>Cost Correction</b> - loading the store transaction for a specified period (plus the opening balances) and filling in the rows for the correction by the <b>Basic Algorithm For Cost Correction Calculation</b>, there are two more ways to create a Cost Correction document. They use generation procedures available in the Transaction document.

## Cost Correction Generation Procedure For The Actual Cost Of The Current Transaction

This generation procedure updates the cost of the store transactions in the current Transaction document. 

For each row, the following actions are applied:

 1.  Loading the actual cost by the <i>current moment</i> (i.e. this is the sum of the original cost from the Transaction row and the addition cost in the row, generated by already created Cost Corrections). This is a sum <b>[current cost]</b>;
 
2. Then, the actual cost for the row is calculated - the sum <b>[actual cost]</b> as usual:

     a. if the Transaction is <b>issuing</b>, the cost is calculated by the average accumulated cost;

     b. if the record is a <b>receipt</b> transaction and is part of a transfer or production process, its cost is re-calculated according to the algorithm from articles <b>Calculating Cost For Produced Products</b>, <b>Calculating Cost For Returned Products</b> and <b>Calculating Cost For Transferred Products</b>;

     c. if the record is a <b>receipt</b> transaction and is not part of a transfer or production process, the original cost is considered the actual cost.

To make valid calculations, the cost of all store transactions affecting the current transactions should be re-calculated correctly.

At the end, the difference <b>[actual cost] - [current cost]</b> is calculated. Provided that it is different than zero, a new row is added in the <b>Cost Correction</b> sub-document for the current Transaction row, which contains the difference.

## Cost Correction generation procedure for the current Transaction results

This generation procedure updates the costs of all transactions that depend on the current Transaction rows. 

The following actions are executed:

1. Loading all store transactions (with the opening balances if needed) which depend on the current document;

2. Тhe <b>Basic Algorithm For Cost Correction Calculation</b> is applied over the loaded set of records;

3. For each store transaction from the set of records, the difference between the algorithm result and the actual cost valid before the creation of the current transaction, is calculated. If it is a non-zero result, a new row in the <b>Cost Correction</b> is added.

Loading the records is performed iteratively. Before the first iteration, the following is created:

<b>[current set of records]</b> = the transactions in the current Transaction document;

<b>[current <i>Movement Type</i>]</b> = <i>Movement Type </i>of the current Transaction;
  
<b>[result] = [current set of records]</b> + the opening balances for the current store of the current products from the transactions of the <b>[current set of records]</b> (the opening balances are for the <i>Transaction Timestamp</i> date)
  
Then, a cycle of iterations is performed, and for each iteration, the following is executed:
  
- if the <b>[current <i>Movement Type</i>] = receipt</b>, a new set of records is loaded;
  
<b>[new set of records]</b> = all transactions for the stores and the products (and the lots, if the product keeps separated cost for each lot) from the <b>[current set of records]</b> whоse <i>Transaction Timestamp</i> is greater than or equal to the <i>Transaction Timestamp</i>  in the <b>[current set of records]</b>.
  
- If the<b>[current <i>Movement Type </i>]= issue</b> and the <b>[current set of records]</b> has records that are part of a transfer/production process, then the <b>[new set of records]</b> is as follows:
  
<b>[new set of records]</b> = all <b>receipt</b> transactions from the specified transfer/production processes, whose <i>Transaction Timestamps</i> are greater than or equal to the <i>Transaction Timestamps</i> in the <b>[current set of records]</b>.
  
- The result is updated and the current set of records becomes:
  
<b>[result] = [result]</b> U <b>[new set of records]</b> (the opening balances are added for every new store which is part ot <b>[new set of records]</b> but is not part of <b>[current set of records])</b>;
  
<b>[current set of records] = [new set of records]</b>.
  
- At the end, if <b>[current <i>Movement Type</i> ] = receipt</b>, then <b>[current <i>Movement Type</i>]</b> is set to <b>issue</b> and if it was <b>[current <i>Movement Type</i>] = issue</b>,<b>[current Movement Type]</b> is set to <b>receipt</b>.
  
These iterations are performed until an iteration has a <b>[new set of records]</b> that is empty.


