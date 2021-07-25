# Lots Issue
The current article describes the principles of lots issue when goods are issued from the store.
Lots issue is actually the obligation to issue products from certain lots before others. The lots are prioritized and the priority is mandatory when goods are issued from the store (i.e. when Store Transactions are released). This priority is at least advisable when lots are entered before the Store Transaction documents (Store Orders, Shipment Orders, Sales Orders and more). The final goal is the lots selection in the document lines to be executed in the correct order.

<b>Example 1:</b>

In the document line, <b>10 Pcs</b> of the product have to be sold/shipped/issued and the lot is not specified. The lot with the highest priority (let’s name it <b>[Lot 1#]</b>) has <b>17 Pcs</b> available. So following the principle of lots issue, the user has to select/be offered <b>[Lot 1#]</b> in the line.

There are cases when the first lot does not have enough available quantity to fulfill the whole line quantity. Then, more than one lot has to be used. The quantity in the line has to be divided into several lines and in each line the lot has to be specified with its quantity. Again, the lots order defines their priority in the lots issue.

<b>Example 2:</b>

If there are <b>30 Pcs</b> in the line and no lot is selected, and the three top priority lots - <b>[Lot 1#]</b>, <b>[Lot 2#]</b>, and <b>[Lot 3#]</b> - have available quantities of <b>17</b>, <b>8</b>, and <b>12Pcs</b>, then the quantity in the line would be divided into the following lines:

<b>- [Lot #1],17 Pcs</b>*;

<b>- [Lot #2],8 Pcs</b>*;

<b>- [Lot #3],5 Pcs</b>*.

*<i>These are the total quantities of each one of the three lots. The document may be saved in other forms, for example - the 17 Pcs of the first lot may be entered as 17 separated lines, each line with quantity of one [Lot #1]. This may be necessary if the product is serialized, each line must have a serial number specified, and the quantity has to be 1</i>.

Actually, it can be said that there is always line breakdown. In <b>Example 1</b> there is trivial breakdown into only one lot <b>[Lot #1]</b>,<b>10 Pcs</b>.

Defining lots may appear in earlier documents that precede the Store Transactions - Store Orders, Shipment Orders, Sales Orders, etc. In this stage, specifying the lot is recommended. If lots are selected in such a document, they are passed to the next document and may be changed. In some cases, a change may not be recommended and following documents have to keep the selected lots (for example, the customer in the Sales Order requires to receive the lots which are specified in the Sales Order; then, those lots have to be issued from the store). Specifying lots in the Store Transactions is final and mandatory. If it has not happened in previous documents, it has to happen in the Store Transaction. The lots cannot be changed in following documents. 

Store Transactions differ from the other documents with their limits according to the quantities which may be selected for each lot. In the Store Transactions, quantities are limited to the current stock holds. In other documents, there may be more precise restrictions - the “available to promise” (for specified lot). This is a method used to reserve lots. For example, if a Sales Order reserves the whole available quantity of one lot but there is no Store Transaction yet (so the current stock hold is unchanged), it would be wrong if another Sales Order called for quantities from the same lot.

Selecting lots in a document line happens only if the line has no selected lots. If the lot is already specified and there are enough stock holds (with no assurance that the selected lot has the highest priority), only the quantity is validated. Such validation is applied in the Store Transactions, but it is possible to appear earlier (in preceding documents) so the user is warned earlier that he has to select another lot.

## Lots Issue Methods

There are three main lots issuing methods - FIFO (First in, first out), FEFO (First expire, first out), LIFO (Last in, first out). They set the lots priorities. Each product uses a lots issuing method for itself. This is specified in the product definition. The product setting may be specified or null. If it is null, there is no sequence in the product's lots and there are no restrictions which lot should be selected (or the product does not use lots). In such cases, the lot is not mandatory even in the Store Transactions.

The priority may be defined by sorting the lots by the date of their first receipt or by the date when they expire:

- for the FIFO method - the lots are sorted in an ascending order by the date of first receipt;

- for the FEFO method - the lots are sorted in an ascending order by their expiring dates (if no expiration date is specified, the null date is considered the largest date);

- for the LIFO method - the lots are sorted in a descending order by the date of first receipt.

<b>Example 3:</b>

There are <b>30 Pcs</b> in a document line and lots of the product in the line have the following details (lot, available quantity/current stock hold, date of first receipt, expiry date):

<b>[Lot #1], 11 Pcs</b>, <b>01.12.2021</b>, <b>05.01.2022</b>;

<b>[Lot #2], 17 Pcs</b>, <b>03.12.2021</b>, <b>03.01.2022</b>;

<b>[Lot #3], 14 Pcs</b>, <b>07.12.2021</b>, <b>null</b>.

This document line is divided into two or three document lines with quantities from different lots depending on the lots issuing method of the product:

- when FIFO is selected:

<b>-[Lot #1],11 Pcs</b>*;

<b>-[Lot #2],17 Pcs</b>*;

<b>-[Lot #3],2 Pcs</b>*.

- when FEFO is selected:

<b>-[Lot #2],17 Pcs</b>*;

<b>-[Lot #1],11 Pcs</b>*;

<b>-[Lot #3],2 Pcs</b>*.

- when LIFO is selected:

<b>-[Lot #3],14 Pcs</b>*;

<b>-[Lot #2],16 Pcs</b>*.

*<i>Again, additional lines breakdown may be necessary if the product uses serial numbers or other information for the current transaction.</i>

If the quantity of <b>Example 3</b> is 5 Pcs and not 30 Pcs, then no line breakdown would be necessary (to be more precise - the trivial breakdown into one line would happen) and the lot would just be selected in the line depending on which lots issuing method the product uses.

When the current stock holds of the product have records for both quantity from a specific lot and quantity with no lot, then the no-lot records have the least priority (because, for example, they may be held for planned receipts which have not arrived yet, and the quantities are only available without being part of the current stock holds; in that case, it would be better if they were used as late as possible while the current stock holds with specified lots are exhausted first). So, for each lots issuing method, the priorities are defined as follows:

- FIFO:

1. the records with lots whose receipt date has value - highest priority (sorted ascending by this date);
 
2. the records with lots with null receipt date (they are considered to arrive in the store as late as possible);
 
3. the records with no lots.
- FEFO:

4. the records with lots whose expiry date has value - highest priority (sorted ascending by this date);

5. the records with lots with null expiry date (they are considered to expire last);
 
6. the records with no lots.
 
- LIFO:

7. the records with lots with null receipt date - highest priority (they are considered to arrive in the store as late as possible);

8. the records with lots whose receipt date has value (sorted descending by this date);

9. the records with no lots.

## Lots Issue Ways

Lots issue may be done in the following manners:

<b>- manually</b> (through the interface - using a panel, list, others);

<b>- automatically</b> (by starting a function by the user or a document event - state change).

### <b>Manual Lot Issue</b>

In these cases, the system suggests to the user a list of lots sorted according to the lot issue method (by the date of first receipt or the expiry date). The user selects the lots and their quantities (his choice is limited to the available quantity).

The most direct approach is the order (sorting) to be shown in the dropdown list of the lot attribute in the line. Thus, the user does the lots breakdown by selecting a lot, editing the quantity (if necessary) and adding a new line with the same product, where he/she can select the next lot and its quantity. In this case, only lots with available quantity are shown in the dropdown list. 

Another approach is the sorted list with available lots to be placed in a separated panel/screen. There are fields where the user can enter the quantity for each lot. Thus, the user sees the list and enters the whole breakdown of the line at once instead of entering it line by line. The panel/screen would contain only available lots.

In both cases, it is useful for the lists to contain additional information: current stock holds, available quantity (for each lot), date of first receipt, expiry date (as date and duration), notes, etc.

### <b>Automatic Lot Issue</b>

Automatic lot issue is executed by the system when the user starts it or when an event happens. The automatic lot issue uses the same sorted list of the lots as the manual lot issue. The difference is that the lots are always issued strictly in the order of the list. In the manual lot issue, the user has the option not to issue a specific lot and to skip its turn and use another lot.

### <b>Calculation Of The Quantity In The Last Lot</b>

In the lot issue process, it is important to keep in mind that the quantities are entered in the measurement unit of the line. Every quantity fulfillment in the examples is done in the base measurement unit because the current stock holds and the available quantities are always shown in that unit. So, in the examples above, the Quantity Base attribute is used. To enter quantity in the Quantity field (where the measurement unit may differ from the base measurement unit of the product), the <b>Product Dimensions</b> would be used. The problem is that if product dimensions are used for all quantities in the breakdown of the line, the total Quantity might be different from the initial Quantity. This may lead to differences in the quantities in the child and the parent documents and as a result new documents may be created.

<b>Example 4:</b>

There is a document line with Quantity of <b>16 l</b> and <b>30 kg</b> Quantity Base (the product dimension is <b>1 l = 1.875 kg</b>). The three lots with highest priorities for this product (<b>[Lot #1]</b>, <b>[Lot #2]</b> and <b>[Lot #3]</b>) have current stock holds/available quantities of <b>10 kg</b>, <b>10 kg</b>, and <b>18 kg</b> . In the breakdown of the initial document line, there would be <b>10 kg</b>  of each lot. If we apply the product dimension for each lot to see the quantity in liters, we would have the following:

<b>- [Lot #1]</b>, Quantity Base = <b>10 kg</b>, Quantity = 10 / 1.875 = <b>5.33333l</b>;

<b>- [Lot #2]</b>, Quantity Base = <b>10 kg</b>, Quantity = 10 / 1.875 = <b>5.33333l</b>;

<b>- [Lot #3]</b>, Quantity Base = <b>10 kg</b>, Quantity = 10 / 1.875 = <b>5.33333l</b>;

But the total quantity would be <b>15.99999 l</b> and not <b>16 l</b> as expected.

This problem is solved by using the remainder and not product dimensions for the last document line (<b>[initial quantity]-[already used quantity]</b>). This algorithm would make the breakdown of <b>Example 4</b> as follows:

 <b>- [Lot #1]</b>, Quantity Base =  <b>10 kg</b>, Quantity = 10 / 1.875 =  <b>5.33333l</b>;
 
 <b>- [Lot #2]</b>, Quantity Base = <b>10 kg</b>, Quantity = 10 / 1.875 =  <b>5.33333l</b>;
 
 <b>- [Lot #3]</b>, Quantity Base =  <b>10 kg</b>, Quantity = 16 - 5.33333 - 5.33333 =  <b>5.33334 l</b>.
 
<b>Example 5:</b>

The same approach for calculating the quantity in the last line from the breakdown is applied in cases of trivial breakdowns (when there is only one lot). Then, the only quantity in the breakdown is the last line. For example, if the line has Quantity of <b>2 l</b> and Quantity Base of <b>0.66667 kg</b> (3 l = 1 kg), and the first lot (with highest priority) has current stock holds/available quantity of <b>10 kg</b>, then the only breakdown is not supposed to be multiplied by 3 to have the quantity in liters (as it would make 0.66667 * 3 = 2.00001 l). The calculation should be 2 - 0 = <b>2 l</b> (this is the initial quantity minus the already used quantity - 0).

