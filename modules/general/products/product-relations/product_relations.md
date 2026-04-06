# Product Relations 

System Product Relation Types define how the system interprets and handles a relation.
Custom Product Relation Types define what that relation means in your business.

Creating your own relation types gives you better control and clarity over product relationships, freedom to reflect your business terminology and logic and the ability to scale and extend product data without development effort.

Product Relations define **typed, directional relationships between products**.

Each relation connects a **source product** (`FromProduct`) to a **target product** (`ToProduct`) and is classified by a **Product Relation Type**, which determines the system behavior and the business meaning of the relationship.

Relations may also have a **validity period** and an optional **quantity factor** (`QtyFactor`), which allows the system to adjust quantities when the relation is used operationally.

# Concepts

## Examples of Product Relations

A Product Relation combines two elements:

- a **System Type**, which defines the system behavior of the relation
- a **Relation Type name**, which describes the business meaning of the relation

The following examples illustrate typical relation names for each System Type.

### Generic

Used for neutral or informational relationships without specific system behavior.

Example relation type names:

- Related product  
- Same product family  
- Equivalent reference  
- Alternative item  

Example:  Product A → Product B /  Relation type: Related product

### Replacement

Used when one product can replace another. Replacement relations may be used by system functions that support product substitution and quantity adjustment through `QtyFactor`.

Example relation type names:

- Supersession  
- Alternative replacement  
- Equivalent replacement  
- New model replaces old model  

Example: Printer Model A → Printer Model B / Relation type: Supersession

### Merchandising

Used for commercial relationships such as accessories, cross-sell items, or upsell suggestions.

Example relation type names:

- Accessory  
- Cross-sell  
- Upsell  
- Bundle component  
- Similar product  

Example: Laptop → Laptop bag / Relation type: Accessory

### Fitment

Used for compatibility relationships between products that can be used together.

Example relation type names:

- Compatible with  
- Fits  
- Matching component  
- Approved part  

Example: Printer → Toner cartridge / Relation type: Compatible with


The system type defines how the relation can be used functionally, while the custom relation type name defines how the relation is understood in the business context. This allows organizations to keep consistent system behavior and, at the same time, use terminology that matches their own product model.

## Using Product Relations

Product Relations are not only used to define links between products, but also support user actions when working with products in **logistics documents**. Currently, the following _functions_ exploit Product Relations. They are accessible from the context menu of a Product field:

### Product replacement - _Replace with..._

Allows the current product in a document row to be replaced with a valid related product of type **Replacement**.

The system uses the current product as `FromProduct` and lists the valid related products from `ToProduct`. If the selected relation defines a positive `QtyFactor`, the quantity in the row is recalculated accordingly.

This function is useful when the original product is discontinued, unavailable, or replaced by a newer model.

See how to use it [HERE](https://docs.erp.net/tech/modules/general/products/how-to/replace-with.html).

### Product addition - _Add related_

Allows a related product to be added as a **new document row** without modifying the current row.

The system uses the current product as `FromProduct` and lists the valid related products from `ToProduct` for relations of type **Merchandise**. If the selected relation defines a positive `QtyFactor`, the quantity of the new row is calculated based on the quantity in the current row.

This function is useful when users need to add complementary or commercially related products during document entry.

See how to use it [HERE](https://docs.erp.net/tech/modules/general/products/how-to/add-related.html)

