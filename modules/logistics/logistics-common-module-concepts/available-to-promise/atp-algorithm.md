## ATP Algorithm

The Current Stock Holds are added to the unfulfilled Store orders chronology. Thus, except the physical availability, the store orders which are not fulfilled yet, but planned to be on a specific date, are taken into account (<i>Planned Release Date</i> field is used for indicating this date). So, besides the physical availability, other stock movements, already planned, are taken into account.

Then, the calculated quantities for each date from the new chronology are reviewed and the smallest value is selected. The smallest value is the ATP quantity for the specified parameters.

We use the smallest value. If a greater value (than for the date when we have the smallest value) is entered as ATP quantity, and this quantity is used for a new issuing operation, it will not be enough for all ordered operations. So the minimal quantity in the new chronology actually shows the greatest value we can use (without violating other issuing store processes) for the specified as a parameter date.

Let’s apply that to the example from <b>Available To Promise</b>:

After adding the physical availability to the chronology, we have:

|Date|Physical availability|Start quantity|Receipt quantity|Issue quantity|End quantity
|:----:|:----:|:-----:|:----:|:----: |:----: 
|2021/10/01|8| 3|-|-|11               
|2021/10/03|8|-|-|2|9
|2021/10/04|8|-|16|4|21
|2021/10/07|8|-|-|8|13
|2021/10/09|8|-|-|7|6
|2021/10/14|8|-|8|-|14
|2021/10/16|8|-|4|9|9
|2021/10/19|8|-|-|2|7

Here is the graphical chart for the new chronology:
 
After reviewing the Value Column (or following the lowest values in the graphical chart), you can see that the lowest value is 6 pcs. This is the <b>Available to promise</b> quantity at <b>2021/10/01</b>.

## Total calculations (for a period)

When we are calculating the ATP for a whole period (for more than one date), the data gathering and chronology and the current stock holds combining is executed the way we described earlier. After that, for every date in the period (greater than or equal to the date specified as a parameter) the ATP is defined as follows:

1. The minimal quantity value for the whole period is defined - let's call it <b>min1</b> - and then we pick the last (the greatest) date for this value- <b>date1</b>. So, for every date from the starting date of the period to <b>date1</b> including, the ATP is <b>min1</b>.

2. The minimal quantity value for the period after <b>date1</b> (if there is such period, i.e., if there are dates in the chronology after <b>date1</b>) - is <b>min2</b> and the last date which has this value is <b>date2</b>. So, from the date after <b>date1</b> and before <b>date2</b> including the ATP, it is <b>min2</b>.

3. This is repeated until the dates in the chronology are covered.

The period, we are making calculations for, is divided into several sub-periods (at least one and at most - equal to the count of the dates in the chronology). In the first sub-period there is a minimal value for ATP. For each following sub-period the ATP is greater than the ATP for the previous sub-period.

For example, let's have have the following chronology for the period from <b>01.10</b> to <b>06.10</b>, calculated after adding the current physical availability to the data from the unexecuted Store Orders.


|Date|Physical availability|Start quantity|Receipt quantity|Issue quantity|End quantity
|:----:|:----:|:-----:|:----:|:----: |:----: 
|2021/10/01|12|8|-|-|20               
|2021/10/03|12|-|2|-|22
|2021/10/08|12|-|5|-|27
|2021/10/09|12|-|2|19|10
|2021/10/12|12|-|-|7|3
|2021/10/15|12|-|28|6|25
|2021/10/16|12|-|-|7|18
|2021/10/20|12|-|6|9|15
|2021/10/21|12|-|-|3|12
|2021/10/24|12|-|24|5|31
|2021/10/30|12|-|-|6|25
|2021/10/31|12|-|-|5|20

After reviewing the chronology, it is visible that the period from<b>2021/10/01</b> to <b>2021/10/06</b> is divided to three sub-periods - one from <b>2021/10/01</b> to <b>2021/10/14</b>, second from <b>2021/10/15</b> to <b>2021/10/23</b> and the last one is from <b>2021/10/24</b> to <b>2021/11/06</b>. For the first period the minimal value (hence the ATP) is <b>3 pcs</b>. For the second period it is <b>12 pcs</b>, and for the last period the ATP is <b>20 pcs</b>. These calculations are represented with graphics as follows:
 
## Modifications in the algorithm implementation

There are some specific changes in the ATP calculation algorithm implementation. The definition of the start quantity for the unexecuted Store Orders for a specified period, (when using the unexecuted Store Orders chronology, instead of starting with an opening balance for a defined period) is not really effective. So, all store movements (i.e., all the unexecuted by now store orders) are used with no limits for date and without calculating the starting value. These store movements calculate the ATP for sub-periods. To calculate the ATP for a specific date, we simply take into account the periods before this date and the minimal value from the last period.

This method is effective enough. However, there are some problematic cases - when we want to calculate the ATP for a date, before all existing unexecuted Store Orders. In these cases, there is no Store Orders chronology for this date and as the opening balance is not calculated (here, it would be zero), the previously mentioned principle for ATP calculation cannot be applied.

In these cases (when the date for which we calculate the ATP is before the earliest unexecuted Store Order) the following principle is applied:

1. All unexecuted Store Orders, after the specified date, are taken into account, and the ATP is calculated according to their chronology. This is a value [ <b>Projected Available Balance</b> ]

3. The current physical available quantity is calculated - value [<b>Current Stock Holds</b>]

5. If there are future Store Orders, unexecuted (i.e. if [ <b>Projected Available Balance </b>]  is not null), than: [<b>ATP</b>] = min([ <b>Projected Available Balance</b>], [<b>Current Stock Holds</b>])

7. Otherwise [<b>ATP</b>] = [<b>Current Stock Holds</b>]

For example, if there is current physical availability of <b>10 pcs</b> and there are the following unexecuted Store Orders:

- 2021/10/09 - <b>2 pcs</b>, receipt;

- 2021/10/13 - <b>7 pcs</b>, issue;

- 2021/10/16 - <b>6 pcs</b>, receipt.

In this case the ATP for the dates from <b>2021/10/09</b> to <b>2021/10/15</b> including is <b>5 pcs</b>, and after this date the ATP is <b>11 pcs</b>.

 E.g., If we have the same data from the previous example, with the only difference: the issue for <b>2021/10/13</b> is <b>1 pcs</b>. , the ATPs would be as follows:
 
- before <b>2021/10/09: 10 pcs</b> (this is the smaller value from the current physical availability and the <b>Projected Available Balance</b>) after <b>2021/10/09</b>);

- from <b>2021/10/09</b> to <b>2020/10/15</b> (including): <b>11 pcs</b>;

- from <b>2021/10/16</b> onwards: <b>17 pcs</b>.

