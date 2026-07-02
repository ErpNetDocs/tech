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

The discount amounts are calculated as separate components of the final line discount.

The three line discount levels are calculated in cascade:

- **Level 1 Discount Amount** is calculated on the original line amount;
- **Level 2 Discount Amount** is calculated on the remaining amount after level 1;
- **Level 3 Discount Amount** is calculated on the remaining amount after levels 1 and 2.

Bonus programs and promotional packages also contribute separate discount amounts.

For bonus programs:

- **Discount** calculates the bonus discount on the original line amount;
- **Cascade discount** calculates the bonus discount on the remaining amount after the standard line discounts.

For promotional packages:

- **Add** and **Replace** calculate the promotional discount on the original line amount;
- **MarkDown** calculates the promotional discount on the remaining amount after the standard line discounts.

As a result, the final discount can be analyzed as a combination of five calculated components.

## Categorized additional amounts

When discount sources are assigned to **Document Amount Types**, the calculated discount amounts can also be recorded as categorized additional amounts.

In this context, document amount types act as discount categories.  
They do not change the calculation itself.  
Instead, they classify the calculated discount amounts for recording, reporting, analytics, and posting.

The sales order creates categorized document amounts only for the discount categories that are actually used in the document.

These document amounts are created automatically with:

- **Input Amount** = `null`
- **Input Percent** = `100%`

This means that each categorized additional amount represents the full calculated discount amount for the selected category.

## Distributed amounts

After the categorized additional amounts are created, the system distributes them to the affected sales order lines.

This distribution is based on the calculated discount amount of the applied source on each line.  
It is not based on a manually entered amount in the document.

As a result, the **Document Distributed Amounts** panel shows which part of each discount category belongs to each sales order line.

## Posting discount categories across documents

Discount categories can be posted directly from sales orders or through invoice templates that reference the related sales order lines.

This is useful when the discount originates from the sales order line, but the accounting entry must use the analytical context of the invoice document and invoice lines.

When an invoice covers only part of the original sales order quantity, the system posts a proportional part of the related discount amount according to the invoiced quantity.

## Rounding and reconciliation

The final line discount is reconciled with the sum of its calculated components.

If a rounding difference appears between the total discount amount and the sum of the five component amounts, the difference is assigned to the largest discount component.

This ensures that the sum of the separate discount amounts matches the final calculated line discount.
