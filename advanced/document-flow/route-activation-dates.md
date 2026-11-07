# Route activation dates

Document routes use date ranges to determine when a route can be used for [document generation](https://docs.erp.net/tech/advanced/document-flow/generation.html).

Each route can have two date ranges:

- **Activation Date / Deactivation Date** — checked against the date of the document generating the next document.
- **Master Document Activation Date / Master Document Deactivation Date** — checked against the date of the original document that started the document flow.

## Why and when to use master document dates

Master document dates are useful when a company changes its document generation process but still has unfinished documents from the old process.

**For example:**

A company introduces a new document route starting **01 Nov 2026**. However, some Sales Orders created in October are still being processed.

These Sales Orders must continue using the old route, even when their next documents are generated in November or later.

Checking only the generating document's date cannot distinguish these old document flows from new ones.

**Master document dates solve this problem.** They allow:

- Existing document flows to continue using the old route.
- New document flows to use the new route.
- Both routes to remain active at the same time.

This is useful whenever a process changes but unfinished document flows must continue under the previous rules.

> [!NOTE]
> Master document activation and deactivation dates are available from version **27.1.1.35**.

## How the date fields work

### Activation Date and Deactivation Date

These fields check the date of the **generating document**.

- **Activation Date** — First applicable date. Required.
- **Deactivation Date** — Last applicable date. Optional.

### Master Document Activation Date and Master Document Deactivation Date

These fields check the date of the **master document**.

- **Master Document Activation Date** — First applicable master document date.
- **Master Document Deactivation Date** — Last applicable master document date.

Both fields are optional. If both are empty, the master document date does not restrict the route.

For all four fields, the date boundaries are **inclusive**. An empty optional date means no limit in that direction.

When both date ranges are configured, **both conditions must be satisfied**. Other route conditions must also be met.

The checks use document dates, **not the current system date or the date when generation is executed**.

## Example: Changing document routes

Consider the following document flow:

**Sales Order → Shipment Order → Shipment**

When generating a Shipment:

- **Sales Order** is the master document.
- **Shipment Order** is the generating document.

The company introduces a new document generation process starting **01 Nov 2026**.

To keep the old process available for existing Sales Orders, configure two routes.

The table below shows only the master document date settings. Both routes must also have a valid **Activation Date**.

| Field | Existing route | New route |
|---|---|---|
| Master Document Activation Date | Empty | 01 Nov 2026 |
| Master Document Deactivation Date | 31 Oct 2026 | Empty |

**Result:**

| Sales Order date | Shipment Order date | Applicable route based on master date |
|---|---|---|
| 18 Oct 2026 | 05 Nov 2026 | Existing route |
| 31 Oct 2026 | 15 Nov 2026 | Existing route |
| 01 Nov 2026 | 05 Nov 2026 | New route |
| 10 Nov 2026 | 20 Nov 2026 | New route |

Even though all Shipment Orders are dated in November, the Sales Order date determines which route meets the master document date condition.

**The generating document date is also checked.** For example, if the existing route has a Deactivation Date of **31 Dec 2026**, a Shipment Order dated **05 Jan 2027** cannot use this route, even if its Sales Order is dated in October 2026.

### Important configuration notes

- Keep the existing route active while unfinished document flows still need it.
- Keep its original generation settings, apart from the necessary date changes.
- Make sure the generating document's **Activation Date / Deactivation Date** also allows documents to be generated after the process change.

> [!WARNING]
> To keep existing document flows using the old process, do not modify or disable the existing route. Instead, create a new route with the updated configuration and use master document dates to control which route applies.

## See also

- [Document generation](https://docs.erp.net/tech/advanced/document-flow/generation.html)
- [Generation procedures](https://docs.erp.net/tech/advanced/document-flow/generation-procedures.html)
- [Document flow](https://docs.erp.net/tech/advanced/document-flow/index.html)
- [Document routes in the Domain Model](https://docs.erp.net/model/entities/Systems.Documents.Routes.html)
