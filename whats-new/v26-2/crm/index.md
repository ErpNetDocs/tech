# CRM

The CRM module in ERP.net manages the entire customer lifecycle — from the first interaction and opportunity tracking to offers and sales orders — ensuring complete visibility and traceability of all customer-related processes. It streamlines front-office activities, centralizes interactions, and provides a structured flow of documents and actions. With the upcoming improvements, CRM becomes more intuitive, more automated, and easier to use, reducing manual steps and creating a smoother, more efficient experience for both users and customers.

## Notable features

### 1. Improved Opportunity → Offer Flow: Customer field now optional

When creating an Offer from an Opportunity (via Run → Create Offer), the system no longer requires a pre-existing Customer record. This simplifies the process and removes the need to create a Customer entry prematurely.
Party information from the Opportunity is automatically transferred to the To Party field, allowing the Offer to be created quickly and efficiently. A formal Customer record is only needed later in the process, once the Offer is approved and moved to Released status.
This enhancement reduces unnecessary steps, minimizes confusion, and provides a more streamlined experience when working with Opportunities and Offers.


### 2. Automatic Customer Creation When an Offer Is Approved

To streamline the offer approval process, the system now automatically creates a Customer record when an Offer is moved to Released (or directly to Completed) status. The newly created Customer is immediately linked back to the Offer through the Customer field.
All necessary data for creating the Customer is taken directly from the To Party information in the Offer, eliminating the need for users to manually create a Customer entry.
This enhancement reduces administrative work, prevents confusion, and ensures a smooth transition from potential client to confirmed customer — all in one seamless step.

## Other features

### 1. Configurable behavior after fiscal receipt printing from Sales Orders

A new configuration option, [`/Crm/Pos/SalesOrderAfterFiscalPrintBehavior`](../../../../reference/config-options-reference.md#76-crmpossalesorderafterfiscalprintbehavior), allows controlling the behavior after a successful fiscal receipt print from the Sales form.

Depending on the selected value, the Sales Order and its sub-documents can either be completed automatically, or the Sales Order can remain in **Released** status, and the Sales form can either close or remain open.

If the option is not set, the default behavior is to complete the Sales Order and its sub-documents automatically and close the Sales form.

This provides more flexibility in POS scenarios by allowing organizations to choose whether the sales process should be completed automatically or remain available for subsequent processing, and whether the Sales form should close or remain open after fiscal printing.

### 2. Print fiscal receipts directly from Invoices

Invoices can now be used directly for fiscal receipt printing through the **Print on fiscal printer** panel.

When the panel is included in the Invoice form layout and the system finds eligible linked payment transactions, it shows the payment that will be used for printing, together with its payment type and amount.

Eligible payments are invoice-linked payment transactions that are not voided, are in state **Planned** or higher, are in the enterprise company base currency, and have not already been printed.

If multiple eligible payment transactions are available, users can switch between them and select which one to print. 

After a successful fiscal print, the form refreshes automatically and shows the next available payment (if any). 

If no eligible payments are available, the **Print (F7)** button is disabled.

This reduces navigation between documents, makes the fiscal printing flow faster, and helps users clearly see what will be printed before starting the operation.

For more information, see [Print on fiscal devices](ErpNetDocs/winclient/country-specific/bulgaria/print-on-fiscal-devices/print-on-fiscal-device.md).
