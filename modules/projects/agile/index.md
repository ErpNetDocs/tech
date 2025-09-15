---
uid: agile
---

# Agile PM

The **Agile Project Management** (Agile PM) module in @@name enables organizations to manage projects in a flexible, iterative, and feedback-driven way — fully aligned with the principles of agile methodologies.

Unlike traditional Waterfall models, Agile PM supports continuous delivery and adaptive planning, making it ideal for dynamic environments such as software development, marketing, finance, and internal process optimization.

What sets **Agile PM** in @@name apart from general-purpose project management tools is its **native integration with the ERP.net platform** — providing direct access to enterprise data, built-in collaboration via Social Groups, and consistent logic, UI, and controls shared across the entire ERP.net system.
All activities are performed within a single, secure system, without the need to switch platforms or integrate third-party tools — ensuring consistent governance, traceability, and compliance across the organization.


## Core structures

At its core, the module introduces configurable structures to reflect business logic and internal workflows:

- [Projects](configuration-and-structure/project-definitions/projects.md) define agile work initiatives by grouping related cases, areas, milestones, sprints, and configurations within a common execution context.
- [Project Groups](configuration-and-structure/project-definitions/project-groups.md) enable logical grouping of projects that share common configurations such as areas and milestones.
- [Project Types](configuration-and-structure/main-setup/project-types.md) help classify projects.
- [Project Areas](configuration-and-structure/project-definitions/project-areas.md) divide work into manageable domains.
- [Project Milestones](configuration-and-structure/project-definitions/project-milestones.md) highlight key delivery points along the project timeline.
- [Sprints](configuration-and-structure/project-definitions/sprints.md) represent fixed timeboxes (typically 1–4 weeks) during which a team works to complete a set of cases toward a defined sprint goal.
- [Case Categories](configuration-and-structure/main-setup/case-categories.md) determine task structure and flow.
- [System States](cases/workflow-states.md#system-states) define the main workflow lifecycle of tasks.
- [User States](configuration-and-structure/main-setup/user-states.md) extend this lifecycle by adding more granular tracking within each system-defined stage.
- [Cases](cases/index.md) serve as the core work units, bringing together all these structures into actionable items that move through the project lifecycle.

## Key capabilities

- **Automated assignment logic** via configurable Assignment Rules, ensuring that each Case is routed to the most appropriate user based on project context, state, and role.
- **Work-in-progress (WIP) limits**, which help prevent overload and maintain a steady flow of work across critical workflow stages.
- **Time tracking tools**, allowing users to log time on work performed within Cases — ensuring reliable input for analysis and planning.
- **Progress and workload monitoring**, based on workflow states and activity logs (case developments), helping teams and managers track task movement, detect delays, and identify bottlenecks.
- **Hierarchical case structuring**, enabling teams to break down the work within a project into traceable, manageable units using parent-child relationships.
- **Integrated collaboration features**, including Social Group associations, internal discussions, activity logs, and smart notifications — all embedded directly into the Case form.
- **Project-based access control**, ensuring users see and interact only with relevant projects and Cases, while maintaining strict security boundaries.

Together, these tools provide agile teams with structure, transparency, and flexibility — allowing them to deliver value continuously, adapt quickly, and scale their efforts confidently across the organization.

## Learn more about Agile PM here:
- [Configuration and structure](configuration-and-structure/index.md)
- [Cases](cases/index.md)
- [Advanced features](advanced-features/index.md)
- [Security](security.md)
