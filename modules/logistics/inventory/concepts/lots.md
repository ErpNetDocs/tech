# Lots

Warehouse lots contain one row for each specific product, status, production batch and other specific warehousing conditions. Lot status can block certain operations. Items in a lot are all of the same type and produced under the same conditions, intended to have uniform quality and characteristics. The lots characteristics are:

- Product - the product of the lot;
- Lot number  
- Receipt store transaction - if the lot isn't created manually, this field stores the receipt store transaction which created the current lot;
- Status - the  status of the warehouse lot may be one of the following: 
    - blocked for document (sales or service order);
    - blocked for party;
    - blocked for inspection;
    - free to use;
- Blocked for party - non-null when the warehouse lot is blocked specifically for some party.
- Blocked for document - if non-null, contains the document for which the lot is blocked.
- License No - the license number for this lot. Null when license number is N/A or unknown.
- Purchase lot number - identification of the purchase lost with which the products from this store lot are received. E.g. the document number of the receiving order. 
- Description;
- Expiry date;
- Receipt date - the date of the first receipt of products in this lot.
