---
uid: determine-product-price
---

# Determine product price

When trying to determine a product price, we have to specify some required conditions:

- **Product**
- **Quantity**
- **QuantityUnit**
- **Date** 

and some not required:
 
- **Customer**
- **Ship to customer**
- **Enterprise company** - Only in the specified enterprised company
- **Enterprise company location** - Only in the specified enterprise company location
- **Distribution channel** - self-explanatory
- **Price list** - self-explanatory
- **Current product price** - The current product price should not be changed if it satisfies the conditions and has the same priority as the determined top price.

@@name filters all product prices for the given product that match these criteria. When a product price is defined with a blank value for the customer, the product price applies to **all** customers. The same goes for Ship To Customer, From Date, Thru Date and all not required parameters from the list above.
 
Generally, the algorithm is the following:
 
- @@name filters the product prices.
- Each of the selected product prices is checked if min and max’s quantities are respectively less and greater than the provided quantity. The price ist of the product price is checked for validity according to the date. If Ship To Customer is provided, its party is considered a Target Party, else the customer's party is taken. If the product price has a target group specified, the target party should be a member of that group or null.
- Among the remaining product prices, the top priority price is selected considering the lowest Price Type's Ordinal Pos, the highest Priority and the newer From Date. 
- If a Current Product Price is provided and it satisfies the conditions and has the same priority as the selected one, then the current product price is selected. 

So, after the selection process, one and only one product price is selected and applied to the document line.
 
## Filtering conditions

- From Date is empty or <= required Date
- Thru Date is empty or >= required Date
- Product is equal to required Product
- Customer is empty or it is equal to the required Customer
- Ship To Customer is empty or it is equal to the required Ship To Customer
- Min Quantity is empty or <= required Quantity
- Max Quantity is empty or >= required Quantity
- Enterprise Company is empty or equal to required Enterprise Company
- Enterprise Company Location is empty or equal to required Enterprise Company Location
- Distribution Channel is empty or equal to the required Distribution channel 
- Price List is empty or valid for the required Date
- The target group is empty or the ship to the customer or the customer is a member of the target group

