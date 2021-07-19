# Setting Transaction Timestamp by Store Orders

Sometimes, the algorithm for automatic set of <i>Transaction Timestamps</i> on Transaction release may not choose the best possible dates and times. This is usually because of the specific logic of the business process of ordering store transactions which are unknown to the Logistics module.

It is possible to set <i>Transaction Timestamps</i> for the ordered transactions in the Store Orders. The module that contains the specific business logic helps setting better and more accurate times and dates in the Store Orders. When the orders are fulfilled, these <i>Transaction Timestamps</i> will be copied to the Transactions and will remain unchanged on Transaction Release.

The current article describes some specific cases which require setting the <i>Transaction Timestamp</i> by the Store Orders.

## In Transitional Store Orders

For more information about transitional documents, see <b>Transitional Documents</b>.

When a Store Order is Transitional, all its rows are filled in with the creation date and time of the parent document. The logic here is as follows: 

If the Store Order is set to transitional, then it is considered that it will happen automatically along with the parent document. So, the <i>Transaction Timestamps</i> will inherit the creation date and time of the parent document.

<i><b>Example 1</b></i>:
  
There is a Work Order where all documents except for the Transactions (Consumption Orders, Output Orders and Store Orders) are <b>transitional</b>. On release, the Store Orders generate released Transactions, i.e. the process is completely automatic.
  
At first, the Work Order has the following technological ratio: 
  
producing <b>1 PCS</b> of a product, the materials are <b>1 PCS</b> of material <b>#1</b> and <b>1 PCS</b> of material <b>#2</b>. 

On Work Order release, all sub-documents are created, and the materials are issued with a <i>Transaction Timestamp</i> of <b>[19 Jan 2020 14:00:07]</b> and the produced product has a <i>Transaction Timestamp</i> of <b>[19 Jan 2020 14:00:09]</b>. Also, because of the quick creation and release of all sub-documents, these are the <i>Transaction Timestamps</i> for creating the producing sub-documents (the Consumption Order is created on <b>[19 Jan 2020 14:00:07]</b> and the Output Order - on <b>[19 Jan 2020  14:00:09]</b>.
  
Then, on <b>22 Jan 2020</b> the Work Order is adjusted and the quantity of the first material is changed from <b>1 PCS</b> to <b>2 PCS</b>. If in the transitional Store Orders the <i>Transaction Timestamp</i> fields are left blank, when releasing the new Transaction for the additional <b>1 PCS </b> of material <b>#1</b>, its <i>Transaction Timestamp</i> would be <b>[19 Jan 2020  23:59:00]</b> because it was released later than its Document Date. In this case, we would have the following chronology:
  
- <b>1 PCS</b> of material <b>#1</b>, <b>issue</b>, <b>19 Jan 2020 14:00:07</b>;
  
- <b>1 PCS</b> of material <b>#2</b>, <b>issue</b>, <b>19 Jan 2020 14:00:07</b>; 
  
- <b>1 PCS</b> of produced product, <b>receipt</b>, <b>19 Jan 2020 14:00:09</b>; 
  
- <b>1 PCS</b> of material <b>#1</b>, <b>issue</b>, <b>19 Jan 2020 23:59:00</b>
  
At <b>14:00:09</b> there will be a receipt of <b>1 PCS</b> of the product for which <b>2 PCS</b> of material <b>#1</b> are needed. By now, only <b>1 PCS</b> is issued (the other piece is issued later). This leads to failure in the issue and receipt balance validation (see <b>Receipt And Issue Balance Validation In Store Transfers</b> and <b>Calculating Cost For Produced Products</b>) because of incorrect time of the last issue transaction.
  
When the Store Orders are transitional, the <i>Transaction Timestamp</i> is equal to the time and date of creation of the parent document, so the last issue transaction will also have <i>Transaction Timestamp</i> <b>[19 Jan 2020 14:00:07]</b> and the problem with the issue/receipt balance would not appear again.
  
## In Store Orders Created from Completing Output Orders
  
When Completing Output Orders are generated from the Work Order document form, specific date and time are set as a <i>Transaction Timestamp</i> in the rows of the Output Order. For each row in the Output Order, the greatest or the last <i>Transaction Timestamp</i> of all timestamps marking the moment the production has entered the store, is set as a <i>Transaction Timestamp</i> (this is the maximum date and time in all receipt transaction rows created by the current Work Order row, which has quantity different from 0). After that, the <i>Transaction Timestamps</i> from the Completing Output Order are passed to the Store Orders and copied to the Transaction rows.

The Completing Output Orders actually distribute the cost of the materials which are not issued on time. As a standard, it is considered that later issues of materials are distributed to the last manufactured products. This is why the greatest <i>Transaction Timestamp</i> of all non-zero receipt transactions for the specified product is set as a <i>Transaction Timestamp</i>.
  
## In Store Orders Created by Consumption Orders for Material  
  
In the generation procedure of Store Orders by Consumption Orders, there is also a specific way of setting the <i>Transaction Timestamp</i> in the Store Orders rows. It appears only if the quantity in the specified row is negative and the greatest transaction timestamp from all material issue transactions in the generated Store Order is used as a <i>Transaction Timestamp</i>.

The Consumption Order rows with negative quantities return unnecessary (exceeding) materials. This process has to be entered in the store with the same cost, as issued. If the material is issued in more than one transaction, the issue transaction preceding the return of the materials is unknown, so the last issue is used as a reference.
  
## In Store Orders Created by Shipment Orders for Products Return
  
This case is similar to the return of materials to the production. If the quantity of the current Shipment Order row is negative, the greatest transaction timestamp from the relevant Store Order row (of all issue transactions happening by now) is set as a <i>Transaction Timestamp</i>.

