---
uid: template-description-jobs
---

# Jobs Documentation Template 

Each Job has a documentation topic, which includes a standardized table which contains detailed information about the job. The standardized table allows us to organize data in a structured way and helps the reader to quickly navigate through the info.

## The Table Columns and Content Explained

| **Template Column Name** | **Template Column Description**                              |
| :----------------------- | ------------------------------------------------------------ |
| Code                     | Unique job code. Always starts with "J" and continues with a digit number. |
| Entity                   | The entity which records are being processed by the job.     |
| Job Type Name            | Unique job type name.                                        |
| Parameters               | The fields used as parameters by the job. Their values serve as conditions in order to be determined the set of entity records that are going to be processed by the job. |
| Description              | An explanation of what the job actually does.                |
| First to Process         | Specifies the condition/s (if any) by which the job determines which records have to be processed first. |
| Records per Iteration    | The count of records that are included in a single iteration of the job.If we are cancelling a manually started job, the job will be aborted after the iteration is finished. |
| Version                  | A list with all versions in which the job has been somehow changed. Usually contains two types of records:"Introduced: 2xxx.x" - the version since which the job type is available;"Updated: 2xxx.x " - the version in which the job has been changed plus a short description of the changes. There could be non or multiple records of this type. |
