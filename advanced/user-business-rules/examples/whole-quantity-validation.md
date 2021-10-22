# Whole quantity validation

If the business requires whole numbers only, user defined business rule may be set to check the users work.

For example - a validation of the sales order lines may be applied with the following data:
- Repository: Crm.Sales.SalesOrderLines
- Events - [COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/commit.html)
- Action - [FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html) + Parameter1Type = Constant + Parameter1 Value = "You have entered decimal number as a quantity. Please, check the data entered in the Sales order lines and try again!"
- Conditions: check if the calculated attribute from the example in here is equal to 'false'

When this user business rule is activated and if the user tries to release a Sales Order with the following lines:
- line 10 - product A - Quantity 5.05
- line 20 - product B - Quantity 5.00

The system would return an error with the text we entered in the action of the user business rule - 'You have entered decimal number as a quantity. Please, check the data entered in the sales order lines and try again!'.

With this user business rule activated, and if the sales order has the following lines:
- line 10 - product A - Quantity 5.00
- line 20 - product B - Quantity 5.00

The release of the document would be possible.
