# Concepts

Discount Management breaks down the discount effect of a sales order line into separate calculated amounts.

This makes it possible to analyze discount sources separately and, when needed, record them by category for distribution and posting.

## Calculated discount amounts

Each sales order line can contain five calculated discount amounts:

- **Level 1 Discount Amount**
- **Level 2 Discount Amount**
- **Level 3 Discount Amount**
- **Bonus Program Amount**
- **Promotional Package Amount**

These amounts are calculated automatically from the discount sources applied to the line.

## Calculation model

The system calculates the discount amounts as separate components of the final line discount.

Each component is calculated by applying the corresponding discount percent to a specific base amount.

The base amount depends on the discount source:

- some discounts are calculated on the original line amount;
- some discounts are calculated on the remaining amount after the three standard line discount levels have been applied.

The original line amount is:

`Quantity × Unit Price`

Each component amount is rounded to two decimal places before the final reconciliation step.

## Standard line discount levels

The three standard line discount levels are calculated in cascade:

- **Level 1 Discount Amount** is calculated on the original line amount;
- **Level 2 Discount Amount** is calculated on the remaining amount after level 1;
- **Level 3 Discount Amount** is calculated on the remaining amount after levels 1 and 2.

This means that each next level uses a reduced base.

### Example

Suppose a sales order line has:

- **Quantity** = `10`
- **Unit Price** = `100.00`

The original line amount is:

`10 × 100.00 = 1,000.00`

If the applied line discount percentages are:

- **Level 1 Discount Percent** = `10%`
- **Level 2 Discount Percent** = `5%`
- **Level 3 Discount Percent** = `2%`

then the calculated amounts are:

- **Level 1 Discount Amount** = `1,000.00 × 10% = 100.00`
- **Level 2 Discount Amount** = `(1,000.00 - 100.00) × 5% = 45.00`
- **Level 3 Discount Amount** = `(1,000.00 - 100.00 - 45.00) × 2% = 17.10`

## Bonus programs

Bonus programs can also contribute a separate discount amount.

The **Bonus Program Amount** is calculated by applying the **Bonus Line Discount Percent** from the applied bonus program to the applicable line base amount.

Its behavior depends on **Bonus Action**:

- **Discount** applies the bonus percent to the original line amount;
- **Cascade discount** applies the bonus percent to the remaining amount after level 1, level 2, and level 3 discounts.
  
### Example

Suppose a sales order line has:

- **Quantity** = `10`
- **Unit Price** = `100.00`

The original line amount is:

`10 × 100.00 = 1,000.00`

Suppose also that a bonus program is applied with:

- **Bonus Line Discount Percent** = `3%`

Then the result depends on **Bonus Action**.

If **Bonus Action** is **Discount**, the bonus percent is applied to the original line amount:

- **Bonus Program Amount** = `1,000.00 × 3% = 30.00`

If **Bonus Action** is **Cascade discount**, the bonus percent is applied to the amount remaining after the standard line discount levels that are applied on the line, if any.

For example, if the applied standard line discount levels reduce the line amount to `837.90`, then:

- **Bonus Program Amount** = `837.90 × 3% = 25.14`

## Promotional packages

Promotional packages can also contribute a separate discount amount.

The **Promotional Package Amount** is calculated by applying the **Standard Discount Percent Adjust** from the applied promotional package line to the applicable line base amount.

Its behavior depends on the package line setup:

- **Add** applies the promotional percent to the original line amount;
- **Replace** applies the promotional percent to the original line amount;
- **MarkDown** applies the promotional percent to the remaining amount after level 1, level 2, and level 3 discounts.

### Example

Suppose a sales order line has:

- **Quantity** = `10`
- **Unit Price** = `100.00`

The original line amount is:

`10 × 100.00 = 1,000.00`

Suppose also that an applied promotional package line has:

- **Standard Discount Percent Adjust** = `4%`

Then the result depends on the promotional package line setup.

If the setup is **Add** or **Replace**, the promotional percent is applied to the original line amount:

- **Promotional Package Amount** = `1,000.00 × 4% = 40.00`

If the setup is **MarkDown**, the promotional percent is applied to the amount remaining after the standard line discount levels that are applied on the line, if any.

For example, if the applied standard line discount levels reduce the line amount to `837.90`, then:

- **Promotional Package Amount** = `837.90 × 4% = 33.516`, rounded to `33.52`

## Rounding and reconciliation

Each discount component is rounded separately to two decimal places.

To reconcile these separately rounded components with the final discount applied on the line, the system also determines the final line standard discount percent for the sales order line.

It then applies that percent to the original line amount to calculate the total line discount amount and compares it with the sum of the five component amounts.

Because the components are rounded separately, a rounding difference can appear.

If this happens, the difference is assigned to the largest discount component.

This ensures that the sum of the component amounts matches the final rounded line discount amount of the sales order line.

The calculated component amounts are returned in the sales order document currency.  
They are typically negative for regular sales lines and positive for lines with negative amount, such as return lines.

## Categorized additional amounts

When discount sources are assigned to **Document Amount Types**, the calculated discount amounts can also be recorded as categorized additional amounts.

In this model, document amount types act as discount categories.

They do not change the discount calculation itself.  
Instead, they classify the calculated discount amounts for:

- recording;
- reporting and analytics;
- posting;
- line-level distribution.

The sales order creates one additional document amount for each distinct **Document Amount Type** that is actually used by the applied discount sources in the document.

These amounts are created automatically with:

- **Input Amount** = `null`
- **Input Percent** = `100%`

This means that each categorized additional amount represents the full calculated discount amount for its category.

## Distributed amounts in the sales order

After the categorized additional amounts are created, the system distributes them to the affected sales order lines.

This distribution is based on the calculated discount amount of the applied source on each line.  
It is not based on a manually entered document amount.

As a result, the **Document Distributed Amounts** panel shows which part of each discount category belongs to each sales order line.

## Posting discount categories across documents

Discount categories can be posted directly from sales orders or through invoice templates that reference the related sales order lines.

This is useful when the discount originates from the sales order line, but the accounting entry must use the analytical context of the invoice document and invoice lines.

If an invoice covers only part of the original sales order quantity, the system posts a proportional part of the related discount amount according to the invoiced quantity.

## Special cases

If no **Document Amount Type** is assigned to a discount source, the discount amount is still calculated in the sales order line.  
However, it is not recorded as a categorized additional amount through this mechanism.

For bonus programs, category-based recording is relevant when **Bonus Action** is set to **Discount** or **Cascade discount**.

For promotional packages, category-based recording is relevant for package lines that define a discount through **Standard Discount Percent Adjust**.
