# Operations
This section describes the main operations used in the **Planned Reconcile** workflow.

These operations follow the reconciliation process from preparing the snapshot, through counting and review, to applying the approved differences in the warehouse.

Use them in the following order:

1. [Generate Snapshot](generate-snapshot.md)  
   Create the reconciliation details from the current warehouse availability.

2. [Initial Count](initial-count.md)  
   Generate the first count orders for the reconciliation scope.

3. [Execute count orders in WMS Worker](execute-count-orders-in-wms-worker.md)  
   Perform the physical count and record the counting result for the current session.

4. [Populate Counted Quantities](populate-counted-quantities.md)  
   Aggregate the performed counts into the reconciliation details.

5. [Approve counted results](approve-counted-results.md)  
   Confirm the rows whose current counted result is accepted.

6. [Generate recount orders](generate-recount-orders.md)  
   Send the selected rows to another counting cycle when another verification is needed.

7. [Generate warehouse transactions](generate-warehouse-transactions.md)  
   Change the document state to **Release** to generate warehouse transactions for the approved differences.

Some operations can be repeated. For example, after a recount is executed in **WMS Worker**, users can populate the counted quantities again, review the result again, and generate another recount if needed.
