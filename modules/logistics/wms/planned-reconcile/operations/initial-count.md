## Initial Count

Use **Initial Count** to generate the first count orders for the reconciliation.

This operation starts the first counting session and creates one or more **Warehouse Orders** based only on the existing **Warehouse Reconciliation Details**.

The purpose of **Initial Count** is to send the selected reconciliation scope to the warehouse workers for the first physical count.

### When to use it

Use **Initial Count** after [Generate Snapshot](generate-snapshot.md) and before any counting has started.

At this stage:

- the reconciliation document is already prepared;
- the snapshot has already created the reconciliation details;
- the first counting session has not started yet.

### What the operation checks

Before generating the count orders, the system checks that:

- the reconciliation document is in state **Planned** or **Firm Planned**;
- the selected warehouse has a defined **CountingOrderDocumentType** policy;
- there is at least one reconciliation detail that is not **Cancelled**;
- all non-cancelled reconciliation details are still in their initial state:
  - **ReviewStatus = Created**
  - **Session = 0**

This means **Initial Count** is used only for the first counting pass.

### What the operation uses as input

The operation uses only the existing **Warehouse Reconciliation Details**.

No additional source is read at this stage.

For order generation, the system includes only details that are:

- **ReviewStatus = Created**
- **Session = 0**

Rows with **ReviewStatus = Cancelled** are not included in the generated orders.

### What the operation creates

The system creates one or more **Warehouse Orders** with:

- **TaskType = Count**
- document type defined by the **CountingOrderDocumentType** policy
- **Warehouse = Warehouse Reconciliation.Warehouse**
- **Parent = Warehouse Reconciliation**
- **DocumentDate = today**
- **State = Planned**

In the order header, **AdditionalDetailsJson** stores the counting session information:

- **CountingSession = 1**

It also stores **TotalQuantityBase** for the details included in the respective order.

### How the order lines are generated

The generated **Warehouse Order Lines** contain only counting locations.

They do not contain detailed product positions.

If the reconciliation details contain several rows for the same **Warehouse Location**, the system creates only one order line for that location.

In other words, the details are grouped by **Warehouse Location**, so each location appears only once in the generated order lines.

Each generated order line contains:

- **Warehouse Location**
- **Warehouse Zone**
- **TaskType = Count**

The detailed product fields remain empty at this stage, because the first counting pass is location-based.

### How the split works

The generated orders can remain in a single document or be split into multiple documents.

This is controlled by the warehouse policy **CountingSplitLevel**.

- If the policy is not defined, the system creates **one Warehouse Order**.
- If the policy is set to **0**, the system creates **one Warehouse Order**.
- If the policy is set to a value greater than **0**, the system splits the orders by warehouse zones at the corresponding hierarchy level.

This split affects only how the initial counting work is distributed.  
The source of the data remains the same — the existing reconciliation details.

### What changes in the reconciliation details

After the orders are generated:

- the included detail rows change from **ReviewStatus = Created** to **ReviewStatus = Started**
- the counting session becomes **Session = 1**

This marks the reconciliation as already started and prevents the first counting session from being generated again as a new initial count.

### What users should expect after the operation finishes

After **Initial Count** is completed:

- one or more **Warehouse Orders** are created;
- each order contains only the locations that need to be counted;
- the reconciliation details are marked as started for the first counting session.

From a user perspective, this is the point where the reconciliation moves from preparation into execution on the warehouse floor.

The next operation is usually to execute the generated count orders in **WMS Worker**. After the first counting pass is completed, the process continues with review and, if needed, 
