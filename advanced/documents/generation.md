# Document Generation


## Description

Document generation is a key part of the [document flow](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/flow.md) in the system and is widely used to automate such flows. It provides for the automatic generation of inheriting documents from a parent document.

Generation is a special case of direct **Order Fulfillment**, when there is only one source document. It usually creates a single target but can often make multiple documents. When many instances are generated, it is because of different values of some key attribute(s) in the different lines of the source document.

## Automating the document generation

Having just a single document as a source allows for easy document generation. One instance can create multiple and different types of target documents under different conditions and events.

The definition of each *Document Type* includes a special sub-entity type called *Workflow Routes*. These routes specify procedures, conditions and events for the automatic generation of inheriting documents. Each *Document Type* can host many *Workflow Routes*. They either start automatically or require a user initiation.

Together, the routes for the different *Document Types* form a general network graph called *Document Flow*.

## Properties of a document generation route

Each document generation route contains the following properties:

- **Generation Events**

Events that trigger the document route. The most often used event is usually the one changing the [document state](https://github.com/ErpNetDocs/tech/blob/master/advanced/documents/states.md).

- **State**

The system state of the source document which will trigger the route. When a user changes this state, the system initiates all routes marked with any intermediate states. For example, if a document has a _Planned_ state changed to _Released_ state, a route specified for the intermediate _Firm Planned_ state **will** be started.

- **User State**

When not blank, it specifies that the route will be started only when the final user state of the source document matches the specified user state. Contrary to system states, when changing this state, routes for the intermediate user states **are not** initiated.

- **Source Enterprise Company**

If left blank, the route will be valid for all enterprise companies. When not blank, the route will be run only for documents in the specified enterprise company.

- **Generation Procedure**

The procedure which will be used to generate the target document.

## Properties of a document generation procedure

Generation procedures are fixed procedures provided by the system. 

When defining a document route, the user is allowed to choose such a procedure from a fixed list.

Each generation procedure is defined in this documentation using the following attributes:

- **Procedure Code** - The unique procedure code used for identification purposes. It has the following structure:

   - **Subsystem Code**<br>
     3-5 characters which uniquely identify the sub-system of the source document.
     
   - **Module Code**<br>
     2 digits that uniquely identify the module within the sub-system of the source document.
      
   - **Procedure Code**<br>
     2 digits which specify the consecutive number of the procedure within the module

For example, ‘*CRM0103*’ specifies a procedure in the ‘CRM’ sub-system, 01-Sales module, procedure #3.

- **Name**<br>
Name of the generation procedure.

- **Obsolete**<br>
Specifies whether the generation procedure is still active in the latest version of the system.</br> Old generations are no-longer supported and are marked as ‘Obsolete’.

- **Source Document Entity Type**<br>
Specifies the entity type of the source document, which defines the general type of the document, for example *Sales Order*. The generation procedure can be used only for documents with specified entity type. There can be many user-defined *Document Types* within a single entity type.

- **Target Document Entity Type**<br>
The entity type of the target document. The generation procedure can generate only documents with a specified entity type. Each *Document Route* can specify different user-defined *Document Types* only within this specified type.

- **Description**<br>
Detailed description and business case when the generation procedure is used.

