---
items: CalculatedAttributesQA
---

# How to use a customer as a company?

When we work with a customer, we can only get its party attributes as company, company location or a person.

If we know that the customer is a company and we need to get their company attributes, we can cast its reference party to **Aloe.EnterpriseOne.Model.General.Contacts.Company**.

For example, to get the responsible person of the customer's company, the following attribute would do the job:

(repository of the attribute: Crm.Customers)
```
10: GETOBJVALUE EXP:20 ResponsiblePersonName
20: CAST REF:Party CONST:Aloe.EnterpriseOne.Model.General.Contacts.Company
```

> [!NOTE]
>
> If the customer is not a company, it would return an error.
