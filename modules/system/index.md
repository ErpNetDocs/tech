# System

The **System** module forms the foundational infrastructure of @@name. It provides the core services for configuration, internal system data, document lifecycle control, data exchange, technical monitoring, business automation, and security. 

These services support and protect all functional modules by supplying configuration options, internal jobs and queues, document metadata, integration endpoints, audit information, and centralized access control.

![pictures](pictures/system_overview.png)

## Structure

System functionality is organized into several submodules, each focused on a specific technical area.

They enable customization, secure access control, integration with external systems, and continuous operation and monitoring in @@name.

| Submodule                | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Automation**           | Provides user-driven business automation. Contains calculated attributes, stored attributes and their categories, user business rules (events, conditions, actions), and process diagrams. Used to extend entity data, define read-only calculated values, and implement rule-based automation without changing application code.                                                                                                          |
| **Configuration**        | Holds global configuration and runtime infrastructure settings. Includes hierarchical configuration options, system jobs, UI and message translations, webhook templates, as well as web hosts and web sites used to host @@name.                                                                                                                                                                                                          |
| **Internal system data** | Stores internal technical data produced and used by the platform. Includes user-defined default values for forms, document jobs, document print images, document versions, instance change requests, notifications, object changesets and changes, object files, and generic object records with versioning.                                                                                                                               |
| **Document flow**        | Defines the structural and behavioral metadata for documents across @@name. Manages document party roles, printout layouts, user-defined data sources (queries), document amount types with dependencies and settings, document types (including statuses, routes, and security conditions), and sequences with their generators for document numbering.                                                                                   |
| **Exchange**             | Describes data exchange operations (import, export, and similar) together with their related objects. Used to track what is exchanged, the transfer status, and other technical details for integration scenarios.                                                                                                                                                                                                                         |
| **Monitoring**           | Provides views and definitions for technical and operational monitoring. Covers audit log entries, information messages, instance statistics and parameters, resolved conflicts, scheduled document events, update procedure executions, procedures, process information, sessions, user presence, application performance, execution statistics, database object information, wait statistics, print images, object files, and web sites. |
| **Security**             | Implements identity and access control across @@name. Manages groups and users (with roles, provider tokens, and provider logins), domains, entities with secured access, and user roles. Also includes access keys, access tokens, system permissions, column permissions, visual permissions, trusted applications (with authorizations), and external applications, forming the complete permission and authorization model.            |

> [!NOTE]
>
> The screenshot taken for this article is from v.26 of the platform.
