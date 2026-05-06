# Sessions and review statuses

This page explains how **Session** and **ReviewStatus** work in **Planned Reconcile**.

These two values show where each **Warehouse Reconciliation Detail** is in the reconciliation process and which counting iteration it belongs to.

## Session

**Session** identifies the counting iteration for a reconciliation row.

Use it to distinguish:

- the initial snapshot state;
- the first counting session;
- each next recount session.

The values progress as follows:

- **Session = 0** — the row is created by [Generate Snapshot](generate-snapshot.md);
- **Session = 1** — the row enters the first counting session through [Initial Count](initial-count.md);
- **Session = 2, 3, ...** — the row enters the next recount session through [Generate recount orders](generate-recount-orders.md).

A new session is created only when a new counting cycle starts for that row.

## ReviewStatus

**ReviewStatus** shows the current state of the reconciliation row inside the process.

The possible values are:

- **Created**
- **Started**
- **Finished**
- **Approved**
- **Recount**
- **Cancelled**

These values show whether the row is still only part of the snapshot, already sent for counting, finished for the current counting session, approved, or selected for another recount cycle.

## How Session and ReviewStatus change

The following table shows the typical lifecycle of a reconciliation row.

## Review decisions and their effect

During the review, the user does not manually enter a review status value. Instead, the user reviews the counted result for each row and chooses what to do next. The system then updates the row accordingly.

## Review statuses

The review status shows the current review result for each reconciliation row after the counted quantities are reviewed.

## Review statuses

The review status shows the current review result for each reconciliation row after the counted quantities are reviewed.

| Workflow step | Session | ReviewStatus | Notes |
|---|---:|---|---|
| [Generate Snapshot](generate-snapshot.md) | 0 | Created | The reconciliation detail is created from the current warehouse availability. |
| [Initial Count](initial-count.md) | 1 | Started | The row enters the first counting session. |
| [Execute count orders in WMS Worker](execute-count-orders-in-wms-worker.md) | no change | Finished | After the orders for the current session are completed, the related rows move from **Started** to **Finished**. |
| [Populate Counted Quantities](populate-counted-quantities.md) | no change | no change | The operation updates the counted quantities, but does not change the session or review status. |
| Make a review decision | no change | Approved / Recount / Cancelled | Review the current counted result for the selected row. Set **Approved** when the result is accepted, **Recount** when another counting cycle is required, or **Cancelled** when the current result should be discarded. |
| [Generate recount orders](generate-recount-orders.md) | next session for selected rows only | Started | Only the selected rows marked with **Recount** move to the next counting session. |
| [Execute count orders in WMS Worker](execute-count-orders-in-wms-worker.md) | no change | Finished | The rows in the recount session move to **Finished** when the recount orders are completed. |
| [Populate Counted Quantities](populate-counted-quantities.md) | no change | no change | The counted result is refreshed for the current recount session. |
| Make the final review decision | no change | Approved / Cancelled | Review the updated result. Set **Approved** when the recount result is accepted, or **Cancelled** when the current result should not be used. |
Recount does not move all reconciliation rows to a new session.

Only the rows selected for recount move to the next session when [Generate recount orders](generate-recount-orders.md) is used.

All other rows keep their current:

- **Session**
- **ReviewStatus**

This is important because a reconciliation can contain rows that are already approved together with rows that continue through another recount cycle.

## Finished rows

A row reaches **Finished** after the related count orders for the current session are completed in [WMS Worker](execute-count-orders-in-wms-worker.md).

This is an automatic transition for the current counting session.

After that, the row is ready for [Populate Counted Quantities](populate-counted-quantities.md), which updates the counted result for review.

## Approved rows

A row reaches **Approved** when the user accepts its current counted result.
An approved row keeps its current session and no longer continues in the active review cycle, unless the process explicitly sends it through another path.

## Recount rows

A row enters another counting cycle when the user selects it and runs [Generate recount orders](generate-recount-orders.md).

At that point:

- the row moves to the next session;
- the row status becomes **Started**;
- the row becomes active in the new recount cycle.

## Cancelled rows

A row with **ReviewStatus = Cancelled** does not participate in the active counting cycle.

Cancelled rows are excluded from count order generation.

## Example

A reconciliation row is created by [Generate Snapshot](generate-snapshot.md).

At that point:

- **Session = 0**
- **ReviewStatus = Created**

Then the warehouse manager runs [Initial Count](initial-count.md).

The row becomes:

- **Session = 1**
- **ReviewStatus = Started**

After the worker completes the order in [WMS Worker](execute-count-orders-in-wms-worker.md), the row becomes:

- **Session = 1**
- **ReviewStatus = Finished**

After [Populate Counted Quantities](populate-counted-quantities.md), the counted result is visible for review.

If the manager wants to approve the result, the Review Status, myst be set to Approved status. 

If the result is not accepted, the user selects the row and runs [Generate recount orders](generate-recount-orders.md).

The row then becomes:

- **Session = 2**
- **ReviewStatus = Started**

This starts the next recount cycle for that row only.
