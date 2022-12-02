---
uid: determine-line-discounts
---

# Determine line discounts

ERP.net allows multiple discounts at multiple levels to be defined.

Line discount is determined automatically among the discounts from level 1.

Level 2 discount is determined automatically among the discounts from level 2 only if two conditions are met:
•	a Price list is set and
•	the Auto Apply Discount Level of this Price list is set to 2 or higher.

Level 3 discount is determined automatically among the discounts from level 3 only if two conditions are met:
•	a Price list is set and
•	the Auto Apply Discount Level of this Price list is set to 3 or higher.

When trying to determine a discount for each level, we have to specify some required conditions:
 
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

@@name filters all discounts from the respective level that match these criteria. When a discount is defined with a blank value for the Customer, the discount applies to **all** customers. The same goes for Customer Type, Product, From Date To Date, MinQuantity, MaxQuantity, Enterprise Company, Price List, etc.
 

## The method’s algorithm

Generally, the method returns three values – LineDiscount, Level2Discount, Level3Discount.
 
Each value is determined separately as follows:

1. ERP.net checks if a Price List is set. If a Price List is set, it checks the Price List’s Auto Apply Discount Level.

•	If no Price list is set OR Price List’s Auto Apply Discount Level is set to 1
- for LineDiscount - ERP.net filters the discounts from level 1
- Level2Discount is not calculated and the method returns NULL
- Level3Discount is not calculated and the method returns NULL
•	If а Price list is set AND Price List’s Auto Apply Discount Level is set to 2
- for LineDiscount - ERP.net filters the discounts from level 1
- Level2Discount - ERP.net filters the discounts from level 2
- Level3Discount is not calculated and the method returns NULL
•	If а Price list is set AND Price List’s Auto Apply Discount Level is set to 3
- for LineDiscount - ERP.net filters the discounts from level 1
- Level2Discount - ERP.net filters the discounts from level 2
- Level3Discount - ERP.net filters the discounts from level 3

3. Among the remaining discounts from the respective level, the one with the highest priority is selected. If there is more than one price within the same highest priority, the newer one is selected (the one with later From Date).

5. If a current line discount is provided and it satisfies the conditions and has the same priority as the selected one, then the current line discount is selected.

 
So, after the selection process, one and only one discount for each level is selected and is returned as LineDiscount, Level2Discount or Level3Discount.
 
## Filtering conditions

- Discount Discount Level == 1 OR Discount Discount Level == 2 OR Discount Discount Level == 3
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

