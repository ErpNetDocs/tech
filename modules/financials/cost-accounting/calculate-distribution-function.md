# Calculate distribution function

The function is used in the [Cost distribution](https://docs.erp.net/tech/modules/financials/cost-accounting/cost-distribution.html) document. When used, it calculates the distributed amounts for each output and for each cost type and fills the Results table with the calculations.

## How does it work?

The function performs the following steps:
1. Calculate the sum of the weight coefficients of all outputs.
2. For each output and for each cost type the distributed amount is calculated by the following algorithm: at first, it is assumed that a proportion of the distributed cost amounts is defined, so the distribution is executed. If we have **n** outputs which we have to distribute cost amounts on, for every row (a row is a combination of output and cost type) a weight is defined - **[k<sub>1</sub>]**, **[k<sub>2</sub>]** ... **[k<sub>n</sub>]**. So if the amount of the coefficients is  **[S]** (i.e. **[S]** = **[k<sub>1</sub>]** +**[k<sub>2</sub>]** + ... + **[k<sub>n</sub>]**) and this amount is not equal to 0, than the **i**-row the proportion is **[k<sub>i</sub>]/[S]**:
      - [distribution to row **i**] = ROUND([cost type amount] **[k<sub>i</sub>] / [S]**, 2);<br/>
This is a standard distribution algorithm. Specific cases are when **[S]** is **0**. Usually, in those cases the cost amount is distributed evenly through the row, using the following formula:
      - [row **i** distribution] = ROUND([cost type amount] / [rows count], 2);<br/>
Sometimes the cost amount may not be able to be distributed exactly through the rows. In these cases, an attempt is made to allocate the balance through the rows which the amount is distributed to. Normally, it is impossible to distribute an equal part of the balance to all rows (otherwise there will be no balance). So the balance is distributed by the first several rows starting with the row with the largest amount. Also, in this balance distribution we cannot distribute less than:
           - [minimal balance distribution on a row] = 1 / 10<sup>[Round Scale]</sup>. (the round scale for line amounts is always 2 (currently), so we cannot distribute cost amount of less than 1/10<sup>2</sup> = 0.01)
  
3. In the Results table, the results of step 2 are saved and for each combination of output and cost type, a new row is added.
 
***Example 1***
Let's say there is a cost distribution document with two cost types with the following data:
- Cost Type: **CT1**; Distributed Cost Amount: **100**;
- Cost Type: **CT2**; Distributed Cost Amount: **500**;

In the Outputs table, the following rows are present:

- LineNo: **10**; Cost Object: **StoreTransactionLine1**; Weight Coefficient: **15.00**;
- LineNo: **20**; Cost Object: **StoreTransactionLine2**; Weight Coefficient: **13.00**;
- LineNo: **30**; Cost Object: **StoreTransactionLine3**; Weight Coefficient: **10.11**;
- LineNo: **40**; Cost Object: **StoreTransactionLine4**; Weight Coefficient: **-0.50**;
- LineNo: **50**; Cost Object: **StoreTransactionLine5**; Weight Coefficient: **29.99**.
 
So **[S]** in the example is: 15.00 + 13.00 + 10.11 + -0.50 + 29.99 = **67.60**.

When the calculate distribution function is started, the results table is filled with the following data:

- OutputLineNo = **10**; Cost Type: **CT1**; Distributed Amount Base: **22.19**; **DistributedAmountBase** = **ROUND([k<sub>Output[LineNo=10]</sub>] / [S] * [Cost Type Amount] ; 2)** = ROUND(15.00 / 67.60 * 100; 2) = 22.19;
- OutputLineNo = **20**; Cost Type: **CT1**; Distributed Amount Base: **19.23**; Calculation steps: **DistributedAmountBase** =  ROUND(13.00 / 67.60 * 100 ; 2) = 19.23;
- OutputLineNo = **30**; Cost Type: **CT1**; Distributed Amount Base: **14.96**; Calculation steps: **DistributedAmountBase** =  ROUND(10.11 / 67.60 * 100 ; 2) = 14.96;
- OutputLineNo = **40**; Cost Type: **CT1**; Distributed Amount Base: **-0.74**; Calculation steps: **DistributedAmountBase** =  ROUND(-0.50 / 67.60 * 100 ; 2) = -1.09;
- OutputLineNo = **50**; Cost Type: **CT1**; Distributed Amount Base: **44.36**; Calculation steps: **DistributedAmountBase** =  ROUND(29.99 / 67.60 * 100 ; 2) = 44.36;
- OutputLineNo = **10**; Cost Type: **CT2**; Distributed Amount Base: **110.95**; Calculation steps: **DistributedAmountBase** =  ROUND(15.00 / 67.60 * 500 ; 2) = 110;
- OutputLineNo = **20**; Cost Type: **CT2**; Distributed Amount Base: **96.15**; Calculation steps: **DistributedAmountBase**=  ROUND(13.00 / 67.60 * 500 ; 2) = 96.15;
- OutputLineNo = **30**; Cost Type: **CT2**; Distributed Amount Base: **74.78**; Calculation steps: **DistributedAmountBase** =  ROUND(10.11 / 67.60 * 500 ; 2) = 74.78;
- OutputLineNo = **40**; Cost Type: **CT2**; Distributed Amount Base: **-3.70**; Calculation steps: **DistributedAmountBase** =  ROUND(-0.50 / 67.60 * 500 ; 2) = -3.70;
- OutputLineNo = **50**; Cost Type: **CT2**; Distributed Amount Base: **221.82**; Calculation steps: **DistributedAmountBase** = ROUND(29.99 / 67.60 * 500 ; 2) = 221.82.
 
***Example 2***

Let's see an example where the sum of the DistributedAmountBase of a cost type is not the cost type distributed cost amount. A cost distribution document is present with one cost type **CT1** with amount of **100.93**.

In the Outputs table, the following rows are present:

- LineNo: **10**; Cost Object: **StoreTransactionLine1**; Weight Coefficient: **15.11**;
- LineNo: **20**; Cost Object: **StoreTransactionLine2**; Weight Coefficient: **0.00**;
- LineNo: **30**; Cost Object: **StoreTransactionLine3**; Weight Coefficient: **10.00**;
- LineNo: **40**; Cost Object: **StoreTransactionLine4**; Weight Coefficient: **20.00**;
- LineNo: **50**; Cost Object: **StoreTransactionLine5**; Weight Coefficient: **15.11**.

So the **[S]** in the examples is 15.11 + 0 + 10 + 20 + 15.11 = **60.22**.

When the calculate distribution function is started, the results table is filled with the following data:

- OutputLineNo = **10**; Cost Type: **CT1**; Distributed Amount Base: **25.32**; **DistributedAmountBase** = **ROUND([k<sub>Output[LineNo=10]</sub>] / [S] * [Cost Type Amount] ; 2)** = ROUND(15.11 / 66.22 * 100.93; 2) = 25.32;
- OutputLineNo = **20**; Cost Type: **CT1**; Distributed Amount Base: **0.00**; Calculation steps: **DistributedAmountBase** =  ROUND(0.00 / 66.22 * 100.93 ; 2) = 0.00;
- OutputLineNo = **30**; Cost Type: **CT1**; Distributed Amount Base: **16.76**; Calculation steps: **DistributedAmountBase** =  ROUND(10.00 / 66.22 * 100.93 ; 2) = 16.76;
- OutputLineNo = **40**; Cost Type: **CT1**; Distributed Amount Base: **33.52**; Calculation steps: **DistributedAmountBase** =  ROUND(20.00 / 66.22 * 100.93 ; 2) = 33.52;
- OutputLineNo = **50**; Cost Type: **CT1**; Distributed Amount Base: **25.32**; Calculation steps: **DistributedAmountBase** =  ROUND(15.11 / 66.22 * 100.93 ; 2) = 25.32;

Now the DistributedAmountBase sum is 22.32 + 0.00 + 16.76 + 33.52 + 22.32 = **100.92** and there is difference of 0.01 between the distributed cost amount of the **CT1** as it is **100.93**. The difference of 0.01 meets the requirement of [minimal balance distribution on a row] = **1 / 10**<sup>[2]</sup> =0.01. The balance distribution amount is 0.01 and it should be distributed on the row with largest amount, the row with the Output **[LineNo=40]**. The final Results now would be as follows:

- OutputLineNo = **10**; Cost Type: **CT1**; Distributed Amount Base: **25.32**;
- OutputLineNo = **20**; Cost Type: **CT1**; Distributed Amount Base: **0.00**;
- OutputLineNo = **30**; Cost Type: **CT1**; Distributed Amount Base: **16.76**;
- OutputLineNo = **40**; Cost Type: **CT1**; Distributed Amount Base: **33.53**; (the balance is distributed here)
- OutputLineNo =**50**; Cost Type: **CT1**; Distributed Amount Base: **25.32**.
 
 
> [!NOTE]
>  If the balance distribution amount in ***Example 2*** was 0.02, it would be distributed on OutputLineNo = **40** and OutputLineNo = **10** as these are the first two largest >amounts through the rows.
 

