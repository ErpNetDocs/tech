---
uid: jobs-J30903
---

# J30903 Document Print Images - Deletе Old Document Print Images

| Code                  | J30903                                                       |
| :-------------------- | ------------------------------------------------------------ |
| Entity                | DocumentPrintImages                                          |
| Job Type Name         | Deletе Old Document Print Images                             |
| Parameters            | DocumentPrintImage.DocumentPrints.Document.EnterpriseCompany.PrintImagesRetentionMonths |
| Description           | The system job deletes all old Document Print Images, whose retention period has expired. <br> A retention period is considered as expired when the period between the Print Time of the Document Print Image and today is larger than the period set in the "Print Images Retention Months" field Enterprise Company's definition. <br> The default value for the "Print Images Retention Months" field is 60 months but this period can be adjusted according to the particular company's needs. |
| First to Process      | DocumentPrintImage.DocumentPrints.PrintTime (ASC)            |
| Records per Iteration | 1000                                                         |
| Version               | Introduced: 2020.1                                           |

> [!Note]
> The job will NOT delete the information from the Document Prints panel/table. The information about when and by whom the document has been printed will continue to be available. The job deletes only the Document Print Image aka the visual representation of the document that has been printed.

**For more information about the Jobs Documentation Template and a short explanation of each column, see topic** [Jobs Template](~/templates/template-description-jobs.md).
