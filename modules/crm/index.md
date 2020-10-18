# Customer Relationship Management (CRM)

The CRM group of applications in @@name is used to manage the front-office activities of a company.

## General concepts and process

The general process flow of the CRM module is:

> *Activity* -> *Opportunity* -> *Offer* -> *Sales Order* -> *Invoice Order* -> *Invoice*

* **Activity** - generic activity, related to a party. Includes support for calendar appointments, reminders, questionnaires, etc. Can be used to represent appointments, scheduled meetings, visits, contracts and just about any generic document.
* **Opportunity** - sales opportunity, with expected revenue and probability. It does not have detail line items.
* **Offer** - sales offer (quote), with line items. It allows optional selection of some of the items, which the customer has accepted.
* **Sales Order** - sales order from the customer. The main sales document. All documents before it are optional. The sales order initiates the logistics and financial processes, related to the sale.
* **Invoice Order** - an order to issue an invoice. This is an internal document, which is used to track the invoices, which we have to issue.
* **Invoice** - legal and financial document, finalizing the sales process.

> [!NOTE]
> The above diagram shows only the CRM part of the whole process.
> The full process involves many different modules of the ERP system.

## CRM Applications

There are many applications in the CRM group.
They are used to manage the different aspects of the CRM processes:

* **Contacts and tasks** - calendar appointments, party definitions, etc.
* **Pre-sales** - Opportunities management.
* **Sales** - Sales Orders, customers, etc.
* **Invoicing** - Invoicing process management, invoices and BI.
* **POS** - Manage point-of-sale activities in physical stores.
* **Marketing** - Marketing campaigns, activities, distribution channels, etc.
* **Distribution** - field sales, sales person targets management, etc.
* **Pricing** - price lists management.
* **Product Configuration** - create products based on specs for job shops (made-to-order and engineer-to-order environments).
* **Products** - manage products master data - products and product measurements, codes, variants, channel, pictures, groups, etc.
