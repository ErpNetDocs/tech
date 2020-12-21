# Jobs

Jobs is a system in @@name, which automatically runs processes. The types of processes, which are run include document state changing, executing scheduled events, or similar. The jobs are run in non-busy hours without requiring any user interaction.

## How to Create and Configure a Job

In most cases, in order to create a job, you have to simply create a new record with the desired Job Type in the Job navigator.

Most parameters of the jobs have a default value and can operate without additional adjustments. An example is the todo:(J30903 DocumentPrintImages - Deletе Old Document Print Images)  jobs, which has only one parameter - "Print Images Retention Months" field Enterprise Company's definition, which has a default value of "60 months".

However, there are jobs that are jobs that are performing more complicated processes and is not logical to be executed for all records in the database. They require configuring additional settings. Such an example is **Document state change job**. 

The parameters and therefore the required settings of each job are described in its documentation.

## How to Run a Job

The jobs can be auto-started on a schedule or they can be run manually. 

### Manual Job Starting

Each job can be manually started through the Run Manually button available in the Job’s definition and the Jobs Navigator. When the job is started the system will display a Process Screen which will show the progress of the procedure. The Process Screen will also contain a Cancel button. The job will be running until all of the records are processed or until it is manually stopped.

> [!Note]
> When cancelled manually the job may not stop immediately. The job will stop right after the currently processed record is finished.

> [!Note] 
> **IMPORTANT:** In Version 2020.1 manual starting of a job is not available.

### Automatic Job Starting

Jobs can be started automatically by the jobs execution system following a predefined schedule.

Note that currently, only an "On Idle" auto-start schedule is available. Generally, the "On Idle" auto-start means that the job will be automatically started in non-busy hours if there are available resources. A job is using the "On Idle" auto-start schedule when the "Run On Idle" option is activated in its definition.

**The jobs execution system will be started only if the following requirements are met:**

- The time of the day is between 22:00 and 03:00.
- The current server sessions are less than 5.
- The last time the job's procedure is completed is more than 12 hours from now.
- The procedure is not currently working
- There is no manually stated jobs that are currently running

Then the conditions described above are met and then the jobs execution system will start a special long-running procedure called "System Jobs". The procedure can be monitored as every other long-running procedure in Procedures navigator in @@name or the Procedures tab in the Server Manager.

The jobs execution system will create a list of pending jobs and will start executing them sequentially. The list is made on the base of the active jobs defined in the databases. Each job runs a maximum of 5 minutes and then it is cancelled by the job runner. Every job can run up to 30 minutes which make a total of 6 times X 5 minutes runs, then it breaks the loop of pending jobs. If the job is interrupted before it's work is finished it must be started again during the 30 minutes period. If there are more records that have to be processed after the 30 minutes have elapsed, the job will start again on the next day. 

## Where is the log?

Each job execution is logged in Information Messages. The log contains information about the starting time, ending time, the processed records and the errors that have occurred during the processing (if possible and if any).

Example:

**Process:** *Job J30777 Finish Store Transactions*

**Message:**

*Succeeded: 259; Failed: 0 <br>
LOG: <br>
[10:00:10] Total: 259 <br>
[10:04:42] Succeeded: 259 <br>
[10:04:42] Failed: 0*

The table columns and content are explained in [Jobs Tamplate](https://github.com/ErpNetDocs/model/blob/master/templates/template-description-jobs.md)

Available jobs:

- [J30632 Notifications - Delete Old Notifications](https://github.com/ErpNetDocs/model/blob/master/jobs/J30632-notifications-delete-old-notifications.md)
- [J30724 Scheduled Document Events - Run Scheduled Events.md](https://github.com/ErpNetDocs/model/blob/master/jobs/J30724-scheduled-document-events-run%20scheduled-events.md)
- [J30777 Documents - Document State Change](https://github.com/ErpNetDocs/model/edit/master/jobs/J30777-documents-document-state-change.md)


