# Customer relationship management (CRM) subsystem

The CRM subsystem in @@name is used to manage customer relationships and other front-office activities of a company.

## General concepts and processes

The main process in the CRM subsystem is:

> *Activity* → *Opportunity* → *Offer* → *Sales order* → *Invoice order* → *Invoice*

* **[Activity](xref:General.Contacts.Activities)** - generic activity, related to a party. Includes support for calendar appointments, reminders, questionnaires, etc. Can be used to represent appointments, scheduled meetings, visits, contracts and just about any generic document.
* **[Opportunity](xref:Crm.Presales.Deals)** - sales opportunity, with expected revenue and probability. It does not have detail line items.
* **[Offer](xref:Crm.Presales.Offers)** - sales offer (quote), with line items. It allows optional selection of some of the items, which the customer has accepted.
* **[Sales order](xref:Crm.Sales.SalesOrders)** - sales order from the customer. The main sales document. All documents before it are optional. The sales order initiates the logistics and financial processes, related to the sale.
* **[Invoice order](xref:Crm.Invoicing.InvoiceOrders)** - an order to issue an invoice. This is an internal document, which is used to track the invoices, which we have to issue.
* **[Invoice](xref:Crm.Invoicing.Invoices)** - legal and financial document, finalizing the sales process.

> [!NOTE]
> The above diagram shows only the CRM part of the whole process.
> The full process involves many different modules of the ERP system.

## Modules

There are many modules in the CRM subsystem.
They are used to manage the different aspects of the CRM processes:

* **[Contacts and tasks](https://docs.erp.net/tech/modules/crm/contacts/index.html?q=Contacts%20and%20tasks)** - calendar appointments, party definitions, etc.
* **[Pre-sales](https://docs.erp.net/tech/modules/crm/presales/index.html?q=crm)** - Opportunities management, quotation, etc.
* **[Sales](https://docs.erp.net/tech/modules/crm/sales/index.html?q=crm%20Sales)** - Sales orders, customers, etc.
* **[Invoicing](https://docs.erp.net/tech/modules/crm/invoicing/index.html?q=crm%20Invoicing)** - Invoicing process management, invoices and BI.
* **[Marketing](https://docs.erp.net/tech/modules/crm/marketing/index.html)** - Marketing campaigns, activities, distribution channels, etc.
* **[Client Center](https://docs.erp.net/tech/modules/crm/clientcenter/index.html)** - a single platform to engage with customers
* **POS** - Manage point-of-sale activities in physical stores.
* **Distribution** - field sales, sales person targets management, etc.
* **Pricing** - price lists management.
* **Product Configuration** - create products based on specs for job shops (made-to-order and engineer-to-order environments).
* **Products** - manage products master data - products and product measurements, codes, variants, channel, pictures, groups, etc.
