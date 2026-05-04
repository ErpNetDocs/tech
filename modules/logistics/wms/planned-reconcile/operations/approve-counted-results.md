## Approve counted results

Use **Approve counted results** to confirm the counted result for the selected reconciliation rows.

This operation is used after the current counting session is completed in **WMS Worker**, the related detail rows have moved to **Finished**, and **Populate Counted Quantities** has refreshed the counted result in the reconciliation details.

### When to use it

Use **Approve counted results** when the user has already reviewed the current result and wants to confirm that no further recount is needed for the selected rows.

At this stage, the selected rows already contain:

- the snapshot quantity;
- the latest counted quantity for the current session;
- the current difference between expected and counted result.

### What the operation uses as input

The operation uses the selected **Warehouse Reconciliation Details**.

The user decides which rows are accepted in their current state and approves only those rows.

This means approval is done per reconciliation row, not for the whole document at once.

### What the operation does

For each selected row, **Approve counted results** confirms the currently visible counted result as accepted for the reconciliation process.

The operation changes the row status to **Approved**.

After that, the row is no longer part of the active review cycle for the current discrepancy, unless the process is explicitly continued in another way.

### What the user approves

The user approves the result for a specific reconciliation row in its current form.

This means the user approves the currently reviewed stock position, for example:

- product **A** in location **L-01** with counted quantity equal to the snapshot quantity;
- product **B** in location **L-02** with a confirmed shortage;
- product **C** with a confirmed excess quantity;
- a row created during counting with **SnapshotQuantity = 0** and a counted quantity greater than zero.

In all of these cases, the user is not approving the counting action itself. The user is approving the current reconciliation result for the selected row.

### Example

A row shows:

- **Product**: Item A
- **Location**: Zone 01 / Loc 01
- **SnapshotQuantity**: 10
- **CountedQuantity**: 8

If the manager reviews the row and decides that the counted quantity of **8** is correct, the row can be approved in that state.

If the manager is not confident that the difference is final, the row should not be approved yet and can be sent to recount instead.

### What users should expect after the operation finishes

After **Approve counted results** is completed:

- the selected reconciliation rows are marked as **Approved**;
- these rows are accepted with their current counted result;
- the remaining unapproved rows can continue through another recount cycle if needed.

From a user perspective, this is the step where the manager confirms which rows already have a final accepted result.

The next operation depends on the remaining rows. If some discrepancies still need another check, users continue with a recount operation. When all required rows are approved, the process can continue with **Release**.
