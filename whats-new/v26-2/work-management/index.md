# Work Management
The **Work Management** module centralizes the entire work lifecycle—from planning and assignment to tracking and completion—into one integrated system. It supports everything from simple To Dos to complex projects, tying together roles, resources, workflows, and time tracking with full traceability. Work Management also includes reporting, auditing, and AI-assisted training tools. It consists of four submodules: **Projects, AI Training, Classic Projects, and To Do**, all receiving major enhancements in v.26.2.

## Notable features

### 1. Project-based access control

Agile PM now supports project-level access control through **Access Keys**. This allows sensitive projects to be secured so that only authorized users and groups can access the project and work with the Cases associated with it.

Permissions are configured in the **Access Permissions** side panel of the project form and can control both general project actions (update, delete, administer) and specific Case state transitions. Access to Cases is also filtered by project access, so users without permission to the project's access key cannot see related Cases in the **Cases navigator** or in **Global Search**.

Key benefits include:

- restricted access to sensitive projects and their Cases;
- per-project control over who can change Cases to specific states;
- automatic filtering of inaccessible Cases from navigation and search results.

For more information, see [Security](/modules/work-management/agile/security.md).

## Other features

### 1. New rule for closing Cases

A Case can be set to CLOSED only if all related Tasks (To-Dos) are COMPLETED. If there are unfinished Tasks, the system will block the action and prompt the user to complete them first.<br>
This revocable rule helps prevent incomplete work and improves process consistency.

### 2. Notifications for favorite implicit Case followers

Users who follow with level **Favorite** at least one object referenced in a Case header, such as the **Project**, **Project Area**, **Project Milestone**, **Sprint**, **Stakeholder Party** and other referenced objects, can now receive notifications for that Case when **Case Development** records a creation, edit, assignment, or state change. The user who performs the action is excluded.

This helps users stay informed about important Cases related to the objects they are most interested in.

For more information, see [R39543 - Case Developments: Notify All Case Implicit Followers](https://docs.erp.net/model/business-rules/R39543.html).
