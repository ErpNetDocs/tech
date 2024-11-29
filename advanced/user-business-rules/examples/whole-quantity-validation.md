---
items: UserBusinessRuleExamples
---

# Whole quantity validation

If a business logic requires only whole numbers, a **[user business rule](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** can be set to check users' work.

For example, a validation of a sales order lines may be applied with the following data:

- **Repository**: Crm.Sales.SalesOrderLines

- **Events** - **[COMMIT](https://docs.erp.net/tech/advanced/user-business-rules/events/commit.html)**

- **Action** - **[FAIL](https://docs.erp.net/tech/advanced/user-business-rules/action-types/fail.html)** + Parameter1Type = Constant + Parameter1 Value = "You have entered decimal number as a quantity. Please, check the data entered in the sales order lines and try again!"

- **Conditions**: check if the **[calculated attribute](https://docs.erp.net/tech/advanced/calculated-attributes/index.html)** from the example in here is equal to 'False'

When this user business rule is activated and you try to release a sales order with the following lines,

- line 10 - product A - Quantity 5.05
- line 20 - product B - Quantity 5.00

the system would return an **error** with the text you entered in the action of the user business rule: <br><br> _You have entered decimal number as a quantity. <br>Please, check the data entered in the sales order lines and try again!_ <br><br>
With this user business rule activated, if the sales order has the following lines,

- line 10 - product A - Quantity 5.00
- line 20 - product B - Quantity 5.00

the release of the document would be **possible**.
