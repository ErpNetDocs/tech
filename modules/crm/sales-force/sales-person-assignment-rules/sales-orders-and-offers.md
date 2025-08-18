---
uid: orders-and-offers
---

# Sales Orders & Offers  

Salesperson assignment is automatically triggered whenever a Sales Order or Offer is saved, and the *Salesperson* field is empty.  
This enables the system to evaluate the document context and assign it to the most appropriate person in charge.  

The logic follows these main steps:  


## 1. Triggering rule evaluation  
Assignment Rules are automatically evaluated when the document is saved, and **all** of the following conditions are met:  

- The *Salesperson* field is empty  
- A *Customer* is selected in the document  


## 2. Rule evaluation  
The system evaluates all **active Sales Person Assignment Rules** that are configured to **apply to documents**, based on the following conditions:  

- The rule must be active on the document’s date (i.e., the document’s date must fall between the rule’s *From Date* and *To Date*, if defined).  
- The *Enterprise Company* specified in the rule must be the same as in the document.  
- The following fields in the rule must either match the values related to the document or be left unspecified:  
  - *Company Division* – as specified in the document (*From Company Division* field)  
  - *Customer Type* – as defined in the selected Customer (*Customer Type* field)  
  - *Sales Area* – as defined in the Customer’s Party (*Area* field)  

If multiple rules match:  
- The one with the **highest Priority** is selected.  
- If multiple rules share the same priority, the rule with the **highest Rule No.** takes precedence.  


## 3. Assignment execution  
Once the best-matching rule is identified, the system automatically assigns the corresponding **Sales Person** to the document.  

If a *Salesperson* has already been entered, no automatic assignment is performed.  
