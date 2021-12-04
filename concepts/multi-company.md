# Multi-company support in ERP instances

@@name allows a single ERP instance (database) to contain **multiple** companies. Different owned companies stored in a database are called **enterprise companies**.

Many **[data objects](https://docs.erp.net/tech/advanced/data-objects/index.html)** (definitions, settings and documents) have an EC attribute. When filled, it specifies that the data is unique to **one** of the enterprise companies. When left blank, it means that the data is valid for **all** enterprise companies.

Some data objects like documents have a **required** enterprise company attribute. <br> In this case, the data is always specific to one enterprise company. 

Let's have the following accounts in a chart of accounts:

- **60201** - Expenses, general
- **60209** - Other expenses (specific to "Company X", one of the companies, managed in the database)

This can be defined as follows:

| Account | Enterprise company |
| :------ | :----------------- |
| 60201   |                    |
| 60209   | Company X          |

Similarly, products and other definitions can belong to a **single** enterprise company or **all** enterprise companies.

> [!NOTE]
> 
> There's no way to make a data object belong to several enterprise companies. It's either one or all.
