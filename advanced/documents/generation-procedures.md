# Generation Procedures Overview


![Generation Procedures](generation-procedure.SVG)

Generation Procedures are automated procedures, which generate @Documents from other documents.
They are the basis for the @document-flow.
Generation Procedures are the arrows in the document flow diagrams.

## Setup

In order to start generating documents, the Generation Procedures need to be configured.
The configuration is performed in the Document Type entity, in the Document Type Routes child entity.

Each Document Type Route is a configuration for a single Generation Procedure.

# Generation Procedures Lifetime Stages

The current topic describes the stages of the lifetime of a generation procedure:

- NEW - in development, cannot be used
- ACTIVE - the generation could be actively used by the users
- AGEING - triggers a warning, can be silenced.
- OBSOLETE – triggers a warning e or an error and has to be replaced by an active generation procedure.

- DEAD – does not work, throws an error or is permanently deleted.

## Details 

When creating a **NEW** generation procedure if it replaces a generation procedure that is currently in use, the old generation is **marked as obsolete** and it enters the lifetime stage **AGEING**. In those cases, the **AGEING** generation procedures, which later become **OBSOLETE** have to be replaced with the **ACTIVE** procedures that have been released, because they maintain the contemporary business logic, methods of computing and have a better and faster performance. The transition does not have to be made immediately after the release of the new version but it has to be performed before the generation procedure enters the stage **DEAD** i.e. before its **Date of Suspension.**

For every Generation Procedure that is marked as an Obsolete is scheduled a **Date of Suspension on** which date the Generation Procedure will be discontinued and could no longer be used.** The date is added in the obsolete procedure's name e.g. "To be deleted: 9.2021". As a result of this date, are defined three periods in which the software will inform users accordingly:

1. **AGEING** - From ([**Date of Suspension**] - 3 years) to (**Date of Suspension**] - 1 year) – a pop-up (balloon) message will be displayed informing the user that it is using an obsolete generation. These messages’ only purpose is to inform the users and they won’t interrupt/stop their operating with the system. The messages will be logged into the Information Messages navigator. The messages will stop popping up if for the particular line of the Document Type's Routes the filed "Allow Obsolete Generation" is check-marked.

2. **OBSOLETE** - From ([**Date of Suspension**] - 1 year) to ([**Date of Suspension**])

- If the filed "Allow Obsolete Generation" is NOT check-marked - an error in a modal window will pop up during the execution of the obsolete generation procedure. The error will inform the users that they are using an obsolete procedure and **the generation of the sub-document will be interrupted**. The error **will stop popping** up if for the particular line of the Document Type’s Routes the filed "Allow Obsolete Generation" is check-marked.

- If the filed "Allow Obsolete Generation" IS check-marked - a pop-up (balloon) message will be displayed informing the user that it is using an obsolete generation. These messages' only purpose is to inform the users and they won’t interrupt/stop their operating with the system. The messages will be logged into the Information Messages navigator. While using this generation, the popping up of this message could **no longer be avoided**.

3. **DEAD** - From [**Date of Suspension**] onwards - generation ceases to operate and enters the the lifetime stage **DEAD.** <br> **An error that can not be avoided will be thrown.**

With the release of the new main version after the Date of Suspension, the obsolete generation procedure is **to be deleted** and it will no longer appear in the drop-down lists.

# Metrics

Sometimes, when creating a new child/sub document by a generation procedure, some of the values of the child fields are not just copied from the parent document but need to be calculated. **The Metrics** are used when the calculation is based on the data about the unfulfilled quantities and amounts by the child documents that have already been created. It usually applies when the parent value has to be fully exhausted by its child values. **Metrics** bring the information which values have to be compared, how and whether the remaining result (if different from zero) has to lead to the creation of a new document or not. Each comparison is a separate metric.

#### Example:



**If we have the information about two metrics with the following description:**

| Fulfillment Name                     | Metric Name           | Measurement Unit                           | Parent Value                        | Child Value                          | New Record |
| :----------------------------------- | :-------------------- | :----------------------------------------- | :---------------------------------- | :----------------------------------- | :--------- |
| StoreOrderLineToStoreTransactionLine | MStandardQuantityBase | StoreOrderLine.Product.BaseMeasurementUnit | StoreOrderLine.StandardQuantityBase | TransactionLine.StandardQuantityBase | YES        |
| StoreOrderLineToStoreTransactionLine | MQuantityBase         | StoreOrderLine.Product.BaseMeasurementUnit | StoreOrderLine.QuantityBase         | TransactionLine.QuantityBase         | NO         |

 **And we know that:**

TransactionLine.StandardQuantityBase = StoreOrderLine.REMAINING(StandardQuantityBase) 

TransactionLine.QuantityBase = StoreOrderLine.REMAINING(QuantityBase)

, where:

- "TransactionLine.StandardQuantityBase" and "TransactionLine.QuantityBase" are the ordered by the parent line quantity values;
- "StoreOrderLine.REMAINING(StandardQuantityBase)" and "StoreOrderLine.REMAINING(QuantityBase)" are the ordered quantities which are not yet fullfilled by subdocumets i.e. (**TransactionLine.StandardQuantityBase - SUM(Child.StoreOrderLine.StandardQuantityBase) and (TransactionLine.QuantityBase - SUM(Child.StoreOrderLine.QuantityBase).**

**Then if we have the following documents:**

Parent.StoreOrderLine  - StandardQuantityBase = **10.00 PCS**, QuantityBase = **10.00 PCS**

Child.TransactionLine1  - StandardQuantityBase = **4.00 PCS**, QuantityBase = **4.00 PCS**

**And we are creating a new Child.TransactionLine2 by a generation procedure from the same parent, then the procedure will create:**

Child.TransactionLine2  - StandardQuantityBase = REMAINING(Quantity) = (10.00 PCS - 4.00 PCS) = **6.00 PCS**, QuantityBase = REMAINING(QuantityBase) = (10.00 PCS - 4.00 PCS) = **6.00 PCS**



## New Record

The last column of the metrics table is called "New Record". This column determines whether a new record must be created if the REMAINING() value of the metric is if different from zero. 

Let's imagine that in the previous example:

Child.TransactionLine1 - StandardQuantityBase = **10.00 PCS**, QuantityBase = **4.00 PCS**

This may be the case if the product in the line is using todo:(Variable(Dynamic)MeasurmentRatios). Then the Child.QuantityBase may be bellow or to exceed the QuantityBase ordered by parent document (i.e. REMAINING(QuantityBase) will be different from zero). But we can see that in the table above for the metric MQuantityBase is set "New Record = NO". Which means that in this situation, when the generation procedure is executed - a new record "Child.TransactionLine2" for remaining **6.00 PCS** of QuantityBase **WON'T** be created.



# Standard Document Attributes



The current article describes standard attributes from the Documents table when a document is created through generation procedure. When the described attributes are not mentioned in a generation procedure, they are filled as follows (* the sub-document is referred as "*sub*"):

- at first, the document route sets the following:

         sub.DocumentType = SubDocumentsType; <br>
         sub.EnterpriseCompany = SubDocumentsEnterpriseCompany; <br>
         sub.EnterpriseCompanyLocation = SubDocumentsEnterpriseCompanyLocation; <br>
         sub.ReadOnly = SubDocumentsReadOnly; <br>
         sub.ParentDocumentRelationshipType = RelationshipType; <br>
         sub.Parent = ParentDocument;

- and then, setting the value in the sub.ParentDocument attribute rises the event of filling in the MasterDocument. This is processed as follows (not the sub-document is current document, so we refer it as "*this*" and the parent document is "*Parent*"):

           this.MasterDocument = Parent.MasterDocument;

- and at the end the following attributes are filled in like: <br>
 //set optional attributes if not already set 
 
           if (this.EnterpriseCompany == null) <br>
             this.EnterpriseCompany = Parent.EnterpriseCompany; 
   
           if (this.EnterpriseCompanyLocation == null) <br>
             this.EnterpriseCompanyLocation = Parent.EnterpriseCompanyLocation; 
   
           if (this.CurrencyDirectory == null) <br>
             this.CurrencyDirectory = Parent.CurrencyDirectory; 
   
           if (this.DocumentNotes == null) <br>
             this.DocumentNotes = Parent.DocumentNotes;
   
           if (this.FromCompanyDivision == null) <br>
             this.FromCompanyDivision = Parent.FromCompanyDivision; 
   
           if (this.ToCompanyDivision == null) <br>
             this.ToCompanyDivision = Parent.ToCompanyDivision; 
   
           if (this.FromParty == null) <br>
             this.FromParty = Parent.FromParty; 
   
           if (this.ToParty == null) <br>
             this.ToParty = Parent.ToParty; 
   
           if (this.ReferenceDate == null) <br>
             this.ReferenceDate = Parent.ReferenceDate;
   
           if (this.ResponsiblePerson == null) <br>
             this.ResponsiblePerson = Parent.ResponsiblePerson; 
   
           if (this.ParentDocumentRelationshipType == null) <br>
             this.ParentDocumentRelationshipType = General.ParentDocumentRelationshipType.Subtask;
