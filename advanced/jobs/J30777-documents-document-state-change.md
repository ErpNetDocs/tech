---
uid: jobs-J30777
---

# J30777 Documents - Document State Change

| Code                  | J30777                                                       |
| :-------------------- | ------------------------------------------------------------ |
| Entity                | Documents                                                    |
| Job Type Name         | Document State Change                                        |
| Parameters            | Job.DocumentJob.Condition// Note that in 2020.1 in the condition can be used only the fields from the Documents table. |
| Description           | The Document State Change job is used to change the state of the desired set of documents. For each Job of this type must be created a record in Document Jobs! This record contains information about the State which has to be set, the new User State (optional), and the Conditions which define the set of documents that are going to be processed. |
| First to Process      | -                                                            |
| Records per Iteration | 1                                                            |
| Version               | 2020.1                                                       |

**IMPORTANT NOTES** about the configurations in Document Jobs:

-  The 'Document Type' field is NOT a filter for the job. If you set a specific Document Type it does not mean that the job will be executed only for documents with this Document Type or even Entity. The only filters which are evaluated to determine the processed documents are the filters in the 'Conditions' field.
-  The 'Conditions' field is the only field that is taken into account to determine which Documents will be processed. <br>
If there are NO conditions, the system will try to process all documents into the database!
-  In 'Conditions' we have to choose and specify the right **combination** of criteria which will filter the desired set of documents among all documents in the system.
<br>Commonly used filters would be:
           
    - Document.Void = false - the job will exclude voided documents.
    - Document.Entity Name - the job will be executed for all documents of this Entity e.g. 'Sales Orders'.
    - Document.Document Type - the job will be executed for all documents of this Document Type/s.
    - Document.State - the job will be executed for all documents with this Document State.
    - Document.User State - the job will be executed for all documents with this User State.
    - Document.Document Date >= and Document.Document Date >= - the job will be executed for all documents with Document Date in this period.
- Currently, the only 'Conditions' which are taken into account are the filters from the 'Document' panel.

**For more information about the Jobs Documentation Template and a short explanation of each column, see topic** [Jobs Template](~/templates/template-description-jobs.md).
