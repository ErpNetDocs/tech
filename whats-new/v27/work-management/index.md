# Work Management

## Notable features

## Other features

### 1. New rule for tracking key Case field changes

Changes to a Case’s **Title**, **Project**, **Project Area**, **Project Milestone**, and **Priority** are now automatically recorded in the **Developments** panel, making important updates easier to trace without using **Change History**.

For more information, see [R101753 - Case: Case Development Info On Key Field Changes](https://docs.erp.net/model/business-rules/R101753.html).

### 2. Tracking users who move Cases between system states

Cases now keep track of the user who moved them to each system state in their lifecycle.

Separate read-only fields record the user who changed the Case System State to BACKLOG, CONSIDER, READY, IN PROGRESS, WAITING, RESOLVED, and CLOSED.

Whenever the System State changes, the corresponding field is automatically updated with the current user. These values are maintained by the system and cannot be manually set, changed, or cleared.

This provides direct visibility into who moved a Case to each state and improves traceability throughout its lifecycle.

For more information, see [R101788 - Case: Set State Change User](https://docs.erp.net/model/business-rules/R101788.html)
