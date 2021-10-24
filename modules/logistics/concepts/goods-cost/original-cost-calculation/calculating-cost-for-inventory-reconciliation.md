# Calculating cost for inventory reconciliation

The cost of the issue and receipt store transactions, which are the result of an inventory reconciliation, are calculated according to the current availabilities in the store, as on the date of the inventory reconciliation.

Since some of the products may not be available, the calculation is performed according to the following algorithm:

- The current availability of the product on the date of the inventory reconciliation is calculated.

- If the current availability is different from 0, the <b>average cost</b> is taken.

- If the current availability is 0, the <b>unit cost</b> of the last issue store transaction is taken.

- If there is no previous issue store transaction, the <b>standard cost</b> is taken (from the product definition).


