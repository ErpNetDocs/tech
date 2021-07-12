# Calculating Cost for Inventory Reconciliation

The cost of the issue and receipt store transactions, which are the result of an Inventory Reconciliation, are calculated according to the current availabilities in the store, as on the date of the inventory reconciliation.

Since some of the products may not be available, the calculation is performed according to the following algorithm:

- The current availability of the product on the date of the inventory reconciliation is calculated.

- If the current availability is different from 0, the <b>Average Cost</b> is taken.

- If the current availability is 0, the <b>Unit Cost</b> of the last issue store transaction is taken.

- If there is no previous issue store transaction, the <b>Standard Cost</b> is taken (from the product definition).


