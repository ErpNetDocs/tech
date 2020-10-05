# How To Use The Customer As A Company?

When we work with the customer, we can only get its party  attributes as the customer may be company, company location or a person.

So if we know that the customer is a company and we need to get his  company attributes, we can cast its reference Party  to Aloe.EnterpriseOne.Model.General.Contacts.Company.

For example, to get the Responsible Person of the company of the customer, the following attribute would do the job:

(repository of the attribute: Crm.Customers)

*Expressions:*

```
10: GETOBJVALUE EXP:20 ResponsiblePersonName
20: CAST REF:Party CONST:Aloe.EnterpriseOne.Model.General.Contacts.Company
```



 

>[!NOTE]If the customer is not a company, it would return an error.