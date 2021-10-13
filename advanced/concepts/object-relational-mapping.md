# Object relational mapping



## Description 

**Entities** and **Entity types** are terms, frequently used throughout the documentation. **Entities** are information objects, which represent real-world objects. **Entity type** is the collection of all objects of a given type.

For example, the customer XYZ is an entity. Customer ABC is another entity. All customers are of an entity type, called 'Customers'.

## Definitions

- **Entity** - Single object of a given entity type. Also called entity object or simply object. It is similar to a data row in a table.
- **Entity yupe** - The set of all objects of a given type. This is similar to a table.
- **Attribute** - a named value, containing information about the entity object. This is similar to a column in a table.

## Relationship to tables and rows

This section contains more advanced information, not usually needed to operate the system. However, a deeper understanding of the inner-workings might help sometimes, especially when one needs to access directly an @@name database, using database tools.

Generally, **entity types**, **entities**, and **attributes** are much like **tables**, **rows**, and **columns**. Data of the entities is ultimately stored in the database in the form of tables and rows. However, there is one important distinction - Entity Types and Entities are object-oriented representation of the table data. A technology, called ORM (Object-Relational Mapping) is used to map between entities and tables.

In order to illustrate better the difference between objects and tables, let's include some real-world tables and objects:

There is an entity type, called **'Party'.** It has a descendant (more specialized) entity type, called **'Company'.** So, **Party** is the more abstract and broad term, and **Company** is just one specialization. **Person** is another descendant of **Party.**

Let's illustrate this using pseudo-graphics:

> Party
>
> +---- company
>
> +---- person

Each party has some attributes, like 'parent party' and area. The company has VAT number and Registration type attributes. Each person has "First Name" and "Last Name".

Now, if we look at the tables, they have the following schema:

- Parties
  - Party Id
  - Parent party Id
  - Area Id
- Companies
  - Party Id
  - VAT number
  - Registration type
- Person
  - Party Id
  - First name
  - Last name

If we look at the objects, they will have the following attributes:

- Party
  - Parent rty
  - Area
- Company
  - Parent party
  - Area
  - VAT Number
  - Registration type
- Person
  - Parent party
  - Area
  - First name
  - Last name

So, if we use table data, in order to access all attributes of a company or a person, we have to relate (join) data from different tables, using unique Identifiers. The identifiers are the so-called "surrogate keys" because they are existing only in the database and have no real-world counterpart. Using such keys and relating data between tables is ordinary in the relational world of the databases.

However, internally, the systems use objects, because it is much simpler to process them. Objects already have all the necessary attributes related together and there is no need to use Identifiers or table relations.

This is only an introduction to the topic of object-relational mapping. More deeper look would go too deep into the developer details of the subject.
