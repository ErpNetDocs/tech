# Customer Relationship Management (CRM)

The CRM module of @@name is primarily intended to manage the relationships with the customers.
However, it has broader reach, managing the office general tasks, calendars, distribution, service and more.

## General concepts and process

The general process flow of the CRM module is:

*Appointment* -> *Opportunity* -> *Offer* -> *Sales Order* -> *Invoice Order* -> *Invoice*

* **Appointment** - generic calendar appointment, but related to a party.
* **Opportunity** - sales opportunity, with expected revenue and probability. It does not have detail line items.
* **Offer** - sales offer (quote), with line items. It allows optional selection of some of the items, which the customer has accepted.
* **Sales Order** - sales order from the customer. The main sales document. All documents before it are optional. The sales order initiates the logistics and financial processes, related to the sale.
* **Invoice Order** - an order to issue an invoice. This is an internal document, which is used to track the invoices, which we have to issue.
* **Invoice** - legal document,  finalizing the sales process. Issued after the products are shipped.

## CRM Sub-modules

There are many sub-modules of the CRM module, which are used to manage different aspects of the CRM processes:

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
