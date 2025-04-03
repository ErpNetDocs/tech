# Sync jobs

Sync Jobs are at the heart of MSSync, enabling you to automatically keep your Microsoft 365 resources in sync with @@name. These jobs are responsible for handling different types of data, ensuring everything stays aligned across both platforms.

## What is a Sync Job?

A Sync Job is a core functionality within MSSync that handles the synchronization of specific types of data between Microsoft 365 and @@name.

Each sync job is responsible for a different category of data, ensuring that information in both systems remains consistent and up-to-date.

For example, the **[Calendar Sync Job](calendar.md)** will synchronize calendar events from Microsoft 365 into corresponding [activities](https://docs.erp.net/model/entities/General.Activities.Activities.html) in @@name, while the **[Mail Sync Job]** ensures that emails sent or received through Microsoft 365 are transferred into @@name.

Sync jobs operate automatically once configured, keeping both systems in sync without requiring manual updates.

## Important considerations

Each sync job in MSSync comes with its own set of requirements and conditions that must be met for it to function correctly. These considerations can include permissions, system settings, and configurations that are essential to ensure smooth synchronization between Microsoft 365 and @@name.

All relevant details and setup instructions are provided on the respective pages for each sync job, guiding you through the specific steps needed for proper configuration.

## Sync job types

[!list limit=1000 erp.type=syncjob erp.topic=mssync default-text="None"]