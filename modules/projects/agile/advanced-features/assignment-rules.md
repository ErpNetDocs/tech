---
uid: assignment-rules
---

## Assignment rules

Case assignments in **Agile PM** can be managed either **manually** or **automatically**. While manual assignment is always available, organizations can streamline their workflows by defining **Assignment Rules** — a flexible system for automatic case routing based on predefined criteria.


### Rule settings

Assignment Rules are configured in the **Agile PM → Setup → Assignment Rules** section.  

Each rule includes several key fields that define:

**Rule availability (activation conditions)**
These settings determine whether the rule is eligible for evaluation:

- **Is Active** – indicates whether the rule is currently enabled. Only active rules are considered by the system.

- **From Date / To Date** – optional start and end dates that define a period during which the rule is valid. Useful for setting temporary or seasonal rules.


**Rule trigger (matching conditions)**
These fields define when the rule is evaluated and executed:

- **Condition Fields** – the rule is triggered when one or more of these Case fields match the configured values:  
  *Project, Project Area, Project Milestone, Case Category, Stakeholder Party, System State, or User State.*

- **Priority** – defines the importance level of the rule. When multiple rules match, the one with the highest priority is applied.

- **Rule No.** – a unique sequence number used to determine precedence when more than one rule shares the highest priority.  
  The number is auto-generated but can be modified manually if needed.


**Assignment logic (execution behavior)**
This setting defines who the Case should be assigned to when the rule is triggered:

  - **Assignment Kind** – specifies how the system determines the assignee. The available options include:

  - **Area Responsible** – assigns to the user set as *Primary User* for the **Project Area**.  
    *Suitable for domain-specific team structures.*

  - **Project Responsible** – assigns to the user set as *Primary User* for the **Project**.  
    *Useful for centralized case control or project leadership.*

  - **Case Owner** – assigns to the user set as *Owner* of the Case.  
    *Ensures that the designated responsible party receives it.*

  - **Current User** – assigns to the user performing the triggering change (e.g., status update).  
    *Enables contextual or self-assignment.*

  - **Specific User** – assigns to a fixed, manually selected user.  
    *In this case, the **Assign To User** field becomes mandatory.*

This setup provides flexibility to support both static and dynamic assignment patterns, allowing the system to reflect organizational structure, business rules, and real-time actions.

`[screenshot]`


### Rule logic

Assignment Rules are automatically evaluated whenever one of the configured **condition fields** is modified in a Case. This allows the system to dynamically react to changes in the Case’s state, structure, or categorization.

When a Case is updated, the system checks all **active** Assignment Rules whose condition fields are affected. If multiple rules match, the one with the **highest priority** is applied.  
If more than one rule shares the highest priority, the one with the **highest Rule No.** is selected.

Once a matching rule is found, the system executes the corresponding assignment action based on the **Assignment Kind** defined in the rule, assigning the Case to the designated user by updating the **Assigned To User** field.

This logic allows cases to be automatically routed as soon as a key attribute changes. 

**For example:** <br>
If a Case is moved to the state "In Progress" and its Project Area is "Infrastructure", it can automatically be assigned to the responsible user for that area.
