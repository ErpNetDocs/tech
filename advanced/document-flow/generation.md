# Document generation

Document generation is a key part of the **[document flow](index.md)** as it's not only used to automate it, but to provide the automatic generation of inheriting documents from a parent document.

Generation is a special case of direct **[order fulfillment](fulfillment.md)** when there's only one source document. 

It creates a single target but can often make multiple documents. When many instances are generated, it's because of different values of some key attribute(s) in the different lines of the source document.

## Automating the document generation

Having just a single document as a source allows for easy document generation. One instance can create multiple and different types of target documents under different conditions and events.

The definition of a document type includes a special sub-entity type called **[workflow routes](xref:Systems.Workflow.Routes)**. 

These routes specify procedures, conditions and events for the automatic generation of inheriting documents. 

Each document type can host **many** workflow routes. They start automatically or require user initiation.

Together, the routes of different document types form a general network graph called **document flow**.

## Properties of a document generation route

Each document generation route contains the following properties:

- **Generation events**

Events that trigger the document route. The most used event usually changes the **[document state](~/concepts/documents/states.md)**.

- **State**

The system state of the source document which will trigger the workflow route. 

When you change a state, the system initiates all routes marked with **intermediate** states. If a document has a 'Planned' state changed to 'Released', a route specified for the intermediate 'Firm Planned' state will be started.

- **User state**

When not blank, it specifies that the workflow route will be started only when the final user state of the source document matches the specified user state. Contrary to system states, when changing this state, routes for the intermediate user states are **not** initiated.

- **Source enterprise company**

If left blank, the route will be valid for **all** enterprise companies. 

When not blank, it'll be run only for documents in a specified enterprise company.

- **Generation procedure**

The procedure which will be used to **[generate](generation-procedures.md)** a target document.

## Properties of a document generation procedure

Generation procedures are fixed procedures provided by the system. 

When defining a document route, you can choose one from a list.

Each generation procedure is defined using the following attributes:

- **Procedure code** - A unique procedure code used for identification purposes. It has the following structure:

   - **Subsystem code**<br>
     3-5 characters which uniquely identify the sub-system of the source document.
     
   - **Module code**<br>
     2 digits that uniquely identify the module within the sub-system of the source document.
      
   - **Procedure code**<br>
     2 digits which specify the consecutive number of the procedure within the module.

For example, ‘CRM0103’ specifies a procedure in the **[CRM](~/modules/crm/index.md)** sub-system, 01-Sales module, procedure #3.

- **Name**<br>

Name of a generation procedure.

- **Obsolete**<br>

Specifies whether a generation procedure is still active in the latest version of the system.</br> Old generations are no longer supported and are marked as ‘Obsolete’.

- **Source document entity type**<br>

Specifies the entity type of a source document, which defines the general type of the document (e.g sales order). The generation procedure can be used only for documents with specified entity type. There can be many user-defined document types within a single entity type.

- **Target document entity type**<br>

The entity type of a target document. A generation procedure only generates documents with specified entity type. Each document type can specify different user-defined document types only within this specified type.

- **Description**<br>

Detailed description and business case when a generation procedure is used.

