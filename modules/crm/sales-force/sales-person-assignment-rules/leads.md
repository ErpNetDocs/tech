---
uid: leads
---

# Leads  

Salesperson assignment is automatically triggered whenever a **Lead** is saved and the *Assigned To* field is empty.  
This allows the system to assign each lead to the most appropriate sales representative, based on the relationship with a known company and its customer profile.  

The logic follows these main steps:  


## 1. Triggering rule evaluation  
Assignment Rules are automatically evaluated when the Lead is saved and **all** of the following conditions are met:  

- The *Assigned To* field is empty  
- An *Identified Company* is selected in the Lead  
- The *Identified Company* has a defined Customer record for the same Enterprise Company as the Lead  


## 2. Rule evaluation  
The system evaluates all **active Sales Person Assignment Rules** that are configured to **apply to customers**, based on the following conditions:  

- The rule must be active on the current date (i.e., today must fall between the rule’s *From Date* and *To Date*, if defined).  
- The *Enterprise Company* specified in the rule must be the same as in the Lead.  
- The following fields in the rule must either match the values defined in the related Customer record or be left unspecified:  
  - *Customer Type* – as defined in the Customer  
  - *Sales Area* – as defined in the Customer’s Party  

If multiple rules match:  
- The one with the **highest Priority** is selected.  
- If multiple rules share the same priority, the rule with the **highest Rule No.** takes precedence.  


## 3. Assignment execution  
Once the best-matching rule is identified, the system automatically assigns the corresponding **Sales Person** to the Lead.  

If a *Sales Person* has already been entered in the *Assigned To* field, no automatic assignment is performed.  
