---
uid: generation-procedures-update
---

# Generation procedures

Generation procedures are automated procedures which generate documents from other documents.

They're the basis of the **[document flow](index.md)** and the arrows in the document flow diagrams.

## Setup

In order to start generating documents, the procedures need to be **configured**.

The configuration is performed in the document type routes child entity.

Each document type route is a configuration of a single generation procedure.

## Generation procedures lifetime stages

This is the lifetime of a generation procedure:

- **NEW** - in development, cannot be used.

- **ACTIVE** - could be actively used by users.

- **AGEING** - triggers a warning, can be silenced.

- **OBSOLETE** – triggers a warning or an error and has to be replaced by an active generation procedure.

- **DEAD** – does not work, throws an error, or is permanently deleted.

## Details 

When creating a **NEW** generation procedure, it may replace one that's currently in use. 

The older generation enters the **AGEING** lifetime stage. 

In this case, the **AGEING** generation procedures, which later becomes **OBSOLETE**, has to be replaced by an **ACTIVE** procedures that have been released, because they maintain the contemporary business logic, methods of computing and have better and faster performance. 

The transition doesn't need to be happen after the release of the new version, but it must be performed **before** the generation procedure enters the **DEAD** stage - before its date of suspension. This is the date on which an **OBSOLETE** generation procedure will be discontinued. 

It's added in the procedure's name like 'To be deleted: 9.2021'.

There are three time periods in which the software will inform users:

1. **AGEING** - From ([date of suspension] - 3 years) to (date of suspension] - 1 year)

A pop-up (balloon) message will display, saying that the generation is now **obsolete**. The purpose is to inform users so they don’t interrupt/stop their workings with the system. The message will be logged into the **Information Messages** navigator and will stop popping up if the field _Allow Obsolete Generation_ is check-marked for the particular line of the document type's routes.

2. **OBSOLETE** - From ([date of suspension] - 1 year) to ([date of suspension])

  - If _Allow Obsolete Generation_ is **NOT** check-marked, an error in a modal window will pop-up during the execution of the obsolete generation procedure. The error will inform users that they're using an obsolete procedure and the generation of the sub-document will be **interrupted**. The error stops popping up if _Allow Obsolete Generation_ is check-marked.

  - If _Allow Obsolete Generation_ **IS** check-marked, a pop-up message will be displayed saying that the generation is obsolete. The purpose of the message is the same as in the AGEING stage. Messages will be logged into the **Information Messages** navigator. While using this generation, popping up could **no longer** be avoided.

3. **DEAD** - From [date of suspension] onwards  
 
The generation ceases to operate and enters the **DEAD** lifetime stage.

An unavoidable error will be thrown.

With the release of a new main version after the date of suspension, the obsolete generation procedure is 'to be deleted' and it'll no longer appear in the drop-down lists.
