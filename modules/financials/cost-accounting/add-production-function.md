# Add Production Function

The function is used in the **[Cost distribution](https://github.com/ErpNetDocs/tech/blob/master/modules/financials/cost-accounting/cost-distribution.md)** document. When used, it adds the production from the specified period and store in the document.

## How does it work?

The function selects all store transaction lines, filtered by the following conditions:

1. they are part of a document which is at least Released and non-voided.
2. they are part of a document with the same Enterprise Company as the one of the Cost Distribution document.
3. they are part of a store transaction with a store equal to the one in the Cost Distribution header (if specified); if the store of the Cost Distribution header is empty, then the current filter is not applied.
4. the store transaction's movement type is "Receipt";
5. their Transaction Timestamp is in the specified in the document header period.
6. their quantity base is not 0.
7. the ParentStoreOrderLine is not null.
8. the store order, specified in the ParentStoreOrderLine field, has Output Order as a parent document.

When the set of store transaction lines is ready, it is loaded in the Outputs panel of the Cost Distribution document. The fields in the panel are filled as follows:

- Line No - unique, consecutive line number. The field is AutoNumber;
- Cost Object - the id of the store transaction line;
- Weight Coefficient - the function sets the Line Base Cost Corrections as a coefficient. The Line Base Cost Corrections equals the sum of [LineBaseCost] (in the current store transaction line) and the sum of [BaseCostAdjustment] of all Cost Correction lines which are non-voided and at least released and referring the current store transaction lines.

When the data is filled in the Cost Distribution Outputs table, the Cost Distribution document is saved.

