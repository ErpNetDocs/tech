# Concepts

## Calculated discount amounts

Discount management breaks down the final line discount into five system-calculated amounts:

- **Level 1 Discount Amount**
- **Level 2 Discount Amount**
- **Level 3 Discount Amount**
- **Bonus Program Amount**
- **Promotional Package Amount**

These amounts are calculated on the sales order line and can be used for visualization, analytics, and accounting.

### How discount amounts are calculated

The discount amounts are calculated as separate components of the total line discount.

Each component amount is calculated from its corresponding discount percent and the applicable sales order line base amount (`Quantity × Unit Price` or the remaining amount after standard line discounts).  
Each component is rounded to two decimal places before the final reconciliation step.

**Line discount levels**

The three line discount levels are calculated in cascade from their corresponding line discount percentages:

- **Level 1 Discount Amount** is calculated from **Level 1 Discount Percent** on the original line amount;
- **Level 2 Discount Amount** is calculated from **Level 2 Discount Percent** on the remaining amount after level 1;
- **Level 3 Discount Amount** is calculated from **Level 3 Discount Percent** on the remaining amount after levels 1 and 2.

**Bonus programs**

Bonus programs contribute a separate discount amount, calculated from **Bonus Line Discount Percent** of the applied bonus program.

Its calculation depends on **Bonus Action**:

- **Discount** calculates the bonus discount on the original line amount;
- **Cascade discount** calculates the bonus discount on the remaining amount after the standard line discounts have been applied.

**Promotional packages**

Promotional packages also contribute a separate discount amount, calculated from **Standard Discount Percent Adjust** of the applied promotional package.

Its calculation depends on the package line setup:

- **Add** and **Replace** calculate the promotional discount on the original line amount;
- **MarkDown** calculates the promotional discount on the remaining amount after the standard line discounts have been applied.

Bonus program and promotional package amounts are calculated independently from each other.  
Their calculation base can be either the original line amount or the amount remaining after the standard line discounts.

If a discount source is not applied, its corresponding component amount is `0`.

**Rounding and reconciliation**

The system first determines the final standard line discount percent for the sales order line.  
It then calculates the total line discount amount and compares it with the sum of the five calculated discount components.

If a rounding difference appears, the difference is assigned to the largest discount component.

This ensures that the sum of the separate discount amounts matches the total calculated line discount.

The calculated component amounts are returned in the sales order document currency.  
For regular sales lines they are typically negative, while for return lines they can be positive.

## Categorized additional amounts

When discount sources are assigned to **Document Amount Types**, the calculated discount amounts can also be recorded as categorized additional amounts.

In this context, document amount types act as discount categories.  
They do not change the calculation itself.  
Instead, they classify the calculated discount amounts for recording, reporting, analytics, posting, and line-level distribution.

The sales order creates categorized document amounts only for the distinct discount categories that are actually used in the document.

These document amounts are created automatically with:

- **Input Amount** = `null`
- **Input Percent** = `100%`

This means that each categorized additional amount represents the full calculated discount amount for the selected category.

## Distributed amounts in the sales order

After the categorized additional amounts are created, the system distributes them to the affected sales order lines.

This distribution is based on the calculated discount amount of the applied source on each line.  
It is not based on a manually entered amount in the document.

As a result, the **Document Distributed Amounts** panel shows which part of each discount category belongs to each sales order line.

## Posting discount categories across documents

Discount categories can be posted directly from sales orders or through invoice templates that reference the related sales order lines.

This is useful when the discount originates from the sales order line, but the accounting entry must use the analytical context of the invoice document and invoice lines.

When an invoice covers only part of the original sales order quantity, the system posts a proportional part of the related discount amount according to the invoiced quantity.

## Special cases

If no **Document Amount Type** is assigned to a discount source, the discount amount is still calculated in the sales order line.  
However, it is not recorded as a categorized additional amount through this mechanism.

For bonus programs, category-based recording is relevant when **Bonus Action** is set to **Discount** or **Cascade discount**.

For promotional packages, category-based recording is relevant for package lines that define a discount through **Standard Discount Percent Adjust**.
