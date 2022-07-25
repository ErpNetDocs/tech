# Display format

Each **[entity object](https://docs.erp.net/tech/advanced/concepts/object-relational-mapping.html)** must have a representation as text, so it can be visualized in a user interface - in @@winclientfull or @@webclientfull. This is quite a simple task for entity types that have few attributes - not so much for the ones that don't. 

**Let's see the following entity types as examples:**
- Client
- Product

They're one of the most commonly used in a typical workflow, and can expand to real (sample) data like entities.

**Client**

| Number | Name | Sales person |
| --- | --- | --- |
| nmb001 | Nia Cartwright | Kristy Griffin |
| 123456 | Kamile Farrington | Natalie Dunn |
| ab1234 | Kurtis Dickinson | Anderson Fraser |

**Product**

| Code | Name | Measurement unit | Group |
| --- | --- | --- | --- |
| 1103 | DEO GALERIA PINK F 150 ML | pcs | Goods |
| 1102-01-011 | 1U Server | pcs | Computers |
| 12345678 | Remote support | h | Services |

These entities make sense in the context of others (documents, reports, analysis, etc). 

The easiest way to visualize them is to display their names (the "Name" attribute):

> **Client**
>
> Nia Cartwright
>
> Kamile Farrington
>
> Kurtis Dickinson

> **Product**
>
> DEO GALERIA PINK F 150 ML
>
> 1U Server
>
> Remote support

#### Everything seems fine, but what if you need something more? 

This entity visualization should also apply when you choose a **customer** or a **product**. 

How will you act when you have several products named *"1U Server"*? 

Wouldn't it be better to see more information about each entity? 

What about if you see the product availability at the time that you choose it?

This is where **display format** helps. @@name allows you to **specify** it for each entity type.

If you need more attributes to be displayed, or a specific format of your choice, you're free to customize it. 

Here's an example of how you could customize a product's entity type:

| Display format | Visualization |
| --- | --- |
| `{Name:T}` | DEO GALERIA PINK F 150 ML |
| `{Name:T} ({Code})` | DEO GALERIA PINK F 150 ML (1103) |
| `{Name:T} #{Code}` | DEO GALERIA PINK F 150 ML #1103|
| `{Code}` | 1103 |
| `{Code}: ({Name:T})` | 1103: (DEO GALERIA PINK F 150 ML) |

Display formats use **[string interpolation](https://docs.erp.net/tech/advanced/string-interpolation/index.html)**, allowing you to customize your entity types.

## Configuring display format

Changing the display format of an entity type is an easy task. 

Just open its definition and edit the 'Display Text Format' attribute to the desired one.

![picture1](./pictures/entity-type-display-format.png)


As a result, each entity of this type will be displayed according to the selected display format. 

In the picture below, you can see how a customer dropdown is shown in the @@webclient:

![picture2](./pictures/webclient-dropdown.png)

Furthermore, it's possible to specify the display format yourself, if the pre-defined formats don't suit you. 

Just follow the rules when specifying the **string interpolation**.

> [!NOTE]
> 
> How do you know the specific attributes of the entity type that you need? <br> Refer to the **[@@erpnet Domain Model documentation](https://docs.erp.net/model/entities/)**. <br> Following the example above, all the necessary information is available in **[Crm.Customers Entity](https://docs.erp.net/model/entities/Crm.Customers.html)**. <br> The display format attribute for an entity is located in the **[Systems.Core.EntitySettings Entity](https://docs.erp.net/model/entities/Systems.Core.EntitySettings.html#displaytextformat)** table.

## Display format inside look

Each entity type has its corresponding record in another entity- [EntitySettings](https://docs.erp.net/model/entities/Systems.Core.EntitySettings.html). There's an attribute DisplayTextFormat- here is stored the interpolated string, which defines the display format for the entity type. If there's no settings record for an entity, then the default display format takes place.

### Defaults

The default display format for an entity is defined at the system level. For entities that have **Code** and **Name** attributes, the default display format is specified by the database configuration option [CodeNameFormat](../../reference/config-options-reference.md#47-codenameformat) - the system default is **{Name}**.

> [!NOTE]
> 
> Often the **Code** and **Name** attributes for an entity are not literally named so. They are expressed by the types **CodeDataMember** and **NameDataMember**.

In the table below you can see some entities and their Code and Name attributes (i.e., the CodeDataMember and NameDataMember):

| Entity    | Code attribute | Name attribute  |
| --------- | -------------- | --------------- |
| Products  | PartNumber     | Name            |
| Customers | Number         | Party.PartyName |


**DefaultDisplayTextFormat**, **CodeDataMember** and **NameDataMember** can be found in the documentation of each entity.

### Searchable

**Display text** attribute is searchable. This means that when an entity is searched, the attributes, defined in the **display format** are also searched for a match.

![picture3](./pictures/webclient-custom-display-format.png)

![picture4](./pictures/webclient-search-by-display-format.png)

You can find more information here, 
<br/>
https://docs.erp.net/dev/domain-api/query-options/search.html

## Examples

In this section, you can see several examples of different entity types: 

- sample data
- available predefined display formats

and their corresponding visualization.

#### Customers

**[Customers entity documentation](https://docs.erp.net/model/entities/Crm.Customers.html)**

#### Sample data

<br>

| Number | Name |
| --- | --- |
| nmb001 | Nia Cartwright |
| 123456 | Kamile Farrington |
| ab1234 | Kurtis Dickinson |

#### Display formats

<br>

| Display format | Visualization |
| --- | --- |
| `{Party.PartyName:T}` | Nia Cartwright |
| `{Party.PartyName:T} ({Number})` | Nia Cartwright (nmb001) |
| `{Party.PartyName:T} #{Number}` | Nia Cartwright #nmb001 |
| `{Number}` | nmb001 |
| `{Number}: ({Party.PartyName:T})` | nmb001: (Nia Cartwright) |
| | |
| `{Party.PartyName:T}` | Kamile Farrington |
| `{Party.PartyName:T} ({Number})` | Kamile Farrington (123456) |
| `{Party.PartyName:T} #{Number}` | Kamile Farrington #123456 |
| `{Number}` | 123456 |
| `{Number}: ({Party.PartyName:T})` | 123456: (Kamile Farrington) |
| | |
| `{Party.PartyName:T}` | Kurtis Dickinson |
| `{Party.PartyName:T} ({Number})` | Kurtis Dickinson (ab1234) |
| `{Party.PartyName:T} #{Number}` | Kurtis Dickinson #ab1234 |
| `{Number}` | ab1234 |
| `{Number}: ({Party.PartyName:T})` | ab1234: (Kurtis Dickinson) |

#### Products

**[Products entity documentation](https://docs.erp.net/model/entities/General.Products.Products.html)**

#### Sample data

<br>

| Name | Part number |
| --- | --- |
| DEO GALERIA PINK F 150 ML | 1103 |
| 1U Server | 1102-01-011 |
| Remote support | 12345678 |

#### Display formats

<br>

| Display format | Visualization |
| --- | --- |
| `{Name:T}` | DEO GALERIA PINK F 150 ML |
| `{Name:T} ({PartNumber})` | DEO GALERIA PINK F 150 ML (1103) |
| `{Name:T} #{PartNumber}` | DEO GALERIA PINK F 150 ML #1103 |
| `{PartNumber}` | 1103 |
| `{PartNumber}: ({Name:T})` | 1103: (DEO GALERIA PINK F 150 ML) |
| | |
| `{Name:T}` | 1U Server |
| `{Name:T} ({PartNumber})` | 1U Server (1102-01-011) |
| `{Name:T} #{PartNumber}` | 1U Server #1102-01-011 |
| `{PartNumber}` | 1102-01-011 |
| `{PartNumber}: ({Name:T})` | 1102-01-011: (1U Server) |
| | |
| `{Name:T}` | Remote support |
| `{Name:T} ({PartNumber})` | Remote support (12345678) |
| `{Name:T} #{PartNumber}` | Remote support #12345678 |
| `{PartNumber}` | 12345678 |
| `{PartNumber}: ({Name:T})` | 12345678: (Remote support) |
