# Product relations

With the latest update, we’re introducing a new concept: _Product Relations_, bringing more flexibility, clarity, and automation to the way products are connected.
This functionality is implemented through two new tables:

🧩 Product Relation Types – define what kind of relationship exists between products (e.g., Replacement, Compatibility, Merchandising).
🔗 Product Relations – store the actual links between products (from → to), including validity dates and quantity factors.

## What Does This Bring?

The new model allows the system to understand how products relate to each other — not just by code or category, but by real business relationships:

🔁 Replacement – automatically suggest substitute products when one is discontinued or out of stock.
🧠 Merchandising – provide intelligent product recommendations such as upsell, cross-sell, or similar products.
⚙️ Fitment – ensure only compatible components are used in configurations or production.
🧱 Generic – define your own custom relation types for unique business cases.

## Why It Matters

These new tables make product data management more flexible, centralized, and extensible.
Instead of separate, disconnected structures (for replacements, accessories, or compatibility), we now have a unified model that can evolve without database or code changes.

This turns Product Management into a more powerful tool for:

- process optimization (faster order handling and support),
- improved customer experience through smarter product suggestions,
- and deeper insight into product relationships and lifecycle data.

🧭 In short:
The new Product Relations transform Product Management from a static catalog into a dynamic network of product knowledge, enabling automation, recommendations, and data-driven decisions across the business.

-------------------------------------------------------------
Learn more about the two major entities within product relations framework: 
1. [Types of Product Relations](https://docs.erp.net/tech/modules/general/products/product-relations/product_relation_types.html)
2. [Product Relations](https://docs.erp.net/tech/modules/general/products/product-relations/product_relations.html)

If you need to access the **domain model**, click here:
1. [General.Products.ProductRelationTypes Entity](https://docs.erp.net/model/entities/General.Products.ProductRelationTypes.html)
2. [General.Products.ProductRelations Entity](https://docs.erp.net/model/entities/General.Products.ProductRelations.html)
