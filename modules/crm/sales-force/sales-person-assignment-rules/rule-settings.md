---
uid: rule-settings
---

# Rule settings  

Assignment Rules are configured in the *Sales Force → Definitions → Sales Person Assignment Rules* section.  

Each rule is defined by the following settings:

## Rule availability (activation conditions)  
These settings determine whether the rule is eligible for evaluation:  

- **Active** – indicates whether the rule is currently enabled. Only active rules are considered by the system.  
- **From Date** / **To Date** – optional start and end dates that define a period when the rule is applicable. Useful for setting temporary rules.  


## Rule trigger (matching conditions) 
The criteria for applying a rule are defined by specifying values in **condition fields**.  
The available condition fields are: **Enterprise Company**, **Company Division**, **Sales Area**, and **Customer Type**.  

When the system evaluates a rule, it compares each condition field with the corresponding value from the source record (e.g. Offer, Sales Order, Opportunity, Customer, Lead) or related records.  
For a rule to match:  

- The **Enterprise Company** in the rule must match the one in the source record.  
- The other condition fields must either match the corresponding values in the source record or be left empty in the rule.  
- You can define one or more condition fields — the more you specify, the more narrowly the rule will apply.  


## Assignment logic (execution behavior)
This setting controls how the assignment is performed. It involves two components:  

- **Assignment application** – specifies whether the rule applies to Customers (Customer or Lead) or to Documents (Offer, Sales Order, or Opportunity). One of these must be selected.  
- **Sales Person** – specifies the user to whom the customer/document should be assigned.  


## Rule conflict resolution
These settings define how the system resolves conflicts when multiple rules are applicable at the same time:  

- **Priority** – defines the importance level of the rule. Priority may be: *highest*, *high*, *medium*, *low*, *lowest*.  
When multiple rules match the same conditions, the one with the highest priority is applied.  
- **Rule No** – a unique sequence number used to determine precedence when two or more rules share the same priority.  
In such cases, the rule with the highest number is applied.  
The rule number is auto-generated but can be modified manually if needed.  
