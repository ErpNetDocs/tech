# Documents


### Description
Documents are one of the three main categories of entities in @@name. They represent things that have occurred or will occur.

The main categories are:

- **Documents** - facts; things that occur:

Sales orders, Invoices, Purchase orders, etc.

- **Definitions** - they represent real-world objects; things that (generally) do not change:

Customers, Products, Stores, etc.

- **Settings** - system-related; data about the way the system works:

Document types, Document routes, Form views, etc.

### The Most Important Attributes

All documents derive from a base entity type called **Document** and share similar attributes.

This is a non-extensive list of the more important attributes:

- **Enterprise Company** - the company that created the document.

- **Company Location** - the location of the company that created the document.

- **Document Date** - the date the document was constituted. If it was created electronically, then this is the system date of creation. When it is created outside the system and entered post-factum, the attribute contains the date of actual creation.

- **Document Type** - a user-defined document type for classification of the documents. It also deals with print-out forms, document flow and other rules.

- **Document Number** - a unique number within the sequence, defined in Document Type. Usually created by the system, but can also be set up to accept manual entry or import from external sources.

- **State** - each document in the system has a current state at any given moment. It affects how the document influences the system and whether it is updateable.

- **Currency Directory** - the primary directory for currency rates which will be used for currency conversions throughout the document. See **Multi-currency (TBD)** for details.

## Further Reading:

- **[Document states](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/document-states.md)** 
- **[Document flow](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/document-flow.md)** — The sequence of documents in a process form the document flow of the process.
- **[Additional amounts](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/additional-amounts/index.md)**
- **Document versions (TBD)**
- **[Transitional documents](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/transitional-documents.md)**
- **[Adjustment documents](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/adjustment-documents.md)**
- **[Creating a duplicate document and a new document from current](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/creating-a-document.md)**
- **[Displaying and finding document and line numbers](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/displaying-document.md)**


