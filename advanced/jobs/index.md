# Jobs

Jobs is a system in @@name that runs processes such as document state changing, executing scheduled events, deleting old notifications, print images, and others. Running can be done both **manually** and **automatically** - in non-busy hours, without requiring any user interaction.

## Create and configure a job

For a start, you have to create a new record with a desired job type in the **Job** navigator.

Most job parameters have a default value and can operate without additional adjustments.

An example is **[J30903 Document print images - Delete old document print images](https://docs.erp.net/tech/advanced/jobs/J30903.html)**. <br> It has only one parameter - the *Print Images Retention Months* field in the enterprise company's definition, with a default value of '60 months'.

However, there are jobs performing more complicated processes that shouldn't be executed for all records in the database. They require additional settings. An example is the **[Document state change](https://docs.erp.net/tech/advanced/jobs/J30777.html)** job. 

The parameters and settings for each job are described in its documentation.

## Job scheduling

Jobs can be started **automatically** by an execution system, following a predefined schedule.

> [!NOTE]
> 
> Idle jobs are started in non-busy hours, subject to availability of resources.
> A job uses the **on-idle** auto-start schedule only when the *Is Active* and *Run On Idle* options are activated in its definition.

**The jobs execution system works only when the following requirements are met:**

- The time of day is between 22:00 and 03:00.
- The current server sessions are **fewer** than 5.
- The last time the job's procedure was completed is **more** than 30 minutes from now.
- The procedure is **not** currently working.
- There are **no** manually started jobs currently running.

If these conditions are met, the execution system initiates a special long-running procedure called **System Jobs**, which can be monitored like any other long-running procedure in the **Procedures** navigator in @@name, or the *Procedures* tab in the **Server Manager**.

The jobs execution system will then create a list of pending jobs and will start executing them sequentially. The list is made on the basis of active jobs defined in the databases

Each job can run a maximum of 5 minutes before it's cancelled by the job runner. Jobs can actually execute up to six 5-minute runs, or 30 minutes, until they break the existing loop of pending jobs.

If a job is interrupted before its work is finished, it must be started again during the 30-minute period. <br> If there are more records that need to be processed after the 30-minute window has elapsed, the job will start again on the next day. 

## Manual job execution

Each job could be started manually. 

This way, its execution begins **immediately**, without the need to wait for the next on-idle iteration.

**There are a few important things to keep in mind when executing a job manually:**

- The same job **can't** be executed more than once simultaneously (e.g. "in parallel").
- The jobs execution system will **discard** its job's queue if there's a manual job execution running.
- A job execution **won't** start if the *Is Active* option is disabled in its definition.

## Execution log

Each job execution is logged in **Information Messages**. The log contains information about the starting time, ending time, the processed records and errors that have occurred during the processing.

**Example:**

Process: *Job J30777 Finish Store Transactions*

Message

```
Succeeded: 259; Failed: 0
LOG:
[10:00:10] Total: 259
[10:04:42] Succeeded: 259
[10:04:42] Failed: 0
```
----------------
### See more

[!list items=Operators limit=100 default-text="None"]

