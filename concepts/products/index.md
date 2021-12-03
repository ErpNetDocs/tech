# Products

### Description 

*Products* are the most detailed items which a company sells or buys. Products can be tangible or intangible. A **tangible** product is a physical object that can be perceived by touch such as a building, vehicle, gadget, or clothing. An **intangible** product is a product that can only be perceived indirectly such as services. 

In @@name, all product-specific data is kept in the product’s definition. 

Product’s definition includes the information that is needed to identify the product, for example:

-	product name;
-	part number;
-	product group.

And some other basic data that describes and categorizes the product, for example:

-	product type;
-	measurement unit;
-	costing currency and others.

Different panels can also be visualized in the product’s definition, allowing the user to have access to all of the product related information such as product dimensions, current stock holds, serial numbers, lots, product prices and others.  


### Part numbers, product codes, serial numbers, and lots

The products are identified in @@name by their **part numbers**. The part number is the unique identifier of the product. You cannot create a product without entering a product part number that is unique for the whole database. Conversely, the **product name** is not designed to be unique identifier, so it is possible to have different products with the same name but with different part numbers.

In addition to the part number, the user is able to specify alternative **product codes** – e.g. supplier’s product codes, client’s product codes, barcodes, etc. In this way, the product can be searched and selected not only by its product number but by its product codes as well. For more information, see [Product codes](product-codes.md) and [Coding systems](coding-systems.md).

As opposed to part numbers and codes, the **serial numbers** are used to identify not the whole product but its separate pieces and help to keep track of what happens with them (e.g., to whom they are sold, if they are under guarantee, etc.). If the option **Serialized** in the product definition is checked, this product cannot be used in the logistic documents if its serial number is not explicitly indicated. For more information, see [Serial numbers](serial-numbers.md).

@@name allows the separate product units to be grouped in **lots**. An unlimited number of lots could be defined for a particular product. Each lot can contain product units that have the same expiry date or that are received within the same receiving order or that are produced within the same production output order. For more information, see [Lots](/modules/logistics/inventory/lots/index.md).

In the product definition, you can manage the settings of using lots by determining the following parameters:
- whether the lots are allowed or not allowed or required
- the method by which the lots are automatically issued – FIFO, LIFO, and FEFO
- the standard cost per lot
- the standard price per lot
- the size of a standard lot. 

The above information is represented in the following table as an example:

| Part number | Product name | Product code    (Coding system: Billa) | Product code   (Coding system: Metro) | Serial number | Lot number    (Expiry date) |   
| :---------  | :----------- | :------------------------------------- | :------------------------------------ | :------------ | :-------------------------- |
| 456789      | X            | 88559910                               | 777RR69PP                             | 1111111111    | 20200611                    |
| 456789      | X            | 88559910                               | 777RR69PP                             | 1111111112    | 20200611                    |
| 456789      | X            | 88559910                               | 777RR69PP                             | 1111111113    | 20220810                    |
| 999888      | X            | 55889941                               | 777RR69PP                             |               |                             |

### Product groups and product types

Each product must belong to a user defined **product group** (e.g. goods, materials, services …) as well as to a user defined **product type** (e.g. goods, materials, services …):

- The Product groups allow the products to be grouped according to different criteria, so they could inherit certain properties from the groups – such as next part number, default measurement unit, product name mask, default product type, etc. For more information, see [Product groups](product-groups.md).

- The Product types provide the functionality of creating different automatizations for a certain product type - e.g., you can set whether the products of a certain type are allowed to be serviced, shipped, stocked, etc. For more information, see [Product types].

### Measurement units

The products can be presented in multiple measurement units. A **base measurement category** is used for storing the product in the warehouse, for sales reporting, etc. However, you may choose a different **measurement unit** that will be loaded by default when creating documents with this product. In order to make conversions between the different units of measurement for the same quantity, the user is able to define measurement ratios. For more information, see [Measurement categories], [Measurement units] and [Product dimensions](product-dimensions.md).

Furthermore, no matter what the recalculation based on the measurement ratios is, if the option **Allow variable measurement ratios** is checked, the user has the opportunity to manually adjust the right base quantity in the particular situation. For more information, see [Variable (dynamic) measurement ratios](variable-dynamic-measurement-rations.md).

Example of setting different measurement units for a product:

| Part number | Product name | Base measurement category | Measurement unit | Purchase measurement unit  | Product dimension                   |   
| :---------  | :----------- | :------------------------ | :--------------- | :------------------------- | :---------------------------------- |
| 456789      | X            | PCS                       | KG               | Pallet                     | 5 kg = 1 PCS;     1 pallet = 10 PCS |


### Other settings

When creating a product, the user must specify the **currency** in which the product cost will be calculated. By default - this is the base currency of the enterprise company.
It is important to define the costing method as well. If the costing method is not set in the product definition, the one set in the enterprise company definition will be used instead.  

Some of the products are used as materials for producing other products. In this case, a **flushing method** must be set in the product definition. This method determines how the material will be written off from the warehouse – manually (using consumption orders) or automatically (by releasing or finishing the work order).

The product can be activated or deactivated depending on whether it is a part of the company’s sales or procurement product lists. These settings are managed via the **Active** field in the product definition. In addition, there is an option to show or not this product in the company’s catalogs, related to its product group. If the option **Is featured** is checked – the product will be presented at the title space in promotional materials, web pages, etc.

@@name provides a functionality to add one or several **pictures** of the product in order to be visually presented in the system. Pictures can be displayed when searching for products, printing reports, documents, etc.

To automate the creation of the Intrastat declaration some fields in the product definition must be filled as well:  **Intrastat commodity code**, **Intrastat Supplementary Unit**, and **Origin Country**.

In the product definition the user can specify some **other parameters** of the product, such as those listed below:

- short name – the name that will be used for space-constrained devices, like mobile phones, fiscal printers, etc.
- expiry period days (from the date of production);
- guarantee period days (if the product type is serviced);
- cargo type – by choosing one of the user defined cargo types (e.g. container cargo, Liquid cargo, etc.);
- minimum sales quantity base;
- minimum sales price;
- planning demand time fence days;
- scrap rate (when the product is used as an ingredient);
- ABC class – product importance classification where A is the highest class and C is the lowest class. The products in class A are with the highest turnover and with the highest value; 
- valuation group – a user-defined group that is used in reconciliations when compensating pluses and minuses.
- excise product – the excise product code (if the product is excised);
- excise alcoholic atrength (if the product is subject to alcoholic Excise reporting).
