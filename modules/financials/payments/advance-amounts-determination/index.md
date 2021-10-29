# Advance amounts determination

The current article describes the algorithm which defines what part of the amounts of a given payment is paid in advance. This algorithm is applicable both in income payments and expense payments so it can determine the advance amounts in both sales orders and purchase orders.
 
Input algorithm data:
 
- Payment transactions which contains the advance amounts;
- [Is Amount With VAT] - a parameter that may be True or False and defines if the amounts include VAT or not.

Output algorithm data:
 
- Collection of the advance amounts found in the Payment Transaction, which meets the parameter [Is Amount With VAT];
- The total remaining advance amount does not meet the parameter [Is Amount With VAT].

The advance amounts are extracted from the Payment Transaction rows and their calculation depends on the data in the payment orders which are referred to in the rows. The algorithm uses the following schema:
 
1. Determine the rows containing advance amounts.
2. Grouping the rows from step 1.
3. For each group, a total amount is determined, which meets the [Is Amount With VAT] parameter, and this total amount is added to the collection of advance amounts.
4. All rows (from all groups), which contain advance amounts and do not correspond to [Is Amount With VAT], are summed up and they define the remaining amount.

For a more detailed explanation of the algorithm, see Advance Amount Calculation Algorithm](https://docs.erp.net/tech/modules/financials/payments/advance-amounts-determination/advance-amount-calculation-algorithm.html?q=advance).
