# Cost correction

The current article describes the calculation (and recalculation) of the <b>actual cost</b>. The article [Original cost calculation](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/index.html?q=Original%20Cost%20Calculation) describes how the </b>original cost</b> is calculated. Those calculations are accurate as long as the store transactions are entered in their original chronology. If the order is incorrect, so will be the cost.

<b><i>Example 1:</b></i>

There are two receipt transactions and one issuing transaction entered in the system:

- <b>receipt</b>, Timestamp: <b>05 Jan 2020 12:45, 4 PCS</b>, total cost: <b>100 EUR</b>;

- <b>receipt</b>, Timestamp: <b>05 Jan 2020 17:27, 3 PCS</b>, total cost: <b>75 EUR</b>;

According to the [original cost calculation](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/original-cost-calculation/index.html?q=Original%20Cost%20Calculation)** for average cost, the issuing transaction should be:

- <b>issue</b>, Timestamp: <b>08 Jan 2020 11:29, 5PCS</b>, total cost: 5 * (175/7) = <b>125 EUR</b>;

There is another receipt transaction not entered on time. It happened on <b>07 Jan 2020</b>  and was entered on <b>08 Jan 2020</b>:

- <b>receipt</b>, Timestamp: <b>07 Jan 2020 23:59, 3PCS </b>, total cost: <b>105 EUR</b>;

If the third receipt transaction is entered on time, then the unit cost on <b>08 Jan 2020</b> would be 280/10 = <b>28</b>, not <b>25</b>, as it was originally calculated in the issuing transaction. This is happening due to the late entering of the transaction in the system. The cost of the issuing transaction is incorrect and a recalculation is needed.

The effect of the incorrect cost from <b><i>example 1</b></i> may influence not only issuing transactions. If the issuing operation was about ingredient consumption from the Production module, for example, then the cost of the production output would be incorrect as well. This leads to incorrect cost when issuing the production output.

If you don't enter the transactions in the system on time, there will be negative consequences. To correct them, there is a [basic algorithm for cost correction calculation](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/cost-correction/basic-algorithm-for-cost-correction-calculation.html?q=Basic%20algorithm%20for%20cost%20correction%20calculation). This algorithm changes the costs as if they were entered on time. There is a document named cost correction, where the results from this calculation should be saved. Тhe rows of the document show how the cost is changed (base cost, product cost, store cost, and document cost) for each Transaction row affected.

Cost corrections allow the original cost to be changed. In each transaction row the fields are as follows:

<b>[actual/corrected cost] = [original cost] + [adjustment cost]</b>

where:

<b>[original cost]</b> = the product, store, document, and base cost saved in the transaction row;

<b>[adjustment cost]</b> = the sum of all product, store, document, and base cost values saved in the rows of all the released, non-voided cost corrections referring to the current transaction row.

For more specific information, see:

- **[Basic algorithm for cost correction calculation](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/cost-correction/basic-algorithm-for-cost-correction-calculation.html?q=Basic%20algorithm%20for%20cost%20correction%20calculation)**

- **[Models for maintaining the actual cost](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/cost-correction/models-for-maintaining-the-actual-cost.html?q=Models%20For%20Maintaining%20The%20Actual%20Cost)**

- **[Specific procedures of cost corrections](https://docs.erp.net/tech/modules/logistics/concepts/goods-cost/cost-correction/specific-procedures-of-cost-corrections.html?q=Specific%20Procedures%20of%20Cost%20Corrections)**

