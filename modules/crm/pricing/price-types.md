# Price types

**Price types** are used to set additional priority conditions for the prices. 

5 is the highest priority level that can be selected in the *Priority* field of the price. 

To add an additional higher priority, a price type must be **defined** and **selected** as a price type of the price. 

**Priorities** among the different price types are set by filling a number in the ordinal position field in the definition of the price type – the lower the number, the higher the priority.

#### Price types add additional priority under the **following algorithm:**

If a price has a defined price type, this price will be with the highest priority among other prices - no matter their level of priority. 

If more than one price has a defined price type, the price with the price type that has the lowest ordinal position will be with the highest priority.

If more than one price has a defined price type and their price types have equal ordinal positions, the price with the highest priority will be selected.
