# Calculating cost for transferred products

Store Transfers create two parallel sub-document flows - receipt and issue flow. The cost of the issue store transactions is calculated by the average cost in the store, while the one in the receipt store transactions - specifically by the store transfer. It is formed by the following two components:

- Issue cost (of the issued goods);

- [Additional amounts](https://docs.erp.net/tech/advanced/document-amounts/index.html?q=Additional%20amounts) in the store transfer, added to the products (representing increased goods cost e.g because of transport taxes).

For each store transfer the following must be valid:

<b>[receipt cost] = [issue cost] + [[Additional amounts](https://docs.erp.net/tech/advanced/document-amounts/index.html?q=Additional%20amounts) for cost]</b>

Each store transaction row is calculated separately (so <b>[[Additional amounts](https://docs.erp.net/tech/advanced/document-amounts/index.html?q=Additional%20amounts) for cost]</b> is the additional amount distributed to the current row). These calculations are executed when the receipt store order is generated and the calculated cost is saved in the <i>Line Cost</i> field in the rows of the store order. So if the generated store order receipt follows the generation of the issue documents (orders and their executions, providing the issue cost), then the issue cost may be copied to the receipt orders.

<b><i>Example 1</b></i>:

There is a store transfer with two rows - row #1 with Product 1 for <b>10 PCS</b> and row #2 with Product 2 for <b>12 PCS</b>. At first, there are two issue transactions:

- <b>issue, Product 1</b>, Timestamp: 01 Dec 2020 <b>13:50, 8 PCS</b>, document cost: <b>88</b>;

- <b>issue, Product 2</b>, Timestamp: 01 Dec 2020 <b>13:50, 6 PCS</b>, document cost: <b>90</b>.

Afterwards, store orders receipt will be created with the same quantities and set costs in the rows:

- row #10, <b>Product 1, 8 PCS</b>, line cost: <b>88</b>;

- row #20, <b>Product 2, 6 PCS</b>, line cost: <b>90</b>.

When executing this store order, the result is transactions receipt for <b>8 PCS</b> and <b>6 PCS</b> with cost of <b>88</b> and <b>90</b>, respectively. And when the rest of the transfer quantities are issued:

- <b>issue, Product 1</b>, Timestamp: 07 Dec 2020 <b>10:05, 2 PCS</b>, document cost: <b>20</b>;

- <b>issue, Product 2</b>, Timestamp: 01 Dec 2020 <b>10:05, 6 PCS</b>, document cost: <b>102</b>.

a new receipt store order will be created with rows as follows (the store transfer will try to create a new store order for the whole issued cost from the four issue transactions. However, a store order for the first two issues already exists, so the <b>Discrepancy system</b> will create new order only for the second issues):

- row #10, <b>Product 1, 2 PCS</b>, line cost: <b>20</b>;

- row #20, <b>Product 2, 6 PCS</b>, line cost: <b>102</b>.

When executing this store order, the receipt cost will be equal to the issue cost.

The next example describes the calculations when there is an additional amount for the transport added to the goods cost.

<b><i>Continuation of Example 1:</i></b>

There is an additional transport amount of </b>66</b> (in document currency) distributed in the two rows as follows: 

<b>30</b> on the first row and <b>36</b> on the second row. 

These amounts will be added to the row costs in the generated store orders, proportionally to their quantities. So their rows become:

- Store Order #<b>1</b>, row #<b>10, Product 1, 8 PCS</b>, row cost: 88 + 30 * (8 / 10) = <b>112</b>;

- Store Order #<b>1</b>, row #<b>20, Product 2, 6 PCS</b>, row cost: 90 + 36 * (6 / 12) = <b>108</b>;

- Store Order #<b>1</b>, row #<b>10, Product 1, 2 PCS</b>, row cost: 20 + 30 * (2 / 10) = <b>26</b>;

- Store Order #<b>1</b>, row #<b>20, Product 2, 6 PCS</b>, row cost: 102 + 36 * (6 / 12) = <b>120</b>;

The standard generation of store orders receipt from store transfers always creates a store order receipt for the exact quantity already issued by transactions. The user may change the quantities (only <b>decreasing</b> them - see the end of the current article) in the receipt documents or enter them manually (the cost in the receipt documents has to be proportional to the one calculated by the system).

<b><i>Example 1 (alternative case):</b></i>

If due to correction or manual work the receipt store order #1 is as follows:

- row #<b>10, Product 1, 5 PCS</b>, row cost: <b>55</b>;

- row #<b>20, Product 2, 4 PCS</b>, row cost: <b>60</b>;

then, the rest of the cost – 33 for row #10 and 30 for row #20, will be added along with the quantities in the second receipt order:

- row #<b>10, Product 1, 5 PCS</b>, row cost: <b>53</b>;

- row #<b>20, Product 2, 8 PCS</b>, row cost: <b>132</b>;

## Issue and receipt cost balance

In the examples above, it is possible to receive only less quantity than the issued - the rest will come later. The receipt value in a document cannot be more than the issued’s. It is not possible to receive more than the amount issued from the first store when transferring stocks. Although these cases are just theoretical, they may lead to incorrect cost (especially after [cost correction](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/cost-correction/index.html?q=cost%20correction), as discrepancies may appear).

<b><i>Example 2:</b></i>
  
In Store 1, where <b>5 PCS</b> are available from a product, cost: <b>100</b>, and in Store 2, there are <b>10 PCS</b> from the same products with the cost of <b>200</b>. A transfer from Store 2 to Store 1 for <b>3 PCS</b> is executed. At first, <b>1 PCS</b> is issued from Store 2, then immediately all <b>3 PCS</b> are received. The total availability in both stores is 8 + 9 = <b>17</b> instead of <b>15</b>. There will also be an artificial cost increase. If this availability and cost condition is kept for some time, there may be incorrect cost calculations of the store transactions.
  
Limitations for what is possible to be entered in the target store from a store transfer are required. They are applied when releasing or voiding the released transactions from the transfer. 

A limitation could be: 
  
For each <i>transaction timestamp</i> on all transactions of the current transfer, the following must be true: 
  
The sum of the issues up to this timestamp (including the timestamp) is larger or equal to the sum of the receipts up to this timestamp (including the timestamp).
  
<b>Example 3:</b>
  
If we use the store transfer of <b>3 PCS</b> from Store 2 to Store 1 from <b><i>Example 2</b></i>, the first issue is as follows:
  
- <b>issue</b>, Timestamp: 10 Dec 2020 <b>17:04, 1 PCS</b>, cost: <b>20</b>;
  
Now, the user is not able to make a transaction <b>receipt</b> for <b>3 PCS</b>. The user is able to enter up to <b>1 PCS:</b> in Store 1.
  
- <b>receipt</b>, Timestamp: 10 Dec 2020 <b>17:27, 1 PCS,</b> cost: <b>20</b>;
  
The user is not able to change the <i>transaction timestamp</i> to a value less than 10 Dec 2020 <b>17:04</b>. After releasing the transaction <b>receipt</b>, the user is not able to void the <b>issue</b> transaction because on 10 Dec 2020 <b>17:27</b> there will be a total <b>issue</b> of <b>0 PCS</b>, which is less than the total <b>receipt</b> of <b>1PCS</b>.
  
For more information about the validation, see [Receipt and issue balance validation in store transfers](https://docs.erp.net/tech/modules/logistics/inventory/receipt-and-issue-balance-validation-in-store-transfers.html?q=Receipt%20And%20Issue%20Balance%20Validation%20In%20Store%20Transfers).

