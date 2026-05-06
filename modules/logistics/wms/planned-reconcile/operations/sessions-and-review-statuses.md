# Sessions and review statuses

This page explains how **Session** and **ReviewStatus** work in Planned Reconcile.

These two values show where each Warehouse Reconciliation Detail is in the reconciliation process and which counting iteration it belongs to.

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

**ReviewStatus** shows the current state of the reconciliation row in the process.

The possible values are:

- **Created**
- **Started**
- **Finished**
- **Approved**
- **Recount**
- **Cancelled**

## Workflow

The following table shows the typical workflow of a reconciliation row through the counting and review cycle.

| Workflow step | Session | ReviewStatus | Notes |
|---|---:|---|---|
| [Generate Snapshot](generate-snapshot.md) | 0 | Created | The reconciliation detail is created from the current warehouse availability. |
| [Initial Count](initial-count.md) | 1 | Started | The row enters the first counting session. |
| [Execute count orders in WMS Worker](execute-count-orders-in-wms-worker.md) | — | Finished | After the orders for the current session are completed, the related rows move from **Started** to **Finished**. |
| [Populate Counted Quantities](populate-counted-quantities.md) | — | — | The operation updates the counted quantities, but does not change the session or review status. |
| Review the counted result | — | Approved / Recount / Cancelled | Review the current counted result for the selected row. Set **Approved** when the result is accepted, **Recount** when another counting cycle is required, or **Cancelled** when the current result should be discarded. |
| [Generate recount orders](generate-recount-orders.md) | 2, 3, 4, ... | Started | Only the selected rows marked for **Recount** move to the next session. |
| [Execute count orders in WMS Worker](execute-count-orders-in-wms-worker.md) | — | Finished | The rows in the recount session move to **Finished** when the recount orders are completed. |
| [Populate Counted Quantities](populate-counted-quantities.md) | — | — | The counted result is refreshed for the current recount session. |
| Review the recounted result | — | Approved / Cancelled | Review the updated result and set **Approved** or **Cancelled**. |

> [!NOTE]
> Recount does not move all reconciliation rows to a new session.
> Only the rows selected for recount move to the next session when [Generate recount orders](generate-recount-orders.md) is used.
> All other rows keep their current **Session** and **ReviewStatus**.
