# CRM Step by Step

## A quick path to getting started with CRM in @@name

This section presents the shortest and most practical path to start using the CRM functionalities in @@name.  
Its goal is not to describe all capabilities of the system, but to provide clear guidance on where to start and what is minimally required for the CRM process to be usable in a real business environment.

CRM in @@name is designed to:

- not require entering all information upfront;
- allow you to start with what you actually have;
- add structure gradually as the process evolves.

In short, to start working with CRM:

- you choose where your process begins — you can start from a Lead, Opportunity, or Offer, depending on your business needs; the system does not restrict you;
- you enter only the records required for the current stage;
- you move forward when the information becomes logically necessary.

The following list summarizes these steps in a short checklist that shows what is realistically expected from you to start a CRM process without unnecessary complexity.

---

## Short startup checklist

### Define the entry point of your CRM process

Decide whether your business starts with unstructured contacts collected through marketing lists, events, or campaigns, or whether you work directly with specific customers and concrete inquiries.  
In the first case, start with **Leads**; in the second case, you can start directly with **Opportunity** or **Offer**.

For an overview of how these records fit together, see  
**[CRM Overview](./index.md)**.

---

### If you use Leads – create at least one Marketing Campaign

A **Campaign** is the only mandatory requirement for working with Leads. It allows you to group contacts by source and later analyze the relationship between marketing activities and actual sales.

For details on Campaigns and marketing sources, see  
**[Marketing](./marketing/index.md)**.

---

### When moving to Opportunity – introduce structure

To manage real deals, the system requires you to know who you are negotiating with (**Party**) and which sales representative is responsible for the deal (**Sales Person**). This is the point at which CRM starts to provide accountability and control.

More details about Opportunities and sales ownership can be found in  
**[Presales](./presales/index.md)** and **[Sales Force](./sales-force/index.md)**.

---

### Use Offers to formalize commercial terms

Offers can be created only for Parties that are defined as **Customers**, reflecting the point at which a Company or Person becomes part of the customer list and commercial negotiations are formalized. Offers allow you to structure proposals to the customer, create variations, and preserve the history of negotiations.

For pricing logic, discounts, and offer behavior, see  
**[Pricing](./pricing/index.md)** and **[Presales](./presales/index.md)**.

---

### Create a Sales Order once the deal is agreed

A **Sales Order** confirms the agreed terms and continues the existing document flow. No additional setup is required, provided that a **Customer** is defined.

Sales Orders and their role in the sales execution phase are described in  
**[Sales](./sales/index.md)**.

---

### Complete the process with Invoicing by using document relationships

Invoicing can be done directly, but the greatest value is achieved when the **Invoice** follows the **Sales Order** and reuses the already agreed data, thus closing the entire **Lead to Cash** process.

For invoicing documents and options, see  
**[Invoicing](./invoicing/index.md)**.

---

## How to read the next section

Below, each of these steps is described in more detail, explaining:

- what can be done at each stage;
- which data is required;
- why these requirements exist and what practical value they provide.

This will allow you not only to start working quickly, but also to understand the logic on which the CRM process in @@name is built.

Conceptual background and rules are explained in more detail in  
**[CRM Concepts](./concepts.md)**.

---

## Detailed explanation of the steps in the CRM process

The following points describe the same short path, but with more context and explanation.  
The goal is not only to know what is required, but why the system works this way.

---

## 1. Decide where your process starts

CRM in @@name does not enforce a fixed entry point.  
The system is designed to adapt to how your business actually operates.

If your work starts with:

- marketing lists,
- event registrations,
- campaigns, trade fairs, or external sources,

the most logical starting point is **Leads**.  
They are intended for storing and initially processing contacts that may or may not become real customers.

If, however, you have:

- a potential customer with a clear inquiry,
- inquiries from existing customers,

you can start directly with **Opportunity** or **Offer**, without using Leads.

This flexibility is explained further in  
**[CRM Concepts](./concepts.md)**.

---

## 2. If you use Leads – prepare only one thing

To start working with Leads, you need to have at least one **Marketing Campaign**.

This is the only mandatory requirement at this stage.

A Campaign can be created:

- directly from the **Campaign** field in the Lead form using **Create New**;
- or in advance in **Marketing → Campaigns**.

More details can be found in  
**[Marketing](./marketing/index.md)**.

Everything else about Leads is intentionally flexible.  
The system allows:

- entering minimal information;
- importing data from Excel without fixed templates;
- adding custom fields;
- creating custom list views.

---

## 3. When moving to Opportunity – two records are required

Opportunity is the first step where the process becomes more structured.

To work with Opportunities, you need to create:

- **Party** – the company or individual with whom negotiations are conducted;
- **Sales Person** – the sales representative responsible for the deal.

These concepts are covered in  
**[Presales](./presales/index.md)** and **[Sales Force](./sales-force/index.md)**.

At this stage:

- real management of potential deals begins;
- sales **Activities** (meetings, demos, calls) can be linked to a specific Opportunity;
- multiple Opportunities can be linked to a single Activity when one meeting leads to more than one potential deal;
- tracking the efforts and results of sales representatives becomes possible.

---

## 4. Offer – no complex setup, full history

To create Offers, the Party must be defined as a **Customer**.  
This is an existing Party record that you explicitly designate as part of your customer list.

Offer behavior and pricing logic are described in  
**[Presales](./presales/index.md)** and **[Pricing](./pricing/index.md)**.

---

## 5. Sales Order – ready to use “out of the box”

A Sales Order marks the moment when the deal is considered agreed and moves from the commercial phase to execution.

Sales Orders are part of the **Sales** module, described in  
**[Sales](./sales/index.md)**.

From this point on, the system allows the process to be extended according to business needs — including invoicing, logistics, warehouse operations, or other operational processes.

---

## 6. Invoicing – use the power of relationships

Invoices can be created directly, but the greatest value is achieved when invoicing is part of the document flow and linked to the Sales Order.

After a Sales Order, the system allows the creation of an **Invoice Order**, which provides additional control over invoicing scenarios.

Details about these documents can be found in  
**[Invoicing](./invoicing/index.md)**.

In this way, the CRM process naturally closes as **Lead to Cash**, while remaining flexible and suitable for different business scenarios.

---

## What to explore next

Now that you have a working overview of the CRM process and know the minimal requirements to start using it, you can continue with the sections that match your current needs.

### Learn the structure and logic of CRM
- **[CRM Overview](./index.md)** – a high-level view of the CRM model, core records, and the Lead to Cash flow.
- **[CRM Concepts](./concepts.md)** – explains why the system works this way, how document relationships provide traceability, and what best practices to follow.

### Go deeper into the operational modules
- **[Presales](./presales/index.md)** – working with Leads, Opportunities, Offers, and Activities.
- **[Sales](./sales/index.md)** – converting offers into sales orders and executing the sales process.
- **[Pricing](./pricing/index.md)** – price lists, discounts, and pricing rules.
- **[Invoicing](./invoicing/index.md)** – Invoice Orders, invoices, and invoicing scenarios.

### Extend the process when needed
- **[Marketing](./marketing/index.md)** – campaigns, sources, and lead generation.
- **[Sales Force](./sales-force/index.md)** – sales personnel, responsibilities, targets, and reporting.
- **[Subscriptions](./subscriptions/index.md)** – recurring services and periodic invoicing.
- **[POS](./pos/index.md)** – point-of-sale operations.
- **[Client Center](./clientcenter/index.md)** – customer-facing portals and self-service.

You do not need to configure everything upfront.  
Start simple, let the process work, and extend it step by step as your business grows.
