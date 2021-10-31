# Automatic lot creation

This function is used when the user wants to automatically create new lots when purchasing products.
 
This is achievable by the product type definition and the *Lot Auto Creation* field. If checked, it specifies that lots are automatically created by the receiving orders with which the products are received.
 
When such product is purchased, the following actions are performed for each purchase order row:
 
- if the Lot field has value, nothing happens;
- if the Lot field is empty, the system checks the value of the product type's definition Lot Auto Creation field (of the product of the current row):
    - if it is false - nothing happens;
    - if it is true - then an attempt to set a lot in the current row is performed:
        - an already existing lot of the current product is searched, which has the number of the current document set in the Purchase Lot Number field;
           - if such lot is found - it is filled in the current row;
           - if no such lot is found - a new lot is created.

##  New lot algorithm creation

The new lot, created in the last step of the actions described above, is created as follows:
 
- the product from the purchase order row is set as 'Product' in the new lot definition;
- the 'Purchase Lot Description' from the purchase order header is set as 'Description' in the new lot definition;
- the Document Number of the current document is set as 'Purchase Lot Number' in the new lot definition;
- the 'Lot Number' of the new lot is formed by the biggest lot number (in alphabetic order) of the already existing ones (regardless of Product, Description or Purchase Lot Number), and this number is increased by 1; if there are no existing lots in the database '00001' is set.

