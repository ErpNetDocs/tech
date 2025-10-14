# CRM

The Customer Relationship Management (CRM) subsystem in @@name is used to manage customer relationships and other front-office activities of a company. It forms the foundation for managing customer interactions, from initial contact and opportunity tracking to final invoicing, ensuring full traceability across all customer-related processes.

## General concepts and processes

CRM manages the following sequence of documents and activities:

> *Activity* → *Opportunity* → *Offer* → *Sales order* → *Invoice order* → *Invoice*

- **Activity** – A generic action related to a party. Supports calendar appointments, reminders, questionnaires, and other activities such as meetings, visits, and contracts.  
- **Opportunity** – A sales prospect with expected revenue and probability. Does not include line-level detail.  
- **Offer** – A formal sales proposal (quote) that includes line items and allows optional selection of accepted items.  
- **Sales order** – The main sales document created from the customer’s order. It initiates the logistics and financial processes related to the sale.
- **Invoice order** – An internal document used to track invoices that must be issued.  
- **Invoice** – A legal and financial document that finalizes the sales process.

> [!NOTE]
> 
> The above diagram shows only the CRM part of the whole process. <br>
> The full process involves many different modules of the ERP system.

## Structure

The CRM module consists of several **submodules**, each managing a specific aspect of the customer relationship and sales process.

| Module | Description |
|---------|-------------|
| **[Invoicing](https://docs.erp.net/tech/modules/crm/invoicing/index.html?q=crm%20Invoicing)** | Oversees the invoicing process, including invoice orders and issued invoices. | 
| **[Marketing](https://docs.erp.net/tech/modules/crm/marketing/index.html)** | Plans and executes marketing campaigns and manage distribution channels. |
| **POS** | Manages point-of-sale operations in physical retail environments. |
| **[Presales](https://docs.erp.net/tech/modules/crm/presales/index.html?q=crm)** | Handles opportunities, quotations, and pricing discussions. |
| **Pricing** | Creates bonus programs, line discounts, product prices, promotional packages and similar price-related entities.
| **[Sales](https://docs.erp.net/tech/modules/crm/sales/index.html?q=crm%20Sales)** | Manages sales order documents. |
| **[Sales Force](https://docs.erp.net/tech/modules/crm/sales-force/index.html)** | Manages sales personnel, their group structures, assignment rules, and performance targets, providing tools to define, organize, and track the activities and objectives of sales representatives within the CRM framework.
| **Subscriptions** | Handles agreements with customers for periodic delivery of services and billing.
| **[Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/index.html)** | Offers a single platform for customer engagement and self-service. |
