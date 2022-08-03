# Documents


### Description
Documents are one of the three main categories of entities in @@name. They represent things that have occurred or will occur.

The main categories are:

- **Documents** - facts; things that occur:

Sales orders, invoices, purchase orders, etc.

- **Definitions** - they represent real-world objects; things that (generally) do not change:

Customers, Products, Stores, etc.

- **Settings** - system-related; data about the way the system works:

Document types, Document routes, Form views, etc.

### The most important attributes

All documents derive from a base entity type called **Document** and share similar attributes.

This is a non-extensive list of the more important attributes:

- **Enterprise company** - the company that created the document.

- **Company location** - the company location where the document was created.

- **Document date** - the date the document was constituted. If it was created electronically, then this is the system date of creation. When it is created outside the system and entered post-factum, the attribute contains the date of actual creation.

- **Document type** - a user-defined document type for classification of the documents. Also defines print-out forms, document flow and other rules.

- **Document number** - a unique number within the sequence, defined in Document type. Usually created by the system, but can also be set up to accept manual entry or import from external sources.

- **State** - each document in the system has a current state at any given moment. It affects how the document influences the system and whether it is updateable.

- **Currency directory** - the primary directory for currency rates which will be used for currency conversions throughout the document. 


### Further reading:

- **[States](states.md)**

- **[Display and choose](display.md)**

- **[Adjustments](adjustments.md)**

### Advanced topics:

- **[Document flow](/tech/advanced/document-flow/index.md)**

- **[Document amounts](/tech/advanced/document-amounts/index.md)**

