# Document Generation


## Description

Document generation is a key part of the document flow in the system and is widely used to automate such flows. It provides for the automatic generation of inheriting documents from a parent document.

Document generation is a special case of direct [**Document Fulfillment**](https://github.com/ErpNetDocs/tech/blob/362feb42dff42c7bb6ce84d5bcde14d1afdc6ddb/advanced/documents/document-fulfillment.md), when there is only a single source document. Document generation usually creates only one target document, but can sometimes make multiple documents. When multiple documents are generated, it is usually because of different values of some key attribute(s) in the different lines of the source document.

## Automating the document generation

Having just a single document as a source allows the easy automation of the document generation. One document can (automatically) create multiple and different types of target documents under different conditions and events.

The definition of each *Document Type* includes a special sub-entity type, called *Workflow Routes*. Workflow routes specify procedures, conditions and events for the automatic generation of inheriting documents. Each *Document Type* can include many *Workflow Routes*. Routes can start automatically or require a user initiation.

The routes for the different *Document Types* form together a general network graph, called the *Document Flow*.

## Properties of a document generation route

Each document generation route contains at least the following properties:
- **Generation Events**
Contains the events that trigger the document route. The most often used event is usually the event of changing the document state.
- **State**
The system state of the source document which will trigger the document route. When the user changes the state of the document, the system consecutively initiates all routes, marked with any intermediate states. For example, if a document has a Planned state, which is then changed to Released state, a route specified for the intermediate Firm Planned state *will* be started.
- **User State**
When not blank, specifies that the route will be started only when the final user state of the source document equals the specified user state. Contrary to the system behavior with system states, when changing the user state, routes for the intermediate user states *are not* started.
- **Source Enterprise Company**
This might be left blank, then the route will be valid for all enterprise companies. When not blank, the route will be run only for documents in the specified enterprise company.
- **Generation Procedure**
The generation procedure which will be used to generate the target document.

## Properties of a document generation procedure

The generation procedures are fixed procedures, provided by the system. When defining a document route, the user is allowed to choose a document generation procedure within a system providing a fixed list of procedures.

Each generation procedure is defined in this documentation using the following attributes:
- **Procedure Code**
The unique procedure code is used for identification purposes. The code has the following structure:
    - **Subsystem Code**<br>
      3-5 characters which uniquely identify the sub-system of the source document.
    - **Module Code**<br>
      2 digits, which uniquely identify the module within the sub-system of the source document.
    - **Procedure Code**<br>
      2 digits, which specify the consecutive number of the procedure within the module

For example, ‘*CRM0103*’ specify a procedure in ‘CRM’ sub-system, 01-Sales module, procedure #3.
- **Name**<br>
Name of the generation procedure.
- **Obsolete**<br>
Specify whether the generation procedure is still active in the latest version of the system. Old generations, which are no-longer supported are marked as ‘Obsolete’.
- **Source Document Entity Type**<br>
Specifies the entity type of the source document. The generation procedure can be used only for documents of the specified entity type. The entity type specifies the general type of the document, for example *Sales Order*. There can be many user-defined *Document Types* within a single entity type.
- **Target Document Entity Type**<br>
The entity type of the target document. The generation procedure can generate only documents with the specified entity type. Each *Document Route* can specify different user-defined *Document Types* that should be generated, but only within the specified entity type.
- **Description**<br>
Detailed description and business case when the generation procedure is used.

