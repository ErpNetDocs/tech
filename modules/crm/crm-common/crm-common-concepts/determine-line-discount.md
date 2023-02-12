---
uid: determine-line-discount
---

# Determine line discount

ERP.net allows multiple discounts at multiple levels to be defined.

Typically, Level 1 discount is determined among the discounts from level 1. This means that if we want to calculate Level 1 discount, we might not explicitly specify a Discount Level filter, because its default value is 1.

For the discounts for all other levels, we need to specify a Discount Level filter that is equal to the level we are trying to calculate.

When trying to determine a discount for each level, we have to specify some required conditions:
 
- **Product**
- **Date**
- **Quantity**
- **List of customers**

and some not required:
 
-	**Discount level** – default is 1, can be changed if we are calculating the discount for a higher level
- **Enterprise company** - Only in the specified Enterprise Company
- **Enterprise company location** - Only in the specified Enterprise Company location
- **Price list** - self-explanatory
- **Distribution channel** - self-explanatory
- **Current line discount** - The current discount should not be changed if it satisfies the conditions and has the same priority as the determined top discount.

@@name filters all discounts from the respective level that match these criteria. When a discount is defined with a blank value for the Customer, the discount applies to **all** customers. The same goes for Customer Type, Product, From Date To Date, MinQuantity, MaxQuantity, Enterprise Company, Price List, etc.
 

Generally, the algorithm is the following:

•	ERP.net filters the discounts from the respective level.

•	Among the remaining discounts, the one with the highest priority is selected. If there is more than one price within the same highest priority, the newer one is selected (the one with later From Date).

•	If a current line discount is provided and it satisfies the conditions and has the same priority as the selected one, then the current line discount is selected.

So, after the selection process, one and only one discount is selected and applied to the document line.

 
## Filtering conditions

- Discount Discount Level is equal to the specified level
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

