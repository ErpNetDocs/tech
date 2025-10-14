# CRM

The Customer Relationship Management (CRM) subsystem in @@name is used to manage customer relationships and other front-office activities of a company. It forms the foundation for managing customer interactions, from initial contact and opportunity tracking to final invoicing, ensuring full traceability across all customer-related processes.

## General concepts and processes

CRM manages the following sequence of documents and activities:

> *Activity* → *Opportunity* → *Offer* → *Sales order* → *Invoice order* → *Invoice*

- **Activity** – A generic action related to a party. Supports calendar appointments, reminders, questionnaires, and other activities such as meetings, visits, and contracts.  
- **Opportunity** – A sales prospect with expected revenue and probability. Does not include line-level detail.  
- **Offer (quote)** – A formal sales proposal (quote) that includes line items and allows optional selection of accepted items.  
- **Sales order** – The main sales document created from the customer’s order. It initiates the logistics and financial processes related to the sale.
- **Invoice order** – An internal document used to track invoices that must be issued.  
- **Invoice** – A legal and financial document that finalizes the sales process.

> [!NOTE]
> 
> The above diagram shows only the CRM part of the whole process. <br>
> The full process involves many different modules of the ERP system.

## Modules

The CRM module consists of multiple submodules, each managing a specific aspect of the customer relationship and sales process.

| Module | Description |
|---------|-------------|
| **[Contacts and tasks](https://docs.erp.net/tech/modules/crm/contacts/index.html?q=Contacts%20and%20tasks)** | Manages parties, calendar appointments, and related interactions. |
| **[Pre-sales](https://docs.erp.net/tech/modules/crm/presales/index.html?q=crm)** | Handles opportunities, quotations, and pricing discussions. |
| **[Sales](https://docs.erp.net/tech/modules/crm/sales/index.html?q=crm%20Sales)** | Manages sales order documents. |
| **[Invoicing](https://docs.erp.net/tech/modules/crm/invoicing/index.html?q=crm%20Invoicing)** | Oversees the invoicing process, including invoice orders and issued invoices. |
| **[Marketing](https://docs.erp.net/tech/modules/crm/marketing/index.html)** | Plans and executes marketing campaigns and manage distribution channels. |
| **[Common concepts](https://docs.erp.net/tech/modules/crm/crm-common/index.html)** | Provides shared mechanisms such as pricing logic and line discount determination. |
| **[Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/index.html)** | Offers a single platform for customer engagement and self-service. |
| **POS** | Manages point-of-sale operations in physical retail environments. |
| **Distribution** | Supports field sales and sales target management. |
| **Product configuration** | Enables configurable, made-to-order and engineer-to-order products. |
| **Products** | Maintains product master data, including measurements, codes, variants, and channels. |
