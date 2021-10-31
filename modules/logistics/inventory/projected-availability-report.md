# Projected availability report

This report is based on [projected available balance](https://docs.erp.net/tech/modules/logistics/planning/projected-available-balance.html?q=projected%20available%20balance) and shows the inventory balance projected into the future.

## Fields

This article describes the most important fields in the report:

- Document date - this is the planned release date of the store orders;
- On hand quantity base - the stock holds for *today*;
- Planned quantity base - planned movement of the product (negative number when issuing, positive number when receiving). The result is calculated from non-voided, at least released store transactions, with transactions timestamps equal to the Document date field;
- Planned quantity base to date - planned movement of the product so far. It is basically the running total of the Planned quantity base field. The result is calculated from non-voided at least released store orders with planned release date  equal to the Document date field;
- Projected available balance - this is the planned stock holds after the planned movements happen;
- Available to promise - the minimum quantity available for use in future issuing operations and which will not violate the current issue operations, already planned or done with this product.

This data is calculated for a specified store and/or product.
