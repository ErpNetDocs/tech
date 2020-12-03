# Multi-Company Support In ERP Instances



@@name allows a single database to contain multiple companies. The different own companies, stored in the database are called "Enterprise Companies".

Many data objects (definitions, settings and documents) have an "Enterprise Company" attribute. When filled, it specifies that the data is specific to one of the enterprise companies. When the attribute is left blank, the data is valid for all enterprise companies.

Some data objects have a required "Enterprise Company" attribute. In this case, the data is always specific to one enterprise company. For example, all documents have a required enterprise company attribute.

For example, lets have the following *Accounts* in our chart of accounts:

- 60201 - Expenses, general
- 60209 - Other Expenses (specific to "Company X", one of the companies, managed in the database)

This can be defined as follows:

| Account | Enterprise Company |
| :------ | :----------------- |
| 60201   |                    |
| 60209   | Company X          |

In much the same way, the products and many other definitions can be defined to belong to only a single enterprise company or to all enterprise companies.



There is no way to define a data object to belong to several enterprise companies. It is either one or all. However, it is usually possible to restrict access, using the todo:[Security System (TBD)]().