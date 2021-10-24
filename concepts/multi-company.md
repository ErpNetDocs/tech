# Multi-company support in ERP instances

@@name allows a single ERP instance (database) to contain multiple companies. The different own companies, stored in the database are called "Enterprise companies".

Many data objects (definitions, settings and documents) have an enterprise company attribute. When filled, it specifies that the data is specific to one of the enterprise companies. When the attribute is left blank, the data is valid for all enterprise companies.

Some data objects have a required enterprise company attribute. In this case, the data is always specific to one enterprise company. For example, all documents have a required enterprise company attribute.

For example, lets have the following *Accounts* in our chart of accounts:

- 60201 - Expenses, general
- 60209 - Other expenses (specific to "Company X", one of the companies, managed in the database)

This can be defined as follows:

| Account | Enterprise Company |
| :------ | :----------------- |
| 60201   |                    |
| 60209   | Company X          |

In much the same way, the products and many other definitions can be defined to belong to only a single enterprise company or to all enterprise companies.

> [!NOTE]
> There is no way to define a data object to belong to several enterprise companies. It is either one or all.
