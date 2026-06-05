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

A job is picked up by the automatic scheduler only when both of the following are true in its definition:

- The *Is Active* option is enabled.
- The *Schedule* is set to *Night*.

> [!NOTE]
> 
> The *Run On Idle* option does **not** decide whether a job is scheduled. It only controls how the job reacts when the server is busy (see [Server session limit](#server-session-limit) below). A job with *Schedule = Night* still runs at night even when *Run On Idle* is off, regardless of the session count.

### Idle period gate

The scheduler runs on a timer that fires roughly every 60 seconds. On each tick it starts the job procedure only when **all** of the following are met:

- The time of day is within the idle period - between **22:00 and 05:00** (start 22:00, duration 7 hours).
- The **System Jobs** procedure is **not** already running.
- The last time the job procedure completed is **more** than 30 minutes ago.

When these conditions are met, the scheduler starts a special long-running procedure called **System Jobs**, which can be monitored like any other long-running procedure in the **Procedures** navigator in @@name.

### Building the job list

After the procedure starts, it builds the list of pending jobs. Jobs are processed only when the system is the **primary** instance and is in **production** mode; otherwise an information message is logged and no jobs run.

The list contains the jobs that are *Active* and have *Schedule = Night*.

### Server session limit

Before queueing the jobs, the scheduler checks the number of active non-system server sessions:

- If there are **5 or more** active non-system sessions, the jobs flagged *Run On Idle* are removed from the list and an information message is logged. Jobs that are *Night*-scheduled but not *Run On Idle* still run.
- This session check can be disabled by setting **/JobsManager/IgnoreSessionsForIdleSchedule** to `1`. See the [Config Options Reference](../../reference/config-options-reference.md). When disabled, *Run On Idle* jobs run regardless of the session count.

### Executing the jobs

The collected jobs are executed **sequentially**. For each job:

- **One job at a time.** If another job is already running (for example a manually started one), the idle procedure stops with a message and the remaining jobs are skipped.
- **Skip if already done in this idle period.** A job is skipped if it has already completed successfully in the current idle period - that is, it is marked completed, was not cancelled, and less than 7 hours have passed since it completed.
- **5-minute run limit.** Each job run is cancelled after 5 minutes. If a job is cancelled by this timeout before finishing, it is re-queued and retried later in the same procedure run.
- **30-minute procedure cap.** The whole procedure runs for at most 30 minutes total (across all jobs, not per job). When this limit is reached, the remaining and unfinished jobs are deferred and continue in the next idle period.

If a job still has records to process after the 30-minute window elapses, it resumes on the next idle period (effectively the next night). 

## Manual job execution

Each job could be started manually. 

This way, its execution begins **immediately**, without the need to wait for the next on-idle iteration.

**There are a few important things to keep in mind when executing a job manually:**

- The same job **can't** be executed more than once simultaneously (e.g., "in parallel").
- A manual run has **no** time limit. Unlike the idle run, it is not cancelled after 5 minutes; it runs until it finishes or is stopped manually.
- The idle job execution will **discard** its queue if a manual job is running.
- A job execution **won't** start if the *Is Active* option is disabled in its definition.

## Execution log

Each job execution is logged in **Information Messages**. The log contains information about the starting time, ending time, the processed records, and errors that have occurred during the processing.

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

## Failure log

Each job failure is logged in **Information Messages**. The log contains the reason for the job failure.

**Example:**

Process: *Job J30903 Delete Print Images*

Message

```
There is a running job. This job execution can't continue and will be skipped.
```

----------------
### See more

[!list items=Jobs limit=100 default-text="None"]
