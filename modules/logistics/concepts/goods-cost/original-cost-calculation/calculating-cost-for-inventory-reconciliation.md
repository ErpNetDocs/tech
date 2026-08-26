# Calculating cost for inventory reconciliation

The cost of the receipt and issue store transactions resulting from an Inventory Reconciliation is calculated according to the availability at the Transaction Timestamp of the Inventory Reconciliation.

Before applying this algorithm, the system determines which store transactions participate in the original cost calculation. For details, see [Original cost calculation](index.md).

The cost is determined in the following order:

1. The current availability of the Product in the Store is calculated at the Transaction Timestamp of the Inventory Reconciliation.

2. If the available quantity is different from zero, the average cost of the availability is used.

   The average cost is calculated as:

   `Accumulated Cost / Available Quantity`

   If the available quantity is different from zero but the accumulated cost is zero, the average cost is zero. In this case, the Standard Cost Per Lot is not used.

3. If the available quantity is zero, the unit cost of the last preceding issue store transaction is used.

4. If there is no preceding issue store transaction, the Standard Cost Per Lot from the Product definition is used.

5. If none of the preceding sources provides a cost, the Inventory Reconciliation transaction is created with zero cost.

## Example: Available quantity with zero accumulated cost

Before an Inventory Reconciliation receipt, the Store contains 1 PCS of the Product with zero accumulated cost.

The available quantity is different from zero, so the system uses the average cost:

`0 / 1 PCS = 0`

The Inventory Reconciliation receipt is therefore created with zero cost.

The Standard Cost Per Lot is not used because the available quantity is not zero.
