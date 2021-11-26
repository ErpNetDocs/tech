# Serial numbers 

Serial numbers are a way of identifying the different pieces of a product. They may be used for equipment, software, assets and more. With the Serial numbers the user can follow what happens with objects, which are otherwise identified by the system with one product definition (i.e. one Product_Id). The Serial numbers are also important for identification when providing guarantee and support. 

For example, in a sales order, the user may enter a row with three pieces which will have to be shipped separately (1 piece at a time). But (in the sales order) the user cannot mark which one of the three pieces is shipped first, which one is shipped second and etc. In the sales order, three Serial numbers are entered, but in the Shipments, the user may specify by Serial numbers which one is shipped each time and  which Shipment exactly refers to it. 

## Implementation 

The Serial numbers are recorded in a separate table where each record is an individual Serial number. Additional information is specified as Product, Lot (eventually), Availability (is the current piece blocked), Serial number card data and more. 

This way of implementation is preferred instead of the initial idea of defining number groups. In this implementation, the numbers in each group cannot be identified by something other than the symbols of their record. This is not very helpful because there are cases with fundamental differences between two Serial numbers which may be entered in one document row. For example, one of them may be blocked for future usage, and the second one - not. Other than that, visually, it looks better when the different Serial numbers are displayed in different document rows. This corresponds with the fact that we treat the products with different Serial numbers as different products.  

Also, the current implementation considerably eases the entering of Serial numbers by barcode scanner. Tracking of the current availability is easier as well as the tracking of the product with a specified serial number. 

## Usage in documents 

Whether a product should be used with or without Serial numbers, is a property set in its definition - *Is Serialized* field. If a product is not serialized, Serial numbers are **forbidden** when working with this product. If it is serialized, than serial number usage is **required** in Transactions and Reconciliations, and in the other documents it is **allowed**, but not required. 

Usually, Serial numbers are entered in the transactions and reconciliations. In the previous documents (Receiving orders, Sales orders etc.) the user is able to enter a serial number but such kind of usage is rare. If the serial number is not entered, for example in the Receiving order, the user may enter just one row with the quantity of **10 PCS** and breaking down this row to 10 separated rows with different Serial numbers and quantity of **1 PCS** happens in the Transaction. The main way to break down one row to several with different Serial numbers happens through the Barcode commands panel for Store orders execution. 

## Data entry validation 

The serial number is specified in the documents rows by selecting it from a dropdown list. When the value in this field changes, the following validations should be performed: 

- if the row is a Transaction row or a Reconciliation row - then the value should be different than null only if the product is serialized; 
- if the row is a different document row (not a Transaction or a Reconciliation) - then the value may (but not necessarily) be not-null only if the product is serialized. If it is not serialized, then null value is required; 
- If there is a serial number in the row, then the quantity in the row must be 1, 0 or -1 and the measurement unit must be *pieces* ; 
- if the entered value in the *Serial Number* field is different from null, then the product from the current row must be the same as the product in the serial number definition. 

## Easy entry/selection 

Entering new Serial numbers and selecting an already entered one should be as easy as possible. 

For this purpose, when entering a serial number and in a dropdown list a number ( nonexistent in the database for the current product) is selected, then a record with this value is created in the database automatically. This will have the greatest effect when working with the Barcode commands panel. This panel has a working mode which creates new Serial numbers and it is available only when *receiving* goods in the store. If the user *issues* goods, they can choose only Serial numbers, which are already entered in the database. 

Also, there are modes for quick entering/selection of a list of Serial numbers. By them, the user may enter directly the numbers separated by commas (for example - "KHC4500071, KHC4500072, KHC4500073, KHC4500074, KHC4500075, KHC4500076, KHC4500077"), or they may set a range of numbers (in the previous example list, the user may enter just "KHC4500071" and "KHC4500077"). 

For more information about the Barcode panel's serial number modes, see **Barcode Panel Modes** and its subtopics. 

## Availability And product tracking 

The products availability (both current and at a specified date) for serialized products is detailed to serial number level. 

The same is valid for the stock movements reports. By them, the user is able to track the movements of specified products and their Serial numbers. Such tracking is always executed by store documents (i.e. store movements) and if there comparing operations from specialized modules is required, then a link between the Transactions and the documents from the specified module is used (for example - links as [Parent Document] <-> [Sub-Document]). 

For example, in purchasing orders Serial numbers will rarely be entered (except for returns) and the Serial numbers will show up in the transactions. So if the user wants to see when a specified serial number is bought, then they would use stock movements and follow the link to the Purchasing orders (for example - through the parent document of the Store order).
