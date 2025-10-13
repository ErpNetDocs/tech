---
uid: product-relation-types
---

# Product Relation Types 

The Product Relation Types framework defines a unified and extensible model for representing various relationships between products within the system.
Its main purpose is to allow consistent storage, management, and functional use of product-to-product relations such as replacements, compatibility, merchandising, and other custom links.

In other words, it provides a single, structured way to describe how products relate to each other — functionally, commercially, or technically.

# System Type Relations 

## 1. Generic (GEN)

   - Description:
A general or neutral link between two products without any built-in business logic.

   - Expected behavior:
The system only stores and displays the relation; no automatic actions are triggered.
Used for free associations or for future relation types that don’t fit into other categories.

## 2. Replacement (RPL)

- Description:
Defines a relation where one product can replace another.

- Expected behavior:

The system should provide one-click replacement in all processes where a product is selected (e.g., SalesOrder, WorkOrder).
When a product is discontinued, invalid, or out of stock, the system automatically suggests a valid replacement (ToProduct).
The Qty_Factor field is used to calculate adjusted quantities during replacement (e.g., 1 X = 2 Y).
Relation validity is controlled by FromDate and ToDate.
Can be used to model a supersession chain — tracking product replacements over time.

## 3. Merchandising (MRC)

   - Description:
A relation for commercial or marketing purposes — e.g., upsell, cross-sell, similarity, or accessories.

  -  Expected behavior:

The system should use these relations to automatically suggest related products in the UI (Product Details, Cart, Sales screens, etc.).
Subtypes can be defined via the Code field (e.g., UPSELL, CROSSSELL, SIMILAR).
Relations can be time-bound using FromDate and ToDate (e.g., seasonal campaigns).
Data can also be used for analytics such as attach rate, conversion uplift, and similar KPIs.

## 4. Fitment (FIT)

  - Description:
Defines compatibility between products — i.e., which products can be used together in configurations, technologies, or documents.

   - Expected behavior:

When a product is selected in a configuration, the system should filter or validate the available compatible products.
Relations can be one-directional or bi-directional depending on the domain logic.
Commonly used for verifying correctness in product recipes, technical documents, or assemblies.

## Summary:

|SystemType |	Code|	Purpose| Behaviour|
|-----------|-----|--------|----------|
|Generic    |	GEN |	Free / universal relation|	Only record and display; no functional behavior.|
|Replacement|	RPL	|Product substitution	| One-click replacement; Qty_Factor; date validity.|
|Merchandising|	MRC|	Commercial / marketing relation	|Automatic recommendations (upsell, cross-sell, accessories).|
|Fitment|	FIT|	Product compatibility	|Filtering and validation of compatible products.|
