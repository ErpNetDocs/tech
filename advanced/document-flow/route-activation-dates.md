# Route activation dates

Document routes use date ranges to determine whether a route can be used when a document generates the next document in the flow.

Each route can have two date ranges:

- **Activation Date / Deactivation Date** — checked against the date of the document generating the next document.
- **Master Document Activation Date / Master Document Deactivation Date** — checked against the date of the original document that started the document flow.

## Why and when to use master document dates

Master document dates are useful when a company changes its document generation process but still has unfinished document flows from the old process.

**For example:**

A company introduces a new document generation process starting **01 Nov 2026**. However, some Sales Orders created in October are still being processed.

Document flows started by these Sales Orders must continue using the old routes, even when later documents in the flow are generated in November or later.

Checking only the generating document's date cannot distinguish these older document flows from new ones.

**Master document dates solve this problem.** They allow:

- Existing document flows to continue using the old routes.
- New document flows to use the new routes.
- Both old and new routes to remain active at the same time.

This is useful whenever a process changes but unfinished document flows must continue under the previous rules.

##### Note

Master document activation and deactivation dates are available from version **27.1.1.35**.

## How the date fields work

When a document generates the next document through a route, the system checks whether that route is applicable.

### Activation Date and Deactivation Date

These fields check the date of the **generating document** — the document that is currently generating the next document in the flow.

- **Activation Date** — First applicable date. Required.
- **Deactivation Date** — Last applicable date. Optional.

### Master Document Activation Date and Master Document Deactivation Date

These fields check the date of the **master document** — the original document that started the document flow.

- **Master Document Activation Date** — First applicable master document date.
- **Master Document Deactivation Date** — Last applicable master document date.

Both fields are optional. If both are empty, the master document date does not restrict the route.

For all four fields, the date boundaries are **inclusive**. An empty optional date means no limit in that direction.

When both date ranges are configured, **both conditions must be satisfied**. Other route conditions must also be met.

The checks use document dates, **not the current system date or the date when generation is executed**.

## Example: Changing document routes

Consider the following document flow:

**Sales Order → Shipment Order → Shipment**

When a Shipment Order generates a Shipment:

- **Sales Order** is the master document.
- **Shipment Order** is the generating document.
- **Shipment** is the newly generated document.

The company introduces a new document generation process starting **01 Nov 2026**.

To keep the old process available for document flows that started before this date, configure separate master document date ranges on the existing and new routes.

The table below shows only the master document date settings. Both routes must also have a valid **Activation Date**.

| Field | Existing route | New route |
| --- | --- | --- |
| Master Document Activation Date | Empty | 01 Nov 2026 |
| Master Document Deactivation Date | 31 Oct 2026 | Empty |

**Result:**

| Sales Order date | Shipment Order date | Applicable route based on master date |
| --- | --- | --- |
| 18 Oct 2026 | 05 Nov 2026 | Existing route |
| 31 Oct 2026 | 15 Nov 2026 | Existing route |
| 01 Nov 2026 | 05 Nov 2026 | New route |
| 10 Nov 2026 | 20 Nov 2026 | New route |

Even though all Shipment Orders in the example are dated in November, the Sales Order date determines which route satisfies the master document date condition.

The generating document date is checked separately.

For example, if the existing route has a **Deactivation Date** of **31 Dec 2026**, a Shipment Order dated **05 Jan 2027** cannot use this route, even if its Sales Order is dated in October 2026.

## Important configuration notes

- Keep the existing route active while unfinished document flows still need it.
- Keep its original generation settings, apart from the necessary date changes.
- Make sure the generating document's **Activation Date / Deactivation Date** also allows the route to be used after the process change.

##### Warning

Master document dates do not preserve previous route configurations automatically.

If an existing route is changed or disabled, unfinished document flows may no longer be able to generate documents using the old process.

To avoid this, keep the existing route active and unchanged, and create a new route with the updated configuration. Use master document dates to control which route applies to existing and new document flows.
