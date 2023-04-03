---
uid: bonus-program
---

# Bonus programs

*Bonus programs* are a tool that automates including a bonus product or a discount on the sales order when the document meets certain conditions. Using bonus program automation reduces the chances that a mistake is made. For example, if the business model requires using a lot of bonuses, there is a high probability an employee would forget to include a free product or a discount, but using bonus programs ensures that if all conditions are met, the customer receives the bonus.

*Bonus programs* define bonuses and conditions, which specify when the bonuses should be applied to the sales order.

Conditions for the particular *bonus programs* are set in the ‘condition’ fields and are verified for the whole sales order.

|Bonus program conditions: |Description:
|:----|:----|    
|Active|That’s the main condition if the bonus must be applied. The other conditions are verified only for active bonus programs.
|Priority|from 1 (the lowest) to 5 (the highest) of the bonus program compared to the other bonus programs.
|Condition Customer|Specifies that the bonus program must be applied only for the customer that is set in the field. If ‘Condition Customer = NULL’, then it’s applied for all customers.
|Condition Customer Filter XML| Sets a custom filter for clients. The bonus program is only applied if the customer meets the specified criteria. Currently, only criteria from the related ’Customers’ and ‘Parties’ tables are supported. The filter can contain custom properties.
|Condition Ship To Customer|Specifies that the bonus program must be applied only when shipping to the customer that is set in the field. If ‘Condition Customer = NULL’, then it’s applied to all customer’s company locations.
|Condition Ship To Customer Filter XML| The bonus applies only when shipping to a customer that meets the specified criteria. Currently, only criteria from the related ’Customers’ and ‘Parties’ tables are supported. The filter can contain custom properties.
|Condition Product|If there is no value in the field, then all other conditions must be evaluated for the whole sale order. Otherwise, the bonus only applies to the lines that contain the product. If the bonus program is valid for more than one product, then another condition product could be added in the panel 'Bonus program products'.
|Condition Product Group|The bonus program only applies to products from the specific group or its subgroups.  Currently, the condition for the product group can’t be used with conditions for Min and Max quantity. That’s because if the base measurement units of the products in the group are different, there is no way the right calculation is made and the bonus program won’t be applied
|Condition Min Quantity|Specifies a condition for the minimum quantity of the condition product in the base measurement unit. If there is no condition product, then a minimum quantity can not be set for the current bonus program. If the condition products are more than one, then all of them have to use the same base measurement unit. Otherwise, there is no way the right calculation to be made and the bonus program won’t be applied. 
|Condition Max Quantity|Specifies a condition for the maximum quantity of the condition product in the base measurement unit. If there is no condition product, then a maximum quantity can not be set for the current bonus program. If the condition products are more than one, then all of them have to use the same base measurement unit. Otherwise, there is no way the right calculation to be made and the bonus program won’t be applied.
|Condition Min Amount|Specifies a condition for the minimum sum of amounts of the sales order lines, for which the bonus is valid.
|Condition Max Amount|Specifies a condition for the maximum sum of amounts of the sales order lines, for which the bonus is valid.
|Condition Document Currency |The bonus program only applies if the document currency is the same as the currency in this field. Condition Document Currency is also required if any of the amount conditions are set.
|Condition From Date|Starting date (inclusive) from which the bonus program is valid.
|Condition To Date|End date (inclusive) to which the bonus program is valid.
|Condition Target Group|Specifies that the bonus program only applies for the customers from the specified target group.
|Condition Distribution Channel|Specifies that the bonus program only applies when the specified distribution channel is used in the document.
|Condition Distribution Channel Filter XML |The bonus only applies when the distribution channel in the document meets the specified criteria.

> [!NOTE]
> When forming the maximum and minimum quantity of products purchased with the particular sales order, the system sums a total quantity of all purchased products defined in the bonus program. For example, if a *bonus program* is valid for two products - product A and product B and the condition for minimum quantity is 5 pieces, the *bonus program* will be applied no matter what is the ratio between those two products (2 pcs of product A and 3 pcs of product B, 1 pcs of A and 4 of B, 0 pcs of A and 5 of B …).

**Currently, three types of bonuses are supported:**
- **Product** – Аdds a sales order line with a free product. Works as follows: If all conditions are met, a new line with the bonus product is created. The quantity in the line is determined by the values of the bonus program fields *For Each* and *Bonus Product Quantity*. For Example: if there is a bonus program with a product 'Pencil', which is offered as a gift for each 10 ordered books, then if in the sale order there are 30 notebooks, a bonus row with 3 pencils will be created. The line amount is '0.00'.
- **Discount** – Sets a percentage discount that **replaces the standard discount percent** for a specific sales order line. Works as follows: To all sales order lines that meet the conditions, the standard discount percent is replaced by the value set in the *Bonus Line Discount Percent* field. Bonus programs do not apply to lines with zero quantity.
- **Cascade discount** – Sets a percentage discount that **is applied after the standard discount percent** for a specific sales order line. Works as follows: To all lines that meet the conditions, the value set in the *Bonus Line Discount Percent* field is applied after the standard discount percent. So, the standard discount percent is calculated as follows: Line Standard Discount Percent = 1 - (1 – Line Standard Discount Percent) * (1 - Bonus Line Discount Percent). Bonus programs do not apply to lines with zero quantity.

In the sales order line field *Bonus program* there is information about the name of the bonus program that is currently applied.

A bonus type is required for each bonus program. Bonus types can not be used simultaneously.


|Data fields:|Description:
|:----|:----|
|Bonus Action|Specifies the type of the bonus – a product, a discount or a cascade discount.
|Bonus Product|The product that the customer receives for free, if the conditions of the bonus program are met. The field is required when there is value in Bonus Product.
|Bonus Product Quantity|The quantity of the bonus product. The field is required if there is a value in Bonus Product.
|Bonus Product Quantity Unit|The measurement unit of the bonus quantity of the product. The field is required if there is a value in Bonus Product.
|For Each|Specifies an amount of the condition product, for which the bonus quantity is applied every time. For example, if we want to use the common form of sales promotion 'Buy X get Y for free' we should set the 'X' quantity in the field 'For Each'. This way if the customer buys 2*Х quantity, then will receive 2*Y bonus.
|Bonus Line Discount Percent|The percent discount that is going to be applied in the rows.
