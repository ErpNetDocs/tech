---
uid: projects
---

## Projects

A **Project** in **Agile PM** represents a business initiative with a defined goal – such as delivering a product, providing a service, or executing an internal improvement.  
Projects can be client-facing or internal, and they structure the work, timeline, people, and deliverables related to the initiative.

A Project can only be created if [Project Types](../main-setup/project-types.md) have already been defined.  
Each Project belongs to exactly one Project Type.

> [!Note]
> The layout of the Project form may vary depending on the selected Project Type.  
> This allows each Project to display only the fields and panels relevant to its type.  
>  
*For examples of real-world Projects and their types, see [Project Types](../main-setup/project-types.md).

![Projects](pictures/projects.png)


### Responsibility and collaboration settings

Each Project must have a designated **Owner** — the person responsible for its execution and coordination.

**Configuration path:** *Project definition → Basic panel → Owner field*  
*Display panel name:* `Basic`<br>
*System panel name:* `Project`<br>
*Display field name:* `Owner`<br>
*System field name:* `Primary User`

![Project Basic](pictures/project-basic.png)

If the Project is initiated by or serves an external party, a **Customer** can also be specified.  
However, for internal initiatives, this field may remain empty.

Optionally, a **Social Group** may be assigned to the Project.  
This group represents the team or department involved in the discussions and decision-making related to the Project.

**Configuration path:**  
*Project definition → Advanced panel → Customer and Social Group fields*  
*Display panel name:* `Advanced`<br>
*System panel name:* `Project`

![Project Advanced](pictures/project-advanced.png)


## Association with Project Groups
Each Project can optionally be associated with a [Project Group](project-group.md), which enables multiple related projects to share common configurations such as [Project Areas](project-areas.md) and [Project Milestones](project-milestones.md).  
This allows organizations to avoid duplication and manage shared structures more efficiently across related initiatives.  

**For example**:
The **Marketing Projects** group may include projects such as **Website Redesign** and **Campaign Launch**, both benefiting from shared areas and milestones defined at the group level.  

**Configuration path:** *Project definition → Advanced panel → Project Group field*  
*Display panel name:* `Advanced`<br>
*System panel name:* `Project`<br>

![Project Group Association](pictures/group-association.png)


### WIP (work-in-progress) Limits

WIP Limits are an optional tool that restricts the number of Cases that are allowed to remain in specific workflow states within a Project.  
They are designed to prevent:

- Overloading teams or individual employees  
- Cases remaining too long in the same state without progressing

WIP Limits promote balanced work distribution and support more efficient progress by encouraging smart resource allocation.

A separate WIP limit can be defined for each of the following System States:  
**CONSIDER**, **READY**, **IN PROGRESS**

If a limit is exceeded, the system will block transitions to the respective state until the number of Cases in that state within the Case’s Project is reduced.

**Configuration path:** *Project Definition → WIP Limits panel → Consider, Ready, and In Progress fields*  
*Display panel name:* `WIP Limits`<br>
*System panel name:* `Project`<br>
*Display field name:* `Consider WIP Limit`, `Ready WIP Limit`, and `In Progress WIP Limit` fields <br>
*System field name:* `Consider WIP Limit`, `Ready WIP Limit`, and `In Progress WIP Limit` fields

![Project WIP Limits](pictures/project-wip.png)

