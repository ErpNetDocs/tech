---
uid: determine-level-2-discount
---

# Determine level 2 discount

Level 2 discount is determined automatically only if two conditions are met:
- a Price list is set and
- the Auto Apply Discount Level of this Price list is set to 2 or higher.

When trying to determine a level 2 discount, we have to specify some required conditions:
 
- **Product**
- **Date**
- **Quantity**
- **List of customers**

and some not required:
 
- **Enterprise company** - Only in the specified Enterprise Company
- **Enterprise company location** - Only in the specified Enterprise Company location
- **Price list** - self-explanatory
- **Distribution channel** - self-explanatory
- **Current line discount** - The current discount should not be changed if it satisfies the conditions and has the same priority as the determined top discount.

@@name filters all discounts from level 2 that match these criteria. When a discount is defined with a blank value for the Customer, the discount applies to **all** customers. The same goes for Customer Type, Product, From Date To Date, MinQuantity, MaxQuantity, Enterprise Company, Price List, etc.
 
Generally, the algorithm is the following:

-	ERP.net checks if a Price List is set. 
-	Then checks the Price List’s Auto Apply Discount Level.
-	If Auto Apply Discount Level is set to 2 or higher - ERP.net filters the discounts from level 2
- Among the remaining level 2 discounts, the one with the highest priority is selected. If there is more than one price within the same highest priority, the newer one is selected (the one with later From Date).
- If a current line discount is provided and it satisfies the conditions and has the same priority as the selected one, then the current line discount is selected.
 
So, after the selection process, one and only one discount is selected and applied to the document line.
 
## Filtering conditions

- Discount Discount Level == 2
- Discount From Date is empty or <= required Date
- Discount To Date is empty or >= required Date
- Discount Product is empty or equal to required Product
- Discount Min Quantity is empty or <= required Quantity
- Discount Max Quantity is empty or >= required Quantity
- Discount Customer is empty or it is in the required list of customers
- Discount Product Group is empty, the same as the product group or parent of the product group
- Discount Distribution Channel is empty or equal to required Distribution channel 
- Discount Price List is empty or valid for the required Date
- The discount Target group is empty or at least one of the customers is a member of the target group
- Discount Customer type is empty or it is in the list of customer types, derived from the required customer’s list

