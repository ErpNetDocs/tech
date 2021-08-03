# Sales Order Row Types

The classification of the Sales Order rows describes three main row types - Normal Sale, Sales Return and Neutral operation. The row type is important for some generation procedures from Sales Order.

## Types

The row type is defined by the signs of the quantity value and the amount in it. These criteria are chosen because it is most common and natural. For example, it is possible to define if a Sales Order row is for stock return or not by the values in the Return For Sales Order Line field in the lines or the header field - ReturnForSalesOrder. But it is also possible for the user to enter a Sales Order for stock to directly return negative values in the quantity and/or amount fields without using tools such as ReturnForSalesOrderLine or ReturnForSalesOrder. Thus, the signs of the values in the Quantity and Line Amount fields are the most common and natural criterion to determine the row type.
 
Thus, according to the signs of the quantity and the amount, there are three main types of Sales Order rows:
 
- ***normal sale*** - rows with quantity > 0 or amount > 0;
- ***sales return*** - rows with quantity < 0 or amount < 0;
- ***neutral operation*** - rows with quantity == 0 and amount == 0.

## Why Defining Row Type Is Important?

The types, listed above, are used in the generation procedures of Store Orders and Shipment Orders from Sales Orders and the row type is important.
 
For example, if the row type is sales return, then if the product is shippable or not doesn’t matter - the Store Orders and Invoicing Orders are generated always directly from the Sales Order. If the row type is a normal sale - then if the product is shippable or not is important and it defines if Shipment Order has to be created or Store Order and Invoice Order directly from the Sales Order.
 
The rows with neutral operation do not participate in these generation procedures as for a row with zero quantity and zero amount there is no point of creating nor Store Orders, nor Invoice Orders.
 
## Row Data Validations And Rules

To avoid ambiguity when defining the type of a Sales Order row, certain restrictions are required when entering data in the Sales Orders. For example, quantity < 0 is not allowed with amount > 0 in one row as this row would be normal sale and return sale at the same time, which would lead to double Store Orders and Invoice Orders generation for the current row.
 
These are all restrictions in the data in the Sales Orders, related to the row types definition:
 
- the quantity and the amount in the row must be with the same signs (for example, one is > 0 and the second is < 0);
- if the quantity and the amount in the row are positive then the ReturnForSalesOrderLine, ReturnForInvoiceLine and HistoricalUnitCost must be null; the header fields "ReturnForSalesOrder and ReturnForInvoice must be also null;
- if one of the quantities or the amount in the row is negative and the product is not stocked then the HistoricUnitCost must be null;
- if one of the quantities or the amount in the row is negative and the product is stocked, then exactly one of the fields must have value - ReturnForSalesOrderLine and HistoricUnitCost.

These restrictions are also required because they maintain the overall validity of the data in the Sales Order according to the business logic of the fields being part of the constraints.
 
Validation is not only applied when the data is entered in the row, it may also appear and during the execution of a generation procedure.

