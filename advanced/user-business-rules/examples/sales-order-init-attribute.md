---
items: UserBusinessRuleExamples
---

# Set an initial attribute for a new sales order


If a business logic requires only whole numbers, a **[user business rule](../index.md)** can be set to check users' work.

For example, a validation of a sales order lines may be applied with the following data:

- **Repository**: Crm.Sales.SalesOrders

- **Events** - **[CREATENEW](../events/create-new.md)**

- **Action** - **[SETVALUE](../action-types/setvalue.md)** + Parameter1Type = `Attribute` + Parameter1 Value = `Note` + Parameter2Type = `Constant` + Parameter2 Value = `your initial value`.

- **Conditions**: No conditions for such a simple task.

