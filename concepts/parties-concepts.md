# Parties Concepts


## Description
Parties in @@name are one of the most widely used definition. Generally, a party is a participant in any business relations or transaction.

Examples of parties include:

- Business customers
- Consumer customers
- Employees in our or external companies
- Contacts
- Dealers
- Company Locations
- Departments
- etc...

## Basic Party Types
Parties do not exist by their own. They are always created as another object. Most parties are created as Person or Company. In object terms, it means that Person and Company inherit Party. The Party itself is called to be of type Person or Company.

> [!Note]
> Parties cannot be directly created. They are always instantiated as some sub-type, like Person or Company.

This diagram shows the relationship between Party, Person and Company:

![Party Basic](Party-basic.png)

## Party Attributes Inheritance

The fact, that Person and Company inherit Party also means, that all attributes of Party are also attributes of Person and Company. <br>
For example, a Party has an "Area" attribute. So, all Person and Company objects would also have an "Area" attribute. <br>
The opposite is not true. E.g. Person and Company objects have attributes, which are specific to them and are not general Party attributes.<br>
For example:

![Party Attributes](Party-attributes.png)

Party has "Parent Party" and "Area" attributes, which are inherited by Company and Person. But persons "First Name" and "Last Name" are specific only to persons. Neither companies, nor generally parties have "First Name".

## Relationships with Other Entity Types

Although parties do not exist on their own, they can participate in relationships. For example, a Customer or Supplier Contract are objects, which can have a relationship with a Party. Relationship with Party means, that an actual Customer Contract object would relate to either a Person or a Company. This is shown on the following diagram:

![Party Basic Contracts](Party-basic-contracts.png)

> [!Note]
> Customer (Contract), Supplier (Contract) and Dealership (Contract) are actually called simply Customer, Supplier and Dealer in @@name.

> [!Note]
> The diagram shows, that one Party object can participate in relationships with many Customer Contract objects. In fact however, the current implementation of EnterpriseOne allows many Customer Contracts per party, but only one for each Enterprise Company. This means, that one party can have only a single Customer Contract with any given Enterprise Company.

To clarify the above diagrams, lets provide an example. Suppose we have:

- A customer, which is a company, called "ABC"
- A supplier, which is a person, named "John"

This will be represented with the following objects:

- Party (ABC)
- Company (ABC), which inherits Party (ABC)
- Customer (ABC), which points to Party (ABC)
- Party (John)
- Person (John), which inherits from Party (John)
- Supplier (John), which points to Party (John)

If we query the system with a query, that can be stated as "Show me ALL parties", the result will be:

- Party (ABC)
- Party (John)

If we query with "Show me ALL customers", the result will be:

- Customer (ABC)

# Party Hierachy

The basic party types are Person and Company, but there are some more party types. Among them are Department and Division. By using all the party types, the data about parties can be nicely organized. Particularly handy is the ability to hierarchically structure the parties. Having the departments and divisions as parties allows flexible representation of the different corporate hierarchies.

For example, lets have Corporation A structured in the following way:

- Corporation A
  - Division 1
    - Sales Department
    - Marketing Department
  - Division 2
    - Sales Department
    - Marketing Department
  - Global Marketing Department
  - Global Accounting Department

The flexible party hierarchy also allows structuring even different companies in a corporation:

- Corporation B
  - Company A
    - Consumer Electronics Division
      - Sales Department
    - Business Consulting Division
      - Sales Department
    - Accounting Department
  - Company B
    - Sales Department
    - Accounting Department
  - Corporate Financials Department



