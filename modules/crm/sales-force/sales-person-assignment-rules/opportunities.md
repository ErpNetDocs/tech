---
uid: opportunities
---

# Opportunities  

## Assignment logic  
Sales Person assignment is automatically triggered whenever any of the following fields in an **Opportunity** are changed: *Enterprise Company, From Division, or Party*.  
This allows the system to assign the most appropriate **Leading Sales Person** based on predefined assignment logic.  

The logic follows these main steps:  

### 1. Triggering rule evaluation  
Assignment Rules are automatically evaluated when any of the following fields in an Opportunity are updated: 
- *Enterprise Company*  
- *From Division*  
- *Party*  

In addition, the Party selected in the Opportunity must have a defined Customer record for the same Enterprise Company as the document's Enterprise Company.  


### 2. Rule evaluation  
The system evaluates all **active Sales Person Assignment Rules** that are configured to **apply to documents**, based on the following conditions:  

- The rule must be active on the Opportunity’s document date (i.e., the document’s date must fall between the rule’s *From Date* and *To Date*, if defined).  
- The *Enterprise Company* specified in the rule must match the one in the Opportunity.  
- The following fields in the rule must either match the values related to the Opportunity or be left unspecified:  
  - *Company Division* – as specified in the Opportunity (*From Company Division* field)  
  - *Customer Type* – as specified in the Customer linked to the selected Party (*Customer Type* field)  
  - *Sales Area* – as defined in the Customer’s Party (*Area* field)  

If multiple rules match:  
- The one with the **highest Priority** is selected.  
- If multiple rules share the same priority, the rule with the **highest Rule No** takes precedence.  


### 3. Assignment execution  
Once the best-matching rule is identified, the system automatically assigns the corresponding **Sales Person** to the *Leading Sales Person* field in the Opportunity.  

If no applicable rule is found, the field remains empty.  

> [!NOTE]  
> If the system can determine a Sales Person based on the current user or an existing Customer record, that assignment takes precedence over the rule-based logic.



## Manual assignment via UI function  

The Opportunity form includes a UI function called **Assign Default Salesperson**, available from the **Run** menu of the record.  

This function allows users to manually apply the same assignment logic described above, even when a *Leading Sales Person* is already selected.  
It evaluates the applicable rules and replaces the current assignment with the one determined by the best-matching rule (if found).  

Before executing, the system verifies that the selected Party has a defined Customer record for the same Enterprise Company as the Enterprise Company of the document.  
If not, the function is aborted with an appropriate error message.  
If the condition is met, the user is prompted to confirm the reassignment.  

This is particularly useful when rules are introduced or modified after opportunities have already been created, enabling realignment with the current assignment strategy.  

> [!NOTE]  
> The function is only available for saved opportunities and is disabled when the document has a state *Released* or higher.  

