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
![Party Basic](party-basic.png)

## Party Attributes Inheritance

The fact, that Person and Company inherit Party also means, that all attributes of Party are also attributes of Person and Company. <br>
For example, a Party has an "Area" attribute. So, all Person and Company objects would also have an "Area" attribute. <br>
The opposite is not true. E.g. Person and Company objects have attributes, which are specific to them and are not general Party attributes.<br>
For example:

![Party Attributes](party-attributes.png)



