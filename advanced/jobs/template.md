---
uid: template-description-jobs
---

# Jobs documentation template 

Each job has a documentation topic that includes a standardized table containing detailed information about it. This table allows you to organize data in a structured way and helps you quickly navigate through the info.

### The table columns and content explained

| **Template Column Name** | **Template column description**                              |
| :----------------------- | ------------------------------------------------------------ |
| Code                     | Unique job code. Always starts with 'J' and continues with a digit number. |
| Entity                   | The entity records processed by the job.     |
| Job type name            | Unique job type name.                                        |
| Parameters               | Field values (conditions) determining the entity records which will be processed by the job. |
| Description              | An explanation of what the job does.                |
| First to process         | Specifies the condition/s by which the job determines which records will be processed first. |
| Automatically created | Shows whether the job is created and activated automatically into the databases or not.<br> Possible values are YES and NO.|
| Version                  | A list of all versions in which the job has been changed. It usually contains two types of records: 'Introduced: 2xxx.x' - the version since which the job type has been **available**; <br> 'Updated: 2xxx.x ' - the version in which the job has been **changed** (including description of the changes). There could be neither no records nor multiple records of this type. |
