# Projected availability report

This report is based on **[Projected available balance](https://github.com/ErpNetDocs/tech/blob/master/modules/logistics/logistics-common-module-concepts/projected-available-balance.md)** and shows the inventory balance projected into the future.

## Fields

This article describes the most important fields in the report:

- Document Date - this is the *Planned Release date* of the Store orders;
- On Hand Quantity Base - the Stock Holds for *Today*;
- Planned Quantity Base - planned movement of the product (negative number when issuing, positive number when receiving). The result is calculated from non-voided, at least Released Store transactions, with Transactions Timestamps equal to the Document date field;
- Planned Quantity Base To Date - planned movement of the product so far. It is basically the running total of the Planned quantity base field. The result is calculated from non-voided at least Released store orders with Planned release date  equal to the Document date field;
- Projected Available Balance - this is the planned Stock Holds after the planned movements happen;
- Available To Promise - the minimum quantity available for use in future issuing operations and which will not violate the current issue operations, already planned or done with this product.

This data is calculated for a specified store and/or product.
