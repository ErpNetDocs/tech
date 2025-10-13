---
uid: index-product-relations
---
# Product Relations

The Product Relations framework provides a unified and extensible way to **define and manage how products are connected within the system** — whether functionally, commercially, or technically. 

Its purpose is to establish a single, consistent model for representing different types of product-to-product relationships, such as replacements, compatibility, merchandising links, or generic associations.
By standardizing these relations, the model enables automation of key business processes (e.g., one-click replacements, cross-sell suggestions, configuration validation), improves data consistency across modules, and simplifies future scalability.

Ultimately, Product Relations **aim** to create a flexible foundation that supports better product lifecycle management, smarter system behavior, and richer customer experiences across all product-driven operations.

## Business Benefits

- Improved operational efficiency: Enables automatic handling of replacements, compatibility checks, and related product suggestions — reducing manual effort.

- Enhanced sales opportunities: Supports upselling, cross-selling, and targeted recommendations to boost revenue.

- Better customer experience: Ensures that users and customers always see valid, compatible, and up-to-date product information.

- Lifecycle transparency: Tracks product replacements and compatibility history across time for clearer product evolution management.

## Technical Benefits

- Unified data model: One schema covers all product relationships — no need for multiple specialized tables.

- Scalability and flexibility: New relation types can be introduced without changing the database structure.

- Integration-friendly: Provides a consistent API and data model for internal and external systems.

- Future-ready foundation: Can potentially replace existing component structures (e.g., ProductComponents or BOM) with a single, generalized model.

 ## Scope and Applicability
 Where, how, and by whom the Product Relations model is expected to be used across the system and business processes?

The Product Relations framework is designed as a core, cross-functional component of the product data model.
It applies to multiple business domains and system modules that rely on accurate, flexible, and contextual relationships between products.
Its purpose is to ensure that product interactions — such as replacements, compatibility checks, and related product suggestions — are handled consistently across the platform.

### Functional Scope

- Sales and Order Management
  Supports one-click product replacement (RPL) when a product is discontinued, and displays alternative or related items to sales users.
- E-Commerce and Customer
  Portals	Provides product recommendations based on merchandising (MRC) links such as upsell, cross-sell, or accessories.
- Production and Work Orders
  Uses replacement and fitment (RPL, FIT) relations to validate compatible materials, tools, or components during production planning.
- Product Configuration and Bill of Materials (BOM) Management
  Ensures component compatibility (FIT) and enables potential integration with or replacement of existing BOM structures.
- After-Sales and Service Management
  Helps technicians identify suitable replacement parts (RPL) or compatible alternatives for maintenance and repairs.
Product Information Management (PIM)	Maintains a centralized, structured source of truth for all product relationships, ensuring consistent data distribution across systems.
   
# Example Use Cases per Relation Type

|System Type|	Example|	Description|
|----------|---------|-------------|
|Generic (GEN)	| Product A ↔ Product B|	A general link between two products, e.g., products that are frequently used together in projects or documentation, without specific system logic.|
|Replacement (RPL)	|Old Filter X → New Filter Y	|Product Y replaces product X after it is discontinued. The system automatically suggests Y as a valid substitute in orders or work documents.|
|Merchandising (MRC)	|Laptop → Wireless Mouse|	Defines a cross-sell or upsell relation. When Laptop is viewed or added to cart, the system suggests compatible accessories like the Wireless Mouse.|
|Fitment (FIT)	|Oil Filter → Vehicle Model	|Defines compatibility between components. The Oil Filter is compatible only with certain Vehicle Models, and the system validates this during configuration.|

Learn more about the two major entities within product relations framework: 
1. Product Relations Types
2. Product Relations
