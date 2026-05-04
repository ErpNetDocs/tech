## Populate Counted Quantities

Use **Populate Counted Quantities** to update the reconciliation details with the latest counted result from the completed count session.

This operation reads the performed counts and aggregates them into the corresponding **Warehouse Reconciliation Details**. It is the step that turns the raw counting result into a reviewable reconciliation result.

### When to use it

Use **Populate Counted Quantities** after count orders have been executed in **WMS Worker** and before the next review step.

This operation is used after every counting iteration:

- after **Initial Count**;
- after **Recount (Split Level)**;
- after **Recount (Single Order)**.

In practice, it is the recurring step between execution and approval.

### What the operation uses as input

The operation uses:

- the current **Warehouse Reconciliation**;
- the existing **Warehouse Reconciliation Details**;
- the performed warehouse counts for the current counting session.

It works only with the rows that belong to the current reconciliation and to the active counting session.

### What the operation updates

For each reconciliation detail, the operation updates the counted result with the aggregated quantities from the performed counts.

The main updated fields are:

- **CountedQuantityBase**
- **CountedQuantity**
- **LastAggregatedAt**

The counted quantities are refreshed from the latest aggregated counting result for the current session.

### How the aggregation works

The operation matches the performed counts to the reconciliation details by the same detailed stock position.

The aggregation follows the detailed characteristics of the counted position, such as:

- warehouse location;
- product;
- variant;
- lot;
- serial number;
- logistic unit.

When several count records belong to the same reconciliation detail, their result is aggregated into that detail.

This produces one updated counted result per reconciliation row.

### What happens when counted data exists for a missing detail

If the performed counts contain a position that does not yet exist in the reconciliation details, the operation creates a new **Warehouse Reconciliation Detail** for it.

The new row is created with:

- the current **Warehouse Reconciliation**;
- the matching warehouse and product characteristics from the counted position;
- **SnapshotQuantityBase = 0**;
- **SnapshotQuantity = 0**;
- populated counted quantities from the aggregated count result.

This ensures that newly discovered counted positions also participate in the review process.

### What users should expect after the operation finishes

After **Populate Counted Quantities** is completed:

- the reconciliation details contain the latest counted result for the current session;
- newly counted positions that were not part of the snapshot can appear as new reconciliation rows;
- the reconciliation is ready for review and approval.

From a user perspective, this is the operation that refreshes the reconciliation result after each counting iteration.

The next operation is usually **Approve**. If some rows still need another verification, the process can continue with another recount cycle.
