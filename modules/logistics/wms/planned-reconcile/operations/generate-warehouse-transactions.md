## Generate warehouse transactions

The warehouse manager changes the document state of the **Warehouse Reconciliation** to **Release** to generate **Warehouse Transactions** for the approved reconciliation differences.

Use this operation after the counting and review are finished and the required reconciliation rows are already approved.

The system uses the approved **Warehouse Reconciliation Details**. For each approved row, it compares the snapshot quantity with the approved counted quantity and generates the corresponding warehouse transaction for that stock position.

The generated transactions use:

- **TaskType = Count**;
- the warehouse and stock position from the approved reconciliation row;
- the quantity of the approved difference.

The transaction direction depends on the approved result:

- **Count IN** for positive differences;
- **Count OUT** for negative differences.

### Example

A row shows:

- **SnapshotQuantity**: 10
- **CountedQuantity**: 8

After the row is approved, the warehouse manager changes the document state to **Release**. The system then generates a **Count OUT** warehouse transaction for the corresponding quantity.

If another approved row has a counted quantity greater than the snapshot quantity, the system generates a **Count IN** warehouse transaction.

### What users should expect after the operation finishes

After the warehouse manager changes the document state to **Release**:

- warehouse transactions are generated for the approved reconciliation differences;
- the approved differences are applied in the warehouse process;
- the reconciliation moves from reviewed result to applied result.

### What changes in the reconciliation details

**Generate warehouse transactions** does not start a new counting session and does not change the counting lifecycle of the reconciliation rows.

At this stage, the operation works with rows that are already **Approved** and uses them to generate warehouse transactions when the document state changes to **Release**.

> [!NOTE]
> For an overview of how **Session** and **ReviewStatus** change throughout the process, see [Sessions and review statuses](sessions-and-review-statuses.md).

This is the final operation in the reconciliation workflow.
