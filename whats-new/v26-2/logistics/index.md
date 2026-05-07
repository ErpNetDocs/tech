# Logistics
Here we share the latest improvements and updates in Logistics, designed to make warehouse operations faster, smoother, and more reliable.

## Improved Serial Number Sequences in Execute Store Orders (v26.2)

In version **26.2**, we introduced an important improvement in the Barcode panel when working with serial numbers during **Execute Store Orders**.

### What changed?

Previously, the **SEQUENCE START / SEQUENCE END** modes were limited to Receipt-only scenarios.

Now the system supports more flexible and realistic warehouse workflows:

- **Issue-only lines**  
  → existing serial numbers are correctly identified and applied.

- **Receipt-only lines**  
  → new serial numbers are generated as expected.

- **Mixed Receipt/Issue documents**  
  → when an Issue line is detected, the system automatically uses existing serial numbers.

### Current limitation

To generate new serial numbers on Receipt lines, all visible document lines must still be of movement type **Receipt**.

### Why this matters

This improvement allows warehouse operators to handle serial numbers faster and more reliably in real-world scenarios, while maintaining strict control over serial number generation.

Learn more here: https://docs.erp.net/winclient/introduction/barcode-commands/panel-modes/sequence-start.html


## Planned Reconcile in WMS

We now have **Planned Reconcile** in WMS — a structured process for warehouse stock counting.

It helps businesses organize counting activities more clearly, review the results, repeat the count only where needed, and apply the approved differences in a controlled way.

This makes Planned Reconcile a good fit for warehouses that need a more manageable and reliable inventory counting process.

Read the documentation to learn how it works and how to set it up:

[Planned Reconcile](https://docs.erp.net/tech/modules/logistics/wms/planned-reconcile/index.html)
