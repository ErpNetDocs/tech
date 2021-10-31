# Object relational mapping



## Description 

**Entities** and **Entity types** are terms, frequently used throughout the documentation. **Entities** are information objects, which represent real-world objects. **Entity type** is the collection of all objects of a given type.

For example, the customer XYZ is an entity. Customer ABC is another entity. All customers are of an entity type, called 'Customers'.

## Definitions

- **Entity** - Single object of a given entity type. Also called entity object or simply object. It is similar to a data row in a table.
- **Entity type** - The set of all objects of a given type. This is similar to a table.
- **Attribute** - a named value, containing information about the entity object. This is similar to a column in a table.

## Relationship to tables and rows

This section contains more advanced information, not usually needed to operate the system. However, a deeper understanding of the inner-workings might help sometimes, especially when one needs to access directly an @@name database, using database tools.

Generally, **entity types**, **entities**, and **attributes** are much like **tables**, **rows**, and **columns**. Data of the entities is ultimately stored in the database in the form of tables and rows. However, there is one important distinction - entity types and entities are object-oriented representation of the table data. A technology, called ORM (Object-Relational Mapping) is used to map between entities and tables.

In order to illustrate better the difference between objects and tables, let's include some real-world tables and objects:

There is an entity type, called **'Party'.** It has a descendant (more specialized) entity type, called **'Company'.** So, **Party** is the more abstract and broad term, and **Company** is just one specialization. **Person** is another descendant of **Party.**

Let's illustrate this using pseudo-graphics:

> Party
>
> +---- company
>
> +---- person

Each party has some attributes, like 'parent party' and area. The company has VAT number and registration type attributes. Each person has "first name" and "last name".

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

So, if we use table data, in order to access all attributes of a company or a person, we have to relate (join) data from different tables, using unique identifiers. The identifiers are the so-called "surrogate keys" because they are existing only in the database and have no real-world counterpart. Using such keys and relating data between tables is ordinary in the relational world of the databases.

However, internally, the systems use objects, because it is much simpler to process them. Objects already have all the necessary attributes related together and there is no need to use Identifiers or table relations.

This is only an introduction to the topic of object-relational mapping. More deeper look would go too deep into the developer details of the subject.

## Display format

Each entity object must have a representation as text, so that it can be visualized in a user interface - e.g. in @@winclientfull or @@webclientfull. This is quite a simple task for entity types that have few attributes, but in reality most do not. Let's see the following usual entity types as examples,

> Client
>
> Product

These entity types are one of the most commonly used in a typical workflow. Now we will expand these entity types to real (sample) data- i.e. entities.


> **Client**

| Number | Name | Sales person |
| --- | --- | --- |
| nmb001 | Nia Cartwright | Kristy Griffin |
| 123456 | Kamile Farrington | Natalie Dunn |
| ab1234 | Kurtis Dickinson | Anderson Fraser |


> **Product**

| Code | Name | Measurement unit | Group |
| --- | --- | --- | --- |
| 1103 | DEO GALERIA PINK F 150 ML | pcs | Goods |
| 1102-01-011 | 1U Server | pcs | Computers |
| 12345678 | Remote support | h | Services |

Usually these entities make sense in the context of other ones. E.g. documents, reports, analysis, etc... And therefore, they must be visualized in some way. The most typical way is to display their names (i.e. the "Name" attribute):

**Client**
> Nia Cartwright
> Kamile Farrington
> Kurtis Dickinson

**Product**
> DEO GALERIA PINK F 150 ML
> 1U Server
> Remote support

Ok, everything seems fine, but what if we need something more ? Think in general, not just about printouts or reports, this entity visualization should also apply when we choose a customer or a product (respecting the example above). How will you handle the situation when you have several products, named *"1U Server"* ? Wouldn't it be better to see more information (i.e. additional attribute/s) about each entity ? How about if you see what's the product availability at the time you choose it ?

And this is where the display format becomes important. 

@@name allows you to specify the display format of each entity type.

So if you need more attributes to be displayed or a specific format of your choise, you are free to customize it. 
Here is an example of how you could customize the products entity type:

| Display format | Visualization |
| --- | --- |
| `{Name:T}` | DEO GALERIA PINK F 150 ML |
| `{Name:T} ({Code})` | DEO GALERIA PINK F 150 ML (1103) |
| `{Name:T} #{Code}` | DEO GALERIA PINK F 150 ML #1103|
| `{Code}` | 1103 |
| `{Code}: ({Name:T})` | 1103: (DEO GALERIA PINK F 150 ML) |

The common thing between all display formats is the fact they use string interpolation- it gives you the opportunity to customize how each one of your entity types will be displayed.

You can find more information on the topic of [string interpolation here](../string-interpolation/index.md).