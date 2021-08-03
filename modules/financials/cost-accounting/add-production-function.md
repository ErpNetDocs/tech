# Add Production Function

The function is used in the **[Cost distribution](https://github.com/ErpNetDocs/tech/blob/master/modules/financials/cost-accounting/cost-distribution.md)** document. When used, it adds the production from the specified period and stores it in the document.
## How does it work?
 
The functions selects all store transaction lines, filtered by the following conditions:

1. They are part of a document which is at least Released and non-voided.
2. They are part of a document with the same Enterprise Company as the Enterprise Company of the Cost distribution document.
3. They are part of a store transaction store of which is equal to the store in the Cost Distribution header (if specified); if the store of the Cost Distribution header is empty, then the current filter is not applied.
4. The store transaction's movement type is "Receipt";
5. Their Transaction Timestamp is in the specified in the document header period.
6. Their quantity base is not 0.
7. The ParentStoreOrderLine is not null.
8. The store order, specified in the ParentStoreOrderLine field, has Output order as a parent document.
 
When the set of store transaction lines is ready, it is loaded in the Outputs panel of the Cost distribution document. The fields in the panel are filled as follows:
- Line No - unique, consecutive line number. The field is AutoNumber;
- Cost object - the id of the store transaction line;
- Weight coefficient - the function sets the Line base Cost corrections as a coefficient. The Line base Cost corrections equals the sum of [LineBaseCost] (in the current store transaction line) and the sum of [BaseCostAdjustment] of all Cost correction lines which are non-voided and at least released and which refer to the current store transaction lines.

When the data is filled in the Cost distribution outputs table, the Cost distribution document is saved.

