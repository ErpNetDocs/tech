
# Advance Amount Calculation Algorithm
 
## 1. Determination Of The Rows Containing Advances

Advance amounts are considered the amounts from all rows where the Party in the Payment Order is the same as the Party in the Payment Transaction and the Payment Order has no value in the <i>Referent Invoice Number</i> field.
 
The condition in the <i>Referent Invoice Number</i> field is appropriate for Sales Orders and Purchase Orders because there we expect that after the Invoice or the Purchase Invoice is released, the Payment Orders are (re)generated with data from the invoice and the <i>Referent Invoice Number</i> field would be filled in. 
 
> [!]
> So the Payment Order with no <i>Referent Invoice Number</i>, created before the invoice and its payment releases, is a payment before the invoice release and is considered an advance.
 
<b><i>Example 1</i></b>:
 
There is a Payment Transaction where the Party is <b>Company 1</b> and it consists of 10 rows:
 
- row #10, Covered Amount = 20 BGN, Amount = 20 EUR, Payment Order = PO #1;
- row #20, Covered Amount = 38 BGN, Amount = 38 EUR, Payment Order = PO#2;
- row #30, Covered Amount = 50 BGN, Amount = 50 EUR, Payment Order = PO #3;
- row #40, Covered Amount = 20 BGN, Amount = 20 EUR, Payment Order = PO #4;
- row #50, Covered Amount = 35 BGN, Amount = 35 EUR, Payment Order = PO #5;
- row #60, Covered Amount = 30 BGN, Amount = 30 EUR, Payment Order = PO #6;
- row #70, Covered Amount = 25 BGN, Amount = 25 EUR, Payment Order = PO #7;
- row #80, Covered Amount = 40 EUR, Amount = 80 BGN, Payment Order = PO #8;
- row #90, Covered Amount = 25 EUR, Amount = 50 BGN, Payment Order = PO #9;
- row #100, Covered Amount = 20 EUR, Amount = 40 BGN, Payment Order = PO #9.



For each of the nine Payment Orders the following data is available:
 
- PO #1: Party = Company 1, Reference Invoice Number = null;
- PO #2: Party = Company 1, Reference Invoice Number = null;
- PO #3: Party = Company 1, Reference Invoice Number = "1100056";
- PO #4: Party = Company 1, Reference Invoice Number = "10700149";
- PO #5: Party = Company 1, Reference Invoice Number = null;
- PO #6: Party = Company 1, Reference Invoice Number = null;
- PO #7: Party = Company 1, Reference Invoice Number = null;
- PO #8: Party = Company 2, Reference Invoice Number = null;
- PO #9: Party = Company 1, Reference Invoice Number = null;

So from these 10 rows, the following rows would be separated - row #10, row #20, row #50, row #60, row #70, row #90 and row #100, and they will be used for the calculation of the advance amounts.
 
## 2. Grouping The Rows

The Payment Transaction Rows, determined in step 1, are grouped by the fields <i>@@name Location, Total Amount Currency</i> and <i>Ref Document</i> from the referred Payment Orders. Thus, for each combination of values from these three fields, a group is formed from the Payment Transaction Rows that meet this data.
 
<b><i>Example 2</i></b>:
 
Let’s use the data from <b><i>Example 1</b></i> and the Payment Orders has the following values in the <i>@@name Location, Total Amount Currency</i> and  <i>Ref Document</i> values:
 
- PO #1, @@name Location = "@@name Location 1", Total Amount Currency = BGN, Ref Document = null;
- PO #2, @@name Location = "@@name Location 1", Total Amount Currency = BGN, Ref Document = null;
- PO #5, @@name Location = "@@name Location 1", Total Amount Currency = BGN, Ref Document = "Sales Order 20001052";
- PO #6, @@name Location = "@@name Location 1", Total Amount Currency = BGN, Ref Document = "Sales Order 20001052";
- PO #7, @@name Location = "@@name Location 1", Total Amount Currency = BGN, Ref Document = "Sales Order 20001052";
- PO #8, @@name Location = "@@name Location 1", Total Amount Currency = EUR, Ref Document = "Sales Order 20001052";

Thus in these seven separated rows, three groups are formed:
 
- Group 1: row #10, row #20 (for "@@name Location 1", BGN and null ref document);
- Group 2: row #50, row #60, row #70 (for "@@name Location 1", BGN and "Sales Order 20001052" ref document);
- Group 3: row #90, row #100 (for "@@name Location 1", EUR and "Sales Order 20001052" ref document).

## 3. Determining The Advance Amount For Each Group

For each group from step 2, an advance amount is calculated, which meets the parameter [Is Amount With VAT]. The amounts are summed up from all rows (the values in the Covered Order Amount field), where the <i>Is Amount With VAT</i> has the same value as the parameter [Is Amount With VAT]. When summing the amounts from the rows the following condition should be considered - if the direction of the Payment Order is different than the direction of the Payment Transaction, then the value in the <i>Covered Order Amount</i> field should be multiplied by -1 before adding it into the total.
 
<b><i>Example 3</b></i>:
 
Let’s use the data from <b><i>Example 1</b></i> and <b><i>Example 2</b></i>  and the [Is Amount With VAT] parameter is True and in all Payment Orders, the <i>Is Amount With VAT</i> field is True, except for PO #5 and PO #6. Also, the direction of the Transaction is <i>Income</i> and all Payment Orders are income, except for PO #1, PO #5 and PO #7, which direction is <i>Expense</i>. So for each group, the following calculations are performed:
 
- for Group 1: [advance amount] = -1 * 20 BGN + 38 BGN = 18 BGN;
- for Group 2: [advance amount] = 30 BGN + -1 * 25 BGN = 5 BGN (the amount from PO #5 is skipped as it does not meet the [Is Amount With VAT] parameter;
- for Group 3: [advance amount] = 0 EUR, as the Payment Orders from all rows do not meet the [Is Amount With VAT] parameter.

In the end, the collection of advance amounts which meet the [Is Amount With VAT] parameter consists of two amounts - 18 BGN and 5 BGN (the last one with 0 EUR is skipped).
 
## Defining The Remaining Amount

In the end, the values from the Amount fields in all group rows are summed up where the value in the <i>Is Amount With VAT </i> field is different from the [Is Amount With VAT] parameter. All these values are not included in the calculations in the previous step. They form the remaining amount. In the current calculation, the amount should be multiplied by -1 if the Payment Order direction differs from the Payment Transaction Direction.
 
<b><i>Example 4</b></i>:
 
Using the data from <b><i>Example 1, Example 2</b></i> and <b><i>Example 3</b></i>, the remaining amount is formed by the amounts from PO #5 and PO #9 as they do not meet the [Is Amount With VAT] parameter. So the result is:
 
[remaining amount]  = -1 * 35 BGN + 50 BGN + 40 BGN = 55 BGN.

