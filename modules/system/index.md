# System

The **System** module forms the foundational infrastructure of @@name. It provides the core services for configuration, internal system data, document lifecycle control, data exchange, technical monitoring, business automation, and security. 

These services support and protect all functional modules by supplying configuration options, internal jobs and queues, document metadata, integration endpoints, audit information, and centralized access control.

![pictures](pictures/system_overview.png)

## Structure

System functionality is organized into several **submodules**, each focused on a specific technical area.

They enable customization, secure access control, integration with external systems, and continuous operation and monitoring in @@name.

| Submodule                | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Automation**           | Provides user-driven business automation. It contains **[calculated attributes](https://docs.erp.net/tech/advanced/calculated-attributes/index.html?q=calculated%20attributes)**, **stored attributes** and their **categories**, **[user business rules](https://docs.erp.net/tech/advanced/user-business-rules/index.html)** (events, conditions, actions), and **process diagrams**. Used to extend entity data, define read-only calculated values, and implement rule-based automation without changing application code.                                                                                                          |
| **Configuration**        | Holds global configuration and runtime infrastructure settings. It includes hierarchical **[configuration options](https://docs.erp.net/tech/reference/config-options-reference.html?q=config)**, **[system jobs](https://docs.erp.net/tech/advanced/jobs/index.html?q=jobs)**, **[UI translations](https://docs.erp.net/tech/concepts/multi-language.html?q=translation)**, **[webhook templates](https://docs.erp.net/tech/advanced/user-business-rules/action-types/webhook.html?q=web%20hosts)**, as well as **web hosts** and **web sites** that can be hosted.                                                                                                                                                                                                          |
| **Internal system data** | Stores **internal system data produced and used across @@name**. It includes user-defined default values for columns, document jobs, document print images, document versions, instance change requests, notifications, object changesets and changes, object files, and generic object records with versioning. It also allows for the creation and management of reports.                                                                                                                               |
| **Document flow**        | Defines the structural and behavioral metadata for documents across @@name. It manages **document party roles**, **printout layouts**, user-defined **data sources** (queries), **[document amount types](https://docs.erp.net/tech/advanced/document-amounts/index.html?q=amount%20type)**, **[document types](https://docs.erp.net/tech/advanced/document-flow/generation.html)**, and **sequences**.                                                                                   |
| **Exchange**             | Describes **data exchange operations** (import, export, and similar) together with their related objects.                                                                                                                                                                                                                        |
| **Monitoring**           | Provides various dynamic views and definitions for technical and operational monitoring. Its reach includes but is not limited to **audit log entries**, **information messages**, **instance statistics**, **resolved conflicts**, **[scheduled document events](https://docs.erp.net/tech/advanced/concepts/scheduled-document-events/index.html?q=document%20event)**, and **update procedure executes**. |
| **[Security](https://docs.erp.net/tech/modules/system/security/index.html)**             | Implements identity and access control across @@name. Manages groups and users (with roles, provider tokens, and provider logins), domains, entities with secured access, and user roles.          |

> [!NOTE]
>
> The screenshot taken for this article is from v.26 of the platform.
