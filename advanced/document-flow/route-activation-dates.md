# Route activation dates

Document routes can be configured with date ranges that determine when a
[document generation](generation.md) route is applicable.

There are two independent date ranges:

- **Activation Date** and **Deactivation Date** are compared with the document
  date of the **generating document**.
- **Master Document Activation Date** and **Master Document Deactivation Date**
  are compared with the document date of the **master document**.

The generating document is the document from which the route generates another
document. The master document is the document that starts the document flow.

> [!NOTE]
> Master document activation dates are available from version **27.1.1.35**.

## Activation Date and Deactivation Date

These fields define the period during which a route is applicable based on the
document date of the generating document.

- **Activation Date** is the first date on which the route is applicable.
- **Deactivation Date** is the last date on which the route is applicable.
  If empty, there is no deactivation date.

Both boundaries are **inclusive**. Activation Date is required.

### Example

A route has the following settings:

| Field | Value |
| --- | --- |
| Activation Date | 01 Jan 2026 |
| Deactivation Date | 31 Dec 2026 |

The route is applicable to a generating document dated **01 Jan 2026** or
**31 Dec 2026**, but not to one dated **01 Jan 2027**.

Other route conditions must also be met for the route to run.

## Master Document Activation Date and Master Document Deactivation Date

These fields define the period during which a route is applicable based on the
document date of the master document.

- **Master Document Activation Date** is the first master document date for
  which the route is applicable.
- **Master Document Deactivation Date** is the last master document date for
  which the route is applicable. If empty, there is no master document
  deactivation date.

Both boundaries are **inclusive**. Both fields can be left empty.

### Example

Consider the following document flow:

**Sales Order → Shipment Order → Shipment**

The Sales Order is the master document. A route from Shipment Order to Shipment
has a master document period from **01 Nov 2026** to **30 Nov 2026**.

| Sales Order date | Within the master document period? |
| --- | --- |
| 31 Oct 2026 | No |
| 01 Nov 2026 | Yes |
| 30 Nov 2026 | Yes |
| 01 Dec 2026 | No |

When the route is evaluated, the date of the **Sales Order** is checked against
the master document period, not the date of the Shipment Order.

## Combining both periods

When both periods are configured, the corresponding document dates must meet
**both** conditions:

1. The generating document date must fall within the Activation Date and
   Deactivation Date period.
2. The master document date must fall within the Master Document Activation Date
   and Master Document Deactivation Date period.

The route must also be active and satisfy its other configured conditions.

### Example

A route has these settings:

| Field | Value |
| --- | --- |
| Activation Date | 01 Jan 2026 |
| Deactivation Date | 31 Dec 2026 |
| Master Document Activation Date | 01 Oct 2026 |
| Master Document Deactivation Date | 31 Oct 2026 |

For a Sales Order dated **18 Oct 2026** and a generating Shipment Order dated
**05 Nov 2026**, both dates are within their respective periods. The date
conditions are satisfied.

If the Shipment Order is dated **05 Jan 2027**, the generating document date
is outside the first period. The route does not meet the date conditions, even
though the Sales Order date is within the master document period.

## Changing routes for new document flows

Master document dates can be used to apply different routes to existing and new
document flows.

For example, configure two routes with non-overlapping master document periods:

| Route | Master Document Activation Date | Master Document Deactivation Date |
| --- | --- | --- |
| Existing route | Empty | 31 Oct 2026 |
| New route | 01 Nov 2026 | Empty |

A flow with a master document dated **18 Oct 2026** can continue using the
existing route. A flow with a master document dated **01 Nov 2026** can use the
new route.

Keep the existing route active and applicable to the old master document dates
for as long as those flows may need it. Its generating document date period and
other conditions must also allow it to run.

> [!IMPORTANT]
> Changing a route's master document period does not by itself preserve an old
> route configuration. If a route is changed, disabled, or configured with a
> period that excludes an existing flow's master document date, do not assume
> that the flow can generate further documents through that route.
>
> Documents generated before the change may already exist. This is different
> from generating a new document through a route after its settings change.

## See also

- [Document generation](generation.md)
- [Generation procedures](generation-procedures.md)
- [Document flow](index.md)
- [Document routes in the Domain Model](xref:Systems.Documents.Routes)
