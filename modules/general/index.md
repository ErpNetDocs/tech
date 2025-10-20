# Foundation

The Foundation module provides the core set of configurable master data and structural definitions essential for the operation of the entire @@name system. Its primary function is to define the organizational structure, master units of measurement, geographical boundaries, and other basic reference data used universally across all modules. 

## Structure

This module contains fundamental definitions, serving as the common dictionary for the entire enterprise.

| Submodule | Description |
| :--- | :--- |
| **Enterprise** | Defines the legal and operational **enterprise companies** within an organization that issue documents and are involved in transactions. |
| **Activities** | Provides generic **task management** and **event scheduling**, supporting workflow and task allocation across an organization. |
| **Contacts** | Defines **individuals** and **entities** outside an immediate enterprise, used for managing relationships with customers, vendors, and partners. |
| **Currencies** | Defines named sets of **currency exchange rates** against a single reference currency for a given date. |
| **[Documents](https://docs.erp.net/tech/modules/general/documents/index.html)** | Contains all formal documents issued by and to the enterprise. |
| **[Files](https://docs.erp.net/tech/modules/general/files/index.html)** | Manages **documents and attachments**, providing a centralized repository for files linked to records. |
| **Geography** | Establishes the geographical master data, including country definitions, administrative boundaries, sales territories, and specific mapping points used for routing and location services. |
| **[Products](https://docs.erp.net/tech/modules/general/products/index.html)** | Defines **goods, materials, and services** fundamental to the Inventory, Sales, Procurement, and Production modules. |
| **Resources** | Defines all **physical and non-physical assets** used in processes, including machinery, labor, and tools. This is the foundation on which the **[Production module](https://docs.erp.net/tech/modules/production/index.html)** builds its capacity and competence model. |

* **[Documents](documents/index.md)**
* **[Files](files/index.md)**
* **[Products](products/index.md)**
