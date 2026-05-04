# Operations
This section describes the main operations used in the **Planned Reconcile** workflow.

These operations follow the reconciliation process from preparing the snapshot, through counting and review, to applying the approved differences in the warehouse.

Use them in the following order:

- [Generate Snapshot](generate-snapshot.md) - Create the reconciliation details from the current warehouse availability.
- [Initial Count](initial-count.md) - Generate the first count orders for the reconciliation scope.
- [Execute count orders in WMS Worker](execute-count-orders-in-wms-worker.md) - Perform the physical count and record the counting result for the current session.
- [Populate Counted Quantities](populate-counted-quantities.md) - Aggregate the performed counts into the reconciliation details.
- [Approve counted results](approve-counted-results.md) - Confirm the rows whose current counted result is accepted.
- [Generate recount orders](generate-recount-orders.md) - Send the selected rows to another counting cycle when another verification is needed.
- [Generate warehouse transactions](generate-warehouse-transactions.md) - Change the document state to **Release** to generate warehouse transactions for the approved differences.

Some operations can be repeated. For example, after a recount is executed in **WMS Worker**, users can populate the counted quantities again, review the result again, and generate another recount if needed.
