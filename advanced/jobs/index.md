# Jobs

*Jobs* is a system in @@name, which automatically runs processes. The types of processes, which can be run include document state changing, executing scheduled events, deleting old notifications or print images, or similar. The jobs could run both manually and automatically- in non-busy hours without requiring any user interaction.

## How to create and configure a job

In most cases, in order to create a job, you have to simply create a new record with the desired job type in the *Job* navigator.

Most parameters of the jobs have a default value and can operate without additional adjustments.
An example is the [J30903 Document print images - Delete old document print images](./J30903.md) job, that has only one parameter - *Print Images Retention Months* field Enterprise Company's definition, having a default value of "60 months".

However, there are jobs that are performing more complicated processes and is not logical to be executed for all records in the database.
They require configuring additional settings. Such an example is **Document state change job**. 

The parameters and therefore the required settings of each job are described in its documentation.

## Job scheduling

Jobs can be started automatically by the jobs execution system following a predefined schedule.

> [!note]
> On idle jobs will be started in non-busy hours, subject upon availability of resources.
> A job is using the *On Idle* auto-start schedule only when the `Is Active` and `Run On Idle` options are activated in its definition.

**The jobs execution system will be started only if the following requirements are met:**

- The time of the day is between 22:00 and 03:00.
- The current server sessions are less than 5.
- The last time the job's procedure is completed is more than 12 hours from now.
- The procedure is not currently working
- There is no manually started jobs that are currently running

Then the conditions described above are met and then the jobs execution system will start a special long-running procedure called 'System Jobs'.
The procedure can be monitored as every other long-running procedure in procedures navigator in @@name or the procedures tab in the server manager.

The jobs execution system will create a list of pending jobs and will start executing them sequentially.
The list is made on the base of the active jobs defined in the databases.
Each job runs a maximum of 5 minutes and then it is cancelled by the job runner.
Every job can run up to 30 minutes which make a total of 6 times X 5 minutes runs, then it breaks the loop of pending jobs.
If the job is interrupted before it's work is finished it must be started again during the 30 minutes period.
If there are more records that have to be processed after the 30 minutes have elapsed, the job will start again on the next day. 

## Manual job execution

Each job could be started also manually. This way its execution starts immediately without the need to wait for the next on idle iteration.

**There are a few important notes to keep in mind when executing a job manually:**

- The same job can't be executed more than once simultaneously (e.g. "in parallel").
- The jobs execution system will discard its job's queue if there is a manual job execution running.
- A job execution won't start if the `Is Active` option is disabled in its definition.

## Execution log

Each job execution is logged in *Information Messages*.
The log contains information about the starting time, ending time, the processed records and the errors that have occurred during the processing (if possible and if any).

Example:

**Process:** *Job J30777 Finish Store Transactions*

**Message:**

```
Succeeded: 259; Failed: 0
LOG:
[10:00:10] Total: 259
[10:04:42] Succeeded: 259
[10:04:42] Failed: 0
```

## Available jobs

[!list items=Jobs limit=100 default-text="None"]
