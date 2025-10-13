---
uid: index-product-relations
---
# Product Relations

The Product Relations framework provides a unified and extensible way to **define and manage how products are connected within the system** — whether functionally, commercially, or technically. 

Its purpose is to establish a single, consistent model for representing different types of product-to-product relationships, such as replacements, compatibility, merchandising links, or generic associations.
By standardizing these relations, the model enables automation of key business processes (e.g., one-click replacements, cross-sell suggestions, configuration validation), improves data consistency across modules, and simplifies future scalability.

Ultimately, Product Relations aim to create a flexible foundation that supports better product lifecycle management, smarter system behavior, and richer customer experiences across all product-driven operations.


# Example Use Cases per Relation Type

|SystemType|	Example|	Description|
|----------|---------|-------------|
|Generic (GEN)	| Product A ↔ Product B|	A general link between two products, e.g., products that are frequently used together in projects or documentation, without specific system logic.|
|Replacement (RPL)	|Old Filter X → New Filter Y	|Product Y replaces product X after it is discontinued. The system automatically suggests Y as a valid substitute in orders or work documents.|
|Merchandising (MRC)	|Laptop → Wireless Mouse|	Defines a cross-sell or upsell relation. When Laptop is viewed or added to cart, the system suggests compatible accessories like the Wireless Mouse.|
|Fitment (FIT)	|Oil Filter → Vehicle Model	|Defines compatibility between components. The Oil Filter is compatible only with certain Vehicle Models, and the system validates this during configuration.|
