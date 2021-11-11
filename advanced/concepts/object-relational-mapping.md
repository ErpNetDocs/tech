# Object relational mapping

Entities and entity types frequently used terms throughout the documentation. 

**Entities** are information object which represent real-world objects. <br>
**Entity types** are a collection of all objects of a given type.

For example, customer 'XYZ' is an entity. Customer 'ABC' is another entity. All customers are of an entity type called 'Customers'.

### Definitions

- **Entity** - A single object of a given entity type. Also called 'entity object' or simply 'object'. 
- **Entity type** - The set of all objects of a given type. 
- **Attribute** - A named value containing information about an entity object. 

## Relationship to tables and rows

This section contains more advanced information not usually needed to operate the system. However, a deeper understanding of the inner-workings might help when you need to access an @@name database directly using database tools.

Generally, entity types, entities, and attributes are much like tables, rows, and columns. <br> Data of the entities is ultimately stored in the database in the form of tables and rows. 

There's one important distinction: entity types and entities are **object-oriented representation of table data**. <br> A technology called ORM (Object-Relational Mapping) is used to map between entities and tables.

#### In order to better illustrate the difference between objects and tables, let's include some real-world tables and objects:

There's an entity type called 'Party'. It has two descendants (more specialized) entity types called 'Company' and 'Person'. 

'Party' is the more abstract and broad term, while 'Company' and 'Person' are just specializations. 

Let's illustrate this:

> **Party**
>
> +---- **company**
>
> +---- **person**

Each party has some attributes such as 'parent party' and 'area'. <br>
Each company has 'VAT number' and 'registration type' attributes. <br>
Each person has 'first name' and 'last name'.

#### Now, if you look at the tables, they have the following schema:

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

### If you look at the objects, they'll have the following attributes:

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

If you use table data, in order to access all attributes of a company or a person, you need to **relate** (join) data from different tables, using unique identifiers. These are the so-called 'surrogate keys' because they exist only in the database and have no real-world counterpart. Using such keys and relating data between tables is expected in the world of databases.

Internally, the systems use **objects** because it's much easier to process them. Objects already have all necessary attributes related together and there's no need to use identifiers or table relations.

#### Conclusion:

This is only an introduction to the topic of object-relational mapping. A deeper look would exceed the developer details of the subject.
