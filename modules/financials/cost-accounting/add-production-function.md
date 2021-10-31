# Add production function

This function is used in the [Cost distribution](https://docs.erp.net/tech/modules/financials/cost-accounting/cost-distribution.html) document. 

When used, it adds the production from the specified period and store to the document.

## How does it work?

The function selects all store transaction lines, filtered by the following conditions:

1. They are part of a document which is at least Released and non-voided.
2. They are part of a document with the same enterprise company as the one of the cost distribution document.
3. They are part of a store transaction with a store equal to the one in the cost distribution header (if specified); if the store of the cost distribution header is empty, then the current filter is not applied.
4. The store transaction's movement type is "Receipt";
5. Their Transaction Timestamp is in the period specified in the document header.
6. Their quantity base is not 0.
7. The ParentStoreOrderLine is not null.
8. The store order specified in the ParentStoreOrderLine field has output order as a parent document.

When the set of store transaction lines is ready, it is loaded in the *Outputs* panel of the cost distribution document. The fields in the panel are filled as follows:

- Line No - unique, consecutive line number. The field is AutoNumber;
- Cost Object - the id of the store transaction line;
- Weight Coefficient - the function sets the Line Base Cost Corrections as a coefficient. The line base cost corrections equals the sum of [LineBaseCost] (in the current store transaction line) and the sum of [BaseCostAdjustment] of all cost correction lines which are non-voided and at least released and referring the current store transaction lines.

When the data is filled in the cost distribution outputs table, the [Cost distribution](https://docs.erp.net/tech/modules/financials/cost-accounting/cost-distribution.html) document is saved.

