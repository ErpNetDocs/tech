# Pricing

When a user enters a sales order (or similar document), the system automatically assigns the appropriate sales price. 

Selecting the correct price is the main topic of the pricing.

### Product prices in reality

Each product can have multiple prices associated with it.

For example, product A can have 3 standard prices:

- 50.00 USD - open price, for everyone who asks. This price is defined as Standard.
- 48.00 USD - for regular customers
- 45.00 USD - for special customers

Additionally, product A can have a special price for some customers:

- 44.00 USD for Customer X
- 43.50 USD for Customer Y

Also, there might be a discount campaign:

- 42.00 USD for everyone, from 1/1/2021 till 2/2/2021. This price is defined as Promotion and it should be with higher priority than the Standard price.

## Entering product prices in @@name

The following table shows how we can define the prices from the above example in @@name.

| Product   | Customer   | Price list | From date | To date  | Price type | Priority | Price |
| --------- | ---------- | ---------- | --------- | -------- | ---------- | -------- | ----- |
| Product A |            |            |           |          | Standard   | 1        | 50.00 |
| Product A |            | Regular    |           |          |            | 2        | 48.00 |
| Product A |            | Special    |           |          |            | 2        | 45.00 |
| Product A | Customer X |            |           |          |            | 3        | 44.00 |
| Product A | Customer Y |            |           |          |            | 3        | 43.50 |
| Product A |            |            | 1/1/2021  | 2/2/2021 | Promotion  | 5        | 42.00 |

## How @@name determines the correct price

The most important thing to note is the Price type field. The price type with the lowest Ordinal position is with highest priority. 

If the Price type field has a blank value, the first thing that is taken into consideration is the Priority field of the price. The higher the priority, the more likely the price will be selected. 

After the user specifies the customer, date and product, @@name filters all prices, that match this criteria. When a price is defined with blank value for Customer, the price is applicable to **all** customers. The same goes for Price list, From date, To date, etc. Only the Product field is required, it cannot be blank. If it could be blank, this means, that we can define the same price for ALL products.

Generally, the algorithm is the following:

@@name filters the prices, based on Product, Customer, Price list and all other conditional fields.

- If among the remaining prices, there are prices with defined price type, the one that has a price type with the lowest Ordinal position is selected

**If there is more than one price within the same lowest Ordinal position, the one with the highest priority is selected*

- If among the remaining prices, there are no prices with defined price type, the one with the highest priority is selected

**If there is more than one price within the same highest priority, the newer one is selected (the one with later From date)*

So, after the selection process, one and only one price is selected and applied to the sales document.

**For a detailed description of the algorithm of the method determining the product price, see @determine-product-price topic.**

## More conditional filtering fields

@@name employs many more conditional fields, which allow fine-grained tuning of the product pricing strategy. All conditional fields work in the same basic way as described above.

The following additional conditional fields further filter down the prices:

- **Enterprise Company** - for sales only in the specified enterprise company
- **Min Quantity** - for sales quantities above (or equal to) the specified
- **Max Quantity** - for sales quantities below (or equal to) the specified
- **Target Group** - for customers in the target group
- **Ship To Customer** - self explanatory
- **Distribution Channel** - self explanatory
- **Customer Type** - self explanatory

## Specifying the price

The price is specified using the following fields:

- **Price** - the decimal part of the price
- **Currency** - the currency of the price
- **Quantity** - the quantity for which the price is specified
- **Quantity Measurement Unit** - the measurement unit in which the quantity is specified

Examples:

> 5.00 USD for 1 pcs
>
> 10.00 EUR for 3 packs
