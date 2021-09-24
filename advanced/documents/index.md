# Documents


### Description
Documents are one of the 3 main categories of entities in @@name. Documents represent things that have occurred or will occur.

The 3 main categories are:
- **Documents** - facts; things that occur
- **Definitions** - they represent real-world objects; things that (generally) do not change
- **Settings** - these are system settings; data related to the way the system works

Examples of **Documents** are: Sales orders, Invoices, Purchase orders, etc.

Examples of **Definitions** are: Customers, Products, Stores, etc.

Examples of **Settings** are: Document types, Document routes, Form views, etc.

### The Most Important Attributes
All documents derive from a base entity type, called **Document** and share similar attributes. This is a non-extensive list of the attributes having more importance:
- **Enterprise Company** - the company that created the document.
- **Company Location** - the company location where the document was created.
- **Document Date** - this is the date, when the document was constituted. If the document was electronically created in the system, this is the system date by the time of creation. When the document was created outside the system, and was entered post-factum, the attribute contains the date of the actual creation.
- **Document Type** - user-defined document type, used for classification of the documents. Also defines print-out forms, document flow and other rules.
- **Document Number** - the unique document number, within the sequence, defined in Document Type. Usually created by the system, but can also be set up to accept manual entry or import from external sources.
- **State** - the current state of the document. See **Document states** for details.
- **Currency Directory** - the primary directory of currency rates, which will be used for currency conversions throughout the document. See **Multi-currency (TBD)** for details.

## Further Reading:
- **Document States** — Each document in the system has a current state at any given moment. The state affects how the document affects the system and whether the document is updateable.
- **Document Flow** — The sequence of documents in a process form the document flow of the process.
- **Additional Amounts**
- **Document Versions (TBD)**
- **Transitional Documents**
- **Adjustment Documents**
- **Creating A Duplicate Document And A New Document From Current**
- **Displaying And Finding Document And Line Numbers**


