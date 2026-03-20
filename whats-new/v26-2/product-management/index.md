# Product Management
The **Product Management** module is the heart of product data management — where all products are defined, structured, and connected within the system.
Its purpose is to ensure complete, accurate, and consistent product information throughout the entire lifecycle — from definition and maintenance to sales, service, and analytics.

![homepage](pictures/homepage.png)

## Notable features

### Introduction of a new entity ["Product Relations"](product-relations/index.md)

With the latest update, we’re introducing a new concept: _Product Relations_, bringing more flexibility, clarity, and automation to the way products are connected.
This functionality is implemented through two new tables:

🧩 Product Relation Types – define what kind of relationship exists between products (e.g., Replacement, Fitment, Merchandising).<br>
🔗 Product Relations – store the actual links between products (from → to), including validity dates and quantity factors.

This brings to the table new features and functions too.

## Other features

### 1. Replace a product

ERP.net allows you to replace one product in a document line with another product that has been defined as a valid Replacement in the Product Relations framework.<br>
The function is called **"Replace with..."** and is available in both the Web Client and the Desktop Client.<br>
It helps users select approved substitute products without searching manually and ensures that only currently valid replacements are offered.<br>
Learn how to use it [HERE](https://docs.erp.net/tech/modules/general/products/how-to/replace-with.html).

Desktop client
![picture](pictures/replace_with.png)

Web client
![picture](pictures/replace_with_web.png)

### 2. Add a related product
