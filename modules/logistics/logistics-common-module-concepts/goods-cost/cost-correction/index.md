# Cost Correction

The current article describes the calculation (and re-calculation) of the <b>actual cost</b>. The article <b>Original Cost Calculation</b> describes how the </b>original cost</b> is calculated. Those calculations are accurate as long as the store transactions are entered in their original chronology. If the order is incorrect, so will be the cost.

<b><i>Example 1:</b></i>

There are two receipt transactions and one issuing transaction entered in the system:

- <b>receipt</b>, Timestamp: <b>05 Jan 2020 12:45, 4 PCS</b>, total cost: <b>100 EUR</b>;

- <b>receipt</b>, Timestamp: <b>05 Jan 2020 17:27, 3 PCS</b>, total cost: <b>75 EUR</b>;

According to the <b>Original Cost Calculation</b> for average cost, the issuing transaction should be:

- <b>issue</b>, Timestamp: <b>08 Jan 2020 11:29, 5PCS</b>, total cost: 5 * (175/7) = <b>125 EUR</b>;

There is another receipt transaction not entered on time. It happened on <b>07 Jan 2020</b>  and was entered on <b>08 Jan 2020</b>:

- <b>receipt</b>, Timestamp: <b>07 Jan 2020 23:59, 3PCS </b>, total cost: <b>105 EUR</b>;

If the third receipt transaction is entered on time, then the unit cost on <b>08 Jan 2020</b> would be 280/10 = <b>28</b>, not <b>25</b>, as it was originally calculated in the issuing transaction. This is happening due to the late entering of the transaction in the system. The cost of the issuing transaction is incorrect and a re-calculation is needed.

The effect of the incorrect cost from <b><i>Example 1</b></i> may influence not only issuing transactions. If the issuing operation was about ingredient consumption from the Production module, for example, then the cost of the production output would be incorrect as well. This leads to incorrect cost when issuing the production output.

If you don't enter the transactions in the system on time, there will be negative consequences. To correct them, there is a <b>Basic Algorithm For Cost Correction Calculation</b>. This algorithm changes the costs as if they were entered on time. There is a document named Cost Correction, where the results from this calculation should be saved. Тhe rows of the document show how the cost is changed (base cost, product cost, store cost, and document cost) for each Transaction row affected.

Cost Corrections allow the Original Cost to be changed. In each Transaction row the fields are as follows:

<b>[actual/corrected cost] = [original cost] + [adjustment cost]</b>

where:

<b>[original cost]</b> = the product, store, document, and base cost saved in the Transaction row;

<b>[adjustment cost]</b> = the sum of all product, store, document, and base cost values saved in the rows of all the released, non-voided Cost Corrections referring to the current Transaction row.

For more specific information, see:

- <b>Basic Algorithm For Cost Correction Calculation</b>

- <b>Models For Maintaining The Actual Cost]</b>

- <b>Specific Procedures of Cost Corrections]</b>

