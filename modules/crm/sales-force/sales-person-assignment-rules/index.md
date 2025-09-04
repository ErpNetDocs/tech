---
uid: sales-person-assignment-rules
---

# Sales Person Assignment Rules

Sales documents and definitions can be automatically routed to salespeople through **assignment rules**. These rules automate and streamline the assignment of sales tasks and records to the appropriate persons.


## Benefits of using Assignment Rules
Assignment rules provide several key benefits:

- **Efficiency and speed** – automatically assigns both existing and new entries to the appropriate person.  
- **Consistency** – ensures every record is assigned based on predefined logic (e.g., territory, business unit, customer classification, or a combination of these), reducing human error or bias.  
- **Improved customer response** – assigns records faster to the right person, enabling quicker responses and better service.  
- **Scalability** – supports business growth by removing the need for manual assignment.  
- **Customer satisfaction** – helps maintain a single contact point for each customer, ensuring proper account management.  


## Basic logic
In a typical sales team, individual salespeople are responsible for specific aspects of the sales process — for example, a particular region or a defined customer group. When an **Offer, Sales Order, Opportunity, Customer, or Lead** is created, it should be assigned to the most appropriate salesperson. Assignment rules make this happen automatically, while exceptions can still be handled manually.

## Assignment rule targets
Assignment rules can apply to two types of records:

- **Customers** – includes both Customers and Leads.  
- **Documents** – includes Offers, Sales Orders, and Opportunities.  

Each type of target is evaluated according to specific logic tailored to that record type.


## How it works for users
Assignment rules are evaluated by the system either when a new or existing sales-related record is saved, or — in specific cases like Opportunities — when certain key fields are modified.

If no salesperson has been assigned through another system rule or manual input, and the record meets the trigger conditions, the system looks for active assignment rules that match the record’s context. It then applies the rule with the highest priority.
If multiple rules have the same priority, the one with the latest Rule No is selected.

This ensures that sales ownership is assigned consistently and automatically, based on predefined business rules — not individual user actions.


## Quick assignment editing with UI functions
If you need to apply rules to existing records, you can update assignments directly from the related document or definition (e.g., Opportunity, Offer, Customer). Select **Run** on the record, then choose **Assign Default Salesperson** from the dropdown menu. The system will apply the relevant rule — even replacing a manually selected salesperson — with the default one defined in the rules.  

This feature allows team managers to quickly reassign records in line with current or newly introduced assignment rules.


## Learn more
To fully understand how assignment rules are set up and applied, see:

- [**Rule settings**](rule-settings.md) – explains how to configure assignment rules and define their key parameters.  
- [**Sales Orders & Offers**](sales-orders-and-offers.md) – еxplains how rules are evaluated and applied when sales documents are saved. 
- [**Opportunities**](opportunities.md) – explains how rules are triggered and applied when opportunity fields are updated. 
- [**Customers**](customers.md) – explains how rules assign salespeople to customer records.
- [**Leads**](leads.md) – explains how rules are applied when saving leads linked to known companies.   
