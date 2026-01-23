# Scripting in calculated attributes

Calculated Attributes can use JavaScript to compute their values dynamically, enabling custom logic beyond what integrated expressions can provide.

This makes Calculated Attributes significantly more flexible and expressive, especially in scenarios where:

- The logic is too complex or verbose for integrated expressions
- Conditional or procedural calculations are required
- Existing domain data needs to be combined in non-trivial ways

JavaScript-based calculated attributes are evaluated on demand and return their computed value directly.

## How it works

- **Script language**  
  Choose `JavaScript` as the `ScriptLanguage` of the calculated attribute.

- **Script text**  
  Write JavaScript code in the calculated attribute's `ScriptText`.  
  This script is executed whenever the calculated attribute is evaluated.

The script runs in a sandboxed environment with access to:

- The entity for which the calculated attribute is being evaluated
- The entire @@name Domain Model (via the Domain object)

Unlike user business rules, calculated attribute scripts are expected to **produce a value**.  
The value returned by the script becomes the value of the calculated attribute.

## Returning a value

Calculated attribute scripts are written as **function bodies** and may use a top-level `return` statement.

Example:

```js
var base = 10;
var multiplier = 2;
return base * multiplier;
```

The returned value is the calculated attribute's value.

If the script returns `null` or returns nothing (`undefined`), the calculated attribute value is `null`.

> [!IMPORTANT]
> Use JavaScript calculated attributes with care.  
> A script can easily query large datasets (or run many queries), which results in heavy processing during evaluation and may noticeably degrade performance for lists, forms, and reports where the attribute is shown.

## Example: New customer check (exactly one released sales order)

This calculated attribute determines whether the current customer is a "new customer", based on the number of related sales orders.

- **Repository:** Crm.Sales.Customers
- **Script Language:** JavaScript
- **Script Text:**
```js
const salesOrders = Domain.Crm.Sales.SalesOrdersRepository.query(
    {
        Customer: subject,
        Status: 'Released'
    },
    { fetch: 2 }
);
return salesOrders.length == 1;
```

Notes:

- `subject` is the current Customer entity instance (the entity this calculated attribute belongs to).
- The script queries `SalesOrdersRepository` for sales orders:
  - `customer: subject` (only orders for the current customer)
  - `status: 'Released'` (only released orders)
- `{ fetch: 2 }` limits the retrieved records to a maximum of 2. This is an optimization:
  - `0` results -> no released orders
  - `1` result -> exactly one released order (treated as "new customer")
  - `2` results -> at least two released orders (not a new customer)
- The calculated attribute returns a boolean value (`true`/`false`).

## Example: Sales order count for previous vs current month

This calculated attribute returns a summary of how many sales orders a customer has in the **previous month** and the **current month**.

The result is formatted as a string in the form:

```text
<previousMonthCount>/<currentMonthCount>
```

- **Repository:** Crm.Sales.Customers
- **Script Language:** JavaScript
- **Script Text:**
```js
const now = new Date();
const firstDayCurrentMonth = new Date(now.getFullYear(), now.getMonth(), 1);
const firstDayPrevMonth = new Date(now.getFullYear(), now.getMonth() - 1, 1);

const salesOrders = Domain.Crm.Sales.SalesOrdersRepository.query({
    Customer: subject,
    Status: 'Released',
    DocumentDate: {
        greaterthanorequal: firstDayPrevMonth
    }
});

var prevMonthSales = 0;
var currentMonthSales = 0;

salesOrders.forEach((so) => {
    const isPreviousMonth = so.documentDate < firstDayCurrentMonth;

    if (isPreviousMonth)
        prevMonthSales++;
    else
        currentMonthSales++;
});

return `${prevMonthSales}/${currentMonthSales}`;
```

Notes:

- `subject` is the current Customer entity instance (the entity this calculated attribute belongs to).
- Only `released` sales orders with a `documentDate` on or after the first day of the previous month are considered.
- Sales orders are split into:
  - **Previous month**: orders with `documentDate` before the first day of the current month
  - **Current month**: orders with `documentDate` on or after the first day of the current month  
- The calculated attribute returns a formatted string suitable for display in lists or detail views.

## Example: Total ATP across all stores (as-of shipment required date)

This calculated attribute returns the total Available-to-Promise (ATP) quantity for a shipment order line's product, summed across all stores.

- **Repository:** Logistics.Shipment.ShipmentOrderLines
- **Script Language:** JavaScript
- **Script Text:**
```js
const shipmentOrder = subject.ShipmentOrder;
const product = subject.Product;
const enterpriseCompany = shipmentOrder
    ? shipmentOrder.EnterpriseCompany
    : null;

const asOfDate =
    (shipmentOrder ? shipmentOrder.RequiredDeliveryDate : null)
    || (shipmentOrder ? shipmentOrder.DocumentDate : null)
    || new Date();

if (!product || !enterpriseCompany || !asOfDate) {
    return 0;
}

// Load ATP rows for ALL stores for this product/company up to the selected date.
const atpRows = Domain.Logistics.Inventory.DemandManagement.AvailableToPromiseRepository.query({
    Product: product,
    EnterpriseCompany: enterpriseCompany,
    FromDate: { lessthanorequal: asOfDate }
});

// Keep only the latest ATP row per store (the one with the greatest FromDate).
const latestRowPerStore = {};

atpRows.forEach((r) => {
    if (!r || !r.Store || !r.Store.Id)
        return;

    const storeId = r.Store.Id;
    const current = latestRowPerStore[storeId];

    if (!current
        || (r.FromDate && current.FromDate && r.FromDate > current.FromDate)
        || (r.FromDate && !current.FromDate)) {
        latestRowPerStore[storeId] = r;
    }
});

// Sum the ATP of the latest row from each store.
let totalAtp = 0;

for (const storeId in latestRowPerStore) {
    const row = latestRowPerStore[storeId];

    // If there's no ATP value, treat it as 0.
    const atpValue = (row && row.ATPBase && row.ATPBase.Value != null)
        ? row.ATPBase.Value
        : 0;

    totalAtp += atpValue;
}

return totalAtp;
```

Notes:

- `subject` is the current **Shipment Order Line** (`Logistics.Shipment.ShipmentOrderLines`) instance.
- The "as-of" date is taken from:
  - `ShipmentOrder.RequiredDeliveryDate`, then
  - `ShipmentOrder.DocumentDate`, then
  - current date/time.
- The script sums `ATPBase.Value` (ATP in base unit) across **all stores**, using the latest ATP snapshot per store up to `asOfDate`.

## Example: Unique invoice numbers for a sales order (DISTINCT)

This calculated attribute returns a comma-separated list of the **unique invoice numbers** that have invoiced the current **sales order**.

The result is formatted as:
```text
0001, 0003, 0005...
```

- **Repository:** `Crm.Sales.SalesOrders`
- **Script Language:** JavaScript
- **Script Text:**
```js
// Load all invoice lines related to the current Sales Order.
const invoiceLines = Domain.Crm.Invoicing.InvoiceLinesRepository.query({
    SalesOrder: subject
});

// Collect unique invoice numbers (DISTINCT) locally.
const seen = new Set();
const uniqueInvoiceNos = [];

invoiceLines.forEach((line) => {
    const invoiceNo = (line && line.Invoice && line.Invoice.DocumentNo)
        ? line.Invoice.DocumentNo
        : null;

    if (!invoiceNo)
        return;

    if (seen.has(invoiceNo))
        return;

    seen.add(invoiceNo);
    uniqueInvoiceNos.push(invoiceNo);
});

return uniqueInvoiceNos.join(', ');
```

Notes:

- `subject` is the current **Sales Order** (`Crm.Sales.SalesOrders`) instance.
- The script performs DISTINCT **locally** (in JavaScript), because it cannot be pushed down to the database query.
- The invoice number is taken from `Invoice.DocumentNo`.

## Example: ATP by lots (latest per lot as of today)

This calculated attribute returns a readable list of **Available-to-Promise (ATP)** quantities **per lot** for the selected product, as of today (`FromDate <= today`).

Because the `AvailableToPromiseByLots` view can contain **multiple rows per lot** (for different dates), the script keeps **only the latest row per lot** (maximum `FromDate` up to today), and then formats the result as:
```text
No lot: 1
L260122: 15
L260123: 22
...
```

> [!WARNING]
> The view may return many rows (lots * dates).  
> Keep filters as narrow as possible (e.g., company/store/date) to avoid slow calculated attribute evaluation.

- **Repository:** Crm.Sales.SalesOrderLines
- **Script Language:** JavaScript
- **Script Text:**
```js
const product = subject.Product;
const salesOrder = subject.SalesOrder;
const enterpriseCompany = salesOrder ? salesOrder.EnterpriseCompany : null;

// Pick a store context (line store if set, otherwise header store)
const store =
    (subject.LineStore ? subject.LineStore : null)
    || (salesOrder ? salesOrder.Store : null);

const now = new Date();
const today = new Date(now.getFullYear(), now.getMonth(), now.getDate());

if (!product || !enterpriseCompany || !store) {
    return '';
}

// Load ATP-by-lot rows for the product, up to today (ignore future dates)
const atpRows = Domain.Logistics.Inventory.DemandManagement.AvailableToPromiseByLotsRepository.query({
    Product: product,
    EnterpriseCompany: enterpriseCompany,
    Store: store,
    FromDate: { lessthanorequal: today }
});

// Keep only the latest row per lot (max FromDate)
const latestRowPerLotKey = {};

atpRows.forEach((r) => {
    const lotKey = (r && r.Lot && r.Lot.Id) ? r.Lot.Id : '__NO_LOT__';
    const current = latestRowPerLotKey[lotKey];

    if (!current
        || (r.FromDate && current.FromDate && r.FromDate > current.FromDate)
        || (r.FromDate && !current.FromDate)) {
        latestRowPerLotKey[lotKey] = r;
    }
});

// Build a user-friendly "Lot: Qty" list
const resultLines = [];

// Put "No lot" first (if present)
const noLotRow = latestRowPerLotKey['__NO_LOT__'];
if (noLotRow && noLotRow.ATPBase && noLotRow.ATPBase.Value != null) {
    resultLines.push(`No lot: ${noLotRow.ATPBase.Value}`);
}

// Then list all lots
for (const lotKey in latestRowPerLotKey) {
    if (lotKey === '__NO_LOT__')
      continue;

    const row = latestRowPerLotKey[lotKey];
    const lotName = (row && row.Lot) ? row.Lot.DisplayText : lotKey;
    const qty = (row && row.ATPBase && row.ATPBase.Value != null) ? row.ATPBase.Value : 0;

    resultLines.push(`${lotName}: ${qty}`);
}

return resultLines.join('\n');
```

Notes:

- `subject` is the current **Sales Order Line** (`Crm.Sales.SalesOrderLines`) instance.
- Only rows with `FromDate <= today` are considered (future ATP is ignored).
- Duplicates per lot are resolved by taking the row with the latest `FromDate` for each lot, then formatting the output as a multi-line string suitable for display.

-------------

For more details and advanced scripting scenarios, see the [Scripting documentation](../../scripting/index.md).
