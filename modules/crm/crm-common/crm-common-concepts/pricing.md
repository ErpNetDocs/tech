# Pricing

## Description

When a user enters a Sales Order (or similar document), the system automatically assigns the appropriate sales price. Selecting the correct price is the main topic of the pricing.

## Product prices in reality

Each product can have multiple prices associated with it.

For example, Product A can have 3 standard prices:

- 50.00 USD - open price, for everyone who asks
- 48.00 USD - for regular customers
- 45.00 USD - for special customers

Additionally, Product A can have a special price for some customers:

- 44.00 USD for Customer X
- 43.50 USD for Customer Y

Also, there might be a discount campaign:

- 42.00 USD for everyone, from 1/1/2016 till 2/2/2016

## Entering product prices in @@name

The following table shows how we can define the prices from the above example in @@name.

|Product|Customer|Price List|From Date|To Date|Priority|Price
|:----:|:----:|:-----:|:----:|:----:|:----:|:----:
|Product A|-|-|-|-|1|50.00           	
|Product A|-|Regular|-|-|2|48.00
|Product A|-|Special|-|-|2|45.00
|Product A|Customer X|-|-|-|3|44.00
|Product A|Customer Y|-|-|-|3|43.50
|Product |-|-|1/1/2021|2/2/2021|5|42.00

## How @@name determines the correct price

The most important thing to note is the Priority attribute. The higher the priority, the more likely the price will be selected. After the user specifies the customer, date and product, @@name filters all prices, that match these criteria. When a price is defined with a blank value for the Customer the price applies to **all** customers. The same goes for Price List, From Date To Date, etc. Only the Product attribute is required, it cannot be blank. If it could be blank, this means, that we can define the same price for ALL products.

Generally, the algorithm is the following:

- @@name filters the prices, based on Product, Customer, Price List and all other conditional attributes.
- Among the remaining prices, the one with the highest priority is selected.
- If there is more than one price within the same highest priority, the newer one is selected (the one with later From Date).

So, after the selection process, one and only one price is selected and applied to the sales document.
 
## More conditional filtering attributes

@@name employs many more conditional attributes, which allow fine-grained tuning of the product pricing strategy. All conditional attributes work in the same basic way as described above.

The following additional conditional attributes further filter down the prices:

- **@@name** - for sales only in the specified @@name
- **Min Quantity** - for sales quantities above (or equal to) the specified
- **Max Quantity** - for sales quantities below (or equal to) the specified
- **Target Group** - for customers in the target group
- **Ship To Customer** - self-explanatory
- **Distribution Channel** - self-explanatory
- **Customer Type** - self-explanatory

## Specifying the price

The price is specified using the following attributes:

- **Price** - the decimal part of the price
- **Currency** - The currency of the price
- **Quantity** - the quantity for which the price is specified
- **Quantity Measurement Unit** - the measurement unit in which the quantity is specified

Examples:
5.00 USD for 1 pcs

10.00 EUR for 3 packs

